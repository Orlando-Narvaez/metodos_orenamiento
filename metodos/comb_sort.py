class Ordenamiento:
    @staticmethod
    def get_next_gap(gap):
        # Shrink gap by Shrink factor
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap

    def comb_sort(self, arr):
        n = len(arr)

        # Initialize gap
        gap = n

        # Initialize swapped as true to make sure that
        # loop runs
        swapped = True

        # Keep running while gap is more than 1 and last
        # iteration caused a swap
        while gap != 1 or swapped == 1:

            # Find next gap
            gap = self.get_next_gap(gap)

            # Initialize swapped as false so that we can
            # check if swap happened or not
            swapped = False

            # Compare all elements with current gap
            for i in range(0, n - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
