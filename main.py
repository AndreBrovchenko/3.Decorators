from logger import logger
from application.salary import calculate_salary
from application.people import get_employees


@logger(2, 3, print, 'logs')
def division(a, b):
    return a / b


if __name__ == '__main__':
    division(6, 1)
    print('MAIN')
    calculate_salary('John')
    get_employees('bookkeeping')
    print('DIRTY_MAIN')
    calculate_salary('Smith')
    get_employees('economic department ')
