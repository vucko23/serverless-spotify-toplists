from src.generate import generate_toplist_csv
from pathlib import Path

out = Path("samples")
out.mkdir(parents=True, exist_ok=True)
p = out / "sample-output.csv"
p.write_text(generate_toplist_csv(), encoding="utf-8")
print(f"Wrote {p} ({p.stat().st_size} bytes)")
