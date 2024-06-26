import os
import json
from collections import defaultdict


def print_scores(filename):
    with open(filename) as json_file:
        record = json.load(json_file)
        result = defaultdict(list)

        print('班級:', record['class'])
        for record in record['score']:
            for subject, score in record.items():
                result[subject].append(score)

        for subject, scores in result.items():
            print('科目:', subject)
            print('\t最高分:', max(scores))
            print('\t最低分:', min(scores))
            print('\t平均:', sum(scores) / len(scores))


def print_dir_scores(dirname):
    for filename in os.listdir(dirname):
        if filename.endswith('.json'):
            print('讀取檔案: ', filename)
            print_scores(os.path.join(dirname, filename))


print_dir_scores(r'.\data\scores')
