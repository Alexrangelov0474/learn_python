number_of_electrons = int(input())
shell = []
number_of_shell = 0
while number_of_electrons > 0:
    number_of_shell += 1
    max_electrons_in_shell = 2 * number_of_shell ** 2
    if number_of_electrons >= max_electrons_in_shell:
        shell.append(max_electrons_in_shell)
    else:
        shell.append(number_of_electrons)
    number_of_electrons -= max_electrons_in_shell
print(shell)