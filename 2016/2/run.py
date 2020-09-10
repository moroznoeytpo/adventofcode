class Keypad:
    def __init__(self, filename: str = 'input.txt'):
        self._filename = filename
        self._keyboard = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self._current = [1, 1]
        self._password = []

    @property
    def password(self) -> str:
        return ''.join(self._password)

    def _get_instruction(self) -> tuple:
        with open(f'2016/2/{self._filename}') as file:
            for line in file:
                yield line

    def _move_line(self, line):
        for index in range(len(line)):
            move = line[index]
            if move == 'U' and self._current[0] > 0:
                self._current[0] -= 1
            elif move == 'D' and self._current[0] < 2:
                self._current[0] += 1
            elif move == 'L' and self._current[1] > 0:
                self._current[1] -= 1
            elif move == 'R' and self._current[1] < 2:
                self._current[1] += 1

    def _save_password(self):
        self._password.append(str(self._keyboard[self._current[0]][self._current[1]]))

    def press(self) -> None:
        for line in self._get_instruction():
            self._move_line(line)
            self._save_password()


if __name__ == '__main__':
    obj = Keypad('tmp.txt')
    obj.press()
    print(obj.password)
