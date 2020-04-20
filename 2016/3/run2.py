class Triangles:
    def __init__(self, filename: str = 'input.txt'):
        self._filename = filename
        self._count = 0
        self._line_position = 0

        self._triangles = self._get_clean_triangles()

    @property
    def count(self) -> int:
        return self._count

    def _get_clean_triangles(self):
        return [[], [], []]

    def _read_file(self) -> tuple:
        with open(f'2016/3/{self._filename}') as file:
            for line in file:
                yield line

    def _read_line(self, line: str):
        numbers = []
        for item in line.split(' '):
            if item:
                numbers.append(int(item))
        return numbers

    def _collect_triangle(self, numbers: list) -> None:
        for index, item in enumerate(numbers):
            self._triangles[index].append(numbers[index])
        if self._line_position % 3 == 0:
            for item in self._triangles:
                self._check_triangle(item)
            self._triangles = self._get_clean_triangles()

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

    def execute(self):
        for line in self._read_file():
            self._line_position += 1
            numbers = self._read_line(line)
            self._collect_triangle(numbers)


if __name__ == '__main__':
    obj = Triangles('input.txt')
    obj.execute()
    print(obj.count)
