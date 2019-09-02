/*
 * Problem: Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
 *
 * Example 1:
 * Input: [1, 2, 5, 3, 7, 10, 9, 12]
 * Output: 5
 * Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
 *
 * Example 2:
 * Input: [1, 3, 2, 0, -1, 7, 10]
 * Output: 5
 * Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
*/
public int sort(int[] arr)
{
   //Step 1: Initialize the two Pointers
  int low = 0, high = arr.length - 1;

  // Step 2: find the first number out of sorting order from the beginning
  while (low < arr.length - 1 && arr[low] <= arr[low + 1])
    low++;

  if (low == arr.length - 1) // if the array is sorted
    return 0;

  // Step 3: find the first number out of sorting order from the end
  while (high > 0 && arr[high] >= arr[high - 1])
    high--;

  // Step 4: find the maximum and minimum of the subarray
  int subarrayMax = Integer.MIN_VALUE, subarrayMin = Integer.MAX_VALUE;
  for (int k = low; k <= high; k++) {
    subarrayMax = Math.max(subarrayMax, arr[k]);
    subarrayMin = Math.min(subarrayMin, arr[k]);
  }

  // Step 5: extend the subarray to include any number which is bigger than the minimum of the subarray
  while (low > 0 && arr[low - 1] > subarrayMin)
    low--;

  // Step 6: extend the subarray to include any number which is smaller than the maximum of the subarray
  while (high < arr.length - 1 && arr[high + 1] < subarrayMax)
    high++;

  return high - low + 1;
}
