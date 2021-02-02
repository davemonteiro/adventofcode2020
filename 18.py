import time


def process_operators_lr(lst: list) -> str:
    # Returns: sum/product of expression evaluated left-to-right
    # Sentence includes numbers along with
    # addition and multiplication symbols
    total = int(lst.pop(0))
    while len(lst) > 0:
        if lst.pop(0) == '+':
            total += int(lst.pop(0))
        else:
            total *= int(lst.pop(0))

    return str(total)


def process_operators_am(lst: list) -> str:
    # Returns: sum/product of expression evaluated with
    # all additions carried out before multiplications
    while '+' in lst:
        pos = lst.index('+')
        lst.pop(pos)
        prod = int(lst[pos-1]) + int(lst.pop(pos))
        lst[pos-1] = prod

    total = int(lst.pop(0))
    while len(lst) > 0:
        lst.pop(0)
        total *= int(lst.pop(0))

    return str(total)


def match_parens(sentence: str) -> tuple:
    # Returns the indices of a pair of parens
    # that can be evaluated - starting with the
    # open paren located most to the right
    left = sentence.rfind('(')+1
    right = left
    while sentence[right] != ')':
        right += 1

    return (left, right)


def eval_parens(left: int, right: int, sentence: str, mode: str) -> str:
    # Returns the evaluated expression from within a set of parentheses
    if mode == 'lr':
        paren_result = process_operators_lr(sentence[left:right].split(' '))
    else:
        paren_result = process_operators_am(sentence[left:right].split(' '))

    return sentence[0:left-1] + paren_result + sentence[right+1:]


start = time.time()

sentences = []
with open('18_input.txt') as f:
    for line in f.readlines():
        sentences.append(line)

total_lr = 0
for sentence in sentences[:]:
    while '(' in sentence:
        l, r = match_parens(sentence)
        sentence = eval_parens(l, r, sentence, mode='lr')

    total_lr += int(process_operators_lr(sentence.split(' ')))

print('Part 1: ', total_lr)
# 2743012121210

total_am = 0
for sentence in sentences:
    while '(' in sentence:
        l, r = match_parens(sentence)
        sentence = eval_parens(l, r, sentence, mode='am')

    total_am += int(process_operators_am(sentence.split(' ')))

print('Part 2: ', total_am)
# 65658760783597

end = time.time()
print('Time elapsed: ', end-start)
# <0.02s

"""
--- Day 18: Operation Order ---

Summary:
Evaluate mathematical expressions.

The homework (your puzzle input) consists of a series of expressions that
consist of addition (+), multiplication (*), and parentheses ((...)). Just
like normal math, parentheses indicate that the expression inside must be
evaluated before it can be used by the surrounding expression. Addition
still finds the sum of the numbers on both sides of the operator, and
multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating
multiplication before addition, the operators have the same precedence, and are
evaluated left-to-right regardless of the order in which they appear.

Before you can help with the homework, you need to understand it yourself.
Evaluate the expression on each line of the homework; what is the sum of the
resulting values?

--- Part Two ---

You manage to answer the child's questions and they finish part 1 of their
homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're
not the ones you're familiar with. Instead, addition is evaluated before
multiplication.

What do you get if you add up the results of evaluating the
homework problems using these new rules?
"""
