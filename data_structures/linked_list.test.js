// Run only tests in this file:
// npm test -- data_structures/linked_list.test.js

// Reference: https://www.geeksforgeeks.org/implementation-linkedlist-javascript/

// https://www.javascripttutorial.net/es6/javascript-class/
// JavaScript classes are syntactic sugar over the prototypal inheritance. ES6 classes are just special functions.

// Old ES5 way:
// function Person(name) {
//     this.name = name
// }
// Person.prototype.getName = function() {
//     return this.name
// }
// var john = new Person("John")
// console.log(john.getName())

// ES6 way:
// class Person {
//   constructor(name) {
//     this.name = name
//   }
//   getName() {
//     return this.name
//   }
// }
// const john = new Person("John")
// console.log(john.getName())

class Node {
  constructor(val) {
    this.val = val
    this.next = null
  }
}

class LList {
  constructor() {
    this.head = null
  }

  isEmpty() {
    if (this.size() === 0) {
      return true
    }
    return false
  }

  // add to end
  append(val) {
    let newNode = new Node(val)

    if (this.head === null) {
      this.head = newNode
    } else {
      let current = this.head
      while (current.next) {  // "current.next !== null" is more precise
        current = current.next
      }
      current.next = newNode
    }

    return this
  }

  to_list(array) {
    let list = new LList()
    array.forEach((val) => {
      list.append(val)
    })
    return list
  }

  // add to start
  prepend(val) {
    let newNode = new Node(val)
    newNode.next = this.head
    this.head = newNode

    return this
  }

  size() {
    let count = 0
    if (this.head) {
      let current = this.head
      while(current) {
        current = current.next
        count++
      }
    }
    return count
  }

  // change list to array
  to_a() {
    let current = this.head,
        array = []

    while(current) {
      array.push(current.val)
      current = current.next
    }
    console.log(array)

    return array
  }

  // return first node with this value
  findByVal(val) {
    let current = this.head
    while(current) {
      if (current.val === val) {
        return current
      }
      current = current.next
    }
    return "Value not found"
  }

  findByIndex(index) {
    if (index >= this.size() || index < 0) {
      return "Index out of bounds"
    }
    let current = this.head,
        count = 0

    while(current) {
      if (count === index) {
        return current
      }
      current = current.next
      count++
    }
  }

  indexOf(val) {
    let current = this.head,
        count = 0

    while(current) {
      if (current.val === val) {
        return count
      }
      current = current.next
      count++
    }
    return "Value not found"
  }

  insert(index, val) {
    if (index >= this.size() || index < 0) {
      return "Index out of bounds"
    }

    let newNode = new Node(val),
        current = this.head,
        count = 0

    while(count < index) {
      current = current.next
      count++
    }

    let nextNode = current.next
    current.next = newNode
    newNode.next = nextNode

    return this
  }

  deleteAt(index) {
    if (index >= this.size() || index < 0) {
      return "Index out of bounds"
    }

    let current = this.head,
        count = 0,
        previous

    if (index == 0) {
      this.head = current.next
      current.next = null
      return this
    }

    while(count < index) {
      previous = current
      current = current.next
      count++
    }

    let nextNode = current.next
    current.next = null
    previous.next = nextNode

    return this
  }

  // delete first node with this value
  deleteVal(val) {
    let current = this.head,
        previous = null

    while(current) {
      if(current.val === val) {

        if(previous === null) { // delete head node
          this.head = current.next
        } else {
          previous.next = current.next
        }
        current.next = null

        return this
      }

      previous = current
      current = current.next
    }

    return "Value not found"
  }

  // reverse linked list by convert to array first.
  // Complexity: O(n) time, O(n) space. Uses more memory.
  reverseArray() {
    let reversed = new LList()
    this.to_a().reverse().forEach((val) => {
      reversed.append(val)
    })

    return reversed
  }

  // Reverse linked list in place (iterative way). Use 3 pointers: previous, current, next.
  // Good video explanation: https://www.youtube.com/watch?v=myqO52fwY5k
  // https://www.geeksforgeeks.org/reverse-a-linked-list/
  // Complexity: O(n) time, O(1) space
  reverse() {
    let previous = null,
        current = this.head,
        next = current?.next || null

    // console.log(`*previous: ${previous}, current: ${current?.val || null}, next: ${next?.val || null}`)

    while(current) {
      current.next = previous // point back to last node
      previous = current
      current = next
      next = next?.next || null

      // console.log(`previous: ${previous?.val || null}, current: ${current?.val || null}, next: ${next?.val || null}`)
    }

    this.head = previous
    return this
  }

  // Reverse linked list in place (recursive way)
  // Best video explanation: https://www.youtube.com/watch?v=Ip4y7Inx7QY
  // Complexity: O(n) time, O(1) space
  recursiverse() {
    this.head = this.recursive(this.head)
    return this
  }

  recursive(current) {
    // console.log(`Down recursive ladder: current = ${current?.val || null}`)

    if(current === null || current.next === null) {
      // console.log(`Bottom of recursion. Start of new_head = ${current?.val || null}`)
      return current
    }

    let new_head = this.recursive(current.next)
    // console.log(`Up recursive ladder: old current = ${current?.val || null}`)

    // Next node points BACK to current node as we go up recursive ladder. Reverses pointer.
    current.next.next = current
    // This gets overwritten by last line as we go up recursive ladder
    current.next = null

    // let h = new LList()
    // h.head = new_head
    // console.log(`Up recursive ladder: new_head, after pointer reversed: ${h.to_a()}`)

    return new_head
  }
}

let list

describe("Linked List function tests", () => {
  beforeEach(() => {
    list = (new LList()).to_list(["a", "b", "c"])
  })

  it("says if linked list is empty", () => {
    list2 = new LList()
    expect(list2.isEmpty()).toBe(true)
    expect(list.isEmpty()).toBe(false)
  })

  it("append() adds value to end of linked list", () => {
    expect(list.head.val).toBe("a")
    expect(list.head.next.val).toBe("b")
    expect(list.head.next.next.val).toBe("c")
    expect(list.append("d").to_a()).toEqual(["a", "b", "c", "d"])
    expect(list.head.next.next.next.next).toBe(null)
  })

  it("creates linked list from array", () => {
    list2 = new LList()
    expect(list2.to_list([]).to_a()).toEqual([])
    expect(list2.to_list(["a"]).to_a()).toEqual(["a"])
    expect(list2.to_list(["a", "b", "c"]).to_a()).toEqual(["a", "b", "c"])
  })

  it("prepend() adds value to start of linked list", () => {
    expect(list.prepend("e").to_a()).toEqual(["e", "a", "b", "c"])
    expect(list.prepend("d").to_a()).toEqual(["d", "e", "a", "b", "c"])
    expect(list.head.next.next.val).toBe("a")
  })

  it("finds linked list size", () => {
    expect(list.size()).toBe(3)
  })

  it("prints linked list as array", () => {
    expect(list.to_a()).toEqual(["a", "b", "c"])
  })

  it("finds first node with certain value", () => {
    expect(list.findByVal("d")).toBe("Value not found")
    expect(list.findByVal("c")).toEqual({ val: 'c', next: null })
    expect(list.findByVal("b")).toEqual({ val: 'b', next: { val: 'c', next: null } })
  })

  it("finds node by index", () => {
    expect(list.findByIndex(3)).toBe("Index out of bounds")
    expect(list.findByIndex(2)).toEqual({ val: 'c', next: null })
    expect(list.findByIndex(1)).toEqual({ val: 'b', next: { val: 'c', next: null } })
  })

  it("finds index by value", () => {
    expect(list.indexOf("d")).toBe("Value not found")
    expect(list.indexOf("c")).toBe(2)
  })

  it("at index, inserts value", () => {
    expect(list.insert(3, "d")).toBe("Index out of bounds")
    expect(list.insert(-1, "d")).toBe("Index out of bounds")
    expect(list.insert(0, "d").to_a()).toEqual(["a", "d", "b", "c"])
    expect(list.insert(1, "e").to_a()).toEqual(["a", "d", "e", "b", "c"])
    expect(list.insert(4, "f").to_a()).toEqual(["a", "d", "e", "b", "c", "f"])
  })

  it("deletes node at index", () => {
    expect(list.deleteAt(3)).toBe("Index out of bounds")
    expect(list.deleteAt(0).to_a()).toEqual(["b", "c"])
    expect(list.prepend("a").deleteAt(1).to_a()).toEqual(["a", "c"])
    expect(list.deleteAt(1).to_a()).toEqual(["a"])
    expect(list.deleteAt(0).to_a()).toEqual([])
  })

  it("deletes first node with certain value", () => {
    expect(list.deleteVal("d")).toBe("Value not found")
    expect(list.deleteVal("a").to_a()).toEqual(["b", "c"])
    expect(list.prepend("a").deleteVal("b").to_a()).toEqual(["a", "c"])
    expect(list.insert(0, "b").deleteVal("c").to_a()).toEqual(["a", "b"])
    expect(list.deleteVal("b").deleteVal("a").to_a()).toEqual([])
  })

  it("reverses linked list after first converting to array", () => {
    expect(list.reverseArray().to_a()).toEqual(["c", "b", "a"])
    expect(list.reverseArray().reverseArray().to_a()).toEqual(["a", "b", "c"])
    expect(list.append("d").reverseArray().to_a()).toEqual(["d", "c", "b", "a"])
  })

  it("iteratively reverses linked list in place", () => {
    list2 = new LList()
    expect(list2.reverse().to_a()).toEqual([])
    expect(list2.append("a").reverse().to_a()).toEqual(["a"])
    expect(list2.append("b").reverse().to_a()).toEqual(["b", "a"])

    expect(list.reverse().to_a()).toEqual(["c", "b", "a"])
    expect(list.reverse().to_a()).toEqual(["a", "b", "c"])
    expect(list.append("d").reverse().to_a()).toEqual(["d", "c", "b", "a"])
    expect(list.reverse().reverse().to_a()).toEqual(["d", "c", "b", "a"])
  })

  it("recursively reverses linked list in place", () => {
    list2 = new LList()
    expect(list2.recursiverse().to_a()).toEqual([])
    expect(list2.append("a").recursiverse().to_a()).toEqual(["a"])
    expect(list2.append("b").recursiverse().to_a()).toEqual(["b", "a"])

    expect(list.recursiverse().to_a()).toEqual(["c", "b", "a"])
    expect(list.recursiverse().to_a()).toEqual(["a", "b", "c"])
    expect(list.append("d").recursiverse().to_a()).toEqual(["d", "c", "b", "a"])
    expect(list.recursiverse().recursiverse().to_a()).toEqual(["d", "c", "b", "a"])
  })
})

// OUTPUT of iterative reverse() for ["a", "b", "c"] linked list:

// previous: null, current: a, next: b
// previous: a, current: b, next: c
// previous: b, current: c, next: null
// previous: c, current: null, next: null
// [ 'c', 'b', 'a' ]

// OUTPUT of recursive recursiverse() for ["a", "b", "c"] linked list:

// Down recursive ladder: current = a
// Down recursive ladder: current = b
// Down recursive ladder: current = c
// Bottom of recursion. Start of new_head = c
// Up recursive ladder: old current = b
// Up recursive ladder: new_head, after pointer reversed: c,b
// Up recursive ladder: old current = a
// Up recursive ladder: new_head, after pointer reversed: c,b,a
__________________________________________________
// OUTPUT of all functions:

// > l = new LList()
// LList { head: null }
// > l.append(5)
// LList { head: Node { val: 5, next: null } }
// > l.append(10)
// LList { head: Node { val: 5, next: Node { val: 10, next: null } } }
// > l.append(15)
// LList { head: Node { val: 5, next: Node { val: 10, next: [Node] } } }
// > l.to_a()
// [ 5, 10, 15 ]

// > m = new LList()
// LList { head: null }
// > m.to_list([1,2,3])
// LList { head: Node { val: 1, next: Node { val: 2, next: [Node] } } }
// > m.to_list([1,2,3]).to_a()
// [ 1, 2, 3 ]
// > l.size()
// 3
// > m
// LList { head: null }
// > m.isEmpty()
// true
// > l.isEmpty()
// false
// > l.prepend(4)
// LList { head: Node { val: 4, next: Node { val: 5, next: [Node] } } }
// > l.size()
// 4
// > l.findByVal(10)
// Node { val: 10, next: Node { val: 15, next: null } }
// > l.findByIndex(4)
// 'Index out of bounds'
// > l.findByIndex(3)
// Node { val: 15, next: null }
// > l.findByVal(100)
// 'Value not found'
// > l.to_a()
// [ 4, 5, 10, 15 ]
// > l.insert(0, 20)
// LList { head: Node { val: 4, next: Node { val: 20, next: [Node] } } }
// > l.deleteAt(2).to_a()
// [ 4, 20, 10, 15 ]
// > l.deleteAt(2).to_a()
// [ 4, 20, 15 ]
// > l.deleteVal(4).to_a()
// [ 20, 15 ]
// > l.append(5).to_a()
// [ 20, 15, 5 ]
// > l.to_a()
// [ 20, 15, 5 ]
// > x = l.reverseArray()
// LList { head: Node { val: 5, next: Node { val: 15, next: [Node] } } }
// > x.to_a()
// [ 5, 15, 20 ]
// > l
// LList { head: Node { val: 20, next: Node { val: 15, next: [Node] } } }
// > l.reverse()
// LList { head: Node { val: 5, next: Node { val: 15, next: [Node] } } }
// > l.reverse()
// LList { head: Node { val: 20, next: Node { val: 15, next: [Node] } } }
// > l.append(1)
// LList { head: Node { val: 20, next: Node { val: 15, next: [Node] } } }
// > l.prepend(25)
// LList { head: Node { val: 25, next: Node { val: 20, next: [Node] } } }
// > l.to_a()
// [ 25, 20, 15, 5, 1 ]
// > l.reverse()
// LList { head: Node { val: 1, next: Node { val: 5, next: [Node] } } }
// > l.to_a()
// [ 1, 5, 15, 20, 25 ]
// > l.append(30)
// LList { head: Node { val: 1, next: Node { val: 5, next: [Node] } } }
// > l.recursiverse().to_a()
// [ 30, 25, 20, 15, 5, 1 ]
// > l.recursiverse().to_a()
// [ 1, 5, 15, 20, 25, 30 ]
