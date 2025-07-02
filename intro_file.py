'''

File I/O in Python

Python can be used to perform operations on a file. (read & write data)
Types of all files
1 . Text Files : .txt, .docx, .10g etc.
2. Binary Files : .mp4, .mov, .png, .jpeg etc.
'''


# file = open("file.txt", "w")
# file.write("Hello, i'm ram and i wanna tell you that i'm learning python")
# content = file.read()
# print(content)
# file.close()

# python file operations =>
'''
| Method           | Use                          | Example Use Case                        |
| ---------------- | ---------------------------- | --------------------------------------- |
| `open()`         | Open a file                  | `open("file.txt", "r")`                 |
| `read()`         | Read entire file content     | Load data, configs, or text             |
| `readline()`     | Read one line                | Processing large files line by line     |
| `write()`        | Write string to a file       | Saving user input, logs, or output      |
| `writelines()`   | Write list of strings        | Save multiple lines at once             |
| `close()`        | Close the file               | Always do this to save resources        |
| `with open(...)` | Context manager (auto close) | Best practice for safety and simplicity |

'''


