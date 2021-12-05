import csv
from id3 import TrainingData, id3
from random import shuffle

def get_data_from_file(path):
    data = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(TrainingData(row[1:], row[0]))
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
    database = 'breast-cancer'
    PATH = {
        'breast-cancer': "04 - ID3/data/breast-cancer.data",
        'mushroom': "04 - ID3/data/agaricus-lepiota.data"
    }
    CLASS = {
        'breast-cancer': ["recurrence-events", "no-recurrence-events"],
        'mushroom': ["e", "p"]
    }
    # PATH = "data/agaricus-lepiota.data"
    data = get_data_from_file(PATH.get(database))
    avgs = []
    for _ in range(1000):
        avg, tp, fp, fn, tn = test_id3(data, CLASS.get(database))
        avgs.append(avg)
    print("AVG: " + str(sum(avgs)/len(avgs)), "True Positive: " +  str(tp), "False Positive: " + str(fp), "False Negative: " + str(fn), "True Negative: " + str(tn))

if __name__ == "__main__":
    main()
