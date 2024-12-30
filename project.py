import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("00:00\nTime's up!")

def main():
    try:
        seconds = int(input("Enter the time in seconds for the countdown: "))
        if seconds <= 0:
            print("Please enter a positive number.")
        else:
            print(f"Starting countdown for {seconds} seconds...")
            countdown_timer(seconds)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
