# Netflix: Implement in-memory, key-value database that allows nested transactions. Functions should have worst-case time complexity of O(log n) or better.
# https://leetcode.com/discuss/post/2704068/netflix-phone-screen-by-anonymous_user-c05y/
# https://www.freecodecamp.org/news/design-a-key-value-store-in-go/
# https://medium.com/@rickymondal/system-design-inmemory-key-value-with-transaction-0a6df97ccce1

# Data Functions:
# 1. set(String key, String value). No return value.
# 2. get(String key). Returns value if key is in database. Throws exception if key doesn't exist.
# 3. delete(String key). Deletes key from database, if it exists. If doesn't exist, say this message. No value returned by function in either case.

# Transaction Functions:
# 1. begin(): Signals start of transaction block. No value returned.
# 2. rollback(): Rollback only most recent open transaction block. If this function called outside of transaction, throw exception. No value returned.
# 3. commit(): Commit all operations from all open  trasaction blocks permanently to database. If this function called outside of transaction, throw exception. No value returned.

# The in-memory database should support nesting of transactions, up to 10 levels deep.

# Within a transaction, the data is transient, unless the commit() function is invoked. Outside of transaction, any change of data is applied immediately to database.


class KeyValueDB:
    """
    In-memory key-value database with nested transaction support.
    Uses a stack-based approach where each transaction has its own local store.
    """

    def __init__(self):
        # Global store for committed data
        self.global_store = {}
        # Stack of transactions (each transaction has its own local store)
        self.transaction_stack = []
        # Track deleted keys in transactions (using None as marker)
        self.max_depth = 10

    def set(self, key: str, value: str) -> None:
        """
        Sets the given key to the specified value.
        If inside a transaction, updates the active transaction's local store.
        Otherwise, updates the global store directly.
        """
        if self.transaction_stack:
            # Inside a transaction - update active transaction's local store
            self.transaction_stack[-1][key] = value
        else:
            # Outside transaction - update global store directly
            self.global_store[key] = value

    def get(self, key: str) -> str:
        """
        Returns the value of the specified key.
        Checks active transaction first, then parent transactions, then global store.
        Throws KeyError if key doesn't exist.
        """
        # Check active transactions from top to bottom
        for transaction in reversed(self.transaction_stack):
            if key in transaction:
                value = transaction[key]
                # None is used as a marker for deleted keys
                if value is None:
                    raise KeyError(f"{key} not set")
                return value

        # Check global store
        if key in self.global_store:
            return self.global_store[key]

        raise KeyError(f"{key} not set")

    def delete(self, key: str) -> None:
        """
        Deletes the given key from the database.
        If inside a transaction, marks the key as deleted in the active transaction.
        Otherwise, deletes from global store directly.
        """
        if self.transaction_stack:
            # Inside a transaction - mark as deleted in active transaction
            self.transaction_stack[-1][key] = None
        else:
            # Outside transaction - delete from global store
            if key in self.global_store:
                del self.global_store[key]
            else:
                print(f"{key} not set")

    def begin(self) -> None:
        """
        Signals the start of a transaction block.
        Creates a new transaction and pushes it onto the stack.
        """
        if len(self.transaction_stack) >= self.max_depth:
            raise Exception("Maximum transaction depth exceeded")

        # Create a new transaction (local store)
        new_transaction = {}
        self.transaction_stack.append(new_transaction)

    def rollback(self) -> None:
        """
        Rollback only the most recent open transaction block.
        Throws exception if called outside of transaction.
        """
        if not self.transaction_stack:
            raise Exception("No Active Transaction")

        # Remove the most recent transaction (discard all changes)
        self.transaction_stack.pop()

    def commit(self) -> None:
        """
        Commit all operations from all open transaction blocks permanently to database.
        Propagates changes from all transactions to the global store.
        Throws exception if called outside of transaction.
        """
        if not self.transaction_stack:
            raise Exception("No Active Transaction")

        # Commit all transactions from bottom to top
        # This ensures parent transactions get updates from child transactions
        for transaction in self.transaction_stack:
            for key, value in transaction.items():
                if value is None:
                    # Key was deleted - remove from global store
                    if key in self.global_store:
                        del self.global_store[key]
                else:
                    # Update global store with the value
                    self.global_store[key] = value

        # Clear all transactions after committing
        self.transaction_stack.clear()


# Example usage and testing
if __name__ == "__main__":
    db = KeyValueDB()

    # Example 1
    print("Example 1:")
    db.begin()
    db.set("foo", "bar")
    print(db.get("foo"))  # "bar"
    db.begin()
    print(db.get("foo"))  # "bar"
    db.set("foo", "baz")
    print(db.get("foo"))  # "baz"
    db.rollback()
    print(db.get("foo"))  # "bar"
    db.commit()
    print(db.get("foo"))  # "bar"

    print("\nExample 2:")
    db = KeyValueDB()
    db.begin()
    db.set("foo", "bar")
    db.begin()
    db.set("foo", "baz")
    db.commit()
    print(db.get("foo"))  # "baz"

    print("\nExample 3:")
    db = KeyValueDB()
    db.set("foo", "baz")
    print(db.get("foo"))  # "baz"
    db.begin()
    print(db.get("foo"))  # "baz"
    db.set("foo", "bar")
    db.commit()
    print(db.get("foo"))  # "bar"
    db.begin()
    db.delete("foo")
    print("After delete in transaction")
    db.commit()
    try:
        print(db.get("foo"))
    except KeyError as e:
        print(e)  # "foo not set"

    print("\n" + "=" * 60)
    print("NESTED TRANSACTION TESTS (Up to 10 levels deep)")
    print("=" * 60)

    # Test 1: Basic nested transactions with rollback
    print("\nTest 1: Basic nested transactions with rollback")
    db = KeyValueDB()
    db.begin()
    db.set("a", "1")
    assert db.get("a") == "1", "Level 1: a should be '1'"

    db.begin()
    db.set("a", "2")
    assert db.get("a") == "2", "Level 2: a should be '2'"

    db.begin()
    db.set("a", "3")
    assert db.get("a") == "3", "Level 3: a should be '3'"

    db.rollback()
    assert db.get("a") == "2", "After rollback level 3: a should be '2'"

    db.rollback()
    assert db.get("a") == "1", "After rollback level 2: a should be '1'"

    db.rollback()
    try:
        db.get("a")
        assert False, "After rollback level 1: a should not exist"
    except KeyError:
        pass
    print("✓ Test 1 passed")

    # Test 2: 10 levels deep - setting values at each level
    print("\nTest 2: 10 levels deep - setting values at each level")
    db = KeyValueDB()
    for i in range(10):
        db.begin()
        db.set("level", str(i))
        assert db.get("level") == str(i), f"Level {i + 1}: level should be '{i}'"
    print(f"✓ Created {len(db.transaction_stack)} nested transactions")
    assert db.get("level") == "9", "After creating all levels, should see '9'"

    # Verify we can read from each level (rollback one by one)
    # After each rollback, we should see the value from the previous transaction
    for rollback_count in range(10):
        expected_before = str(9 - rollback_count)
        assert db.get("level") == expected_before, (
            f"Before rollback {rollback_count + 1}: should see level '{expected_before}'"
        )
        db.rollback()
        if rollback_count < 9:
            # After rollback, we should see the value from the previous transaction
            expected_after = str(8 - rollback_count)
            assert db.get("level") == expected_after, (
                f"After rollback {rollback_count + 1}: should see level '{expected_after}'"
            )
        else:
            # After last rollback, level should not exist
            try:
                db.get("level")
                assert False, "After all rollbacks, level should not exist"
            except KeyError:
                pass

    print("✓ Test 2 passed")

    # Test 3: 10 levels deep - different keys at each level
    print("\nTest 3: 10 levels deep - different keys at each level")
    db = KeyValueDB()
    for i in range(10):
        db.begin()
        db.set(f"key_{i}", f"value_{i}")
        # Verify we can see all previous keys
        for j in range(i + 1):
            assert db.get(f"key_{j}") == f"value_{j}", (
                f"Level {i + 1}: key_{j} should be 'value_{j}'"
            )
    print(
        f"✓ Created {len(db.transaction_stack)} nested transactions with different keys"
    )

    # Commit all and verify
    db.commit()
    for i in range(10):
        assert db.get(f"key_{i}") == f"value_{i}", (
            f"After commit: key_{i} should be 'value_{i}'"
        )
    print("✓ Test 3 passed")

    # Test 4: 10 levels deep - updating same key at each level
    print("\nTest 4: 10 levels deep - updating same key at each level")
    db = KeyValueDB()
    db.set("x", "initial")

    for i in range(10):
        db.begin()
        db.set("x", f"level_{i}")
        assert db.get("x") == f"level_{i}", f"Level {i + 1}: x should be 'level_{i}'"

    # Rollback one by one and verify
    for rollback_count in range(10):
        expected_before = f"level_{9 - rollback_count}"
        assert db.get("x") == expected_before, (
            f"Before rollback {rollback_count + 1}: x should be '{expected_before}'"
        )
        db.rollback()
        if rollback_count < 9:
            expected_after = f"level_{8 - rollback_count}"
            assert db.get("x") == expected_after, (
                f"After rollback {rollback_count + 1}: x should be '{expected_after}'"
            )
        else:
            assert db.get("x") == "initial", (
                "After all rollbacks: x should be 'initial'"
            )
    print("✓ Test 4 passed")

    # Test 5: 10 levels deep - commit all at once
    print("\nTest 5: 10 levels deep - commit all at once")
    db = KeyValueDB()
    db.set("base", "value")

    for i in range(10):
        db.begin()
        db.set(f"tx_{i}", f"val_{i}")
        db.set("base", f"updated_{i}")

    assert db.get("base") == "updated_9", "Before commit: base should be 'updated_9'"
    assert len(db.transaction_stack) == 10, "Should have 10 transactions"

    db.commit()
    assert len(db.transaction_stack) == 0, "After commit: should have no transactions"

    for i in range(10):
        assert db.get(f"tx_{i}") == f"val_{i}", (
            f"After commit: tx_{i} should be 'val_{i}'"
        )
    assert db.get("base") == "updated_9", "After commit: base should be 'updated_9'"
    print("✓ Test 5 passed")

    # Test 6: 10 levels deep - delete operations
    print("\nTest 6: 10 levels deep - delete operations")
    db = KeyValueDB()
    db.set("persist", "keep")
    db.set("delete_me", "remove")

    # Create 10 transactions, delete at level 6 (index 5)
    for i in range(10):
        db.begin()
        if i == 5:
            db.delete("delete_me")
        db.set(f"temp_{i}", f"data_{i}")

    # At level 10, delete_me should be marked as deleted
    try:
        db.get("delete_me")
        assert False, "At level 10: delete_me should not be accessible"
    except KeyError:
        pass

    # Rollback to before deletion (rollback 5 transactions)
    for i in range(5):
        db.rollback()

    assert db.get("delete_me") == "remove", (
        "After rollback to before delete: delete_me should exist"
    )

    # Now add back transactions and delete again, then commit all
    for i in range(5):
        db.begin()
        if i == 0:  # Delete in the first of the new transactions
            db.delete("delete_me")
        db.set(f"temp_{i + 5}", f"data_{i + 5}")

    # Verify delete_me is marked as deleted
    try:
        db.get("delete_me")
        assert False, "After re-adding transactions: delete_me should be deleted"
    except KeyError:
        pass

    # Commit all (including the delete)
    db.commit()

    assert db.get("persist") == "keep", "After commit: persist should still exist"
    try:
        db.get("delete_me")
        assert False, "After commit: delete_me should be deleted"
    except KeyError:
        pass
    print("✓ Test 6 passed")

    # Test 7: Maximum depth enforcement
    print("\nTest 7: Maximum depth enforcement")
    db = KeyValueDB()
    for i in range(10):
        db.begin()

    try:
        db.begin()  # Should fail - exceeds max depth
        assert False, "Should raise exception for exceeding max depth"
    except Exception as e:
        assert "Maximum transaction depth exceeded" in str(e), (
            f"Expected depth error, got: {e}"
        )
    print("✓ Test 7 passed")

    # Test 8: Complex nested scenario - commit and rollback mix
    print("\nTest 8: Complex nested scenario - commit and rollback mix")
    db = KeyValueDB()
    db.set("global", "g")

    # Create 5 levels
    for i in range(5):
        db.begin()
        db.set("x", str(i))
        db.set(f"level_{i}", str(i))

    assert db.get("x") == "4", "At level 5: x should be '4'"

    # Rollback 2 levels
    db.rollback()
    db.rollback()
    assert db.get("x") == "2", "After 2 rollbacks: x should be '2'"

    # Commit remaining (should commit 3 transactions)
    db.commit()
    assert db.get("x") == "2", "After commit: x should be '2'"
    assert db.get("level_0") == "0", "After commit: level_0 should exist"
    assert db.get("level_1") == "1", "After commit: level_1 should exist"
    assert db.get("level_2") == "2", "After commit: level_2 should exist"

    try:
        db.get("level_3")
        assert False, "level_3 should not exist (was rolled back)"
    except KeyError:
        pass
    print("✓ Test 8 passed")

    # Test 9: Nested transactions with inheritance
    print("\nTest 9: Nested transactions with inheritance")
    db = KeyValueDB()
    db.begin()
    db.set("parent", "p1")
    db.set("shared", "s1")

    db.begin()
    assert db.get("parent") == "p1", "Child should inherit parent key"
    assert db.get("shared") == "s1", "Child should inherit shared key"
    db.set("child", "c1")
    db.set("shared", "s2")

    db.begin()
    assert db.get("parent") == "p1", "Grandchild should inherit parent key"
    assert db.get("shared") == "s2", "Grandchild should see child's shared value"
    assert db.get("child") == "c1", "Grandchild should inherit child key"
    db.set("grandchild", "gc1")

    db.commit()
    assert db.get("parent") == "p1", "After commit: parent should exist"
    assert db.get("shared") == "s2", "After commit: shared should be 's2'"
    assert db.get("child") == "c1", "After commit: child should exist"
    assert db.get("grandchild") == "gc1", "After commit: grandchild should exist"
    print("✓ Test 9 passed")

    # Test 10: Edge case - rollback outside transaction
    print("\nTest 10: Edge case - rollback outside transaction")
    db = KeyValueDB()
    try:
        db.rollback()
        assert False, "Should raise exception for rollback outside transaction"
    except Exception as e:
        assert "No Active Transaction" in str(e), (
            f"Expected no transaction error, got: {e}"
        )
    print("✓ Test 10 passed")

    # Test 11: Edge case - commit outside transaction
    print("\nTest 11: Edge case - commit outside transaction")
    db = KeyValueDB()
    try:
        db.commit()
        assert False, "Should raise exception for commit outside transaction"
    except Exception as e:
        assert "No Active Transaction" in str(e), (
            f"Expected no transaction error, got: {e}"
        )
    print("✓ Test 11 passed")

    # Test 12: 10 levels - get from global through all levels
    print("\nTest 12: 10 levels - get from global through all levels")
    db = KeyValueDB()
    db.set("global_key", "global_value")

    for i in range(10):
        db.begin()
        # Don't set global_key in any transaction
        assert db.get("global_key") == "global_value", (
            f"Level {i + 1}: should see global_key"
        )

    # All transactions should see the global value
    for i in range(10):
        assert db.get("global_key") == "global_value", (
            f"At depth {10 - i}: should see global_key"
        )
        db.rollback()

    assert db.get("global_key") == "global_value", (
        "After all rollbacks: should still see global_key"
    )
    print("✓ Test 12 passed")

    print("\n" + "=" * 60)
    print("ALL NESTED TRANSACTION TESTS PASSED! ✓")
    print("=" * 60)
