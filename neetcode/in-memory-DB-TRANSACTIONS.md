# Transaction Model Explanation
For [in-memory key-value DB problem](https://github.com/rayning0/ctci/blob/master/neetcode/in-memory-key-value-DB.py).

## When Data Changes Happen "Outside of Transactions"

Data changes happen **outside of transactions** when:
1. **No transaction is active** (i.e., `transaction_stack` is empty)
2. You call `set()`, `delete()`, or `get()` **before any `begin()`** is called
3. You call `set()`, `delete()`, or `get()` **after all transactions are committed or rolled back**

### Example: Operations Outside Transactions

```python
db = KeyValueDB()

# No transaction active - changes go directly to global_store
db.set("x", "1")        # ✅ Immediately written to global_store
db.set("y", "2")        # ✅ Immediately written to global_store
print(db.get("x"))      # ✅ Reads from global_store: "1"

db.begin()              # Now we're inside a transaction
db.set("x", "3")        # ⚠️ Written to transaction_stack[-1], NOT global_store
db.commit()             # Now "x" = "3" is written to global_store

# Transaction ended - back to outside transactions
db.set("z", "4")        # ✅ Immediately written to global_store
```

## Global Store vs Transaction Stack

### `global_store` (Permanent)
- **Purpose**: Stores committed data that persists across the database lifetime
- **When it's updated**:
  - Directly when operations happen **outside** any transaction
  - When `commit()` is called (all transaction changes are merged into global_store)
- **Lifetime**: Exists for the entire lifetime of the `KeyValueDB` instance
- **Scope**: Shared by all transactions - acts as the "database"

### `transaction_stack` (Temporary)
- **Purpose**: Stack of temporary transaction contexts, each with its own local store
- **When it's updated**:
  - New transaction added when `begin()` is called
  - Transaction removed when `rollback()` or `commit()` is called
- **Lifetime**:
  - Created when `begin()` is called
  - Destroyed when `rollback()` or `commit()` is called
- **Scope**: Each transaction is isolated - changes are local until commit

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    KeyValueDB Instance                   │
│                                                           │
│  ┌──────────────────┐         ┌──────────────────────┐  │
│  │  global_store    │         │  transaction_stack   │  │
│  │  (Permanent)     │         │  (Temporary)         │  │
│  │                  │         │                      │  │
│  │  {"x": "1",      │         │  [                   │  │
│  │   "y": "2"}      │         │    {                 │  │
│  │                  │         │      "x": "3",       │  │
│  │  ✅ Persists     │         │      "z": "4"        │  │
│  │  ✅ Shared       │         │    },                 │  │
│  │  ✅ Committed    │         │    {                 │  │
│  └──────────────────┘         │      "a": "5"        │  │
│                               │    }                  │  │
│                               │  ]                    │  │
│                               │  ⚠️ Temporary         │  │
│                               │  ⚠️ Isolated         │  │
│                               │  ⚠️ Discarded on     │  │
│                               │     rollback         │  │
│                               └──────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## Detailed Examples

### Example 1: Outside Transaction (Direct to Global)

```python
db = KeyValueDB()

# transaction_stack is empty []
# All operations go directly to global_store

db.set("name", "Alice")     # global_store = {"name": "Alice"}
db.set("age", "30")         # global_store = {"name": "Alice", "age": "30"}
print(db.get("name"))       # Reads from global_store: "Alice"

# These changes are PERMANENT and IMMEDIATE
```

### Example 2: Inside Transaction (Temporary)

```python
db = KeyValueDB()
db.set("name", "Alice")     # global_store = {"name": "Alice"}

db.begin()                   # transaction_stack = [{}]
db.set("name", "Bob")        # transaction_stack = [{"name": "Bob"}]
                             # global_store still = {"name": "Alice"}

print(db.get("name"))        # Reads from transaction_stack: "Bob"
                             # (transaction overrides global_store)

db.rollback()                # transaction_stack = []
print(db.get("name"))        # Reads from global_store: "Alice"
                             # Transaction changes were DISCARDED
```

### Example 3: Commit (Temporary → Permanent)

```python
db = KeyValueDB()
db.set("x", "1")             # global_store = {"x": "1"}

db.begin()                   # transaction_stack = [{}]
db.set("x", "2")             # transaction_stack = [{"x": "2"}]
db.set("y", "3")             # transaction_stack = [{"x": "2", "y": "3"}]

db.commit()                  # Merges transaction into global_store
                             # global_store = {"x": "2", "y": "3"}
                             # transaction_stack = []

print(db.get("x"))           # Reads from global_store: "2"
print(db.get("y"))           # Reads from global_store: "3"
```

### Example 4: Nested Transactions

```python
db = KeyValueDB()
db.set("x", "1")             # global_store = {"x": "1"}

db.begin()                   # transaction_stack = [{}]
db.set("x", "2")             # transaction_stack = [{"x": "2"}]

db.begin()                   # transaction_stack = [{}, {}]
db.set("x", "3")             # transaction_stack = [{}, {"x": "3"}]
                             # Top transaction overrides parent

print(db.get("x"))           # Reads from top transaction: "3"

db.rollback()                 # transaction_stack = [{}]
print(db.get("x"))           # Reads from parent transaction: "2"

db.commit()                   # Merges parent transaction to global_store
                             # global_store = {"x": "2"}
                             # transaction_stack = []
```

## Key Takeaways

1. **Outside transactions** = `transaction_stack` is empty → changes go directly to `global_store`
2. **Inside transactions** = `transaction_stack` has items → changes go to top transaction's local store
3. **global_store** = Permanent, shared, committed data
4. **transaction_stack** = Temporary, isolated, uncommitted changes
5. **commit()** = Moves all transaction changes to `global_store`, then clears `transaction_stack`
6. **rollback()** = Discards top transaction, removing it from `transaction_stack`

## Visual Timeline

```
Time →  Operations                    global_store      transaction_stack
─────────────────────────────────────────────────────────────────────────
t1      set("x", "1")                 {"x": "1"}       []
t2      begin()                       {"x": "1"}       [{}]
t3      set("x", "2")                 {"x": "1"}       [{"x": "2"}]
t4      begin()                       {"x": "1"}       [{}, {}]
t5      set("x", "3")                 {"x": "1"}       [{}, {"x": "3"}]
t6      rollback()                    {"x": "1"}       [{}]
t7      commit()                      {"x": "2"}       []
t8      set("y", "4")                 {"x": "2",       []
                                      "y": "4"}
```

