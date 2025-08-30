def bombard_region(grid, m):
  n = len(grid)
  best_count = 0
  best_coordinate = None
  destroyed = []

  r = m // 2

  for y in range(r, n-r):
    for x in range(r,n-r):
       if grid[y][x] == 1:
                  coordinate = []
                  count = 0

                  for dy in range(-r,r+1):
                       for dx in range(-r,r+1):
                            if grid[y+dy][x+dx] == 1:
                                count += 1
                                coordinate.append((x+dx,y+dy))

                  if count > best_count:
                      best_count = count
                      best_coordinate = (x,y)
                      destroyed = coordinate
  return best_coordinate, destroyed


grid = [
    [1,0,0,0,1],
    [1,0,1,1,1],
    [1,1,0,1,1],
    [1,0,1,1,0],
    [0,1,0,1,1]
]

m=3
best_coordinate, destroyed = bombard_region(grid, m)
print("Best coordinate to bomb:", best_coordinate)
print("Destroyed island:", destroyed)
