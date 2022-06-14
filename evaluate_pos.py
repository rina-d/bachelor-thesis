import os
import argparse
from sklearn.metrics import (confusion_matrix, ConfusionMatrixDisplay,
                             accuracy_score)
import matplotlib.pyplot as plt


def find_pred_labels(path):
    """This function finds the predicted POS-tags of a book."""
    pos_tags = []
    index = 0
    with open(path, 'r') as f:
        data = f.readlines()
        for item in data:
            line = item.split('\t')
            if len(line) > 1:
                if 'silverspelling' in path or 'orig/' in path:
                    index = line[4].find('[')
                elif 'goldspelling' in path or 'orig_new' in path:
                    index = line[4].find('(')
                pos_tags.append(line[4][:index])

    return pos_tags


def find_gold_labels(path, book_name):
    """This function finds the gold POS-tags of a book."""
    pos_tags = []
    for fname in sorted(os.listdir(path)):
        if fname.startswith(book_name):
            path_to_file = path + '/' + fname
            with open(path_to_file, 'r') as f:
                data = f.readlines()
                [pos_tags.append(item.split('\t')[0]) for item in data
                 if item != '' and item != '\n']

    return pos_tags


def calc_acc_per_class(conf_matr):
    """This function calculates the accuracy per class for the POS-tags."""
    return conf_matr.diagonal()/conf_matr.sum(axis=1)


def print_results(gold, pred, book_name):
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
    print('\n==============================================================\n')

    # Calculate accuracy per class and print
    print('Accuracy per class:')
    print('POS TAG\t| ACCURACY')
    accuracies = calc_acc_per_class(cm)
    for i, label in enumerate(pos_labels):
        print('{}\t| {}'.format(label, accuracies[i]))

    # Visualization of confusion matrix with labels
    cm_obj = ConfusionMatrixDisplay(cm, display_labels=pos_labels)
    cm_obj.plot()

    plt.title(book_name)
    plt.xlabel('Predicted label')
    plt.ylabel('Gold label')
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Compare a gold file with "
                                                 "POS-tags to automatically "
                                                 "annotated POS-tags for "
                                                 "fragments without "
                                                 "normalized spelling, "
                                                 "automatically normalized "
                                                 "spelling and manual"
                                                 "normalized spelling")
    parser.add_argument("gold_path", help="Path to directory that contain the "
                                          "files with the gold POS-tags. "
                                          "For example: pos/gold")
    parser.add_argument("book_filename", help="The filename of the book you "
                                              "want to evaluate. For example: "
                                              "Multatuli_MaxHavelaar")
    parser.add_argument("pred_path", help="Path to the .conll file that "
                                          "contains the automatically "
                                          "produced POS-tags. For "
                                          "example: "
                                          "openboek/pos/goldspelling/"
                                          "Multatuli_MaxHavelaar.conll")
    args = parser.parse_args()

    gold_labels = find_gold_labels(args.gold_path, args.book_filename)
    pred_labels = find_pred_labels(args.pred_path)

    print_results(gold_labels, pred_labels, args.book_filename)


if __name__ == "__main__":
    main()
