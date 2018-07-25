#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')

try:
    total = sum(map(int, operands))
    body = f'The total is: {total}'
except (ValueError, TypeError):
    body = 'Invalid numbers provided, please provide integer numbers'

print('Content-type: text/plain')
print('')
print(body)
