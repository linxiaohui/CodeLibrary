# *-* coding:UTF-8 *-*
'''
credit:
   http://blog.csdn.net/qaswe/article/details/10009581
'''

FILL, EMPTY, NOTHING = '#', 'X', ' '

def read_data(filename):
    width, height, h_tips, v_tips, mark =0, 0, [], [], -1
    f = open(filename, 'r')
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        if line.startswith('# Dimensions'):
            mark = 0
        elif line.startswith('# Horizontal'):
            mark = 1
        elif line.startswith('# Vertical'):
            mark = 2
        elif mark == 0 and line != '':
            size = line.split(' ')
            width, height = int(size[0]), int(size[1])
        elif mark == 1 and line != '':
            tips = line.split(' ')
            h_tips.append([int(t) for t in tips])
        elif mark == 2 and line != '':
            tips = line.split(' ')
            v_tips.append([int(t) for t in tips])
    f.close()
    return (width, height, h_tips, v_tips)
    
def output_data(filename, res):
    f = open(filename, 'w')
    output = ''
    for line in res:
        output += ''.join(line) + '\n'
    f.write(output)
    f.close()
    
#递归穷举每一行或列的所有可能的填充方案
def init_set(tips, length):
    t_len, t_sum, j, res = len(tips), sum(tips), 0, []
    if t_len == 1:
        j = 1
    for i in range(length - t_len + 1 - t_sum + 1):
        res_header = EMPTY * i + FILL * tips[0] + EMPTY * (1 - j)
        if j:
            res_tails = [EMPTY * (length - len(res_header))]
        else:
            res_tails = init_set(tips[1:], (length - len(res_header)))
        res.extend([res_header + res_tail for res_tail in res_tails])
    return res

#找出能够确定的填充格子或永不需要填充的格子    
def decision(candidate_set, idx):
    candidate_len = len(candidate_set)
    mark = candidate_set[0][idx]
    for j in range(1, candidate_len):
        if mark != candidate_set[j][idx]:
            return None
    return FILL if mark == FILL else NOTHING

#淘汰不可能正确的候选组合            
def eliminate(idx, mark, candidate_set):
    candidate_len = len(candidate_set)
    if candidate_set != 'OK' and candidate_len > 1:
        mark = FILL if mark == FILL else EMPTY
        for i in range(candidate_len - 1, -1, -1):
            if candidate_set[i][idx] != mark:
                candidate_set.pop(i)
                
def change_mark(item):
    return NOTHING if item != FILL else FILL

def solve(infilename, outfilename):
    (width, height, h_tips, v_tips) = read_data(infilename)
    h_candidates = [init_set(tips, width) for tips in h_tips]
    v_candidates = [init_set(tips, height) for tips in v_tips]
    cnt, total, result = 0, width * height, []
    for i in range(height):
        result.append([EMPTY] * width)
    while cnt < total:
        for i in range(height):
            if h_candidates[i] == 'OK':
                continue
            if len(h_candidates[i]) == 1:
                for x in range(width):
                    if result[i][x] == EMPTY:
                        result[i][x] = change_mark(h_candidates[i][0][x])
                        cnt += 1
                        eliminate(i, result[i][x], v_candidates[x])
                h_candidates[i] = 'OK'
            else:
                for x in range(width):
                    if result[i][x] != EMPTY:
                        continue
                    mark = decision(h_candidates[i], x)
                    if mark is not None:
                        result[i][x] = mark
                        cnt += 1
                        eliminate(i, mark, v_candidates[x])
        for i in range(width):
            if v_candidates[i] == 'OK':
                continue
            if len(v_candidates[i]) == 1:
                for x in range(height):
                    if result[x][i] == EMPTY:
                        result[x][i] = change_mark(v_candidates[i][0][x])
                        cnt += 1
                        eliminate(i, result[x][i], h_candidates[x])
                v_candidates[i] = 'OK'
            else:
                for x in range(height):
                    if result[x][i] != EMPTY:
                        continue
                    mark = decision(v_candidates[i], x)
                    if mark is not None:
                        result[x][i] = mark
                        cnt += 1
                        eliminate(i, mark, h_candidates[x])
    output_data(outfilename, result)
    
solve('warmup.txt', '32_1.txt')
solve('up.txt', '32_2.txt')