from question import Question

test = [
    '1+1=?\n(a)2\n(b)3\n(c)4\n',
    '11+11=?\n(a)22\n(b)33\n(c)44\n',
    '111+111=?\n(a)222\n(b)333\n(c)444\n',
]

questions = [
    Question(test[0], 'a'),
    Question(test[1], 'a'),
    Question(test[2], 'a')
]


def run_test():
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1

    print(f'你得到{score}分，共{len(questions)}題')


run_test()
