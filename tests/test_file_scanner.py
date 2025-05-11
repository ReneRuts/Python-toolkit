from src.file_scanner import is_email, generate_report, scan_files, send_email
def test_is_email_valid_cases():
    valid = [
        "test@example.com",
        "user.name+tag@sub.domain.com",
        "foo123@bar.co.uk"
    ]
    for email in valid:
        assert is_email(email)

def test_is_email_invalid_cases():
    invalid = [
        "plainaddress",
        "@missinglocal.com",
        "name@.com",
        "name@domain",
        "name@domain..com"
    ]
    for email in invalid:
        assert not is_email(email)

def test_generate_report_includes_all_matches():
    directory = "/some/path"
    pattern = "*.log"
    files = ["/some/path/a.log", "/some/path/b.log"]
    report = generate_report(directory, pattern, files)
    assert "Smart File Scanner Report" in report
    assert "*.log" in report
    assert "- /some/path/a.log" in report
    assert "- /some/path/b.log" in report

def test_generate_report_no_matches():
    report = generate_report("/any/path", "*.pdf", [])
    assert "No files found matching the pattern" in report

def test_scan_files_finds_txt_files(tmp_path):
    f1 = tmp_path / "test1.txt"
    f2 = tmp_path / "test2.txt"
    f1.write_text("Hello")
    f2.write_text("World")

    files = scan_files(tmp_path, "*.txt")
    assert str(f1) in files
    assert str(f2) in files
    assert len(files) == 2

def test_scan_files_returns_empty_for_no_match(tmp_path):
    (tmp_path / "a.jpg").write_text("img")
    files = scan_files(tmp_path, "*.txt")
    assert files == []