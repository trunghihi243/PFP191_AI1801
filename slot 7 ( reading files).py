# f = open('input.txt', 'w+')
# f.write('alo')
# f.seek(0)
# data = f.read()
# mang = {}
# for char in data:
#     if char in mang:
#         mang[char] += 1
#     else:
#         mang[char] = 1
# 
# print("Số lần xuất hiện của từng kí tự:", mang)
# f.close()
##############################


filename = "input.txt"
text = input("Nhập văn bản:")

f= open(filename, "w")
f.write(text)

f=open(filename, "r")
char_count = [0] * 26


for string in f:
    for char in string:
        if char.isalpha():
            char_count[ord(char.lower()) - ord('a')] += 1
for i in range(26):
    if char_count[i] > 0:
        print(chr(i + ord('a')) + " xuat hien:" + str(char_count[i]))
