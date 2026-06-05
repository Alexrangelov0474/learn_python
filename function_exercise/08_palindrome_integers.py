def palindrome_checker(number_to_check):
    if number_to_check == number_to_check[::-1]:
        return True
    return False

numbers = input().split(", ")

for num in numbers:
    result = palindrome_checker(num)
    print(result)