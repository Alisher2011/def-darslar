# def name(a):
#     if a>0:
#         return a+1
#     else:
#         return a
# print(name(int(input("a : "))))

# def name(a):
#     if a>0:
#         return a+1
#     elif a<0:
#         return a-2
#     elif a==0:
#         return 10
# print(name(int(input("a : "))))

# def name(a,b,c):
#     if a>0 and b>0 and c<0:
#         return "2 ta musbat 1ta manfiy"
#     elif a>0 and b<0 and c>0:
#         return "2 ta musbat 1ta manfiy"
#     elif a<0 and b>0 and c>0:
#         return "2 ta musbat 1ta manfiy"
#     elif a<0 and b<0 and c<0:
#         return "3ta manfiy"
#     elif a>0 and b>0 and c>0:
#         return "3ta musbat"
#     elif a<0 and b<0 and c>0:
#         return "2 ta manfiy 1ta musbat"
#     elif a<0 and b>0 and c<0:
#         return "2 ta manfiy 1ta musbat"
#     elif a>0 and b<0 and c<0:
#         return "2 ta manfiy 1ta musbat"
# print(name(int(input("a : ")),int(input("b : ")),int(input("c : "))))

# def name(a,b):
#     if b<a:
#         return a
#     elif a<b:
#         return b
#     else:
#         return "teng"
# print(name(int(input("a : ")),int(input("b : "))))

# def name(a,b):
#     if b<a:
#         return b
#     elif a<b:
#         return a
#     else:
#         return "teng"
# print(name(int(input("a : ")),int(input("b : "))))

# def name(a,b):
#     if b<a:
#         return f"{b} kichik {a} katta"
#     elif a<b:
#         return f"{b} katta {a} kichik"
#     else:
#         return "teng"
# print(name(int(input("a : ")),int(input("b : "))))

# def name(a,b):
#     if a>b:
#         b=a
#         return b
#     elif a<b:
#         a=b
#         return a
# print(name(float(input("a")),float(input("b"))))

# def name(a,b):
#     if a!=b:
#         return a+b
#     elif a==b:
#         return 0
# print(name(int(input("a")),int(input("b"))))

# def name(a,b):
#     if a!=b:
#         if a>b:
#             return a
#         else:
#             return b
#     elif a==b:
#             return 0
# print(name(int(input("a")),int(input("b"))))

# def name(a,b,c):
#     if a>b and b>c:
#         return c
#     elif a>b and b<c:
#         return b
#     elif a<b and b<c:
#         return a
#     elif a==b and b==c:
#         return "hammasi teng"
# print(name(int(input("a : ")),int(input("b : ")),int(input("c : "))))

# def name(a,b,c):
#     if a>b and b>c and a>c:
#         return b
#     elif a>b and b<c and a>c:
#         return c
#     elif a<b and b<c and a<c:
#         return a
#     elif a==b and b==c and a==c:
#         return "hammasi teng"
# print(name(int(input("a : ")),int(input("b : ")),int(input("c : "))))

def name(a,b,c):
    if a>b and b>c and a>c:
        return b
    elif a>b and b<c and a>c:
        return c
    elif a<b and b<c and a<c:
        return a
    elif a==b and b==c and a==c:
        return "hammasi teng"
print(name(int(input("a : ")),int(input("b : ")),int(input("c : "))))