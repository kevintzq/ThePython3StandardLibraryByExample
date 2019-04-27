#!/usr/bin/python3

import textwrap
from Textwrap_Example import sample_text

print("1.2.2")
print(textwrap.fill(sample_text, width=50))
print("------")


print("1.2.3")
dedented_text = textwrap.dedent(sample_text)   #dedent()去除示例文本中所有行前面的空白符
print('Dedented:')
print(dedented_text)
print("------")


print("1.2.4")
dedented_text02 = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
    print('{} Columns:\n'.format(width))
    print(textwrap.fill(dedented_text02, width=width))
print("------")


print("1.2.5")
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += "\n\nSecond paragraph after a blank line."
final = textwrap.indent(wrapped, '>') #indent()在每行开头添加'>'符号
print('block:\n')
print(final)
print("------")


print("1.2.6")
def should_indent(line):
    print('Ident {!r}?'.format(line))
    return len(line.strip()) % 2 == 0
dedented_text_126 = textwrap.dedent(sample_text)
wrapped_126 = textwrap.fill(dedented_text_126, width=50)
final_126 = textwrap.indent(wrapped_126, 'EVEN ', predicate=should_indent)
print('\nBlock:\n')
print(final_126)