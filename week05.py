def is_valid_parentheses(expression : str) -> bool:  # type hint
#expression(문자열) str 괄호를 포함한 수식
    stack = list()
    #스택을 초기화
    brackets = {']': '[', '}': '{', ')': '('}
    for letter in expression:
        if letter in brackets.values():
            stack.append(letter)
            
        if letter in brackets.keys():
            if not stack or stack.pop() != brackets[letter]:
                return False
    return not stack
#결과로 True인지 false인지 알아내는것임 이게 
#만약 첫번째? 이게 false가 나오는건 괄호가 제대로 안닫혀서 그런거임 [ } 이런식으로 만들어져서 그럼
print(is_valid_parentheses("[({1+2)]}"))
print(is_valid_parentheses("[({1+2})]"))
print(is_valid_parentheses(")1+2()"))
print(is_valid_parentheses("(1+2))"))
print(is_valid_parentheses("(1+2)"))
print(is_valid_parentheses("((3*2)/2)"))
print(is_valid_parentheses("((3*2/2)"))
