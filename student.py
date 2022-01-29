from datetime import date, timedelta
import requests

class Student:
    """A Student class as base for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False


    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    
    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"


    def alert_santa(self):
        self.naughty_list = True

    def apply_extension(self, num):
        self.end_date = self.end_date + timedelta(days=num)

    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        return "Something went wrong with your request!"
