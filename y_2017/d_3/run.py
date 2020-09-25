def get_line(number: int):
    square_index = 3
    square = square_index * square_index
    while(True):
        new_square = square_index * square_index
        diff = (new_square - square) / 4
        square = new_square

        if number < square:
            line_index = 4
            line_number = number
            while(True):
                if line_index == 0:
                    break
                if number < line_number:
                    break
                line_index -= 1
                line_number = square - line_index * diff
            middle_line_number = int(line_number - diff / 2)

            shift = 0
            if number > middle_line_number:
                shift = number - middle_line_number
            elif number < middle_line_number:
                shift = middle_line_number - number
            s_i = int(square_index / 2)
            return s_i + shift

        square_index += 2


print(get_line(347991))  # 34581
