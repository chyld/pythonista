x, y, z, n = int(input()), int(input()), int(input()), int(input())
coords = [[xx, yy, zz] for xx in range(x+1) for yy in range(y+1) for zz in range(z+1) if xx + yy + zz != n]
print(coords)
