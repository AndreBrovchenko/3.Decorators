from logger import logger
from datetime import datetime, date, time


@logger(2, 3, print, 'logs')
def get_employees(department):
    out_text = f'{date.today()}: department staff: {department}'
    print(out_text)
    return out_text


if __name__ == '__main__':
    print('get_employees')
