# i: n -> the number of parenthesis i can use in a singular string
# o: res -> a list of the possible strings you can make with n parentheses

# while i <= n, i can add open parenthesis
# on every iteration of dfs i have the choice to add a open or closed parentheses
# if i > n: i should add the current sequence


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        curr = []
        def dfs(opens: int, closes: int):
            if opens == n and closes == n:
                res.append("".join(curr))
                return

            if opens < n:
                curr.append("(")
                dfs(opens + 1, closes)
                curr.pop()

            if closes < opens:
                curr.append(")")
                dfs(opens, closes + 1)
                curr.pop()

        dfs(0, 0)
        return res
            