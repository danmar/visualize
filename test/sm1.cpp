
// state machine


bool MathLib::isDec(const std::string & s)
{
    enum Status {
        START, PLUSMINUS, DIGIT, SUFFIX
    } state = START;
    for (std::string::const_iterator it = s.begin(); it != s.end(); ++it) {
        switch (state) {
        case START:
            if (*it == '+' || *it == '-')
                state = PLUSMINUS;
            else if (isdigit(*it))
                state = DIGIT;
            else
                return false;
            break;
        case PLUSMINUS:
            if (isdigit(*it))
                state = DIGIT;
            else
                return false;
            break;
        case DIGIT:
            if (isdigit(*it))
                state = DIGIT;
            else
                return isValidSuffix(it,s.end());
            break;
        case SUFFIX:
            break;
        }
    }
    return state == DIGIT;
}


