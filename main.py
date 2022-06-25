# This is a sample Python script.
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from dataclasses import dataclass
import csv
import os
from os.path import isfile, join

"""
def plot_student(ax: plt.axes, time_passed):
    current_time = student.grade + time_passed
    current_mastery = student.test_num + student.test_score - 1
    ax.scatter(current_time, current_mastery, label=student.name, s=100, c=50,
               alpha=0.5)

    t = 1
    c = (current_time - current_mastery) / (np.e - t)
    k = float(c) * np.e ** (current_time + t)
    x = np.linspace(current_time, current_time + t, 100)
    y = func(x, k, c)
    ax.scatter(current_time + t, func(current_time + t, k, c), color='blue')
    ax.plot(x, y, color='red', linestyle='dashed')
    """


def func(x, k, c):
    return x - (k * (np.e ** (-x))) + c


def test():
    # s1 = Student('Test 1', 7, 7, 0.50)
    # s2 = Student('test 2', 6, 5, 0.3)

    """sample = []
    current_time = s1.grade+time_passed
    while sample[-1]:
        sample.append()
        current_time += 0.01"""

    # plot_student(ax, s0, time_passed)
    # plot_student(ax, s1, time_passed)
    # plot_student(ax, s2, time_passed)


def get_student_data(name):
    file = open(f"{name}.csv", 'w+')

    reader = csv.reader(file)
    # Date, Grade, Test Number, Test Score
    dates = []
    grades = []
    test_nums = []
    test_scores = []
    for row in reader:
        dates.append(row[0])
        grades.append(row[1])
        test_nums.append(row[2])
        test_scores.append(row[3])

    full_student_data = {
        "name": name,
        "dates": dates,
        "grades": grades,
        "test_nums": test_nums,
        "test_scores": test_scores
    }
    return full_student_data


def parse_existing_csv():
    base_path = './data'
    file_ls = [f for f in os.listdir(base_path) if isfile(join(base_path, f))]
    print(file_ls)


def get_input():
    name = input('Enter the student\'s name: ')
    grade = input('Enter the student\'s grade: ')
    test_num = input('Enter the student\'s assessment number: ')
    test_score = input('Enter the student\'s score: ')

    student = {
        "name": name,
        "grade": grade,
        "test_num": test_num,
        "test_score": test_score
    }

    f = open(f"./data/{name}.csv", 'w+')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow([str(datetime.today()), grade, test_num, test_score])

    return student


def graph_student(data):
    # Graph Setup
    fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')

    x = np.linspace(0, 12, 100)  # Sample data.

    ax.plot(x, x, label='Common Core Standard', color='red')  # Plot y=x
    ax.fill_between(x, x - 0.3, x + 0.3, alpha=0.1)

    # Plot Student Data points
    for i in range(0, len(data["dates"])):
        current_date = datetime.strptime(data["dates"][i], "%Y-%m-%d %H:%M:%S.%f")
        current_grade = int(data["grades"][i])
        current_test_num = int(data["test_nums"][i])
        current_test_score = float(data["test_scores"][i])

        school_start = datetime(current_date.year, 9, 1)
        delta = current_date - school_start
        time_passed = delta.days / 365.25
        ax.scatter(current_grade + time_passed, current_test_num + current_test_score - 1, label=data["dates"][i],
                   s=100, c=50, alpha=0.5)

    ax.set_xlabel('Grade')  # Add an x-label to the axes.
    ax.set_ylabel('Mastery')  # Add a y-label to the axes.
    ax.set_title("Mathnasium: Canton")  # Add a title to the axes.
    ax.legend()  # Add a legend.


if __name__ == '__main__':
    parse_existing_csv()
    new_student_data = get_input()

    current_student = get_student_data(new_student_data["name"])

    graph_student(current_student)

    xt = np.arange(0, 13, 1)  # Create
    plt.xticks(xt)
    plt.xlim([0, 12])
    plt.ylim([0, 12])
    plt.show()
