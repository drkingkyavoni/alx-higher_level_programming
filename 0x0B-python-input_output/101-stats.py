#!/usr/bin/python3
import sys
import signal

status_codes = (200, 301, 400, 401, 403, 404, 405, 500)
result = {}
lines = []


def signal_handler(signum, frame):
    print_result()


def print_result():
    print(f"File size: {sum(len(line) for line in lines)}")
    for code in sorted(result.keys()):
        if code in result:
            print(f"{code}: {result[code]}")


signal.signal(signal.SIGINT, signal_handler)

while True:
    line = sys.stdin.readline()
    lines.append(line)

    for code in status_codes:
        if str(code) in line.split()[-2:]:
            result[code] = result.get(code, 0) + 1

    if len(lines) % 10 == 0:
        print_result()
