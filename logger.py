import datetime
import time
# from datetime import datetime


def logger(sleep_time, n_tries, error_handler, log_dir=''):
    def _make_try(old_function):
        def new_function(*args, **kwargs):
            error = None
            for n_try in range(n_tries):
                try:
                    now = datetime.datetime.now()
                    date_start = now.strftime("%d.%m.%Y")
                    time_start = now.strftime("%H:%M:%S")
                    arguments_args = args
                    arguments_kwargs = kwargs
                    name_function = old_function.__name__
                    value_return = old_function(*args, **kwargs)
                    if len(log_dir) != 0 and log_dir[-1] != '\\':
                        log_path = log_dir + '\\' + 'programm.log'
                    else:
                        log_path = log_dir + 'programm.log'
                    # print(log_path)
                    line_log = f'{date_start} {time_start}\tимя функции:{name_function}\t' \
                               f'аргументы args:{arguments_args}\tаргументы kwargs:{arguments_kwargs}\t' \
                               f'возвращаемое значение:{value_return}'
                    # print(line_log)
                    with open(log_path, 'a', encoding="utf-8") as files_out:
                        files_out.write(line_log + '\n')
                    return value_return
                except Exception as er:
                    print(f'Попытка № {n_try}')
                    print(er)
                    time.sleep(sleep_time)
                    error = er
            raise error
        return new_function
    return _make_try
