def solution(list_of_nums):
    dic1 = {}
    e_cnt = 0
    o_cnt = 0
    for i in list_of_nums:
        if i % 2 == 0:
            e_cnt += 1
        else:
            o_cnt += 1
    dic1 = {'ODD': o_cnt, 'EVEN': e_cnt}
    return dic1
