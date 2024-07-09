from io import BytesIO



# Create a new BytesIO object with initial content
binary_buffer = BytesIO(b'Hii GeeksforGeeks!')
 
# Read from the buffer
read_content = binary_buffer.read()
print("Read content:", read_content)
 
# Write new content to the buffer
binary_buffer.write(b' I am adding New articles.')

# Read from the buffer
read_content = binary_buffer.read()
print("Read content:", read_content)
 
# Get the updated contents of the buffer as bytes
updated_content = binary_buffer.getvalue()
 
# Print the updated content
print("Updated content:", updated_content)