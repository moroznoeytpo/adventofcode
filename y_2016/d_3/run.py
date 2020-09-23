class Triangles:
    def __init__(self, filename: str = 'input.txt'):
        self._filename = filename
        self._count = 0

    @property
    def count(self) -> int:
        return self._count

    def _read_file(self) -> tuple:
        with open(f'2016/3/{self._filename}') as file:
            for line in file:
                yield line

    def _read_line(self, line: str) -> list:
        numbers = []
        for item in line.split(' '):
            if item:
                numbers.append(int(item))
        return numbers

    def _check_triangle(self, numbers: list) -> None:
        max_number = 0
        sum_number = 0
        for number in numbers:
            if max_number:
                if number < max_number:
                    sum_number += number
                else:
                    sum_number += max_number
                    max_number = number
            else:
                max_number = number
        if max_number < sum_number:
            self._count += 1

    def execute(self) -> None:
        for line in self._read_file():
            numbers = self._read_line(line)
            self._check_triangle(numbers)


if __name__ == '__main__':
    obj = Triangles('input.txt')
    obj.execute()
    print(obj.count)
