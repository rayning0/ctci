/*
 * Problem: Given an array of size n and a number x, determine the first two elements in the array, if any, whose sum is exactly x.
*/
public int[] findPairs(int[] arr, int sum) {
    Set<Integer> set = new HashSet();
    for (int i=0; i < arr.length; i++) {
        if (set.contains(sum - arr[i])) {
            int[] pair = {arr[i], sum - arr[i]};
            return pair;
        } else {
            set.add(arr[i]);
        }
    }
    return null;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
