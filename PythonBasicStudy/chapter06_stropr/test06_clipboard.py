import pyperclip
import sys

textDict01 = {'agree': '''yes, i agree your idea'''
              , 'busy': '''sorry, system is busy now'''
              , 'disagree': '''i am sorry, i can't do it'''
}

if len(sys.argv) < 2:
    print('参数个数不少于2个')
    sys.exit()

keyPhrase = sys.argv[1]

if keyPhrase in textDict01:
    pyperclip.copy(textDict01[keyPhrase])
    print('detail for ' + keyPhrase + ' copied to clipboard')
else:
    print('there is no detail for ' + keyPhrase)



