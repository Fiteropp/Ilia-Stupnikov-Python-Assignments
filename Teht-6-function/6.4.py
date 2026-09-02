


def convert_list(str_num_list: list[str]):
    float_list = []

    for item in str_num_list:
        try:
            float_list.append(float(item))
        except ValueError:
            return None

    return float_list


def list_summ(numbers: list[float]):
    summ = 0.0
    for num in numbers:
        summ += num

    return summ


user_input = input("Anna numeroita (erota välilyönnillä): ")
raw_number_list = user_input.split()
number_list = convert_list(raw_number_list)

if number_list == None:
    print("Syötteessä oli ei-numeerisia arvoja.")
else:
    numbers_sum = list_summ(number_list)
    print(f"listan numeroiden summa: {numbers_sum}")
