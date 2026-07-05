class Solution(object):
    def pathsWithMaxScore(self, board):
        n = len(board)
        mod = 10**9 + 7
        
        memo = {}

        def maxval(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
                
            if r >= n or c >= n or board[r][c] == 'X':
                return -float('inf'), 0

            if board[r][c] == 'S':
                return 0, 1

            cur = int(board[r][c]) if board[r][c] != 'E' else 0

            down = maxval(r + 1, c)
            right = maxval(r, c + 1)
            dia = maxval(r + 1, c + 1)

            scr = max(down[0], right[0], dia[0])

            if scr == -float('inf'):
                memo[(r, c)] = (-float('inf'), 0)
                return memo[(r, c)]

            bst_pt = 0

            if down[0] == scr:
                bst_pt += down[1]
            if right[0] == scr:
                bst_pt += right[1]
            if dia[0] == scr:
                bst_pt += dia[1]

            memo[(r, c)] = (cur + scr, bst_pt % mod)
            return memo[(r, c)]


        ans_s, ans_p = maxval(0, 0)

        if ans_s == -float('inf'):
            return [0, 0]
            
        return [ans_s, ans_p]