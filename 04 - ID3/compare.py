import csv
from id3 import TrainingData, id3
from random import shuffle
from statistics import mean

def get_data_from_file(path, class_column):
    data = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if class_column != 0:
                data.append(TrainingData(row[:class_column], row[class_column]))
            else:
                data.append(TrainingData(row[class_column+1:], row[class_column]))
    return data

def test_id3(data, class_):
    shuffle(data)
    training_data = data[: 3*len(data)//5]
    testing_data = data[3*len(data)//5:]
    attributes = set(range(len(training_data[0].get_values())))
    tree = id3(training_data, attributes)
    results = []
    tp, fp, fn, tn = 0, 0, 0, 0
    for data in testing_data:
        expected = data.get_class()
        result = tree.check(data.get_values())
        if expected == result:
            results.append(result)
            if expected == class_[0]:
                tp += 1
            elif expected == class_[1]:
                tn += 1
        else:
            if expected == class_[0]:
                fp += 1
            elif expected == class_[1]:
                fn += 1
    return (tp+tn)/len(testing_data), tp, fp, fn, tn

def main():
    database = 'tic-tac-toe'
    DATABASE = {
        'breast-cancer': ["04 - ID3/data/breast-cancer.data", 0, "recurrence-events", "no-recurrence-events"],
        'mushroom': ["04 - ID3/data/agaricus-lepiota.data", 0, "e", "p"],
        'tic-tac-toe': ["04 - ID3/data/tic-tac-toe.data", -1, "positive", "negative"]
    }
    data = get_data_from_file(DATABASE.get(database)[0], DATABASE.get(database)[1])
    avg = [0] * 100
    tp = [0] * 100
    fp = [0] * 100
    fn = [0] * 100
    tn = [0] * 100
    for i in range(100):
        avg[i], tp[i], fp[i], fn[i], tn[i] = test_id3(data, DATABASE.get(database)[2:])
    print("AVG: " + str(mean(avg)), "True Positive: " +  str(mean(tp)), "False Positive: " + str(mean(fp)), "False Negative: " + str(mean(fn)), "True Negative: " + str(mean(tn)))

if __name__ == "__main__":
    main()
