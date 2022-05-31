import time
import threading

def take_a_nap(x):
    time.sleep(int(x))
    print('Wake up!')

# the join meth waits for the thread finshed
def wait_sleep(th: threading.Thread):
    print('Will wait to the thread finsh')
    th.join()
    

def main():
    x = input('Type the seconds to sleep:')

    # th obj can has a target adn the start will invoke run method, wich set the th as actived
    th = threading.Thread(target=take_a_nap, args=x)
    th.start()
    wait_sleep(th)
    print('The main finishd')


if __name__ == '__main__':
    main()