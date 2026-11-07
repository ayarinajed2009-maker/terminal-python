PACKAGE = "Nano"
VERSION = 0.1
MADE_BY = "Najed Ayari"
NEEDS = "SYSTEM"









import os
import sys
import argparse
import platform
from pathlib import Path


IS_WINDOWS = platform.system() == "Windows"

if IS_WINDOWS:
    import msvcrt
else:
    import tty
    import termios
    import select


class PyNano:

    def __init__(self, filename=None):
        self.filename = filename
        self.lines = [""]
        self.x = 0
        self.y = 0
        self.offset = 0
        self.modified = False
        self.clipboard = ""
        self.running = True
        self.message = "Welcome to PyNano!"

        if filename and os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as f:
                self.lines = f.read().splitlines() or [""]

    # -------------------------
    # TERMINAL
    # -------------------------

    def terminal_size(self):
        try:
            size = os.get_terminal_size()
            return size.columns, size.lines
        except OSError:
            return 80, 24

    def clear(self):
        print("\033[2J\033[H", end="")

    def move_cursor(self, row, col):
        print(f"\033[{row};{col}H", end="")

    def write(self, text):
        print(text, end="")

    # -------------------------
    # DRAW
    # -------------------------

    def draw(self):
        width, height = self.terminal_size()

        visible = max(1, height - 3)

        self.clear()

        title = f" PyNano - {self.filename or 'New File'} "
        self.write("\033[7m" + title[:width].ljust(width) + "\033[0m\n")

        for i in range(visible):
            index = self.offset + i

            if index < len(self.lines):
                line = self.lines[index]
            else:
                line = ""

            self.write(line[:width].ljust(width) + "\n")

        status = (
            f" {'Modified' if self.modified else 'Saved'}"
            f" | Line {self.y + 1}"
            f" | Column {self.x + 1}"
            f" | {self.message}"
        )

        self.write("\033[7m" + status[:width].ljust(width) + "\033[0m\n")

        shortcuts = (
            "^G Help  ^O Save  ^W Search  "
            "^K Cut  ^U Paste  ^X Exit"
        )

        self.write("\033[7m" + shortcuts[:width].ljust(width) + "\033[0m")

        screen_y = self.y - self.offset + 2
        screen_x = min(self.x + 1, width)

        self.move_cursor(screen_y, screen_x)
        sys.stdout.flush()

    # -------------------------
    # KEYBOARD INPUT
    # -------------------------

    def get_key(self):
        if IS_WINDOWS:
            key = msvcrt.getwch()

            if key in ("\x00", "\xe0"):
                special = msvcrt.getwch()

                return {
                    "H": "UP",
                    "P": "DOWN",
                    "K": "LEFT",
                    "M": "RIGHT",
                    "S": "DELETE",
                    "G": "HOME",
                    "O": "END",
                }.get(special, "UNKNOWN")

            if key == "\r":
                return "ENTER"

            if key == "\x08":
                return "BACKSPACE"

            if key == "\x1b":
                return "ESC"

            if key == "\x7f":
                return "UNKNOWN"

            if ord(key) < 32:
                return f"CTRL_{ord(key)}"

            return key

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)

            key = sys.stdin.read(1)

            if key == "\x1b":
                if select.select([sys.stdin], [], [], 0.05)[0]:
                    second = sys.stdin.read(1)

                    if second == "[":
                        third = sys.stdin.read(1)

                        return {
                            "A": "UP",
                            "B": "DOWN",
                            "C": "RIGHT",
                            "D": "LEFT",
                            "H": "HOME",
                            "F": "END",
                            "3": self.read_escape_delete(),
                        }.get(third, "ESC")

                return "ESC"

            if key in ("\r", "\n"):
                return "ENTER"

            if key in ("\x7f", "\x08"):
                return "BACKSPACE"

            if ord(key) < 32:
                return f"CTRL_{ord(key)}"

            return key

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def read_escape_delete(self):
        if IS_WINDOWS:
            return "DELETE"

        if select.select([sys.stdin], [], [], 0.05)[0]:
            sys.stdin.read(1)

        return "DELETE"

    # -------------------------
    # PROMPT
    # -------------------------

    def prompt(self, message):
        width, height = self.terminal_size()

        self.move_cursor(height, 1)
        print("\033[2K" + message, end="", flush=True)

        result = input()

        return result

    # -------------------------
    # SAVE
    # -------------------------

    def save(self):
        if not self.filename:
            self.filename = self.prompt("Save as: ")

        if not self.filename:
            return

        try:
            with open(self.filename, "w", encoding="utf-8",
                      newline="\n") as f:
                f.write("\n".join(self.lines))

            self.modified = False
            self.message = "File saved successfully!"

        except OSError as error:
            self.message = f"Save error: {error}"

    # -------------------------
    # EDITING
    # -------------------------

    def insert(self, char):
        line = self.lines[self.y]

        self.lines[self.y] = (
            line[:self.x] + char + line[self.x:]
        )

        self.x += len(char)
        self.modified = True

    def newline(self):
        line = self.lines[self.y]

        self.lines[self.y] = line[:self.x]
        self.lines.insert(self.y + 1, line[self.x:])

        self.y += 1
        self.x = 0
        self.modified = True

    def backspace(self):
        if self.x > 0:
            line = self.lines[self.y]

            self.lines[self.y] = (
                line[:self.x - 1] + line[self.x:]
            )

            self.x -= 1

        elif self.y > 0:
            previous_length = len(self.lines[self.y - 1])

            self.lines[self.y - 1] += self.lines[self.y]
            del self.lines[self.y]

            self.y -= 1
            self.x = previous_length

        else:
            return

        self.modified = True

    def delete(self):
        line = self.lines[self.y]

        if self.x < len(line):
            self.lines[self.y] = (
                line[:self.x] + line[self.x + 1:]
            )

        elif self.y < len(self.lines) - 1:
            self.lines[self.y] += self.lines[self.y + 1]
            del self.lines[self.y + 1]

        else:
            return

        self.modified = True

    # -------------------------
    # CLIPBOARD
    # -------------------------

    def cut(self):
        self.clipboard = self.lines[self.y]

        if len(self.lines) > 1:
            del self.lines[self.y]
            self.y = min(self.y, len(self.lines) - 1)
        else:
            self.lines[0] = ""

        self.x = 0
        self.modified = True

    def paste(self):
        self.insert(self.clipboard)

    # -------------------------
    # SEARCH
    # -------------------------

    def search(self):
        query = self.prompt("Search: ")

        if not query:
            return

        for i in range(self.y, len(self.lines)):
            start = self.x if i == self.y else 0
            pos = self.lines[i].find(query, start)

            if pos >= 0:
                self.y = i
                self.x = pos
                self.message = "Found!"
                return

        self.message = "Text not found!"

    # -------------------------
    # CURSOR
    # -------------------------

    def move(self, key):
        if key == "UP":
            self.y = max(0, self.y - 1)

        elif key == "DOWN":
            self.y = min(len(self.lines) - 1, self.y + 1)

        elif key == "LEFT":
            if self.x > 0:
                self.x -= 1
            elif self.y > 0:
                self.y -= 1
                self.x = len(self.lines[self.y])

        elif key == "RIGHT":
            if self.x < len(self.lines[self.y]):
                self.x += 1
            elif self.y < len(self.lines) - 1:
                self.y += 1
                self.x = 0

        elif key == "HOME":
            self.x = 0

        elif key == "END":
            self.x = len(self.lines[self.y])

        self.x = min(self.x, len(self.lines[self.y]))

    # -------------------------
    # MAIN LOOP
    # -------------------------

    def run(self):
        try:
            while self.running:
                width, height = self.terminal_size()

                visible = max(1, height - 3)

                if self.y < self.offset:
                    self.offset = self.y

                if self.y >= self.offset + visible:
                    self.offset = self.y - visible + 1

                self.draw()
                key = self.get_key()

                if key == "CTRL_24":
                    if self.modified:
                        answer = self.prompt(
                            "Save changes? (y/n/c): "
                        ).lower()

                        if answer == "c":
                            continue

                        if answer == "y":
                            self.save()

                            if self.modified:
                                continue

                    self.running = False

                elif key == "CTRL_15":
                    self.save()

                elif key == "CTRL_11":
                    self.cut()

                elif key == "CTRL_21":
                    self.paste()

                elif key == "CTRL_23":
                    self.search()

                elif key == "CTRL_7":
                    self.message = (
                        "Ctrl+O Save | Ctrl+X Exit | "
                        "Ctrl+W Search | Ctrl+K Cut"
                    )

                elif key == "ENTER":
                    self.newline()

                elif key == "BACKSPACE":
                    self.backspace()

                elif key == "DELETE":
                    self.delete()

                elif key in (
                    "UP", "DOWN", "LEFT", "RIGHT",
                    "HOME", "END"
                ):
                    self.move(key)

                elif isinstance(key, str) and len(key) == 1:
                    if key.isprintable():
                        self.insert(key)

        finally:
            self.clear()
            print("PyNano closed.")

    # -------------------------
    # PUBLIC OPEN FUNCTION
    # -------------------------

def open_file(filename=None):
    path = None

    if filename:
        path = str(Path(filename).expanduser().resolve())

        if not os.path.isfile(path):
            parent = os.path.dirname(path)

            if parent and not os.path.isdir(parent):
                raise FileNotFoundError(
                    f"Directory does not exist: {parent}"
                )

    editor = PyNano(path)
    editor.run()


# -------------------------
# COMMAND LINE
# -------------------------

def main():
    parser = argparse.ArgumentParser(
        prog="Nano",
        description="Nano - GNU Terminal Text Editor"
    )

    parser.add_argument(
        "file",
        nargs="?",
        help="File to open or create"
    )

    args = parser.parse_args()

    open_file(args.file)

class nano():
    def open():
        main()