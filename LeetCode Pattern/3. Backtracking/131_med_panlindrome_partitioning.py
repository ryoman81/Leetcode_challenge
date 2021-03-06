'''
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
     The method uses backtracking and follows the template
     However, this answer can be improved by using DP to store the panlindrome met before
     Template:
      - State variable: start - the starting index of solution space
      - State: path[] - record current valid result along recursion
      - Choices: from start to the end of string
      - Pruning: if the current substring is not a panlindrome, no need to recursion further
  Complexity:
    Time: O()
    Space: O()
  '''
  def partition(self, s):
    result = []
    path = []

    def backtracking(start):
      # base case
      if start == len(s):
        result.append(path[:])
      # search solution space from start to the end of string
      for i in range(start, len(s)):
        substr = s[start:i+1]
        # prune if the current substr is not validate
        if not self.validate(substr):
          continue
        # set state
        path.append(substr)
        # do backtracking
        backtracking(i+1)
        # reset state
        path.pop()
        
    backtracking(0)
    return result

  # A helper function (actually my AMAZON interview question!!!) to check if palindrome
  # two pointer solution (no need to check if even or odd)
  # simular to question 9
  def validate(self, str):
    left = 0
    right = len(str) - 1
    while left < right:
      if str[left] != str[right]:
        return False
      left += 1
      right -= 1
    return True

## Run code after defining input and solver
input = "aab"
solver = Solution().partition
print(solver(input))