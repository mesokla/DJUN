# 7.6-16.0s of the reel: wallet-size switching (recording 11.6-20.3s, 3.3x), then zoom over "Як це працює" cards (still from 7.3s, frames from kb.py)
ffmpeg -v error -y -i "/root/.claude/uploads/67e304a1-e012-5699-b875-7c8b94ec998c/10ab7fa8-mSgEg-SfvzpXhG6UYQmrWw_1.mp4" -i "/root/.claude/uploads/67e304a1-e012-5699-b875-7c8b94ec998c/63eede92-_____________2026-11-10___13.17.42.mov" -loop 1 -i /tmp/claude-0/-home-user-DJUN/67e304a1-e012-5699-b875-7c8b94ec998c/scratchpad/prop/mask.png -framerate 30 -i /tmp/claude-0/-home-user-DJUN/67e304a1-e012-5699-b875-7c8b94ec998c/scratchpad/prop/kb/f%04d.png -loop 1 -i /home/user/DJUN/kraken-prop-reel/header.png -filter_complex "
[1:v]fps=30,trim=11.6:20.3,setpts=(PTS-STARTPTS)/3.3,crop=2060:1160:300:220,scale=1000:563:flags=lanczos,tpad=stop_mode=clone:stop_duration=0.35[s1];
[3:v]format=yuv420p,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=0.15[s2];
[s1][s2]concat=n=2:v=1:a=0,format=rgba[cc];
[2:v]format=gray,trim=0:8.57[mk];
[cc][mk]alphamerge,fade=in:st=0:d=0.15:alpha=1,setpts=PTS+7.6/TB[ov];
[0:v][ov]overlay=40:612:eof_action=pass[b0];[b0][4:v]overlay=0:0:shortest=1,format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -crf 17 -preset medium -c:a copy -movflags +faststart /home/user/DJUN/kraken-prop-reel/kraken-prop-reel.mp4
