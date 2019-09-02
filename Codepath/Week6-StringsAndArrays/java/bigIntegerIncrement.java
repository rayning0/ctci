/*
 * Problem: Implement a function to increment an arbitrary precision integer represented in the form of an array, where each element in the array corresponds to a digit.
 *
 * Examples:
 * Input: [1,2,3]
 * Output: [1,2,4]

 * Explanation: 123 + 1 = 124
 *
 * Input: [5,8,9]
 * Output: [5,9,0]

 * Explanation: 589 + 1 = 590
*/
public int[] bigIntegerIncrement(int[] arr)
{
    int len = arr.length;
    boolean allNines = true;
    for(int i = 0; i < len; i++)
    {
        if(arr[i] != 9)
        {
            allNines = false;
            break;
        }
    }

    int[] result = (allNines == true) ? new int[len + 1] : new int[len];

    int sum = arr[len - 1] + 1;
    int carry = sum / 10;
    result[result.length - 1] = sum % 10;

    int ptr1 = len - 2;
    int ptr2 = result.length - 2;

    while(ptr1 >= 0)
    {
        sum = arr[ptr1] + carry;
        carry = sum / 10;
        result[ptr2] = sum % 10;
        ptr1--;
        ptr2--;
    }

    if(allNines)
    result[0] = 1;

    return result;
}
