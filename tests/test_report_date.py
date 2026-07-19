from datetime import datetime, timezone

from src.orchestrator import _report_date


def test_report_date_uses_asia_shanghai_calendar_day() -> None:
    late_utc = datetime(2026, 7, 19, 23, 5, tzinfo=timezone.utc)

    assert _report_date(late_utc) == "2026-07-20"
