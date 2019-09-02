# Problem: Given an array of size n and a number x, determine the first two elements in the array, if any, whose sum is exactly x.
def findPairs(arr, sum):
   h = set()
   for i in range(0, len(arr)):
     if (sum - arr[i]) in h:
       return ([arr[i], sum - arr[i]])
     else:
         h.add(arr[i])
   return null

# Time Complexity: O(n)
# Space Complexity: O(n)
