import webbrowser
import time

class LinkOpener:
    def __init__(self):
        self.link = None
        self.time_input = None

    def get_user_input(self):
        self.link = input("Enter the link you want to open: ")
        self.time_input = input("Enter the time in format HH:MM (e.g., 09:30): ")

    def get_link(self):
        return self.link

    def get_time_input(self):
        return self.time_input

class TimeChecker:
    def __init__(self, link_opener):
        self.link_opener = link_opener

    def get_local_time(self):
        return time.strftime("%H:%M")

    def open_link_at_scheduled_time(self):
        while True:
            current_time = self.get_local_time()
            scheduled_time = self.link_opener.get_time_input()

            if current_time >= scheduled_time:
                link_to_open = self.link_opener.get_link()
                webbrowser.open(link_to_open)
                break

            time.sleep(180)  # Wait for 3 minutes (3 * 60 seconds) before checking the time again

def main():
    link_opener = LinkOpener()
    link_opener.get_user_input()

    time_checker = TimeChecker(link_opener)
    time_checker.open_link_at_scheduled_time()

if __name__ == "__main__":
    main()
