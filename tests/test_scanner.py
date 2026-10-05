from security_scanner import scan

def test_finds_vyполнить():
    code = "Выполнить(Строка);"
    assert any(f['severity'] == 'critical' for f in scan(code))
