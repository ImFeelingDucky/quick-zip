# zippit
With a single command, instantly zip a copy of all files in your current directory. Easily configure `zippit` to only zip certain file extensions or name the zip file something different.

## Instructions
There is a quick installation step before you can use `quick-zip`.

1. Paste everything after the `$` sign into a terminal window and hit enter.
```bash
$ curl https://raw.githubusercontent.com/ImFeelingDucky/quick-zip/master/install | bash
```

## Configuration
This will create a new zip file of (by default) all `.py` and `.java` files in your current directory. You will probably want to configure `zippit` to name the zip file something specific, such as `ABCXYZ001.zip`.

1. Open `zip.py` in a code editor.
```bash
$ nano ~/bin/zip.py
```

2. Change the value of FILENAME; for example, so that `zippit` names the zip files as your student number:
```python
FILENAME = 'ABCXYZ001'
```

3. (Optional) You may also want to disable `zippit`'s prompts before it overwrites an older zip file with the same name, like this:
```python
PROMPT_BEFORE_OVERWRITING = False
```

4. (Optional) And lastly, you can change the file extensions `zippit` will include in the zip. For example, to add `.cpp` file extension, for C++ files, edit this line so it appears like this:
```python
DEFAULT_EXTENSIONS = ['.py', '.java', '.cpp']
```

## Usage
You can now use `zippit`!

Just type `zippit` into the terminal inside a directory with the files you want to zip.

Enjoy!
