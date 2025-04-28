from forbiddenfruit import curse


def fix_list():
    def alter_list_item(self, index, func):
        self[index] = func(self[index])
        return self

    def alter_list_range(self, indexi, indexf, func):
        for i in range(indexi, indexf + 1):
            self[i] = func(self[i])
        return self

    def map_list(self, func):
        return [func(x) for x in self]

    def filter_list(self, func):
        return [x for x in self if func(x)]

    curse(list, "alter", alter_list_item)
    curse(list, "alter_range", alter_list_range)
    curse(list, "map", map_list)
    curse(list, "filter", filter_list)
