def mean_time(number_of_calls: int):
    def mean_time_(func):
        times = []
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            times.append(end-start)
            if len(times) == number_of_calls:
                print(f"Mean time over last {number_of_calls} calls for {func.__name__} is: {round(sum(times)/number_of_calls, 4)}")
                while times:
                    times.pop()
            return result
        return wrapper
    return mean_time_


@mean_time(10)
def foo():
    time.sleep(0.01)
 
@mean_time(10)   
def bar():
    time.sleep(0.02)
    
for i in range(10):
    foo()
    bar()
    
# Mean time over last 10 calls for foo is: 0.0103
# Mean time over last 10 calls for bar is: 0.0202