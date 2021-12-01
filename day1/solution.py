depths = list(map(int, open('input.txt')))
depths2 = list(sum(i) for i in zip(depths, depths[1:], depths[2:]))

print(sum(b > a for a, b in zip(depths, depths[1:])))
print(sum(b > a for a, b in zip(depths2, depths2[1:])))
