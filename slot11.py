def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index]=a
    return arr

input_str = input("Nhập dãy số, cách nhau bởi dấu cách: ")
input_list = input_str.split()  # tách các số bằng dấu cách để được một list các chuỗi
try:
    input_list = [int(x) for x in input_list]  # chuyển các chuỗi sang số nguyên
    print("Dãy số đã được sắp xếp:", selection_sort(input_list))
except ValueError:
    print("Dữ liệu đầu vào không hợp lệ. Vui lòng nhập lại.")
######################################################3

inp = input("Nhập văn bản:")
char_count = [0] * 26
for string in inp:
    for char in string:
        if char.isalpha():
            char_count[ord(char.lower()) - ord('a')] += 1
for i in range(26):
    if char_count[i] > 0:
        print(chr(i + ord('a')) + " xuat hien " + str(char_count[i]))
###########################################################
string = "Hello, World!"
string = ''.join(filter(str.isalnum, string))
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print("the letter" , char ,"appears",count, "times", sep=' ')
########################################################
my_list = [5, 2, 8, 4, 0, 6, 1, 3]

sorted_list = sorted(my_list)
print(sorted_list)

my_list.sort(reverse=True)
print(my_list)





