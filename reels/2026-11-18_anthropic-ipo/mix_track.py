"""Mix a ready-made music track under the voice.
The track's own ending (END_IN_TRACK) is aligned to the logo, so the song finishes on the end card.
usage: python3 mix_track.py track.mp3 [end_in_track_seconds]  -> soundtrack.wav"""
import sys, json, re, os, subprocess
here = os.path.dirname(os.path.abspath(__file__))
track = sys.argv[1]; end_in_track = float(sys.argv[2]) if len(sys.argv) > 2 else 185.8
tm = json.loads(re.search(r'window.TIMING = (.*);', open(os.path.join(here, 'timing.js')).read()).group(1))
TOTAL, LOGO = tm['total'], tm['starts'][-1]
start = end_in_track - (LOGO + 0.05)
BED, PEAK = 0.07, 0.40
# bed under the voice, swell over 0.7 s into the logo, short fades at both ends
gain = (f"if(lt(t,{LOGO-0.7:.3f}),{BED},if(lt(t,{LOGO:.3f}),{BED}+({PEAK}-{BED})*(t-{LOGO-0.7:.3f})/0.7,{PEAK}))"
        f"*min(1,t/0.4)*min(1,max(0,({TOTAL:.3f}-t)/0.8))")
pre = (f'[1:a]atrim=start={start:.3f}:duration={TOTAL+0.5:.3f},asetpts=PTS-STARTPTS,aresample=44100,'
       f'aformat=channel_layouts=stereo,volume=\'{gain}\':eval=frame[m];'
       '[0:a]aresample=44100,aformat=channel_layouts=stereo,apad,asplit=2[v][sc];'
       '[m][sc]sidechaincompress=threshold=0.03:ratio=3:attack=25:release=350[md];'
       '[v][md]amix=inputs=2:duration=shortest:normalize=0')
ins = ['-i', os.path.join(here, 'voice.mp3'), '-i', track]
r = subprocess.run(['ffmpeg', '-hide_banner', '-y'] + ins + ['-filter_complex', pre + ',loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json[out]',
                    '-map', '[out]', '-t', f'{TOTAL:.3f}', '-f', 'null', '-'], capture_output=True, text=True).stderr
mj = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:linear=true:measured_I={mj['input_i']}:measured_TP={mj['input_tp']}"
      f":measured_LRA={mj['input_lra']}:measured_thresh={mj['input_thresh']}:offset={mj['target_offset']}")
subprocess.run(['ffmpeg', '-v', 'error', '-y'] + ins + ['-filter_complex', pre + ',' + ln + ',aresample=44100[out]',
               '-map', '[out]', '-t', f'{TOTAL:.3f}', os.path.join(here, 'soundtrack.wav')], check=True)
print(f'soundtrack.wav: track from {start:.2f}s, its ending lands on the logo at {LOGO}s')
