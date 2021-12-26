from logger import logger
from datetime import datetime, date, time


@logger(2, 3, print, 'logs')
def calculate_salary(name):
    out_text = f'{date.today()}: calculate salary for {name}'
    print(out_text)
    return out_text


if __name__ == '__main__':
    print('calculate_salary')
