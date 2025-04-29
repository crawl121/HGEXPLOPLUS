# 🚀 HGExploPlus - Advanced SSH Exploitation Framework

**HGExploPlus** is an advanced SSH brute-force and post-exploitation tool targeting both Linux and Windows servers. It offers both **CLI** and **GUI** modes, supports payload execution, and includes optional port scanning.

## 🧠 Features

- 🔐 SSH brute-force with multi-threading
- 📋 Custom wordlist support (usernames & passwords)
- 🖥️ Target both Linux & Windows servers
- ⚡ Pre-attack port scanning (optional)
- 💥 Payload execution and backdoor deployment
- 🌐 Interactive Flask-based GUI interface
- 🛠️ CLI interface with command-line flags
- 📂 Auto output logging in JSON format


## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/HGExploPlus.git
cd HGExploPlus
```
2.Install dependencies:
```bash
pip install -r requirements.txt
```

## 🧪 Usage

▶ CLI Mode
```bash
cd HGExploPlus
python -m cli.main \
  --targets targets.txt \
  --userlist wordlists/users.txt \
  --passlist wordlists/passwords.txt \
  --threads 20 \
  --port 22 \
  --payload \
  --scan \
  --os linux
```
🌐 GUI Mode

1.Run the GUI:
```bash
cd "C:\Users\YOURNAME\Music\HGExploPlus"
python -m gui.main
```
2.Open your browser and visit:
```bash
http://127.0.0.1:5000
```
The GUI allows you to choose targets, usernames, passwords, OS type, and execute attacks interactively.

## 🔐 Disclaimer

This tool is created for educational and authorized penetration testing purposes only.
Do NOT use this tool on systems you do not own or have explicit permission to test.
The author is not liable for misuse of this tool.

## 👨‍💻 Author

crawl
Developer of HGExploPlus – Engine, UI, Automation

instgram: www.instagram.com/zwn_crawl

github: www.github.com/crawl121

