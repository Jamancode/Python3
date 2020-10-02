with open("pi.txt", "r") as f:
    pi = f.read()

print(len(pi))
print(pi[0])
print(pi[1000001])
print(pi[-10:])
print(pi[0:10])
print(pi[999_991:1_000_001])