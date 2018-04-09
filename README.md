# quick-zip
With a single command, instantly zip a copy of all files in your current directory. Easily configure the quick-zip to only zip certain file extensions or name the zip file something different.

## Instructions
There is a quick installation step before you can use `quick-zip`.

1. Paste everything after the `$` sign into a terminal window and hit enter.
```
$ wget https://raw.githubusercontent.com/ImFeelingDucky/quick-zip/master/install.py && python3 install.py
```

## Configuration
This will create a new zip file of (by default) all `.py` and `.java` files in your current directory. You will probably want to configure quick-zip to name the zip file something specific, such as `ABCXYZ001.zip`.

1. Open `zip.py` in a code editor.
```shell
$ nano ~/bin/zip.py
```

Change the value of FILENAME; for example:
```python
FILENAME = 'ABCXYZ001'
```

## Usage
You can now use quick-zip.

1. In a directory with files you want to zip: type everything after the `$` sign into a terminal window and hit enter.
```shell
$ zip.py
```
Enjoy!
