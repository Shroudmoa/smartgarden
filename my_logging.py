import json
from datetime import datetime, timezone

LOG_FILE = "errors.jsonl"

def log_error(sensor: str, level: str = "ERROR", errormsg: str ="-"):
    entry = {
        "time": datetime.now(timezone.utc).isoformat(),
        "sensor": sensor,
        "level": level,
        "errormsg": errormsg
    }

    try:
        with open(LOG_FILE, "a", buffering=1) as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print(f"[LOGGING FAILURE] {e}")

log_error(sensor = "no sensor", level = "Info", errormsg = "testest")