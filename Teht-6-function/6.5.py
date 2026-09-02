


def convert_list(str_num_list: list[str]):
    float_list = []

    for item in str_num_list:
        try:
            float_list.append(float(item))
        except ValueError:
            return None

    return float_list


def filter_odd_numbers(numbers: list[float]):
    numbers[:] = [num for num in numbers if num % 2 == 0]
    return numbers


user_input = input("Anna numeroita (erota välilyönnillä): ")
raw_number_list = user_input.split()
number_list = convert_list(raw_number_list)
original_list = number_list.copy()

if number_list == None:
    print("Syötteessä oli ei-numeerisia arvoja.")
else:
    filtered_list = filter_odd_numbers(number_list)
    print(f"alkuperäinen lista: {original_list}")
    print(f"muokattu lista: {filtered_list}")
