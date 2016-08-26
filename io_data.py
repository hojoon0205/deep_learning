import csv
import numpy as np

def get_data(csv_name, one_hot):
    data_x = []
    labels = []

    with open(csv_name, 'r') as f:
        next(f, None)
        reader = csv.reader(f)
        for row in reader:
            data_x.append(row[1:])
            labels.append(row[0])

    # train_x = [int(x) for x in row for row in train_x]
    # labels = [int(x) for x in labels]
    data_x = np.array(data_x, dtype=np.int32)
    labels = np.array(labels, dtype=np.int32)

    if one_hot:
        a = np.array(labels)
        b = np.zeros((len(labels), 255))
        b[np.arange(len(labels)), a] = 1
        data_y = b
    else:
        data_y = labels

    return data_x, data_y


def get_train_data(one_hot = True):
    return get_data('data/train.csv', one_hot)


def get_test_data(one_hot = True):
    return get_data('data/test.csv', one_hot)


"""
def save_result(pred_y):
    with open('data/result.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Id", "Label"])
        for idx, y in zip(range(1, len(pred_y)+1), pred_y):
            writer.writerow([idx, y])
"""
