from datetime import datetime

function_calls = []

def logger(func):
    def wrapper(*args, **kwargs):
        call_time = datetime.now()
        result = func(*args, **kwargs)
        call_info = {
            'function_name': func.__name__,
            'args': args,
            'result': result,
            'call_time': call_time
        }
        function_calls.append(call_info)

        print(f"Function: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Result: {result}")
        print(f"Call Time: {call_time}")
        print('-' * 40)

        return result
    return wrapper

def get_logs():
    for call in function_calls:
        yield call

@logger
def multiply(a, b):
    return a * b

multiply(3, 4)
multiply(5, 6)

log = get_logs()

for entry in log:
    print(f"Function: {entry['function_name']}")
    print(f"Arguments: {entry['args']}")
    print(f"Result: {entry['result']}")
    print(f"Call Time: {entry['call_time']}")
    print('-' * 40)
