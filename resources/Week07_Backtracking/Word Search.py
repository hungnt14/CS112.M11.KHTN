class Solution(object):
   def exist(self, board, word):
      n =len(board)
      m = len(board[0])
      for i in range(n):
         for j in range(m):
            if word[0] == board[i][j]:
               if self.find(board,word,i,j):
                  return True
      return False
   def find(self, board,word,row,col,i=0):
      if i== len(word):
         return True
      if row>= len(board) or row <0 or col >=len(board[0]) or col<0 or word[i]!=board[row][col]:
         return False
      board[row][col] = '*'
      res = self.find(board,word,row+1,col,i+1) or self.find(board,word,row-1,col,i+1) or self.find(board,word,row,col+1,i+1) or self.find(board,word,row,col-1,i+1)
      board[row][col] = word[i]
      return res

board = input()[3:-3].split("\'], [\'")
board = [a.split("\', \'") for a in board]
word = input()

if Solution().exist(board, word):
    print("true")
else:
    print("false")