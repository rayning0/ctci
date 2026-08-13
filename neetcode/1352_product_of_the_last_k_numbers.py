# 1. Brute force. getProduct() runs too slowly for LeetCode if k = 4 * 10^4

# class ProductOfNumbers:

#     def __init__(self):
#         self.nums = []

#     # Time: O(1), Space: O(n)
#     def add(self, num: int) -> None:
#         self.nums.append(num)

#     # Time: O(k), Space: O(1) auxiliary (if ignore nums)
#     def getProduct(self, k: int) -> int:
#         prod = 1

#         for i in range(-1, -1 - k, -1):
#             prod *= self.nums[i]

#         return prod

# 2. Prefix product:

class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    # Time: O(1), Space: O(n)
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            # self.prefix[-1] is latest prefix product
            self.prefix.append(self.prefix[-1] * num)

    # Time: O(1), Space: O(1) auxiliary
    def getProduct(self, k: int) -> int:
        # product (if k includes a past added 0) is 0
        if k >= len(self.prefix):
            return 0
        else:
            return self.prefix[-1] //  self.prefix[-1 - k]


def test_example_sequence():
    obj = ProductOfNumbers()

    for num in [3, 0, 2, 5, 4]:
        obj.add(num)

# add(3): prefix = [3]
# add(0): prefix = [1]
# add(2): prefix = [1, 2]
# add(5): prefix = [1, 2, 10]
# add(4): prefix = [1, 2, 10, 40]

    assert obj.getProduct(2) == 20
# k = 2: product = prefix[-1] // prefix[-1-k] = 40 // prefix[-3] = 40 // 2 = 20

    assert obj.getProduct(3) == 40
# k = 3: product = prefix[-1] // prefix[-1-3] = 40 // 1 = 40

    assert obj.getProduct(4) == 0
# k = 4: Since k >= len(prefix) = 4, we hit a past 0. So product = 0

    obj.add(8)
    assert obj.getProduct(2) == 32

def test_product_of_last_one_number():
    obj = ProductOfNumbers()

    obj.add(7)
    assert obj.getProduct(1) == 7

    obj.add(0)
    assert obj.getProduct(1) == 0

    obj.add(9)
    assert obj.getProduct(1) == 9


def test_zero_only_affects_products_that_include_it():
    obj = ProductOfNumbers()

    for num in [2, 3, 0, 4, 5]:
        obj.add(num)

    assert obj.getProduct(1) == 5
    assert obj.getProduct(2) == 20
    assert obj.getProduct(3) == 0
    assert obj.getProduct(4) == 0


def test_multiple_zeros_reset_prefix_segment():
    obj = ProductOfNumbers()

    obj.add(3)
    assert obj.prefix == [1, 3]

    obj.add(0)
    assert obj.prefix == [1]

    obj.add(0)
    assert obj.prefix == [1]

    obj.add(2)
    assert obj.prefix == [1, 2]

    obj.add(5)
    assert obj.prefix == [1, 2, 10]

    assert obj.getProduct(1) == 5
    assert obj.getProduct(2) == 10
    assert obj.getProduct(3) == 0
    assert obj.getProduct(4) == 0


def test_repeated_queries_do_not_change_the_stream():
    obj = ProductOfNumbers()

    for num in [1, 2, 3, 4]:
        obj.add(num)

    assert obj.getProduct(3) == 24
    assert obj.getProduct(2) == 12
    assert obj.getProduct(3) == 24

def run_tests():
    tests = [
        test_example_sequence,
        test_product_of_last_one_number,
        test_zero_only_affects_products_that_include_it,
        test_multiple_zeros_reset_prefix_segment,
        test_repeated_queries_do_not_change_the_stream,
    ]

    failures = 0
    for test in tests:
        try:
            test()
        except AssertionError:
            failures += 1
            print(f"FAIL {test.__name__}")
        else:
            print(f"PASS {test.__name__}")

    if failures:
        raise SystemExit(f"{failures} test(s) failed")

    print(f"{len(tests)} tests passed")

run_tests()
