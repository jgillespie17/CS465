from datetime import timedelta, datetime
from app.helpers import less_than_day, pretty_date

import pytest

def test_seconds_friendly_message():
    assert(less_than_day(15) == "15 seconds ago")

def test_secondsminute_friendly_message():
    assert(less_than_day(60) == "a minute ago")

def test_minute_friendly_message():
    assert(less_than_day(100) == "a minute ago")

def tests_minuteminutes_friendly_message():
    assert(less_than_day(120) == "2 minutes ago")

def test_minutes_friendly_message():
    assert(less_than_day(300) == "5 minutes ago")

def test_hour_friendly_message():
    assert(less_than_day(7000) == "an hour ago")

def test_hourhours_friendly_message():
    assert(less_than_day(7200) == "2 hours ago")

def test_hours_friendly_message():
    assert(less_than_day(7300) == "2 hours ago")

def test_more_hours_friendly_message():
    assert(less_than_day(82800) == "23 hours ago")

def test_pretty_date_time_is_int():
    assert(pretty_date(10) == "49 years ago")

def test_pretty_date_not_time():
    assert(pretty_date())
            
def test_pretty_date_zero():
    assert(pretty_date(datetime.utcnow() - timedelta(seconds=30)) == "30 seconds ago") 

def test_pretty_date_now():
    assert(pretty_date(datetime.utcnow()) == "just now" )

def test_pretty_date_yesterday():
    assert(pretty_date(datetime.utcnow() - timedelta(days=1)) == "Yesterday" )

def test_pretty_date_days():
    assert(pretty_date(datetime.utcnow() - timedelta(days=6)) == "6 days ago" )

def test_pretty_date_weeks():
    assert(pretty_date(datetime.utcnow() - timedelta(days=14)) == "2 weeks ago")

def test_pretty_date_months():
    assert(pretty_date(datetime.utcnow() - timedelta(days=90)) == "3 months ago")

def test_pretty_date_years():
    assert(pretty_date(datetime.utcnow() - timedelta(days=3650)) == "10 years ago")

def test_pretty_date_less_zero():
    assert(pretty_date(datetime.utcnow() + timedelta(seconds=1)) == "just about now")
