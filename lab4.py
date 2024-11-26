# 4.1
# f = open('example.txt', 'w', encoding='utf-8')
# f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n')
# f.write('sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n')
# f.write('Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n')
# f.write('nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\n')
# f.write('reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla\n')
# f.write('pariatur. Excepteur sint occaecat cupidatat non proident, sunt in\n')
# f.write('culpa qui officia deserunt mollit anim id est laborum.\n')
# f.close()
# f = open('example.txt', encoding='utf-8')
# text = f.read()
# f.close()
# print(text)

# 4.3
# file_name =input('Enter the file name: ')
# encoding = input('Enter the encoding: ')

# total_characters = 0

# print('The contents of the file are: ')

# with open(file_name, 'w', encoding=encoding) as f:
#     while True:
#         line = input()
#         if line == '':
#             break
#         f.write(line + '\n')
#         total_characters += len(line)+1

# print(f'The file {file_name} has {total_characters} characters')

#