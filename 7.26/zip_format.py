questions = ['name', 'quest', 'favourite color']
answers = ['Joseph', 'the happiness', 'black']
for q,a in zip(questions, answers):
    print('What is you {0}?\tIt is {1}.'.format(q, a))
    
