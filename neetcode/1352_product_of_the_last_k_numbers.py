class ProductOfNumbers:

    def __init__(self):
        pass


    def add(self, num: int) -> None:
        pass


    def getProduct(self, k: int) -> int:
        pass


# def test_example_sequence():
#     product_of_numbers = ProductOfNumbers()

#     for num in [3, 0, 2, 5, 4]:
#         product_of_numbers.add(num)

#     assert product_of_numbers.getProduct(2) == 20
#     assert product_of_numbers.getProduct(3) == 40
#     assert product_of_numbers.getProduct(4) == 0

#     product_of_numbers.add(8)
#     assert product_of_numbers.getProduct(2) == 32


# def test_product_of_last_one_number():
#     product_of_numbers = ProductOfNumbers()

#     product_of_numbers.add(7)
#     assert product_of_numbers.getProduct(1) == 7

#     product_of_numbers.add(0)
#     assert product_of_numbers.getProduct(1) == 0

#     product_of_numbers.add(9)
#     assert product_of_numbers.getProduct(1) == 9


# def test_zero_only_affects_products_that_include_it():
#     product_of_numbers = ProductOfNumbers()

#     for num in [2, 3, 0, 4, 5]:
#         product_of_numbers.add(num)

#     assert product_of_numbers.getProduct(1) == 5
#     assert product_of_numbers.getProduct(2) == 20
#     assert product_of_numbers.getProduct(3) == 0
#     assert product_of_numbers.getProduct(4) == 0


# def test_products_after_zero_are_based_on_the_new_segment():
#     product_of_numbers = ProductOfNumbers()

#     for num in [0, 6, 2, 3]:
#         product_of_numbers.add(num)

#     assert product_of_numbers.getProduct(1) == 3
#     assert product_of_numbers.getProduct(2) == 6
#     assert product_of_numbers.getProduct(3) == 36
#     assert product_of_numbers.getProduct(4) == 0


# def test_repeated_queries_do_not_change_the_stream():
#     product_of_numbers = ProductOfNumbers()

#     for num in [1, 2, 3, 4]:
#         product_of_numbers.add(num)

#     assert product_of_numbers.getProduct(3) == 24
#     assert product_of_numbers.getProduct(2) == 12
#     assert product_of_numbers.getProduct(3) == 24

# def run_tests():
#     tests = [
#         test_example_sequence,
#         test_product_of_last_one_number,
#         test_zero_only_affects_products_that_include_it,
#         test_products_after_zero_are_based_on_the_new_segment,
#         test_repeated_queries_do_not_change_the_stream,
#     ]

#     failures = 0
#     for test in tests:
#         try:
#             test()
#         except AssertionError:
#             failures += 1
#             print(f"FAIL {test.__name__}")
#         else:
#             print(f"PASS {test.__name__}")

#     if failures:
#         raise SystemExit(f"{failures} test(s) failed")

#     print(f"{len(tests)} tests passed")


if __name__ == "__main__":
    product_of_numbers = ProductOfNumbers()

    for num in [3, 0, 2, 5, 4]:
        product_of_numbers.add(num)

    assert product_of_numbers.getProduct(2) == 20
    assert product_of_numbers.getProduct(3) == 40
    assert product_of_numbers.getProduct(4) == 0

    product_of_numbers.add(8)
    assert product_of_numbers.getProduct(2) == 32
    print("All tests passed!")
