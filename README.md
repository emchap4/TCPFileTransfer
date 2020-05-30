# File Transfer

Send files between computers on the same network using the TCP protocol

## Usage

1. Create virtual env for project 
```bash
python3 -m venv .env && source .env/bin/activate && pip install -r requirements.txt 
```

or simply install requirements without venv
```bash
pip install -r requirements.txt
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
- [ ] Finish pywebview integration
