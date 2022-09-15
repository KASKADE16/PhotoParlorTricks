## [GIFAssemble](https://github.com/KASKADE16/PhotoParlorTricks/tree/main/GIFAssemble)

### What does it do?

it reassemble all pictures in a folder back to a gif picture.

I suggest you using this gadget for folders created by GifDismember,for these photos extracted from thee are already numbered in order.so as to making this rewind more viable.

the usage is quite easy compared to its gemini,just

```bash
python subfolder.py
```

this makes all folder,which are in the same folder as the .py runs.enter its process.



### Index

the gif output feature some indexes,including:

```bash
	usage: subfolder.py [-h] [-f FRAME] [-r REVERSE] [-n NAME]

options:
  -h, --help            show this help message and exit
  -f FRAME, --frame FRAME
                        决定gif的帧数
                        decide the framerate of the gif
  -r REVERSE, --reverse REVERSE
                        决定gif是否倒放
                        decide whether the gif is reversed or not
  -n NAME, --name NAME  决定gif的名字
  						decide the gif's name
```

for example

```bash
python subfolder.py --frame 60 --reverse 1
```

