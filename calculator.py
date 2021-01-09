import re
from operator import itemgetter
from collections import deque
from jinja2.exceptions import TemplateSyntaxError
from jinja2.utils import LRUCache

_lexer_cache = LRUCache(50)

whitespace_re = re.compile(r'\s+', re.U)
string_re = re.compile(r"('([^'\\]*(?:\\.[^'\\]*)*)'"
                       r'|"([^"\\]*(?:\\.[^"\\]*)*)")', re.S)
integer_re = re.compile(r'\d+')
name_re = re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b')
float_re = re.compile(r'(?<!\.)\d+\.\d+')
newline_re = re.compile(r'(\r\n|\r|\n)')

operators = {
    '+':            'add',
    '-':            'sub',
    '/':            'div',
    '//':           'floordiv',
    '*':            'mul',
    '%':            'mod',
    '**':           'pow',
    '~':            'tilde',
    '[':            'lbracket',
    ']':            'rbracket',
    '(':            'lparen',
    ')':            'rparen',
    '{':            'lbrace',
    '}':            'rbrace',
    '==':           'eq',
    '!=':           'ne',
    '>':            'gt',
    '>=':           'gteq',
    '<':            'lt',
    '<=':           'lteq',
    '=':            'assign',
    '.':            'dot',
    ':':            'colon',
    '|':            'pipe',
    ',':            'comma',
    ';':            'semicolon'
}

reverse_operators = dict([(v, k) for k, v in operators.iteritems()])
assert len(operators) == len(reverse_operators), 'operators dropped'
operator_re = re.compile('(%s)' % '|'.join(re.escape(x) for x in
                         sorted(operators, key=lambda x: -len(x))))

def count_newlines(value)
 return len(newline_re.findall(value))

 class Failure(object)
  
def __init__(self, message, cls=TemplateSyntaxError):
        self.message = message
        self.error_class = cls

    def __call__(self, lineno, filename):
        raise self.error_class(self.message, lineno, filename)

class Token(tuple)

 _slots_ = ()
    lineno, type, value = (property(itemgetter(x)) for x in range(3))

    def __new__(cls, lineno, type, value):
        return tuple.__new__(cls, (lineno, intern(str(type)), value))

    def __str__(self):
        if self.type in reverse_operators:
            return reverse_operators[self.type]
        elif self.type is 'name':
            return self.value
        return self.type
    
    def test(self, expr)
     
    if self.type == expr:
            return True
        elif ':' in expr:
            return expr.split(':', 1) == [self.type, self.value]
        return False

     if self.type == expr:
            return True
        elif ':' in expr:
            return expr.split(':', 1) == [self.type, self.value]
        return False
