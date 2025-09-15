from src.generate import generate_toplist_csv, make_s3_key

def test_generate_toplist_csv_has_header():
    csv_text = generate_toplist_csv()
    assert "rank,track,artist,asof_date" in csv_text.splitlines()[0]

def test_make_s3_key_prefix():
    key = make_s3_key("results/")
    assert key.startswith("results/")
