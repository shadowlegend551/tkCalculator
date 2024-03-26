from token import TokenType, Token
from configtokenizer import tokenize


def parse_config(raw: str) -> dict:
    settings = {}
    tokenized = tokenize(raw)

    while len(tokenized):
        # Skip comment lines.
        if tokenized[0].type == TokenType.HASHTAG:
            while tokenized[0].type != TokenType.SEMICOLON:
                del tokenized[0]
            del tokenized[0]
            continue
        
        value = []
        
        key = tokenized.pop(0)
        del tokenized[0]  # Skip =.

        while tokenized[0].type != TokenType.SEMICOLON:
            value.append(tokenized.pop(0).value)
        del tokenized[0]  # Skip ;.

        settings[key.value] = tuple(value)

    return settings