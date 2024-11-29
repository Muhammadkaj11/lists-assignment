
def generate_squares(start, end):

    squares = [x ** 2 for x in range(start, end + 1)]
    
    even_squares = [num for num in squares if num % 2 == 0]
    odd_squares = [num for num in squares if num % 2 != 0]
    
    return even_squares, odd_squares

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

even_squares, odd_squares = generate_squares(start, end)

print(f"Even squares: {even_squares}")
print(f"Odd squares: {odd_squares}")
