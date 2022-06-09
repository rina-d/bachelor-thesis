import os
import argparse
from sklearn.metrics import (confusion_matrix, ConfusionMatrixDisplay,
                             accuracy_score)
import matplotlib.pyplot as plt


def find_pred_labels(fname):
    """This function finds the predicted POS-tags of a book."""
    pos_tags = []
    with open(fname, 'r') as f:
        data = f.readlines()
        for item in data:
            line = item.split('\t')
            if len(line) > 1:
                index = line[4].find('[')
                pos_tags.append(line[4][:index])

        return pos_tags


def find_gold_labels(book_name):
    """This function finds the gold POS-tags of a book."""
    pos_tags = []
    for fname in sorted(os.listdir('./openboek/pos/gold')):
        if fname.startswith(book_name):
            path = './openboek/pos/gold/' + fname
            with open(path, 'r') as f:
                data = f.readlines()
                [pos_tags.append(item.split('\t')[0]) for item in data
                 if item != '' and item != '\n']

    return pos_tags


def print_results(gold, pred, bookname):
    """This function prints a confusion matrix for the gold and predicted
    labels and calculates the accuracy score."""
    # Print confusion matrix in terminal
    pos_labels = ['ADJ', 'BW', 'N', 'SPEC', 'TW', 'WW', 'LID', 'TSW', 'VNW',
                  'VG', 'VZ', 'LET']
    cm = confusion_matrix(gold, pred, labels=pos_labels)
    print('Confusion Matrix:')
    print(cm)

    # Print Accuracy Score
    print('\n==============================================================\n')
    print('Accuracy:', accuracy_score(gold, pred))

    # Visualization of confusion matrix with labels
    cm_obj = ConfusionMatrixDisplay(cm, display_labels=pos_labels)
    cm_obj.plot()

    plt.title(bookname)
    plt.xlabel('Predicted label')
    plt.ylabel('Gold label')
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Compare a gold file with "
                                                 "POS-tags to automatically "
                                                 "annotated POS-tags for "
                                                 "fragments without "
                                                 "normalized spelling and "
                                                 "automatically normalized "
                                                 "spelling")
    parser.add_argument("book_fname", help="The filename of the book you want "
                                           "to compare, example: "
                                           "Multatuli_MaxHavelaar")
    parser.add_argument("pred_file", help="The spelling version you want to "
                                          "compare, either 'orig' or "
                                          "'silverspelling'")
    args = parser.parse_args()

    gold_labels = find_gold_labels(args.book_fname)
    pred_labels = find_pred_labels('./openboek/pos/' + args.pred_file + '/' +
                                   args.book_fname + '.conll')

    print_results(gold_labels, pred_labels, args.book_fname)


if __name__ == "__main__":
    main()


