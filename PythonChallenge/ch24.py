'''
credit:
    http://garethrees.org/2007/05/07/python-challenge/
'''

from PIL import Image

im = Image.open("maze.png")

print(im.size, im.mode)


def bfs_search(maze, tree):
    dirs = (0, 1), (0, -1), (1, 0), (-1, 0)
    wall = (255,) * 4
    w, h = maze.size
    maze.putpixel((1, h - 1), wall)  # Wall off exit
    maze.putpixel((w - 2, 0), wall)  # Wall off entrance
    queue = [(1, h - 2)]            # Start at exit
    tree[queue[0]] = 'exit'
    while queue:
        pos = queue.pop(0)
        for d in dirs:
            new_pos = pos[0] + d[0], pos[1] + d[1]
            if new_pos not in tree and maze.getpixel(new_pos) != wall:
                tree[new_pos] = pos
                queue.append(new_pos)


tree = {}
bfs_search(im, tree)
print(tree[(im.size[0] - 2, 1)])
path = []
pos = (im.size[0] - 2, 1)
while pos != 'exit':
    path.append(im.getpixel(pos)[0])
    pos = tree[pos]

mazezip = bytes(path[::2])
open('maze.zip', 'wb').write(mazezip)

pos = (im.size[0] - 2, 1)
while pos != 'exit':
    im.putpixel(pos, (0, 255,) * 2)
    pos = tree[pos]

im.save('maze-solved.png')
