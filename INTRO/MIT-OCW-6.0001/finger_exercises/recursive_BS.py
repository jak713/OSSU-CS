def bisect_search(sorted_L: list, e: int) -> bool:
    if sorted_L == []:  # O(1)
        return False
    elif len(sorted_L) == 1:  # O(1)
        return sorted_L[0] == e
    else:
        half = len(sorted_L) // 2  # floor division to get int, O(1)
        if (
            sorted_L[half] > e
        ):  #  O(log n) recursive calls (since n is halved every time)
            return bisect_search(sorted_L[:half], e)  # copying list is O(n)
        else:
            return bisect_search(sorted_L[half:], e)


# ∴ O(n) * O(log n) = O(n log n)


def bisect_search2(L: list, e: int) -> bool:
    """Does not copy the list, just points to high/low within the same list. O(log n)"""

    ####
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search, i.e. list size of 1
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)

    #####
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)


def intToStr(i: int) -> str:
    digits = "0123456789"
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i % 10] + result
        print("i%10:", i % 10)
        print("digits[i%10]:", digits[i % 10])
        print("result:", result)
        i = (
            i // 10
        )  # log i, reducing the size of input by a constant factor (10) hence O(log n)
        print("i:", i)
    return result


n = -1  # account for first call of function
i = 0


def genSubsets(L):
    global n
    global i
    n += 1
    if len(L) == 0:
        return [[]]  # empty set
    smaller = genSubsets(L[:-1])  # all subsets before current element
    print("L:", L)
    print("smaller:", smaller)
    extra = L[-1:]  # list of just last (current) element
    print("extra:", extra)
    new = []
    for small in smaller:
        i += 1
        print("small", small)
        print("appending small+extra concatenation:", (small + extra))
        new.append(small + extra)  # all small solutions with the current element
        print("new", new)

    print("result for current L:", (smaller + new))
    return smaller + new  # combine all


genSubsets([1, 2, 3, 4, 5, 6, 7])
print("n:", n)
print(f"i: {i},  2**{n}={2**n}")  # grows 2^n
