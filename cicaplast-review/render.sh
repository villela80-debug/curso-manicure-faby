#!/usr/bin/env bash
# Monta video-final.mp4 (1080x1920, 30 fps) a partir dos cards e da narração.
# Os cortes seguem as pausas da narracao.mp3.
set -euo pipefail
cd "$(dirname "$0")"
CORTES=(0 5.06 14.0 19.3 28.76 35.16 41.1 48.87 57.37 62.0)
tmp=$(mktemp -d)
: > "$tmp/lista.txt"
for i in $(seq 1 9); do
  ini=${CORTES[$((i-1))]}; fim=${CORTES[$i]}
  dur=$(echo "$fim - $ini" | bc)
  frames=$(printf '%.0f' "$(echo "$dur * 30" | bc)")
  ffmpeg -v error -y -loop 1 -i "cards/C0$i.png" -frames:v "$frames" \
    -vf "scale=2160:3840,zoompan=z='1+0.04*on/$frames':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,format=yuv420p" \
    -c:v libx264 -preset medium -crf 18 "$tmp/c$i.mp4"
  echo "file '$tmp/c$i.mp4'" >> "$tmp/lista.txt"
done
ffmpeg -v error -y -f concat -safe 0 -i "$tmp/lista.txt" -i narracao.mp3 \
  -c:v copy -af "apad" -c:a aac -b:a 192k -t 62 -movflags +faststart video-final.mp4
rm -rf "$tmp"
