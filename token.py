from enum import Enum


class TokenType(Enum):
    # Error token.
    ERROR_TOKEN=-1

    # Literals
    IDENTIFIER_LITERAL=0
    NUMERIC_LITERAL=1
    STRING_LITERAL=2

    # Arithmetic operators.
    OPERATOR_ADD=3
    OPERATOR_SUB=4
    OPERATOR_MUL=5
    OPERATOR_DIV=6
    OPERATOR_EXP=7
    OPERATOR_MOD=8

    # Comparison operators.
    COMPARE_EQ=9
    COMPARE_NE=10
    COMPARE_GE=11
    COMPARE_LE=12

    # Assignment operators.
    ASSIGN=13
    ASSIGN_ADD=14
    ASSIGN_SUB=15
    ASSIGN_MUL=16
    ASSIGN_DIV=17
    ASSIGN_EXP=18
    ASSIGN_MOD=19

    # Logical operators.
    LOGICAL_AND=20
    LOGICAL_OR=21
    LOGICAL_XOR=22
    LOGICAL_NOT=23

    # Grouping symbols.
    PAREN_L=24
    PAREN_R=25
    SQ_BRACKET_L=26
    SQ_BRACKET_R=27
    CU_BRACKET_L=28
    CU_BRACKET_R=29

    # Separators.
    DOT=30
    COMMA=31
    COLON=32
    SEMICOLON=33

    # Miscellaneous.
    HASHTAG=34
    QUESTION_MARK=35


class Token:
    def __init__(self, type: TokenType, value=None):
        self.type = type
        self.value = value
