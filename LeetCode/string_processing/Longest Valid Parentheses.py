def longestValidParentheses(s: str) -> int:
    maxes = [0]

    i = 0
    while i < len(s):
        c = s[i]

        if c == '(':
            left_unmatched = 0
            head = i
            for j in range(head, len(s)):
                if s[j] == '(':
                    left_unmatched += 1
                else:
                    left_unmatched -= 1

                if left_unmatched == 0:
                    maxes.append(j - head + 1)
                    i = j
                elif left_unmatched < 0:
                    break

        i += 1

    return max(maxes)


if __name__ == '__main__':
    # print(longestValidParentheses("()()"))
    # print(longestValidParentheses(")()())"))
    # print(longestValidParentheses(""))
    # print(longestValidParentheses(")()())()()("))
    # print(longestValidParentheses(")(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((("
    #                               ")))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()("
    #                               ")(())))((()))()))())"))
    print(longestValidParentheses("(())()(()(("))
    print(longestValidParentheses("(()(("))
    print(longestValidParentheses("((((((((((((((((((((((((((((()())))(())()())((((()())((())))((()))()())))()(()()("
                                  ")(()((()))()()()))()()()(()()((((())()(((()(((())((()))()((()(()))()())))))))))("
                                  "))()())(()()))((()()()()())))((()()((((()()))))(())())()()))))(())()(()))((((((("
                                  ")))(()()()()(())(()((()))(()(())(((()()))(()((((()((((()((((())(())))()(())))()))("
                                  "()((((((((())()()((())((()())()))))())())()(((((()()(((((())()((()(((()))(()(()))("
                                  "()(()())))())(()((((()((()(((((()()))((()(()((())()))))(()(()())((()((()((((())))("
                                  "()())()))()())())()))))(())))(())()((())(()(()))))()())(((()(()(((((((((()(()()("
                                  "))))((()((()())())())(((((()(()))))()))()))))()())()(()(())))(()))))(()))(((("
                                  ")))))())))))(((())((())((((()((()))((())))()))(((()))())()))()()()((()()(()())(("
                                  ")))()()((()())))))())(()())(((())))))())(())()))()())())(()(()((())((()(()((())(("
                                  ")()()(()((()(((()(())()(((())))))()())))))(()((((()(()()))(((())(()))(()()))))(("
                                  "))()((()))()))()()))()((())(()())())())(()))(()()(())()(()((((()())(((())(()()())("
                                  "))(()()))())))(()((())(()()))))(()))((()()((((()())(()()))()())()())))()(()((((("
                                  "))())()(())()))()()(()(()))))))(((()()((()))(()((((()()((())))())())))()())))("
                                  "))))((())()()()))()((()((()))()()())))(())())(()(()(()(()))())()))(())((())()())(("
                                  "(()()(((())(()()))(()())(())))()))(((()()()())))())))(((()))())())())))(((()))()("
                                  "))())())))))()()()()(())))(()())))(()()())))()((((()()()((((()))()())))(()))("
                                  ")))))(()())()))(((((())()((())()))(()())()()()())()(((()(()(())))))(()(((()()))((("
                                  "(()()))()))(((())(()(()))()(())))()()(()))))()))))()())))()))((((((((()()())((()(("
                                  ")()()(((())())())))()()(())(())))()())()())))((()))((((())()()))(())(((())(()()((("
                                  "((()()((()()(((()(()()(((())()))))()(()())(()((((()()())(((()))(())((())()))))("
                                  "))))))(()()()())))()))(())((()())()())()()))(())))((()))()()((()())()()))(()()(("
                                  "))()())(())))((()(((())))()))))((((()))((())())())()(())(()))((((((())()()(((((("
                                  ")))()())(((()(()(())()((()())))(((())(()(())))))(()(()(((()))(())((((())))((())((("
                                  "(((((()(((((()(())))((((((())(()((((()(())()()((())())())((((((((()))))(((())()))("
                                  ")()))(())(())()()())(()()((())(()))())(((())(()((())(())(())))))(()(()(()()(((()("
                                  ")()))())(()))(())())()(((()((())((()())()(((((()()(()))))(((())()()))(()(()(()(()("
                                  "(())))))))(())())()))()(()(()))))()()((((())()())(((())(()))((()())(()((())()()(("
                                  "))((((())))))(())())())(())(()()(()()))(((()((((())(((())))))(()()()()(((()((((("
                                  "))(()))((())()))()(((((((()(()())))((()()(()()((())()))()(())))((()()((((()()()))("
                                  "(())()))((())(((()(()()()(((()((())((())()())())))((()))))))))))(())()()(((()()("
                                  "))))(((()))(()))))(((()(()())(()))(())((()))(((()(()()(((((((()())((((()))((((()(("
                                  ")())())()(((()(()((()))))))))))()()(((()()((((((((((())))))((((())())((()(((()())("
                                  ")))()()(((((())(()())())(((()((())((((((())(((())(((()(()(((((((()(())()())(("
                                  ")))))(()(((()))))))()))(((())))(()(()())()))(()()(()(()((()())()(())((()()((()()("
                                  ")(()(()()))(((((())()(()())()((()())()))(((((()((())()((()((((()(((())())(()()(("
                                  "))()(())(()(())))))(()())((()((()()()())(()))(()))))))(()((())(())((())()())()("
                                  ")))(()((()))(()()))()())(())(()()(()))((())()((())((((((())()(()()(((((())(()())("
                                  "))())()()(()())))))()))()((())((((((()())((()))))))((()(()()(((((((())))))))((("
                                  ")))(())(((()(()(())()()()()(()(())()))))))())()))()(((((()(())(((()))((()))()))()("
                                  ")(()(()((())(()))))()())((()())))))))(()()(()()))()((()(())()((())(()()))())((()("
                                  "))())()()))))((((()()()))())(())()())))()))()))))()))((()(()())()))()))(((()()()("
                                  ")())))())()))((()()())((()())))(((()((()()())(())))()(())(()(()(())(()(((((()()()("
                                  "((())()())(()((()())(()(((()(())((((()())()(())))(((((((()))))())())))(()))()()((("
                                  "()())(()))()())(())()))()((())()((())((()((())()())(()()))(((((()()()((((((((()(("
                                  ")((()()((((((()())))((((((())))())(()(()((((()(()())())()()))()((())())(()((((()(("
                                  "(()())((())))))(()())(()()()(()))()())()()))((()((()())(())()()()((())()()))))())("
                                  ")))())))(()))(()))()))((())()((()((()))))))())(((()))))))()(((()((())))((()())())("
                                  ")))((()(()(()(()))((()()))())))(()())))())(()))(())(())))))()(())(()()))()))((("
                                  "))))(()))(()))))(())()())(()(()))())(()(())(())))(()))())(()())))())(()())((()))("
                                  ")()((()(()()()(((((()((()((())(()())(())))()))))))(((())())))()((((()))()((()))("
                                  "))()))()))(()(()((()()())()()(((()))())))))()((((()()))))()))())))()())))(((((()(("
                                  "))))())(((()))((()))(((()(())())()((()(((()))()())))))((((()))()(()((((((()(()()("
                                  ")())(())((()))()(()()))))))()(((())))(())()())))))((()))(())()))))(()(((()()((())("
                                  "()))))(((((()))))())))()(())(()(()))()))()))(()((())(()((()())()(((()))))())(())("
                                  ")(())))((())(()(((()))(((((()))(()))())))(()((((((())()((((())())()))((())))))())("
                                  "()(())())))))()()(((())()())))))()))()())))()(())())(())()()()(((())))(())(((()))("
                                  "()(((()()))())((()))(((()()()()())()()))(()))))()()))))(((()()))))()()(()()))()()("
                                  ")())())()((())(((()())(((())(()((()(((()(()())()()()(()((())(()()(()()()))))))()(("
                                  "()))))()(()))()))(())()()())))()()(((()))((()()(((()())))((()()())((())))))()())("
                                  ")((())))())(()())()()()()((())((()()())((()()))())(())())()(()(((()))())(()))))(("
                                  ")()))(())))))))()())()((()())()()))()())))((()()(()())()(()))((())()))(((())))("
                                  "))))(((()()())())("))
