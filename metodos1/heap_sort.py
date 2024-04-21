class Ordenamiento:
    def sort(self, arr):
        n = len(arr)

        # Build heap (rearrange array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # One by one extract an element from heap
        for i in range(n - 1, 0, -1):
            # Move current root to end
            arr[0], arr[i] = arr[i], arr[0]

            # call max heapify on the reduced heap
            self.heapify(arr, i, 0)

    # To heapify a subtree rooted with node i which is
    # an index in arr[]. n is size of heap
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # If left child is larger than root
        if l < n and arr[l] > arr[largest]:
            largest = l

        # If right child is larger than largest so far
        if r < n and arr[r] > arr[largest]:
            largest = r

        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)

    @staticmethod
    def print_array(arr):
        for i in arr:
            print(i, end=" ")
        print()
