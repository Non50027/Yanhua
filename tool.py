import os

# 讀取 .env
def load_env(file_path):
    with open(file_path) as f:
        for line in f:
            if line.startswith('#') or '=' not in line:
                continue
            key, value = line.strip().split('=', 1)
            os.environ[key] = value