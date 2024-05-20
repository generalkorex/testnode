
# Read HTML data from file
with open("path_to_your_html_file.html", 'r') as file:
    html_data = file.read()

# Extract colors from HTML data
pattern = r'<div style="background-color:(#[0-9a-fA-F]+)"></div>'
colors = re.findall(pattern, html_data)

# Calculate mean color
total_colors = len(colors)
total_red = sum(1 for color in colors if color == '#FF0000')
mean_color = total_red / total_colors

# Calculate mode color
mode_color = max(set(colors), key=colors.count)

# Calculate median color
colors.sort()
n = len(colors)
if n % 2 == 0:
    median_color = (colors[n//2 - 1] + colors[n//2]) / 2
else:
    median_color = colors[n//2]

# Calculate variance of colors
mean_color = sum(colors) / len(colors)
variance = sum((color - mean_color) ** 2 for color in colors) / len(colors)

# Calculate probability of red color
red_probability = total_red / total_colors

# Save colors and frequencies to PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cursor = conn.cursor()
for color in set(colors):
    frequency = colors.count(color)
    cursor.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, frequency))
conn.commit()
conn.close()

# Recursive searching algorithm
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter a number to search: "))
index = 0
found = False
while index < len(numbers):
    if numbers[index] == target:
        found = True
        break
    index += 1
if found:
    print("Number found!")
else:
    print("Number not found!")

# Generate random binary number and convert to base 10
binary_number = ''.join(str(random.randint(0, 1)) for _ in range(4))
decimal_number = int(binary_number, 2)
print("Random binary number:", binary_number)
print("Decimal equivalent:", decimal_number)

# Calculate sum of first 50 fibonacci sequence
fib_sequence = [0, 1]
for i in range(2, 50):
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
fib_sum = sum(fib_sequence[:50])
print("Sum of first 50 fibonacci sequence:", fib_sum)
