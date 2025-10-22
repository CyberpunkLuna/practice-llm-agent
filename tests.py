# tests.py

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

#TESTING WRITE FILE

print(f'Results for lorem.txt')
print(f'{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")} \n')

print(f'Results for pkg/mroelorem.txt')
print(f'{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")} \n')

print(f'Results for /tmp/temp.txt')
print(f'{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")} \n')


#TESTING GET FILE CONTENT
# print(f'Result for lorem.txt:')
# print(f'{get_file_content("calculator", "lorem.txt")} \n')

# print(f'Result for main:')
# print(f'{get_file_content("calculator", "main.py")} \n')

# print(f'Result for pkg/calculator.py:')
# print(f'{get_file_content("calculator", "pkg/calculator.py")} \n')

# print(f'Result for /bin/cat:')
# print(f'{get_file_content("calculator", "/bin/cat")} \n')

# print(f'Result for pkg/does_not_exist.py:')
# print(f'{get_file_content("calculator", "pkg/does_not_exist.py")} \n')


#TESTING GETFILE INFO
# print(f'Result for current directory:')
# print(f'{get_files_info("calculator", ".")} \n')

# print(f'Result for pkg directory:')
# print(f'{get_files_info("calculator", "pkg")} \n')

# print(f'Result for /bin directory:')
# print(f'{get_files_info("calculator", "/bin")} \n')

# print(f'Result for ../ directory:')
# print(f'{get_files_info("calculator", "../")} \n')
