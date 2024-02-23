import sys, re, os

def separate_sum_sequences(lines:list[str]) -> list[str]:
    separated_lines = list()

    for line in lines:

        groups = re.findall('(.*?)=',line)

        if groups != None:
            for match in groups:
                separated_lines.append(match)

    return groups

def separate_digit_sequence(separated_line:str) -> list[str]:
    sequences = list()

    groups = re.findall('(\d+|\D+)',separated_line)

    if groups != None:

        for match in groups:
            sequences.append(match)

    return sequences

def digit_sequence_sum(sequence:str) -> int:
    sum = 0
    for digit in sequence:
        sum += int(digit)
    return sum

def main() -> None:
    if not os.isatty(0):
        lines = sys.stdin.readlines()

        if lines != None and len(lines) > 0:
            separated_lines = separate_sum_sequences(lines)
            sum_is_on = False

            for line in separated_lines:
                total_sum = 0
                match_groups_sequence = separate_digit_sequence(line)

                for match in match_groups_sequence:
                    if match.casefold() == 'on'.casefold() or match.casefold() == 'offon'.casefold():
                        sum_is_on = True

                    elif match.casefold() == 'off'.casefold():
                        sum_is_on = False

                    elif str(match).isdigit() and sum_is_on:
                            total_sum += digit_sequence_sum(match)

                print(f'Soma = {total_sum}')
        else:
            print('[Error] File is empty. Stopping program execution.')
    else:
        print('[Error] No input file could be found.\nPlease make sure you are piping the file through the standard input, when running program.py')

    return

if __name__ == '__main__':
    main()
    