// https://www.hackerrank.com/challenges/new-year-chaos/problem
func minimumBribes(q []int32) {
    swaps := 0
    r := make([]int32, len(q))
    start := int32(1)
    for i := range r {
        r[i] = start
        start++
    }
    // fmt.Println(q)
    for i := int32(0); i < int32(len(q)); i++ {
        if q[i] == r[i] {
            continue
        }
        if len(q) > 1 && i < int32(len(q)) - 1 && q[i] == r[i+1] {
            swaps++
            r[i], r[i+1] = r[i+1], r[i]
            // fmt.Println(r, swaps)
            continue
        } else if len(q) > 2 && i < int32(len(q)) - 2 && q[i] == r[i + 2] {
            swaps += 2
            r[i + 2] = r[i + 1]
            r[i + 1] = r[i]
            r[i] = q[i]
            // fmt.Println(r, swaps)
            continue
        } else if len(q) > 3 && i < int32(len(q)) - 3 && q[i] >= r[i + 3] {
            fmt.Println("Too chaotic")
            return
        }

    }
    fmt.Println(swaps)
}
