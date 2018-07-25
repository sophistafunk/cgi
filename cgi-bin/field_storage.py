#!/usr/bin/env python
import cgi

print('Content-Type: text/plain')
print('')

form = cgi.FieldStorage()
stringval = form.getvalue('a', None)
listval = form.getlist('b')

print(f'a: {str(stringval)}, b: {str(listval)}')
