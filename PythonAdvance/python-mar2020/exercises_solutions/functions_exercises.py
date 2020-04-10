def square_print(nr):
    print(nr ** 2)  # nr * nr OR pow(nr, 2)


def square(nr):
    return nr ** 2


square_print_result = square_print(9)
square_result = square(9)

print(square_result, square_print_result)
print('Results are equal: ', square_print_result == square_result)


def fizzbuzz(start=1, end=51):
    for nr in range(start, end):
        if nr % 3 == 0 and nr % 5 == 0:
            print('fizzbuzz')
        elif nr % 3 == 0:
            print('fizz')
        elif nr % 5 == 0:
            print('buzz')
        else:
            print(nr)


fizzbuzz()


def odd_numbers(start=0, end=100):
    for i in range(start, end):
        if i % 2 == 1:
            print(i)


odd_numbers(3, 10)
odd_numbers()
odd_numbers(end=5)
odd_numbers(start=94)


def check_speed(speed):
    if speed <= 50:
        print('OK')
        return

    demerit_points = (speed - 50) // 5
    if demerit_points == 0:
        print('Slow down')
    elif demerit_points <= 12:
        print('Points:', demerit_points)
    else:
        print('Licence suspended')


for speed in (45, 53, 89, 160):
    print(f'Check speed={speed}:', end=' ')
    check_speed(speed)


def build_html(tag_type, content):
    start_tag = '<' + tag_type + '>'
    end_tag = '</' + tag_type + '>'
    escaped_content = ''
    for char in content:
        if char == '&':
            char = '&amp;'
        elif char == '<':
            char = '&lt;'
        elif char == '>':
            char = '&gt;'
        elif char == '"':
            char = '&quot;'

        escaped_content += char
    return start_tag + escaped_content + end_tag


def build_html_replace(tag_type, content):
    start_tag = '<' + tag_type + '>'
    end_tag = '</' + tag_type + '>'
    escaped_content = (
        content
        .replace('&', '&amp;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('"', '&quot;')
    )

    return start_tag + escaped_content + end_tag


assert build_html('b', '"Ham & Eggs"') == "<b>&quot;Ham &amp; Eggs&quot;</b>"
assert build_html_replace('b', '"Ham & Eggs"') == "<b>&quot;Ham &amp; Eggs&quot;</b>"
