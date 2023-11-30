class TreeNode:
    def __init__(self, data=None, feature=None, value=None, left=None, right=None, result=None):
        self.data = data  # Training data at this node
        self.feature = feature  # Index of feature to split on
        self.value = value  # Value of the feature to split on
        self.left = left  # Subtree for samples where feature <= value
        self.right = right  # Subtree for samples where feature > value
        self.result = result  # Class label for leaf nodes

def entropy(y):
    classes, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    return -np.sum(probabilities * np.log2(probabilities))

def information_gain(X, y, feature, value):
    mask = X[:, feature] <= value
    left_entropy = entropy(y[mask])
    right_entropy = entropy(y[~mask])
    total_entropy = entropy(y)
    return total_entropy - (np.sum(mask) / len(y) * left_entropy + np.sum(~mask) / len(y) * right_entropy)

def find_best_split(X, y):
    best_gain = 0
    best_feature = None
    best_value = None

    for feature in range(X.shape[1]):
        unique_values = np.unique(X[:, feature])
        for value in unique_values:
            gain = information_gain(X, y, feature, value)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_value = value

    return best_feature, best_value

def build_decision_tree(X, y):
    if len(np.unique(y)) == 1:
        return TreeNode(result=y[0])

    if X.shape[0] == 0:
        return TreeNode(result=np.random.choice(np.unique(y)))

    best_feature, best_value = find_best_split(X, y)

    if best_feature is None:
        return TreeNode(result=np.random.choice(np.unique(y)))

    mask = X[:, best_feature] <= best_value
    left_subtree = build_decision_tree(X[mask], y[mask])
    right_subtree = build_decision_tree(X[~mask], y[~mask])

    return TreeNode(feature=best_feature, value=best_value, left=left_subtree, right=right_subtree)

def predict_sample(tree, sample):
    if tree.result is not None:
        return tree.result

    if sample[tree.feature] <= tree.value:
        return predict_sample(tree.left, sample)
    else:
        return predict_sample(tree.right, sample)

def predict(tree, X):
    return np.array([predict_sample(tree, sample) for sample in X])

# Example usage
if __name__ == "__main__":
    import numpy as np

    # Generate some random data
    np.random.seed(42)
    X = np.random.rand(100, 2)
    y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Simple classification rule

    # Build the decision tree
    tree = build_decision_tree(X, y)

    # Predict using the tree
    y_pred = predict(tree, X)

    # Evaluate accuracy
    accuracy = np.mean(y_pred == y)
    print("Accuracy:", accuracy)
