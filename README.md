# skipping-meeting-excuse

[![make.fun · u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)
[![rank](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/nmlyz/skipping-meeting-excuse/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)
[![reward](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/nmlyz/skipping-meeting-excuse/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)

skipping-meeting-excuse writes one line to a text file: an excuse for skipping a pointless meeting. The line was picked from 36 candidates by pairwise judging against the brief — a 90-minute meeting to pick a font, declined with a single word that does two jobs at once: it is the font picked, and the excuse itself.

> Can't attend — the meeting is 90 minutes to pick a font, and I've already picked one: absent.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt`. The output directory can be changed with `--out-dir` or the `MAKEFUN_OUTPUT_DIR` environment variable:

```sh
python3 main.py --out-dir /tmp/out
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

No network access needed; the same text, byte for byte, on every run.

## Why this line

The meeting's whole job is picking a font, so the excuse answers it on its own terms: the font has already been picked, and the pick is "absent" — one word that is both the decision the meeting exists to make and the reason for not attending. Nothing is explained twice, and the line ends on its strongest beat.

## How it works

Before anything is written, the line passes a structured gate, and every failure is reported by name:

- length within 1–200 characters, and exactly the judged length of 93;
- a single line, with no newline or carriage return inside it;
- no leading or trailing space, and not only whitespace.

After writing, the program reads the file back and confirms the bytes match exactly, the sha256 digest matches the expected value, and the file mode is 0644. A silent partial write fails loudly instead of passing as a finished entry.

## Check the output

```sh
python3 main.py --out-dir /tmp/out
cat /tmp/out/entry.txt
sha256sum /tmp/out/entry.txt
```

The expected digest is:

```
65ddf397a2f4e8fe539da3a91b9e434a65527822be16cb56d5f1b39c21dd067a
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)</sub>
