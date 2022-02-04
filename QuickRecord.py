# Modules
from subprocess import run, Popen, PIPE, STDOUT
from os import path, environ
from sys import argv
from configparser import ConfigParser
from datetime import datetime
Config=ConfigParser()
Config.read(f'{path.abspath(path.split(argv[0])[0])}/settings.ini')
try:
    if argv[1].lower() == 'devices':
        Command='ffmpeg -hide_banner -stats -list_devices true -f dshow -i dummy'
        Process = Popen(Command, encoding='utf-8', stdout=PIPE, stderr=STDOUT)
        print('\nDevices:')
        while True:
            Output = Process.stdout.readline()
            if Output == '' or Process.poll() is not None:
                    break
            if Output:
                try:
                    if '(video)' in Output or '(audio)' in Output:
                        if '(video)' in Output:
                            Splitter='(v'
                            Prefix='Video:'
                        elif 'audio' in Output:
                            Splitter='(a' 
                            Prefix='Audio:'
                        Hardware=Output.strip().split('] ')[1].split(f' {Splitter}')[0].replace('"','')
                        print(f"{Prefix} {Hardware}", end='\n',flush=True)
                except:
                    pass
except:
    Index=1
    AudioDevices=""
    while True:
        try:
            if Config["audio"][str(Index)].lower() == 'none':
                break 
            AudioDevices+=f'-f dshow -i audio="{Config["audio"][str(Index)]}" '
            Index+=1
        except:
            break  
        AudioDevices=AudioDevices.strip()    
    OutputPath=Config['ffmpeg']['output'].lower()
    if OutputPath=='default':
        OutputPath=f'{environ["USERPROFILE"]}/Videos'
    if Config['video']['input'].lower() == 'desktop':
        Input='desktop'
        VideoSize=f'-video_size {Config["video"]["resolution"]}'
    else:
        Input=f'title="{Config["video"]["input"]}"' 
        VideoSize=""  
        print('Warning: Capturing Window Resolution.\n') 

    run('powershell -c (New-Object Media.SoundPlayer "C:\\Windows\\Media\\notify.wav").PlaySync();')
    Command=f'ffmpeg -y -loglevel error -hide_banner -stats -framerate {Config["video"]["fps"]} {VideoSize} -f gdigrab -draw_mouse 1 -i {Input} {AudioDevices} {Config["ffmpeg"]["arguments"]} "{OutputPath}/{datetime.now().strftime("%d-%m-%Y %H-%M-%S")}{Config["video"]["container"]}"'
    print(f'Command: \n{Command}\n')
    print('Press Q to stop recording.\n')
    run(Command,shell=True)