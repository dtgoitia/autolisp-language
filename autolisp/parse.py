import enum
from typing import Iterable, List, Optional, Union

import attr

RESERVER_WORDS = ("defun",)

FunctionName = str
Token = str


class Primitive(enum.Enum):
    BOOL = "bool"
    STR = "str"
    NUMBER = "number"
    FUNCTION = "function"
    LIST = "list"


@attr.s(auto_attribs=True)
class LocalVariable:
    type: Primitive


@attr.s(auto_attribs=True)
class DefineFunction:
    name: FunctionName
    locals: List[LocalVariable]
    body: List


@attr.s(auto_attribs=True)
class Call:
    name: FunctionName
    arguments: Optional[List]


AnyOperation = Union[DefineFunction, Call]


@attr.s(auto_attribs=True)
class Ast:
    body: List[AnyOperation]


def tokenize(lsp: str) -> List[Token]:
    formatted = lsp.replace("(", " ( ").replace(")", " ) ").strip()
    tokens = formatted.split(" ")
    return tokens


_RESERVER_WORDS = {key: True for key in RESERVER_WORDS}


def _convert_to_lists(tokens: Iterable[Token]) -> Iterable[Token]:
    buffer = []

    for token in tokens:
        if token == "(":
            token_list = _convert_to_lists()
            buffer.append(token_list)

    return buffer


def understand(tokens: List[Token]) -> Ast:
    buffer = []
    breakpoint()
    for i, token in enumerate(tokens):
        # function call, or arguments
        if token == "(":
            if not buffer:
                buffer.append(token)
                continue
        if _is_reserved_key(token):
            if token == "defun":
                ...


def parse(lsp: str) -> Ast:
    tokens = tokenize(lsp)
    ast = understand(tokens)
    return ast


def _is_reserved_key(key: Token) -> bool:
    return _RESERVER_WORDS.get(key)
