class Ordenamiento:
    def comp_and_swap(self, a, i, j, dir):
        if (a[i] > a[j] and dir == 1) or (a[i] < a[j] and dir == 0):
            # Swapping elements
            a[i], a[j] = a[j], a[i]

    def bitonic_merge(self, a, low, cnt, dir):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                self.comp_and_swap(a, i, i + k, dir)
            self.bitonic_merge(a, low, k, dir)
            self.bitonic_merge(a, low + k, k, dir)

    def bitonic_sort(self, a, low, cnt, dir):
        if cnt > 1:
            k = cnt // 2
            self.bitonic_sort(a, low, k, 1)  # sort in ascending order
            self.bitonic_sort(a, low + k, k, 0)  # sort in descending order
            self.bitonic_merge(a, low, cnt, dir)

    def sort(self, a, up):
        self.bitonic_sort(a, 0, len(a), up)

    @staticmethod
    def print_array(arr):
        for i in arr:
            print(i, end=" ")
        print()
