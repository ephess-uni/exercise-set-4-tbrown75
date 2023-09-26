""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    shutdown_events = get_shutdown_events(logfile)
    f_shutdown = shutdown_events[0]
    l_shutdown = shutdown_events[-1]
    f_shutdown_time = logstamp_to_datetime(f_shutdown.split(" ")[1])
    l_shutdown_time = logstamp_to_datetime(l_shutdown.split(" ")[1])
    time_difference = l_shutdown_time - f_shutdown_time
    return time_difference
    


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
