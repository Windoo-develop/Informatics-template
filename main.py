# #2
# def F(x, y, z, w):
#     l1 = not(z <= x)
#     l2 = y <= w
#     l3 = l1 or l2
#     l4 = not(y)
#     return int(l3 or l4)
# print('x y z w | F(x, y, z, w)')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if F(x, y, z, w) == 0:
#                     print(f'{x} {y} {z} {w} | {F(x, y, z, w)}')
# #5
# def V(n):
#     s = ''
#     while n > 0:
#         s = str(n % 8) + s
#         n //= 8
#     return s
# def f(n):
#     r = bin(n)[2:]
#     if r[-1] == "0":
#         r = "10" + r
#     else:
#         r = "1" + r + "01"
#     return int(r, 2)
# a = []
# for n in range(1, 1001):
#     if f(n) >= 190:
#         a.append(n)
# print(min(a))
#8
# from itertools import *
# c = 0
# m = []
# for p in product(sorted("ПЛАНЕР"), repeat = 6):
#     s = ''.join(p)
#     c += 1
#     if c % 2 == 1 and s.count("П") == 0 and s.count("Р") == 0 and s.count("А") == 2 and s.count("Н") == 1:
#         m.append([c, s])
# print(m[-1])
#11
# from math import *
# for a in range(1, 1000):
#     n = 440
#     i = ceil(log2(a))
#     v1 = ceil(n * i / 8)
#     vv = v1 * 1892412
#     if vv >= 305726 * 1024:
#         print(a)
#         break
#16
# from functools import *
# @lru_cache
# def F(n):
#     if n == 1:
#         return 1
#     return (n-1) * F(n-1)
# for n in range(1, 17259):
#     F(n)
# print((F(17258)+ 3 * F(17257)) / F(17256))
#PRACTICE
# def f(n):
#     r = bin(n)[2:]
#     if r.count("1") % 2 == 0:
#         r = "10" + r[2:] + "0"
#     else:
#         r = "11" + r[2:] + "1"
#     return int(r, 2)
# a = []
# for n in range(0, 1000):
#     if f(n) >= 16:
#         a.append(n)
# print(min(a))
# from ipaddress import *
# net = ip_network(f'192.168.159.86/255.255.252.0', 0)
# print(net.network_address)
#14 - 1
# alf = "0123456789abcdefghijkl"
# for x in alf:
#     a = int(f'27{x}98876', 22)
#     b = int(f'26{x}51', 22)
#     c = int(f'711{x}5', 22)
#     if (a+b+c)%21 == 0:
#         print((a+b+c)//21)
#         break

#14 - 2
# a = 2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 65
# k = 0 
# while a > 0:
#     ost = a%27
#     if ost > 9:
#         k += 1
#     a = a // 27
#14 - 3
# ans = []
# for x in range(1, 2031):
#     a = 6**2030 + 6**100 - x
#     k0 = 0 
#     while a > 0:
#         ost = a%6
#         if ost == 0:
#             k0 += 1
#         a = a//6
#     ans += [k0]
# print(min(ans))

#2
# def F(x, y, z, w):
#     l1 = y and not x
#     l2 = x == w
#     l3 = l1 or l2
#     return l3 or not z
# print('x y z w | F(x, y, z, w)')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if F(x, y, z, w) == 0:
#                     print(x, y, z, w, '|', F(x, y, z, w))

#5
# def f(n):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = "11" + r + "11"
#     else:
#         r = "1" + r + "00"
#     return int(r, 2)
# ans = []
# for n in range(1, 1000):
#     if f(n) <= 416:
#         ans.append(f(n))
# print(max(ans))

#8
# from itertools import *
# c = 0
# m = []
# for p in product(sorted("ЦИФЕРБЛАТ"), repeat = 5):
#     s = ''.join(p)
#     c += 1
#     if c % 2 == 1 and s[0] != "Р" and s[0] != "Т" and s[0] != "Е" and s.count("Е") >= 2:
#         m.append([c, s])
# print(m[-1])

#7 - музыка
# from math import *
# f = 32000       # частота, Гц
# i = 16          # глубина кодирования, бит
# channels = 2    # моно — 1, стерео — 2
# t = 2 * 60 + 27 # время в секундах

# bits = f * i * channels * t

# print(bits / 8)            # байты
# print(bits / 8 / 1024)     # Кбайты
# print(ceil(bits / 8 / 1024))

#7 specific
# Размер одной фотографии ДО обработки, в битах
# before = 1024 * 768 * 30
# # Размер одной фотографии ПОСЛЕ обработки, в битах
# after = 800 * 600 * 28
# # Экономия на одной фотографии
# saving = before - after
# # Общая экономия: переводим Мбайты в биты
# total_saving = 95431.875 * 1024**2 * 8
# # Количество фотографий
# count = total_saving / saving
# print(count)  # 78848.0

c = 0
with open('9 (1).txt') as f:
    for line in f:
        a = list(map(int, line.split()))
        p = [x for x in a if a.count(x) == 3]
        q = [x for x in a if a.count(x) == 1]
        if len(p) == 3 and len(q) == 3:
            if max(a) ** 3 > q[0] * q[1] * q[2]:
                c += 1
print(c)