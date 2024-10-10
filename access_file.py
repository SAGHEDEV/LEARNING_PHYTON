# Accessibg files with python
file_name =  input("Enter a file name to read the number of line:")

try:
    f_hand = open(file_name)
except:
    print("File not found!")
    quit()
    
line_count = 0

for num in f_hand:
    line_count += 1
    num.rstrip()
    print(num.rstrip().upper())
    
print("Number of file line with Print Statement is:" , line_count)