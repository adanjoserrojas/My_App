import pytest
from sorting import merge_sort, quick_sort, bubble_sort, insertion_sort, topological_sort


COMPARISON_SORTS = [merge_sort, quick_sort, bubble_sort, insertion_sort]


class TestComparisonSorts:
    @pytest.mark.parametrize("sort_fn", COMPARISON_SORTS)
    def test_empty(self, sort_fn):
        assert sort_fn([]) == []

    @pytest.mark.parametrize("sort_fn", COMPARISON_SORTS)
    def test_single_element(self, sort_fn):
        assert sort_fn([1]) == [1]

    @pytest.mark.parametrize("sort_fn", COMPARISON_SORTS)
    def test_already_sorted(self, sort_fn):
        assert sort_fn([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    @pytest.mark.parametrize("sort_fn", COMPARISON_SORTS)
    def test_reverse_sorted(self, sort_fn):
        assert sort_fn([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    @pytest.mark.parametrize("sort_fn", COMPARISON_SORTS)
    def test_duplicates(self, sort_fn):
        assert sort_fn([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

    @pytest.mark.parametrize("sort_fn", COMPARISON_SORTS)
    def test_negative_numbers(self, sort_fn):
        assert sort_fn([-3, 0, -1, 5, 2]) == [-3, -1, 0, 2, 5]

    @pytest.mark.parametrize("sort_fn", COMPARISON_SORTS)
    def test_does_not_mutate_input(self, sort_fn):
        original = [3, 1, 2]
        copy = original[:]
        sort_fn(original)
        assert original == copy


class TestTopologicalSort:
    def test_empty_graph(self):
        assert topological_sort({}) == []

    def test_single_node(self):
        assert topological_sort({"a": []}) == ["a"]

    def test_linear_chain(self):
        graph = {"a": ["b"], "b": ["c"], "c": []}
        result = topological_sort(graph)
        assert result.index("a") < result.index("b") < result.index("c")

    def test_diamond(self):
        graph = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []}
        result = topological_sort(graph)
        assert result.index("a") < result.index("b")
        assert result.index("a") < result.index("c")
        assert result.index("b") < result.index("d")
        assert result.index("c") < result.index("d")

    def test_cycle_raises(self):
        graph = {"a": ["b"], "b": ["c"], "c": ["a"]}
        with pytest.raises(ValueError, match="cycle"):
            topological_sort(graph)

    def test_self_loop_raises(self):
        graph = {"a": ["a"]}
        with pytest.raises(ValueError, match="cycle"):
            topological_sort(graph)

    def test_disconnected_components(self):
        graph = {"a": [], "b": [], "c": []}
        result = topological_sort(graph)
        assert set(result) == {"a", "b", "c"}
        assert len(result) == 3
