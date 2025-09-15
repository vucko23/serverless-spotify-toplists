import csv
import io
from datetime import date

def fake_toplist():
    # Placeholder data — replace with real Spotify logic later
    tracks = [
        {"rank": 1, "track": "Track A", "artist": "Artist A"},
        {"rank": 2, "track": "Track B", "artist": "Artist B"},
        {"rank": 3, "track": "Track C", "artist": "Artist C"},
    ]
    for row in tracks:
        row["asof_date"] = date.today().isoformat()
    return tracks

def generate_toplist_csv() -> str:
    rows = fake_toplist()
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=["rank", "track", "artist", "asof_date"])
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()

def make_s3_key(prefix: str) -> str:
    d = date.today().isoformat()
    prefix = prefix or ""
    if not prefix.endswith("/"):
        prefix += "/"
    return f"{prefix}toplist-{d}.csv"
