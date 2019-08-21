import itertools

from jinja2 import Environment, FileSystemLoader, select_autoescape

DAYS_NUMBER = 30

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

checklist_template = env.get_template('checklist.html')


days = range(1, DAYS_NUMBER + 1)
rows_number = DAYS_NUMBER // 2 + DAYS_NUMBER % 2


def group_by_rows(days):
    def get_row_number(day):
        return (day - 1) % rows_number


    days_by_rows = []
    days = sorted(days, key=get_row_number)
    for k, row_iterator in itertools.groupby(days, get_row_number):
        days_by_rows.append(list(row_iterator))

    return days_by_rows

html = checklist_template.render(days_by_rows=group_by_rows(days))

with open('index.html', 'w', encoding='utf8') as file:
    file.write(html)
