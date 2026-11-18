"""Fit the reel timeline to the real voiceover.
usage: python3 sync_voice.py voice.mp3   -> writes timing.js, copies the mp3 to voice.mp3
then:  node render.js                    -> out/anthropic_ipo_reel.mp4 with sound
Sentence starts are snapped to the pauses ffmpeg finds in the audio."""
import re, subprocess, sys, json, shutil, os
src = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
if os.path.abspath(src) != os.path.join(here, 'voice.mp3'):
    shutil.copy(src, os.path.join(here, 'voice.mp3'))
err = subprocess.run(['ffmpeg', '-i', src, '-af', 'silencedetect=noise=-35dB:d=0.22', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr
dur = float(re.search(r'Duration: (\d+):(\d+):([\d.]+)', err).groups()[2]) + 60 * int(re.search(r'Duration: (\d+):(\d+)', err).group(2))
starts_sil = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', err)]
ends_sil = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', err)]
speech_start = ends_sil[0] if starts_sil and starts_sil[0] < 0.05 else 0.0
speech_end = starts_sil[-1] if len(starts_sil) > len(ends_sil) else dur
# estimated relative sentence lengths (chars + pauses), same numbers as index.html
sent = ["Компанію, яку заснували люди, що боялись штучного інтелекту,", "щойно оцінили майже в трильйон доларів.",
        "У 2021 році кілька людей пішли з OpenAI.", "Їм здавалось, що штучний інтелект розвивають надто швидко і необережно.",
        "Вони заснували Anthropic і зробили Claude.", "П'ять років потому: біржа NASDAQ, тікер ANT, оцінка приблизно трильйон доларів.",
        "Здавалося б, на ринку штучного інтелекту виграє той, хто найголосніше обіцяє.", "Бізнесу потрібен інструмент, якому можна довірити роботу.",
        "З вашою роботою так само.", "Штучний інтелект не зробить усе за вас.", "Але зробить те, що ви чітко пояснили.",
        "Тому в Джун AI академії ми починаємо з однієї рутинної задачі,", "яку можна віддати штучному інтелекту вже цього тижня."]
w = [len(s) + 8 for s in sent]
tot = sum(w); est = []; acc = 0
for x in w:
    est.append(speech_start + acc / tot * (speech_end - speech_start)); acc += x
cands = [e for s, e in zip(starts_sil, ends_sil) if e > speech_start + 0.3]
starts = [0.0]
for i in range(1, len(sent)):
    near = [c for c in cands if abs(c - est[i]) < 1.6 and c > starts[-1] + 0.6]
    starts.append(min(near, key=lambda c: abs(c - est[i])) - 0.05 if near else est[i])
starts.append(speech_end + 0.35)          # end card
total = starts[-1] + 2.8
open(os.path.join(here, 'timing.js'), 'w').write('window.TIMING = ' + json.dumps({'starts': [round(s, 3) for s in starts], 'total': round(total, 3)}) + ';\n')
print('audio', round(dur, 2), 's; starts', [round(s, 2) for s in starts], 'total', round(total, 2))
