import time

execution_count = 0

def execution_timer_and_type_checker(func):
    def wrapper():
        global execution_count
        execution_count += 1
        
        start_time = time.time()
        result = func()
        end_time = time.time()
        
        if type(result) is not str:
            raise ValueError("Return value must be a string.")
        
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        print(f"Function called {execution_count} time(s)")
        
        return result
    return wrapper

@execution_timer_and_type_checker
def concatenate_strings():
    time.sleep(2)
    concat = "salam" + " Motasem"
    return concat

print(concatenate_strings())
