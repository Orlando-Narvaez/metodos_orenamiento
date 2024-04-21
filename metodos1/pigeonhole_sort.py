class Ordenamiento:
    def pigeonhole_sort(self, arr):
        # size of range of values in the list
        # (ie, number of pigeonholes we need)
        my_min = min(arr)
        my_max = max(arr)
        size = my_max - my_min + 1

        # our list of pigeonholes
        holes = [0] * size

        # Populate the pigeonholes.
        for x in arr:
            assert type(x) is int, "integers only please"
            holes[x - my_min] += 1

        # Put the elements back into the array in order.
        i = 0
        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                arr[i] = count + my_min
                i += 1
