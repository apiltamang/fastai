import numpy as np
from sklearn.metrics import confusion_matrix
from fastai.paperpy.dict_generator import DictGenerator

class StatsGenerator:

    @staticmethod
    def evalPredsAndConfusionMatrix(log_preds, y):
        probs = np.mean(np.exp(log_preds),0)
        preds = np.argmax(probs, axis=1)
        cm = confusion_matrix(y, preds)

        classToChar, _ =  DictGenerator.getDicts()

        head = '{:>6}'.format('*')
        for i in range(47):
            head += '{:>6}'.format(classToChar[i])
        head += '\n'

        with open("confusion_matrix_forms.txt", "w") as f:
            f.write(head)
            for i in range(47):
                row = ''
                row += '{:>6}'.format(classToChar[i])
                for j in range(47):
                    row += '{:>6}'.format(cm[i, j])
                row += '\n'
                f.write(row)
            f.close()

        return preds,cm

    @staticmethod
    def genConfusionMatrixFile(cm, classToChar, classRemapping):
        head = '{:>6}'.format('*')
        for i in range(47):
            head += '{:>6}'.format(classToChar[int(classRemapping[i])])
        head += '\n'

        with open("confusion_matrix_forms.txt", "w") as f:
            f.write(head)
            for i in range(47):
                row = ''
                row += '{:>6}'.format(classToChar[int(classRemapping[i])])
                for j in range(47):
                    row += '{:>6}'.format(cm[i, j])
                row += '\n'
                f.write(row)
        f.close()