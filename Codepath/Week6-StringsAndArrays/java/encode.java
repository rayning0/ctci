/*
 * Problem: Given an input string, write a function that returns the run-length encoded string for the input string.
 *
 * Example:
 * Input: "wwwwaaadexxxxxx"
 * Output: "w4a3d1e1x6"
*/
public String encode(String s)
{
    char[] arr = s.toCharArray();
    StringBuilder sb = new StringBuilder();

    int i = 0, j = 1;
    while(i < arr.length)
    {
        int count = 1;
        while(j < arr.length && arr[i] == arr[j])
        {
            j++;
            count++;
        }

        if(count > 1)
        {
            sb.append(count);
            sb.append(arr[i]);
        }
        else{
            sb.append(arr[i]);
        }

        if(sb.length() > s.length())
        {
            break;
        }

        i = j;
        j = i + 1;
    }

    return sb.toString();
}
