def auc(y_pred, y_true):
    sorted_index = sorted(range(len(y_pred)), key=lambda i:y_pred[i])
    sorted_label = [y_true[i] for i in sorted_index]
    pos_num = sum(y_true)
    neg_num = len(y_true) - pos_num
    rank_sum = 0
    for i in range(len(y_pred)):
        if sorted_label[i] == 1:
            rank_sum += i + 1
    res = (rank_sum - (pos_num * (pos_num + 1) / 2)) / (pos_num * neg_num)
    return res

print(auc([0.1,0.4,0.9,0.4], [1,0,1,1]))

