letters = [['h','o','l','i','d','a','y'],
           ['p','r','o','g','r','a','m','m','i','n','g'],
           ['b','o','o','t','c','a','m','p'],
           ['f','l','o','w','c','h','a','r','t']
]

words = [["holi","hi","oil","day","holiday","lady","aid",
         "hay","had","dal","lid","hold","hail"],
         ["programming","pro","ram","gram","pin","ping","go",
          "an","in","no","mom","map","gap","gag","pig","man",
          "pong","pram","prom","ramp"],
          ["bootcamp","bot","boot","camp","cat","bat","mat","am","at",
           "to","cab","map","cop","act"],
           ["flowchart","chart","art","at","chat","low","flow",
            "of","or","wolf","cow","cat","rat","hat","fart"]
]

lives = 5

level = 0

score = 0

while level < 5:

    print('Level {}'.format(level+1))

    print('Create 3 words using the given letters')

    for c in letters[level]:

        print('{}\t'.format(c), end='')

    print()

    wordCount = 0

    watch = False

    word = ''

    oldWord = ''

    while wordCount == 0 or wordCount < 3:

        match = False

        word = input('Word: ')

        if not (word.lower() == oldWord.lower()):

            for w in words[level]:

                if (word.lower() == w):

                    wordCount += 1

                    score += 1

                    oldWord = word

                    match = True

                    break

        if not match:

            print('Wrong Guess')

            lives -= 1

        if lives == 0:

            print('Game Over!! Better Luck Next Time!!')

            print('Your score is {}'.format(score))

            break

    wordCount = 0

    match = False

    word = ''

    if lives == 0:

        break

    if level == 4:

        print('Thanks for playing the game!!!')

        print('Your score is {}'.format(score))

        level += 1

    else:

        choice = input('Do you want to continue to next level? (y/n) ')

        if (choice.lower()[0] == 'y'):

            level += 1

        else:

            print('Thanks for playing the game!!!')

            print('Your score is {}'.format(score))

            break
