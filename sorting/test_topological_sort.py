"""Tests for topological_sort."""

import pytest
from sorting.topological_sort import topological_sort


def _is_valid_ordering(graph, ordering):
    """Return True if *ordering* is a valid topological order for *graph*."""
    index = {node: i for i, node in enumerate(ordering)}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if index[node] >= index[neighbor]:
                return False
    return True


class TestEmptyGraph:
    def test_empty_graph_returns_empty_list(self):
        assert topological_sort({}) == []


class TestSingleNode:
    def test_single_node_no_edges(self):
        assert topological_sort({"a": []}) == ["a"]


class TestLinearChain:
    def test_chain(self):
        graph = {"a": ["b"], "b": ["c"], "c": []}
        result = topological_sort(graph)
        assert _is_valid_ordering(graph, result)
        assert set(result) == {"a", "b", "c"}


class TestDiamond:
    def test_diamond(self):
        graph = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []}
        result = topological_sort(graph)
        assert _is_valid_ordering(graph, result)
        assert set(result) == {"a", "b", "c", "d"}


class TestDisconnected:
    def test_disconnected_nodes(self):
        graph = {"a": [], "b": [], "c": []}
        result = topological_sort(graph)
        assert set(result) == {"a", "b", "c"}


class TestCycleDetection:
    def test_simple_cycle_raises(self):
        graph = {"a": ["b"], "b": ["a"]}
        with pytest.raises(ValueError, match="cycle"):
            topological_sort(graph)

    def test_self_loop_raises(self):
        graph = {"a": ["a"]}
        with pytest.raises(ValueError, match="cycle"):
            topological_sort(graph)

    def test_three_node_cycle_raises(self):
        graph = {"a": ["b"], "b": ["c"], "c": ["a"]}
        with pytest.raises(ValueError, match="cycle"):
            topological_sort(graph)


class TestImplicitNodes:
    """Nodes that appear only as dependencies (not as keys) must still be included."""
    def test_implicit_node_included(self):
        graph = {"a": ["b"]}
        result = topological_sort(graph)
        assert "b" in result
        assert result.index("a") < result.index("b")


class TestIntegerNodes:
    def test_integer_keys(self):
        graph = {1: [2, 3], 2: [3], 3: []}
        result = topological_sort(graph)
        assert _is_valid_ordering(graph, result)
        assert set(result) == {1, 2, 3}
