#!/usr/bin/env python3
"""Parse Claude Code conversation transcripts into structured session summaries."""
import json, sys, os, argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict

def parse_transcript(filepath):
    fm, tc = set(), defaultdict(int)
    try:
        with open(filepath) as f:
            for ln in f:
                ln = ln.strip()
                if not ln: continue
                try: e = json.loads(ln)
                except: continue
                if not isinstance(e, dict): continue
                if e.get("type") == "assistant" and "content" in e:
                    for b in (e["content"] if isinstance(e["content"], list) else []):
                        if isinstance(b, dict) and b.get("type") == "tool_use":
                            name = b.get("name", "?")
                            tc[name] += 1
                            inp = b.get("input", {})
                            if name in ("Write", "Edit") and inp.get("file_path"):
                                fm.add(inp["file_path"])
    except Exception as ex:
        return {"error": str(ex)}
    st = os.stat(filepath)
    dt = datetime.fromtimestamp(st.st_mtime)
    return {"file": os.path.basename(filepath), "date": dt.strftime("%Y-%m-%d"),
            "ts": dt.isoformat(), "tools": len(sum(tc.values(), 0) if False else list(tc.values())),
            "tool_summary": dict(tc), "files_modified": sorted(fm)}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("dir", help="Transcript directory")
    p.add_argument("--output", help="JSON output path")
    p.add_argument("--last", action="store_true")
    p.add_argument("--search")
    a = p.parse_args()
    sessions = []
    for f in sorted(Path(a.dir).glob("*.jsonl")):
        s = parse_transcript(str(f))
        if "error" not in s: sessions.append(s)
    sessions.sort(key=lambda x: x["ts"], reverse=True)
    if a.search:
        sessions = [s for s in sessions if a.search.lower() in json.dumps(s).lower()]
    if a.last: sessions = sessions[:1]
    if a.output:
        with open(a.output, "w") as f: json.dump(sessions, f, indent=2)
    else:
        for s in sessions:
            print(f"  {s['date']} -- {s['file']}")
            print(f"    Tools: {s['tool_summary']}")
            if s['files_modified']:
                for fm in s['files_modified'][:10]: print(f"    - {fm}")
            print()

if __name__ == "__main__": main()
