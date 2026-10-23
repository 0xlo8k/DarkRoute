# DarkRoute
<p align="center">
  <img src="https://giphy.com" width="100%" alt="DarkRoute Banner">
</p>

***

# ⚡ DarkRoute

[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)
[![Speed](https://shields.io)]()

A lightweight, high-speed, multithreaded directory brute-forcer designed to map out hidden web paths using standard input streams. 

## ✨ Features
* 🚀 **Multithreaded Performance:** Utilizes a pool of 25 concurrent workers to rapidly blast through directories.
* 🛡️ **Robust Exception Handling:** Gracefully handles timeouts, connection loss, and unexpected HTTP routing resets.
* 📦 **UNIX Pipeline Ready:** Built to accept data straight from standard input (`stdin`), letting you pipe text cleanly from other tools (`cat`, `scilla`, `gau`, etc.).
* 💾 **Auto-Logging:** Automatically dumps successfully discovered target URLs into a clean `darkroute.txt` file.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3 installed alongside the `requests` library.
```bash
pip install requests
```

### Installation
Clone the repository and jump right into the project directory:
```bash
git clone https://github.com
cd darkroute
```

## 🛠️ Usage

DarkRoute reads directory payloads straight from the terminal stream. Pipe your wordlist file directly into the script execution.

### Linux / macOS
```bash
cat wordlist.txt | python darkroute.py target.com
```

### Windows (PowerShell)
```powershell
Get-Content wordlist.txt | python darkroute.py target.com
```

## 📊 Outputs
* Successfully discovered endpoints (`HTTP 200`) print directly to stdout as `[+] Found`.
* Connection hiccups and request drops register safely as errors without crashing the thread loop.
* All successful hits instantly compile down into a structural `darkroute.txt` artifact in your runtime folder.

## ⚠️ Disclaimer
This tool is built solely for educational purposes and authorized penetration testing. Do not use this tool against targets without prior explicit written consent. The developer assumes no liability for misuse or damage caused by this utility.
