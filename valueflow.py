
import cppcheckdata

def expr(astExpr):
    # all inputs in calculation
    inputs = []
    tokens = [astExpr]
    while len(tokens) > 0:
        token = tokens[0]
        tokens = tokens[1:]
        if not token:
            continue
        if token.str == '(':
            if (token.previous.str[0].isalpha()):
                inputs.append(token.previous.str)
        elif token.str[0].isalpha():
            inputs.append(token.str)
        elif token.str[0].isdigit():
            inputs.append(token.str)
        else:
            tokens.append(token.astOperand1)
            tokens.append(token.astOperand2)
    return str(inputs)

data = cppcheckdata.parsedump('test/1.c.dump')

for scope in data.scopes:
    if scope.type == 'Function':
        print scope.className
        tok = scope.classStart
        while tok and tok != scope.classEnd:
            if tok.astOperand1:
                astTop = tok
                while astTop.astParent:
                    astTop = astTop.astParent

                if astTop.str == '=' and astTop.astOperand1.variable:
                    print(astTop.Id + ' ' + astTop.astOperand1.str + ":=" + expr(astTop.astOperand2))

                if astTop.str == 'return':
                    print(astTop.Id + ' Return ' + expr(astTop.astOperand1))

            tok = tok.next
