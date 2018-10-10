## Python interpreter exercises

~~~~
>>> print 4+5
9
~~~~

~~~~
>>> print 5
5
~~~~

~~~~
>>> print hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
~~~~

~~~~
>>> print 'hello'
hello
~~~~

~~~~
>>> print "hello"
hello
~~~~

~~~~
>>> print '"hello"'
"hello"
~~~~

~~~~
>>> print "'hello'"
'hello'
~~~~

~~~~
>>> hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
~~~~

~~~~
>>> "hello"
'hello'
~~~~

~~~~
>>> 'hello'
'hello'
~~~~

~~~~
>>> 4*4
16
~~~~

~~~~
>>> 9/3
3
~~~~

~~~~
>>> print hello how are you?
  File "<stdin>", line 1
    print hello how are you?
                  ^
SyntaxError: invalid syntax
~~~~

~~~~
>>> print 'hello how are you?
  File "<stdin>", line 1
    print 'hello how are you?
                            ^
SyntaxError: EOL while scanning string literal
~~~~

~~~~
>>> print 'hello how are you?'
hello how are you?
~~~~

~~~~
>>> 'hello how are you?'
'hello how are you?'
~~~~

~~~~
>>> "'hello how are you?'"
"'hello how are you?'"
~~~~

~~~~
>>> "hello how are you?"
'hello how are you?'
~~~~

~~~~
>>> '"hello how are you?"'
'"hello how are you?"'
~~~~

~~~~
>>> 90/10
9
~~~~

~~~~
>>> print "345"
345
~~~~

~~~~
>>> print 345
345
~~~~

~~~~
>>> 123 345
  File "<stdin>", line 1
    123 345
          ^
SyntaxError: invalid syntax
~~~~

~~~~
>>> print 348 345
  File "<stdin>", line 1
    print 348 345
                ^
SyntaxError: invalid syntax
~~~~

~~~~
>>> print '348 345'
348 345
~~~~

~~~~
>>> 2|3
3
~~~~

~~~~
>>> 3&1
1
~~~~

~~~~
>>> 5|4
5
~~~~

~~~~
>>> 5&4
4
~~~~

~~~~
>>> print 7|4
7
~~~~

~~~~
>>> (6&4)|(5|4)
5
~~~~

~~~~
>>> 6&4|5|4
5
~~~~

~~~~
>>> 5 >> 4
0
~~~~

~~~~
>>> 9 >>1
4
~~~~

~~~~
>>> 5>>1
2
~~~~

~~~~
>>> 7<<2
28
~~~~

~~~~
>>> 5>4
True
~~~~

~~~~
>>> 6<0
False
~~~~

~~~~
>>> 45<34
False
~~~~

~~~~
>>> 'arya'>'hanna'
False
~~~~

~~~~
>>> arya>hanna
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'arya' is not defined
~~~~

~~~~
>>> "arya"<"hanna"
True
~~~~

~~~~
>>> '"arya"'<'"hanna"'
True
~~~~

~~~~
>>> '"arya"'
'"arya"'
~~~~

~~~~
>>> "arya>hanna"
'arya>hanna'
~~~~

~~~~
>>> 'hello world'<'how are you?'
True
~~~~

~~~~
>>> 'hello world'>'how are you?'
False
~~~~
