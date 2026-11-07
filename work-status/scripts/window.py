#!/usr/bin/env python3
"""Print the reporting window for a status update.

Usage: window.py [week|month|quarter|year] [DATE] [--now NOW] [--fiscal-start-month M]

DATE is any date inside the wanted period (YYYY-MM-DD); default is today.
NOW overrides the current time (ISO, for tests). If the period contains NOW,
the window ends at NOW. Prints start, end and a title line, as key=value.
"""
import argparse
import calendar
from datetime import date, datetime, timedelta

CADENCES = ("week", "month", "quarter", "year")


def period(cadence, d, fiscal_start_month=1):
    if cadence == "week":
        start = d - timedelta(days=d.weekday())
        return start, start + timedelta(days=6), f"Week of {start:%B} {start.day}, {start.year}"
    if cadence == "month":
        start = d.replace(day=1)
        end = d.replace(day=calendar.monthrange(d.year, d.month)[1])
        return start, end, f"{start:%B %Y}"
    if cadence == "quarter":
        # months since fiscal year start, floor to quarter
        offset = (d.month - fiscal_start_month) % 12
        q = offset // 3
        start_month = (fiscal_start_month - 1 + q * 3) % 12 + 1
        start_year = d.year if start_month <= d.month else d.year - 1
        start = date(start_year, start_month, 1)
        end_month_index = start_month - 1 + 2
        end_year = start_year + end_month_index // 12
        end_month = end_month_index % 12 + 1
        end = date(end_year, end_month, calendar.monthrange(end_year, end_month)[1])
        if fiscal_start_month == 1:
            return start, end, f"Q{q + 1} {start.year}"
        fy_start_year = d.year if d.month >= fiscal_start_month else d.year - 1
        return start, end, f"Q{q + 1} FY{fy_start_year + 1}"
    if cadence == "year":
        if fiscal_start_month == 1:
            return date(d.year, 1, 1), date(d.year, 12, 31), f"{d.year}"
        start_year = d.year if d.month >= fiscal_start_month else d.year - 1
        start = date(start_year, fiscal_start_month, 1)
        end = date(start_year + 1, fiscal_start_month, 1) - timedelta(days=1)
        return start, end, f"FY{start_year + 1}"
    raise ValueError(cadence)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cadence", nargs="?", default="week", choices=CADENCES)
    p.add_argument("date", nargs="?")
    p.add_argument("--now", help="override current time, ISO format")
    p.add_argument("--fiscal-start-month", type=int, default=1)
    a = p.parse_args()

    now = datetime.fromisoformat(a.now) if a.now else datetime.now()
    d = date.fromisoformat(a.date) if a.date else now.date()
    start, end, title = period(a.cadence, d, a.fiscal_start_month)

    start_dt = datetime.combine(start, datetime.min.time())
    end_dt = datetime.combine(end, datetime.max.time().replace(microsecond=0))
    current = start_dt <= now <= end_dt
    if current:
        end_dt = now.replace(microsecond=0)

    print(f"cadence={a.cadence}")
    print(f"start={start_dt.isoformat()}")
    print(f"end={end_dt.isoformat()}")
    print(f"title={title}")
    print(f"period_is_current={'yes' if current else 'no'}")


if __name__ == "__main__":
    main()
