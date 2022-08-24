from BlockProcessor import ProcessBlocks


block_1 = ['A', 'B', 'C', 'D']
block_2 = ['A', 'B', 'C', 'D']
block_3 = ['A', 'B', 'C']
block_4 = ['A', 'B', 'C', 'D']
block_5 = ['E', 'F', 'G']
block_6 = ['E', 'F', 'G']
block_7 = ['E', 'F', 'G']
block_8 = ['E', 'F', 'G']
block_9 = ['E', 'F', 'G']


res_1 = ProcessBlocks(1, block_1)
res_2 = ProcessBlocks(1, block_2)
res_3 = ProcessBlocks(1, block_3)
res_4 = ProcessBlocks(1, block_4)
res_5 = ProcessBlocks(5, block_5)
res_6 = ProcessBlocks(5, block_6)
res_7 = ProcessBlocks(5, block_7)
res_8 = ProcessBlocks(5, block_8)
res_9 = ProcessBlocks(5, block_9)

print(res_1, res_2, res_3, res_4, res_5, res_6, res_7, res_8, res_9)
