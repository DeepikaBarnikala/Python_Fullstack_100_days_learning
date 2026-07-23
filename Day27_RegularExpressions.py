'''#Regular Expression(Regex)
-------------------
-->regex is an sequence of char that can searching pattern
-->to use regex we have import re module..

functions
---------
1.findall
------
-->it will find all the char that are in the string''
eg:-'''
import re
txt='python is a language and also called dynamically typed'
print(re.findall('[an]',txt))



'''2.search()
--------
-->this search()will find the char,but it will the first sequence that found in the string...
eg-'''
import re
txt='python is a language and also called dynamically typed'
print(re.search('[a]',txt))

'''3.split()
--------
eg-'''
import re
txt='python is a language and also called dynamically typed'
print(re.split(' ',txt))

'''4.sub()
------
eg-'''
import re
txt='python is a language and also called dynamically typed'
print(re.sub(' ','&',txt))


'''5.fullmatch()

metachar
--------
[]
^
$
.
*
+
{}

'''
import re
txt='i am studing at codegnan'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))

print(re.search('[0-9]',txt))
print(re.search('[0-9]',txt))
print(re.search('[0-9]',txt))

import re
txt='i am studing at codegnan'
print(re.findall('at codegnan',txt))
print(re.search('at codegnan',txt))

import re
txt='i am studing at codegnan'
print(re.findall('codegnan$',txt))
print(re.search('codegnan$',txt))

import re
any='hello are you doing'
print(re.findall('w..t',any))
print(re.findall('h...o',any))
import re
any='hello are you doing'
print(re.findall('h.*o',any))
print(re.findall('a.*g',any))
print(re.search('a.*g',any))
import re
now='codegnan is a learning platform'
print(re.findall('c.+m',now))
print(re.search('i.+p',now))

import re
now='python is just a language'
print(re.findall('p.{22}',now))
print(re.search('p.{22}',now))
