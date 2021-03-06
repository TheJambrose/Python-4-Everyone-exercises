# Exercise 5: Take the following Python code that stores a string:
#     text = "X-DSPAM-Confidence:    0.8475";
#
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted string
# into a floating point number.
#
# Exercise 6: Read the documentation of the string methods at
# https://docs.python.org/library/stdtypes.html#string-methods
# You might want to experiment with some of them to make sure you understand how
# they work. strip and replace are particularly useful.
#
# The documentation uses a syntax that might be confusing. For example, in
# find(sub[, start[, end]]), the brackets indicate optional arguments.
# So sub is required, but start is optional, and if you include start,
# then end is optional.

text = "X-DSPAM-Confidence:    0.8475";

colon_pos = text.find(":")
# print(colon_pos)

version_num = text[colon_pos + 1:].lstrip()
# print(version_num)


version_num_as_float = float(version_num)
print(version_num_as_float)
