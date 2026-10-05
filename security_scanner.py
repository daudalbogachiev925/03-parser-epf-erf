import re, yaml

RULES = yaml.safe_load(open('rules.yaml'))['dangerous']

def scan(code: str):
    findings = []
    for r in RULES:
        for m in re.finditer(r['pattern'], code):
            findings.append({'pattern': r['pattern'],
                             'severity': r['severity'],
                             'pos': m.start()})
    return findings
