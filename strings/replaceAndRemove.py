def replace_and_remove(size, s):
    # forward iterations: remove 'b's and count the number of 'a's
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    cur_idx = write_idx - 1
    write_idx += a_count - 1


"""
Incomplete due to complexity check again
"""
