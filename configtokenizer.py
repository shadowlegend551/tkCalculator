from token import TokenType, Token


def tokenize(raw: str) -> list:
    raw = list(raw.replace('\n', ' ').replace('\t', ' '))
    raw.append(None)

    output = []

    while raw[0] != None:
        if raw[0] == ' ':
            del raw[0]
            continue

        current_token = raw.pop(0)

        if current_token.isalpha():
            while raw[0].isalnum() or raw[0] == '_':
                current_token += raw.pop(0)

            current_token = Token(TokenType.IDENTIFIER_LITERAL,
                                  current_token)

        elif current_token.isnumeric():
            while raw[0].isnumeric():
                current_token += raw.pop(0)

            current_token = Token(TokenType.NUMERIC_LITERAL,
                                  int(current_token))

        elif current_token == '"' or current_token == "'":
            delimiter = current_token
            current_token = ''

            while raw[0] != delimiter:
                current_token += raw.pop(0)

            del raw[0]
            current_token = Token(TokenType.STRING_LITERAL,
                                  current_token)

        # Equality operators.
        elif current_token == '=':
            if raw[0] == '=':
                type = TokenType.COMPARE_EQ
                del raw[0]
            else:
                type = TokenType.ASSIGN

            current_token = Token(type)


        # Grouping symbols.
        elif current_token == '(':
            current_token = Token(TokenType.PAREN_L)

        elif current_token == '[':
            current_token = Token(TokenType.SQ_BRACKET_L)

        elif current_token == '{':
            current_token = Token(TokenType.CU_BRACKET_L)

        elif current_token == ')':
            current_token = Token(TokenType.PAREN_R)

        elif current_token == ']':
            current_token = Token(TokenType.SQ_BRACKET_R)

        elif current_token == '}':
            current_token = Token(TokenType.CU_BRACKET_R)

        elif current_token == '.':
            current_token = Token(TokenType.DOT)

        elif current_token == ':':
            current_token = Token(TokenType.COMMA)

        elif current_token == ',':
            continue

        elif current_token == ';':
            current_token = Token(TokenType.SEMICOLON)

        # Miscellaneous symbols.
        elif current_token == '#':
            current_token = Token(TokenType.HASHTAG)

        elif current_token == '?':
            current_token = Token(TokenType.QUESTION_MARK)

        # If the token doesn't match to anything, report an error.
        else:
            print([current_token])
            current_token = Token(TokenType.ERROR_TOKEN,
                                  current_token)

        # Return a list with only the error token in erroneous token is
        # encountered.
        if current_token.type == TokenType.ERROR_TOKEN:
            return [current_token]

        output.append(current_token)

    return output
