class Regression:
    def __init__(self):
        self.coefficient_ = 0.0
        self.intercept_ = 0.0

    # learn a linear unvaried regression model by using training inputs and outputs
    def fit(self, trainInputs, trainOutputs):
        phaseInputs = sum(trainInputs)
        phaseOutputs = sum(trainOutputs)
        phase1 = sum(i * i for i in trainInputs)
        phase2 = sum(i * j for (i, j) in zip(trainInputs, trainOutputs))

        w1 = (len(trainInputs) * phase2 - phaseInputs * phaseOutputs) / \
             (len(trainInputs) * phase1 - phaseInputs * phaseInputs)
        w0 = (phaseOutputs - w1 * phaseInputs) / len(trainInputs)

        self.intercept_, self.coefficient_ = w0, w1

    # predict the outputs for some new inputs (by using the learnt model)
    def predict(self, x):
        if isinstance(x[0], list):
            return [self.intercept_ + self.coefficient_ * value[0] for value in x]
        else:
            return [self.intercept_ + self.coefficient_ * value for value in x]
