from pathlib import Path

# One-sentence absurd invention pitch. Judge criteria, in order:
# (1) one sentence pitching a ridiculous invention that fixes a tiny
# everyday annoyance; (2) the laugh comes from the invention itself,
# not a joke bolted on at the end; (3) the fix is silly yet weirdly
# plausible; (4) a fresh absurdity, not a familiar one reheated;
# (5) tight: names the annoyance, the invention and its silly
# mechanism without clutter.
# Revision 2: the entry is pinned as ASCII bytes and written as bytes,
# with a round-trip read-back check, so the artifact is byte-exact.
# The turn is keys that rat themselves out: the lost-keys annoyance
# (patting your pockets) is fixed by the keys confessing their hiding
# spot the moment you pat, so the search ends before it starts. No
# sponsor examples (apologising alarm, complaining sock, sighing
# kettle), no battery cliche, no address to the judge.
ENTRY = (
    "I built keys that confess their hiding spot the moment I pat "
    "my pockets, so the search ends before it starts."
)

# Self-check the gate before writing: 1-220 characters, not only
# whitespace, a single line with no newline inside it.
if len(ENTRY) < 1 or len(ENTRY) > 220 or ENTRY.strip() == "":
    raise SystemExit(f"entry is {len(ENTRY)} characters, outside the 1-220 gate")
if "\n" in ENTRY or "\r" in ENTRY:
    raise SystemExit("entry must be a single line")

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
# Pin the entry as ASCII bytes (strict: any non-ASCII fails loudly),
# write exactly those bytes (no trailing newline), then read back and
# verify the artifact is byte-identical to what was pinned.
try:
    data = ENTRY.encode("ascii")
except UnicodeEncodeError:
    raise SystemExit("entry is not pure ASCII")
if len(data) < 1 or len(data) > 220:
    raise SystemExit(f"entry is {len(data)} bytes, outside the 1-220 gate")
target = out / "entry.txt"
target.write_bytes(data)
if target.read_bytes() != data:
    raise SystemExit("round-trip check failed: entry.txt differs from pinned bytes")
