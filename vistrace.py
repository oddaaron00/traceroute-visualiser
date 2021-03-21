#!/bin/python3

import sys, webbrowser, subprocess

def main(traceIn):
    traceIn.pop()
    url = "http://127.0.0.1:5500/index.html?vals="
    for entry in traceIn:
        print(entry)
        split = entry.split(" ")
        if split[3] != "*" and split[0] != "traceroute":
            ip = split[4][1:-1] if split[0] == "" else split[3][1:-1]
            url = url + ip + ","
    webbrowser.open(url)

trace = subprocess.run(["traceroute",sys.argv[1]], check=True, stdout=subprocess.PIPE, universal_newlines=True)
main(trace.stdout.split("\n"))
