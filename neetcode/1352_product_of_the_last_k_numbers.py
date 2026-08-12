class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        self.nums.append(num)
        print(self.nums)

    def getProduct(self, k: int) -> int:
        prod = 1
        last = len(self.nums) - 1

        for i in range(last, last - k, -1):
            prod *= self.nums[i]

        return prod

def test_example_sequence():
    obj = ProductOfNumbers()

    for num in [3, 0, 2, 5, 4]:
        obj.add(num)

    assert obj.getProduct(2) == 20
    assert obj.getProduct(3) == 40
    assert obj.getProduct(4) == 0

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


def test_products_after_zero_are_based_on_the_new_segment():
    obj = ProductOfNumbers()

    for num in [0, 6, 2, 3]:
        obj.add(num)

    assert obj.getProduct(1) == 3
    assert obj.getProduct(2) == 6
    assert obj.getProduct(3) == 36
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
        test_example_sequence
        # test_product_of_last_one_number,
        # test_zero_only_affects_products_that_include_it,
        # test_products_after_zero_are_based_on_the_new_segment,
        # test_repeated_queries_do_not_change_the_stream,
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

# if __name__ == "__main__":
#     obj = ProductOfNumbers()

#     for num in [3, 0, 2, 5, 4]:
#         obj.add(num)

#     assert obj.getProduct(2) == 20
#     assert obj.getProduct(3) == 40
#     assert obj.getProduct(4) == 0

#     obj.add(8)
#     assert obj.getProduct(2) == 32
#     print("All tests passed!")
