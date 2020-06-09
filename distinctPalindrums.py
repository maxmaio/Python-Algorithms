# Python3 implementation of the approach  
  

  
# Function to return the count  
# of distinct palindromic sub-strings  
# of the given string s  
def palindromeSubStrs(s) :  
  
    # To store the positions of  
    # palindromic sub-strings  
    dp = [[0 for x in range(len(s))] for y in range(len(s))]
      
    # Map to store the sub-strings  
    m = {};  
      
    for i in range(len(s)) : 
  
        # Sub-strings of length 1 are palindromes  
        dp[i][i] = 1;  
  
        # Store continuous palindromic sub-strings  
        m[s[i: i + 1]] = 1;  
      
  
    # Store palindromes of size 2  
    for i in range(len(s)- 1) :  
        if (s[i] == s[i + 1]) : 
            dp[i][i + 1] = 1;  
            m[ s[i : i + 2]] = 1;  
           
  
        # If str[i...(i+1)] is not a palindromic  
        # then set dp[i][i + 1] = 0  
        else : 
            dp[i][i + 1] = 0;  
  
    # Find palindromic sub-strings of length>=3  
    for length in range(3,len(s) + 1) :  
        for st in range(len(s) - length + 1) : 
  
            # End of palindromic substring  
            end = st + length - 1;  
  
            # If s[start] == s[end] and  
            # dp[start+1][end-1] is already palindrome  
            # then s[start....end] is also a palindrome  
            if (s[st] == s[end] and dp[st + 1][end - 1]) : 
  
                # Set dp[start][end] = 1  
                dp[st][end] = 1;  
                m[s[st : end + 1]] = 1;  
  
            # Not a palindrome  
            else : 
                dp[st][end] = 0; 
  
    # Return the count of distinct palindromes  
    return len(m);  
  
  
# Driver code  
if __name__ == "__main__" :  
  
    s = "abaaa";  
    print(palindromeSubStrs(s));  