
import re
import sys

DEBUG = False

def statemachine(filename):
    s = filename
    if s.find('\\')>0:
        s = s[s.rfind('\\')+1:]
    if s.find('/')>0:
        s = s[s.rfind('/')+1:]
    if s.find('.')>0:
        s = s[:s.find('.')]
    print('digraph ' + s + ' {')

    commentpattern = '\\s+\\/\\*(.+)\\*\\/'

    statevar = None
    casestate = 3
    casevar = None
    comment = ''
    for line in open(filename):
        # casestate
        if casestate < 3:
            casestate = casestate + 1
            if DEBUG:
                print(str(casestate) + line)
        if casestate == 1:
            res = re.match(commentpattern,line)
            if res:
                print('  ' + casevar + ' [label="' + casevar + '\\n' + res.group(1) + '"];')

        # switch
        res = re.match('\\s+switch\\s*\\(([a-zA-Z0-9_]+)\\)', line)
        if res:
            statevar = res.group(1)

        # case
        res = re.match('\\s+case\\s+([a-zA-Z0-9_]+):', line)
        if res:
            casevar = res.group(1)
            casestate = 0
            casecomment = ''

        # assign statevar
        res = re.match('\\s+([a-zA-Z0-9_]+)\\s*=\\s*([a-zA-Z0-9_]+);', line)
        if res and res.group(1) == statevar:
            newstate = res.group(2)
            label = ''
            if len(comment)>0:
                label = ' [ label="' + comment + '" ]'
            print('  ' + casevar + ' -> ' + newstate + label + ';')

        # get comment
        comment = ''
        res = re.match('\\s+\\/\\*(.+)\\*\\/', line)
        if res:
            comment = res.group(1)

    print('}')

inputFilename = sys.argv[1]

statemachine(inputFilename)
