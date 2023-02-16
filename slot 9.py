def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

def inprimes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if isprime(num)== True:
            primes.append(num)
        num += 1
    return primes

def get_grade(score):
    if score >= 8.5:
        return 'A'
    elif score >= 7.0:
        return 'B'
    elif score >= 5.5:
        return 'C'
    elif score >= 4.0:
        return 'D'
    elif score >= 2.5:
        return 'E'
    else:
        return 'F'

def convert_to_gpa(score):
    if score >= 8.5:
        return 4.0
    elif score >= 7.0:
        return 3.0
    elif score >= 5.5:
        return 2.0
    elif score >= 4.0:
        return 1.0
    else:
        return 0.0

while True:
    choice = input("Vui lòng chọn một trong hai tùy chọn sau:\n"
                   "1. Tìm n số nguyên tố đầu tiên và lưu vào file.\n"
                   "2. Tính điểm GPA của các sinh viên và thêm sinh viên mới.\n"
                   "Nhập 1 hoặc 2: ")
    
    if choice == "1":
        while True:
            n = input("Nhập số tự nhiên n: ")
            if n.isdigit():
                n = int(n)
                break
            else:
                print("Hãy nhập một số tự nhiên hợp lệ.")
        primes = inprimes(n)
        filename = "input.txt"
        with open(filename, "w") as f:
            f.write(str(primes))
        break
    elif choice == "2":
        grades = {
            'A': 8.5,
            'B': 7.4,
            'C': 6.2,
            'D': 5.1,
            'E': 1.5,
            'F': 0.2
        }
        
        print('Bảng điểm đại học')
        print('------------------------------------------')
        print('{:<10} {:<10} {:<15} {:<10}'.format('Tên', 'Điểm', 'Thang điểm 4 ', 'Xếp hạng'))
        print('------------------------------------------')

        for name, score in grades.items():
            grade = get_grade(score)
            gpa = convert_to_gpa(score)
            print('{:<10} {:<10} {:<15} {:<10}'.format(name, score, gpa, grade))

        while True:
            name = input("Nhập tên sinh viên (hoặc 'done' để kết thúc): ")
            if name == "done":
                break
            score = float(input("Nhập điểm của sinh viên: "))
            grades[name] = score

        print('------------------------------------------')
        print('{:<10} {:<10} {:<10} {:<10}'.format('Tên', 'Điểm', 'Thang điểm 4 ', 'Xếp hạng'))
        print('------------------------------------------')

        for name, score in grades.items():
            grade = get_grade(score)
            gpa = convert_to_gpa(score)
            print('{:<10} {:<10} {:<10} {:<10}'.format(name, score, gpa, grade))

