def valid_solution(board):
    valid_set = set([1,2,3,4,5,6,7,8,9])
    is_valid = True
    col_sets = [set() for i in range(9)]
    square_sets = [set() for i in range(9)]
    for cnt, row in enumerate(board):
        row_set = set(row)
        if len(row_set) != 9:
            is_valid = False
            break
        if row_set != valid_set:
            is_valid = False
            break
        
        square_row_counter = cnt // 3

        for cell_cnt,cell in enumerate(row):
            col_sets[cell_cnt].add(cell)
            square_cell_counter = cell_cnt // 3
            square_sets[square_row_counter*3+square_cell_counter].add(cell)
    
    if is_valid:
        for cnt in range(9):
            if col_sets[cnt] != valid_set or square_sets[cnt] != valid_set:
                print(col_sets[cnt])
                print(square_sets[cnt])
                is_valid = False
                break

    return is_valid



#valid_solution(sol)
print(valid_solution(sol))
print(valid_solution(not_sol))