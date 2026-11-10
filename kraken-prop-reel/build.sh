ffmpeg -v error -y -i "/root/.claude/uploads/67e304a1-e012-5699-b875-7c8b94ec998c/10ab7fa8-mSgEg-SfvzpXhG6UYQmrWw_1.mp4" -i "/root/.claude/uploads/67e304a1-e012-5699-b875-7c8b94ec998c/63eede92-_____________2026-11-10___13.17.42.mov" -loop 1 -i /tmp/claude-0/-home-user-DJUN/67e304a1-e012-5699-b875-7c8b94ec998c/scratchpad/prop/mask.png -filter_complex "
[1:v]fps=30,split=3[r1][r2][r3];
[r1]trim=11.6:20.3,setpts=(PTS-STARTPTS)/3.3,crop=2060:1160:300:220,scale=1000:563:flags=lanczos,tpad=stop_mode=clone:stop_duration=0.35[s1];
[r2]trim=0:3.2,setpts=PTS-STARTPTS,crop=2476:1394:202:0,scale=1000:563:flags=lanczos[s2];
[r3]trim=6.6:8.95,setpts=PTS-STARTPTS,crop=2476:1394:202:0,scale=1000:563:flags=lanczos[s3];
[s1][s2][s3]concat=n=3:v=1:a=0,format=rgba[cc];
[2:v]format=gray,trim=0:8.4[mk];
[cc][mk]alphamerge,fade=in:st=0:d=0.15:alpha=1,fade=out:st=8.2:d=0.15:alpha=1,setpts=PTS+7.6/TB[ov];
[0:v][ov]overlay=40:612:eof_action=pass,format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -crf 17 -preset medium -c:a copy -movflags +faststart /home/user/DJUN/kraken-prop-reel/kraken-prop-reel.mp4
