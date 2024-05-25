# Basic String Operations
s1 = "Hello"
s2 = "World"
result_concatenation = s1 + " " + s2
result_repetition = s1 * 3
first_char = s1[0]
last_char = s1[-1]
substr = s1[1:4]
length = len(s1)

# String Methods
s = "Hello World"
s_lower = s.lower()
s_upper = s.upper()
s_title = s.title()
s_capitalized = s.capitalize()
s_swapcase = s.swapcase()
index_find = s.find("World")
index_index = s.index("World")
exists = "World" in s
new_s = s.replace("World", "Python")
words = s.split()
joined = " ".join(words)
stripped = s.strip()
lstripped = s.lstrip()
rstripped = s.rstrip()
is_alpha = s.isalpha()
is_digit = s.isdigit()
is_alnum = s.isalnum()
is_lower = s.islower()
is_upper = s.isupper()
is_space = s.isspace()
is_title = s.istitle()

# Advanced String Operations
s_format = "Hello %s" % "World"
s_format_method = "Hello {}".format("World")
name = "World"
s_fstring = f"Hello {name}"
left_justified = s.ljust(10)
right_justified = s.rjust(10)
centered = s.center(10)
count = s.count("o")
parts = s.partition(" ")
starts_with = s.startswith("Hello")
ends_with = s.endswith("World")

# Multiline Strings
multi_line = """This is
a multiline
string."""

# Raw Strings
raw_str = r"C:\Users\Name"

# Printing results
print("Concatenation:", result_concatenation)
print("Repetition:", result_repetition)
print("First character:", first_char)
print("Last character:", last_char)
print("Substring:", substr)
print("Length:", length)
print("Lowercase:", s_lower)
print("Uppercase:", s_upper)
print("Title case:", s_title)
print("Capitalized:", s_capitalized)
print("Swapcase:", s_swapcase)
print("Index (find):", index_find)
print("Index (index):", index_index)
print("Substring exists:", exists)
print("Replace:", new_s)
print("Split:", words)
print("Joined:", joined)
print("Stripped:", stripped)
print("Left Stripped:", lstripped)
print("Right Stripped:", rstripped)
print("Is alpha:", is_alpha)
print("Is digit:", is_digit)
print("Is alphanumeric:", is_alnum)
print("Is lowercase:", is_lower)
print("Is uppercase:", is_upper)
print("Is whitespace:", is_space)
print("Is title case:", is_title)
print("Formatted string (old-style):", s_format)
print("Formatted string (str.format()):", s_format_method)
print("Formatted string (f-string):", s_fstring)
print("Left justified:", left_justified)
print("Right justified:", right_justified)
print("Centered:", centered)
print("Count of 'o':", count)
print("Partitioned:", parts)
print("Starts with 'Hello':", starts_with)
print("Ends with 'World':", ends_with)
print("Multiline string:", multi_line)
print("Raw string:", raw_str)
