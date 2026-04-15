import json
from datetime import datetime

LOG_FILE = "errors.jsonl"

def log_error(sensor: str, level: str = "ERROR", errormsg: str ="-"):
    entry = {
        "time": datetime.utcnow().isoformat() + "Z",
        "sensor": sensor,
        "level": error
        "errormsg": errormsg
    }

    try:
        with open(LOG_FILE, "a", buffering=1) as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print(f"[LOGGING FAILURE] {e}")