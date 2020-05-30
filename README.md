# File Transfer

Send files between computers on the same network using the TCP protocol

## Usage

1. Activate python virtual environment
```bash
source venv/bin/activate
```

NOTE: If you would prefer to install the python3 dependencies instead (or the virtual environment doesn't work for some reason), run the following command:
```bash
pip3 install $(cat pip3depends.txt
```

2. Run the program
```bash
python3 run.py
```
(If you want to run two instances of it, run `run2.py` as well. It runs the web server on port 8000 rather than port 5000)

3. Go to `http://127.0.0.1:5000` on your web browser (or `http://127.0.0.1:8000` if you are running `run2.py`)

4. Make sure that the receiver hits the `Listen for File` button BEFORE the sender sends the actual file.

Keep in mind that the `File` inputs refer to files in the current working directory

## To-do:

- [ ] Add multiple port support
- [ ] Establish connection before sending file
