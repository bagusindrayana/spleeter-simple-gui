import sys
import os
from tkinter import *
from tkinter import filedialog
from spleeter import *
from spleeter.utils import *
from spleeter.audio.adapter import get_default_audio_adapter
from spleeter.separator import Separator


root = Tk()

path = ''
output = ''

def proses():
    global path,output
    filename = os.path.basename(path)
    # separator = Separator('spleeter:2stems', stft_backend='auto', multiprocess=False)
    # audio_adapter = get_default_audio_adapter()
    # waveform, _ = audio_adapter.load(path, sample_rate=44100)
    # prediction = separator.separate(waveform)
    # out = prediction['other']

    # audio_adapter.save('/output/'+filename, out, 44100, 'mp3', '256k')
    audio_adapter = get_default_audio_adapter()
    separator = Separator(
        'spleeter:2stems',
        MWF=False,
        stft_backend='auto')
    
    separator.separate_to_file(
        path,
        output,
        audio_adapter=audio_adapter,
        offset=0.,
        duration=600.,
        codec='wav',
        bitrate='128k',
        filename_format='{filename}/{instrument}.{codec}',
        synchronous=False
    )
    separator.join()
    result.config(text=separator)

def browsefunc():
    global path
    path = filedialog.askopenfilename()
    filepathLabel.config(text=path)
    st = os.stat(path)
    filenameLabel.config(text=os.path.basename(path))
    filesizeLabel.config(text=os.path.getsize(path))

def selectFolder():
    global output
    output = filedialog.askdirectory()
    fileOutput.config(text=output)
    prosesbutton.pack()

    
    


browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

filepathLabel = Label(root)
filepathLabel.pack()

filenameLabel = Label(root)
filenameLabel.pack()

filesizeLabel = Label(root)
filesizeLabel.pack()

browsebutton = Button(root, text="Output", command=selectFolder)
browsebutton.pack()

fileOutput = Label(root)
fileOutput.pack()

prosesbutton = Button(root, text="Proses", command=proses)
prosesbutton.pack_forget()

result = Label(root)
result.pack()

root.title('Pisahkan vocal dengan music')
root.geometry("600x400+10+10")
root.mainloop()