import re


NAMED_GROUPS_PATTERN = r'__(?P<method_name>new|init)__\((?P<method_arguments>[a-z*, ]*)\):?'
PATTERN = r'__(new|init)__\(([a-z*, ]*)\)'

f = open('metaclasses.py')
text = f.read()

COMPILED_PATTERN = re.compile(PATTERN)

match_obj = re.search(COMPILED_PATTERN, text)
print(match_obj.group(0), match_obj.group(1), match_obj.group(2))

match_obj_alt = COMPILED_PATTERN.search(text)
print(match_obj.group(0), match_obj.group(1), match_obj.group(2))


match_obj = re.search(NAMED_GROUPS_PATTERN, text)
print(match_obj.groupdict())
print(match_obj.group('method_name'))

match_list = re.findall(COMPILED_PATTERN, text)
print(match_list)

for match in re.finditer(COMPILED_PATTERN, text):
    print(match.group())

words = re.split(r'[^\w]+', text)
print(set(words))

sub_text = re.sub(COMPILED_PATTERN, '<HIDDEN METHOD>', text)
print(sub_text)

word_pattern = r'[a-z]*\b'
match_obj = re.search(word_pattern, 'Bună ziua', flags=re.I | re.A)
print(match_obj.group())

s = "<html> Text</html>"
print(re.search(r"<.*>",s).group())
print(re.search(r"<.*?>",s).group())
