import numpy as np
import re
import os





wd_contents = os.listdir()
parchg_list = []
for item in wd_contents:
    if re.search('^PARCHG[.]([0-9]+|ALLB)[.]([0-9]+|ALLK)$', item):
        parchg_list.append(item)
parchg_list.sort()



header_file = open(parchg_list[0], 'r')
first_parchg = header_file.readlines()
header_file.close()



tmp_a = re.split(' +', first_parchg[2].lstrip().rstrip())
tmp_b = re.split(' +', first_parchg[3].lstrip().rstrip())
tmp_c = re.split(' +', first_parchg[4].lstrip().rstrip())
a = np.array(tmp_a, dtype=np.double)
b = np.array(tmp_b, dtype=np.double)
c = np.array(tmp_c, dtype=np.double)
b_cross_c = np.cross(b, c)
v_cell = np.dot(a, b_cross_c)



parchg_len = len(first_parchg)
header_skip = 0
global cell_size
for i in range(parchg_len):
    if re.search('[a-zA-Z0-9]', first_parchg[i]) == None:
        header_skip = i+2
        cell_size = re.split(' +', first_parchg[i+1].lstrip().rstrip())
        break
for i in range(3):
    cell_size[i] = int(cell_size[i])
num_cells = cell_size[0]*cell_size[1]*cell_size[2]





ipr_list = []
pos_ipr_list = []
neg_ipr_list = []
density_sum_list_pre = []
density_sum_list_post = []
for parchg in parchg_list:
    print(f'working on {parchg}')
    parchg_file = open(parchg, 'r')
    parchg_lines = parchg_file.readlines()
    parchg_file.close()
    ipr = np.zeros(1, dtype=np.double)
    neg_ipr = np.zeros(1, dtype=np.double)
    pos_ipr = np.zeros(1, dtype=np.double)
    for i in range(header_skip, parchg_len-1):
        tmp_list = re.split(' +', parchg_lines[i].lstrip().rstrip())
        tmp_array = np.array(tmp_list, dtype=np.double)
        tmp_array = np.divide(tmp_array, v_cell)
        tmp_array_sq = np.multiply(tmp_array, tmp_array)
        ipr = np.add(ipr, np.sum(tmp_array_sq))
        for density in tmp_array:
            if np.less(density, 0):
                neg_ipr = np.add(neg_ipr, np.multiply(density, density))
            else:
                pos_ipr = np.add(pos_ipr, np.multiply(density, density))
    ipr_list.append(ipr[0])
    neg_ipr_list.append(neg_ipr[0])
    pos_ipr_list.append(pos_ipr[0])
ipr_array = np.array(ipr_list)
pos_ipr_array = np.array(pos_ipr_list)
neg_ipr_array = np.array(neg_ipr_list)
ipr_array = np.multiply(ipr_array, np.divide(v_cell,num_cells))
pos_ipr_array = np.multiply(pos_ipr_array, v_cell/num_cells)
neg_ipr_array = np.multiply(neg_ipr_array, v_cell/num_cells)





print('writing output')
output_file = open('ipr.txt', 'w')
output_file.write(f'      PARCHG file       |          IPR           \n')
output_file.write(f'-------------------------------------------------\n')
for i,ipr in enumerate(ipr_array):
    output_file.write(f'{parchg_list[i]:^24} {ipr:^24}\n')
output_file.close()
