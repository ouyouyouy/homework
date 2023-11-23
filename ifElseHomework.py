# Problem 1
# while True:
#     age = int(input('กรุณากรอกอายุของคุณ: '))
#     if age >= 18:
#         print('คุณสามารถลงทะเบียนเข้าใช้บริการได้')
#     elif age < 18:
#         print('คุณยังไม่สามารถลงทะเบียนเข้าใช้บริการได้')
#     else:
#         print('ไม่รู้จักอายุของคุณ')

#Problem 2
def sieve_of_eratosthenes(start,end):
    # สร้างรายการเพื่อเก็บจำนวนเฉพาะ
    primes = []

    # สร้างรายการเพื่อตรวจสอบว่าตำแหน่งนั้นๆเป็นจำนวนเฉพาะหรือไม่
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False # 0 และ 1 ไม่ใช่จำนวนเฉพาะ

    # ใช้เทคนิค Sieve of Eratosthenes
    for number in range(2,int(end**0.5) + 1):
        if is_prime:
            primes.append(number)
            for multiple in range(number * number, end + 1 , number):
                is_prime[multiple] = False

    # เพิ่มจำนวนเฉพาะที่เหลือลงในรายการ
    for number in range(max(2,int(end**0.5) + 1), end + 1):
        if is_prime[number]:
            primes.append(number)

    # กรองจำนวนเฉพาะที่อยู่ในช่วงที่กำหนด
    result = [prime for prime in primes if prime >= start]

    return result

# รับข้อมูลจากผู้ใช้
while True:
    start = int(input('ป้อนตัวเลขเริ่มต้น: '))
    end = int(input('ป้อนตัวเลขสิ้นสุด: '))

# เรียกใช้ฟังก์ช้นและแสดงผลลัพธ์
    result = sieve_of_eratosthenes(start,end)
    print('จำนวนเฉพาะในช่วง {} ถึง {} คือ : {}'.format(start,end,result))
    





















