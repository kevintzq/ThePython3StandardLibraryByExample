#!/usr/bin/python3

import string

s_low = "hi, my name is kevin"
s_up = string.capwords(s_low)
print("1.1.1")
print(s_low)
print(s_up)
print("------")


values = {'var' : 'foo'}
t = string.Template("""
Variable : $var
Escape : $$
Variable in text : ${var}iable
""")
s = """
Variable : %(var)s
Escape : %%
Variable in text : %(var)siable
"""
s2 = """
Variable : {var}
Escape : {{}}
Variable in text : {var}iable
"""
print("1.1.2")
print('TEMPLATE:', t.substitute(values))
print('INT:', s % values)
print('FORMAT:', s2.format(**values))
print("------")


t_1_3 = string.Template("$var is here, but $missing is not here.")
print("1.1.3")
try:
    print("substitute() :", t_1_3.substitute(values))
except KeyError as err:
    print("Error:", str(err))
print("substitute() :", t_1_3.safe_substitute(values))
print("------")


class myTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'
template_text = """
Delimiter : %%
Replaced: %with_underscore
Ignored : %notunderscored
"""
d = {
    'with_underscore': 'replaced',
    'notunderscored': 'not replaced',
}
t_1_4 = myTemplate(template_text)
print("1.1.4")
print(t_1_4.safe_substitute(d))
print("------")


t_1_5 = string.Template('$var')
print("1.1.5")
print(t_1_5.pattern.pattern)
print("------")


import re
class myTemplate_1_6(string.Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''
t_1_6 = myTemplate_1_6('''
{{{{
{{var}}
''')
print("1.1.6")
print('MATCHES:', t_1_6.pattern.findall(t_1_6.template))
print('SUBSTITUTED:', t_1_6.safe_substitute(var='replacement'))
print("------")


import inspect
def is_str(value):
    return isinstance(value, str)
for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%r\n' % (name, value))

