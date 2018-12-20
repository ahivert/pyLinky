import datetime
import json

from mock import patch
from pylinky import LinkyClient


class TestLinkyClient:

    @classmethod
    def setup_class(cls):
        cls.client = LinkyClient(username="test", password="test")
        cls.today = datetime.date.today()

    @patch.object(LinkyClient, '_get_data')
    def test_data_per_hours(self, fake_get_data):
        with open('tests/per_hours.json') as f:
            response = json.loads(f.read())
        fake_get_data.return_value = response

        data = self.client.get_data_per_hour(
            start_date=self.today,
            end_date=self.today - datetime.timedelta(days=1)
        )

        assert round(sum([d['conso'] for d in data]), 3) == 27.714
        assert len(set([d['time'] for d in data])) == 48  # hours

    @patch.object(LinkyClient, '_get_data')
    def test_data_per_days(self, fake_get_data):
        with open('tests/per_days.json') as f:
            response = json.loads(f.read())
        fake_get_data.return_value = response

        data = self.client.get_data_per_day(
            start_date=self.today,
            end_date=self.today - datetime.timedelta(days=1)
        )

        assert round(sum([d['conso'] for d in data]), 3) == 440.373
        assert len(set([d['time'] for d in data])) == 31  # days

    @patch.object(LinkyClient, '_get_data')
    def test_data_per_months(self, fake_get_data):
        with open('tests/per_months.json') as f:
            response = json.loads(f.read())
        fake_get_data.return_value = response

        data = self.client.get_data_per_month(
            start_date=self.today,
            end_date=self.today - datetime.timedelta(days=1)
        )

        assert round(sum([d['conso'] for d in data]), 3) == 3678.129
        assert len(set([d['time'] for d in data])) == 12  # months

    @patch.object(LinkyClient, '_get_data')
    def test_data_per_years(self, fake_get_data):
        with open('tests/per_years.json') as f:
            response = json.loads(f.read())
        fake_get_data.return_value = response

        data = self.client.get_data_per_year()

        assert round(sum([d['conso'] for d in data]), 3) == 3678.129
        assert len(set([d['time'] for d in data])) == 4  # years
