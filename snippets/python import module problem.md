# Python import module problem
## Error
This is the error:
```bash
ModuleNotFoundError: No module named '<module>'
```

## Solutions
### Solution #1
First of all, che the PYTHONPATH:
```bash
echo $PYTHONPATH
```

If **PYTHONPATH** is null, you have to add the current project dir to the **PYTHONPATH**.
For setting **PYTHONPATH** more permanently (*LINUX*):
1. open the terminal;
2. Open the file *~/.bashrc* in your text editor – e.g. ```atom ~/.bashrc```;
3. Add the following line to the end:
    ```bash
    export PYTHONPATH=$(pwd)
    ```
4. Save, close your terminal application and Start your terminal application again, to read in the new settings, and type this to check:
    ```bash
    echo $PYTHONPATH
    ```

### Solution #2
Another solution is to use both relative path syntax.  
```
try:
    from dir.file import function
    from dir.file import class
except:
    from file import function
    from file import class
```