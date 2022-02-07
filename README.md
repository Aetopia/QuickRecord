# QuickRecord
A Python wrapper for FFmpeg's gdigrab.

# Usage
```ini
[video]
resolution = 1920x1080
fps = 60
container = .mp4
input = desktop

[audio]
1 = none

[ffmpeg]
arguments = -c:v libx264 -crf 0 -preset ultrafast
output = default
```
#### 1. Video
1. `resolution` => Video Resolution.
2. `fps` => Framerate.
3. `container` => Video Container.
4. `input` => desktop (For capturing display.) or specify a window name.

#### 2. Audio
Add Audio Devices. (Use `None` for omitting audio.)
```ini
[audio]
1 = Microphone # Input 1
2 = Stereo Mix # Input 2
```

Get a list of usable devices > `quickrecord.py devices`:                               
Output:
```
Devices:
Video: OBS Virtual Camera
Audio: Microphone (USB PnP Sound Device)
Audio: Stereo Mix (Realtek High Definition Audio)
```

#### 3. FFmpeg
1. `arguments` => Encoding Arguments.
2. `output` => Output Folder (default => User's Videos Folder)
