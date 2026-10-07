class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(s):
            count = 0
            for ch in s:
                if ch == "(":
                    count += 1
                elif ch == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        queue = [s]
        visited = {s}
        while queue:
            result = []
            for curr in queue:
                if is_valid(curr):
                    result.append(curr)
            if result:
                return result
            next_level = []
            for curr in queue:
                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue
                    new_string = curr[:i] + curr[i + 1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.append(new_string)
            queue = next_level

        return [""]