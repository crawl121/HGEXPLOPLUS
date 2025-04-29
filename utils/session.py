# utils/session.py
def load_wordlists(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f]
