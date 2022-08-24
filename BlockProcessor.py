

'''
Assumptions and Thoughts:

1. Blocks are fed in sequence and need to be verified.
a) They need to be verfied sequentially. This means that cryptographically the has of the current block needs to be connect to the previous block.
b) The previous block needs to be verified and cannot be the same as the current block.

'''

# maintains a count for each block occurence
blocks_counts = {}
# array to maintain the blocks at a given height
blocks_at_height = []
current_height = 0


def ProcessBlocks(startHeight, blocks):
    '''
    For each block in the list, add the block to blocks_at_height if the cryptographic hash is valid (in assumptions).
    Increment the count for the block
    If the count for the block at a given height is less than 3, don't add the height to current height (total)
    else add the height to current height (total)
    Return the current height (total)
    '''
    for i, block in enumerate(blocks):
        if len(blocks_at_height) < startHeight + i:
            # if verifyHash(block):
            blocks_at_height.append(block)
        if block in blocks_counts:
            blocks_counts[block] += 1
        else:
            blocks_counts[block] = 1
    global current_height
    total = current_height
    while total < len(blocks_at_height):
        if (blocks_counts[blocks_at_height[total]] < 3):
            break
        total += 1
    current_height = total
    return current_height

# Time Complexity: O(n)

# Function to verify whether block is one character greater than the last item at blocks_at_height
# Its an example for a function that can be used to verify the cryptographic hash of a block (not being used here)


def verifyHash(block):
    if len(blocks_at_height) > 0:
        if block == blocks_at_height[-1] + chr(1):
            return True
        else:
            return False
    else:
        return True
