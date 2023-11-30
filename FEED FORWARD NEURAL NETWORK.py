import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_output = np.zeros((1, self.output_size))

    def forward(self, inputs):
        # Perform forward pass
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden)
        self.hidden_layer_output = sigmoid(self.hidden_layer_input + self.bias_hidden)

        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output)
        self.output_layer_output = sigmoid(self.output_layer_input + self.bias_output)

        return self.output_layer_output

    def train(self, inputs, targets, learning_rate, epochs):
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(inputs)

            # Calculate error
            error = targets - output

            # Backpropagation
            output_delta = error * sigmoid_derivative(output)
            hidden_layer_error = output_delta.dot(self.weights_hidden_output.T)
            hidden_layer_delta = hidden_layer_error * sigmoid_derivative(self.hidden_layer_output)

            # Update weights and biases
            self.weights_hidden_output += self.hidden_layer_output.T.dot(output_delta) * learning_rate
            self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

            self.weights_input_hidden += inputs.T.dot(hidden_layer_delta) * learning_rate
            self.bias_hidden += np.sum(hidden_layer_delta, axis=0, keepdims=True) * learning_rate

        print("Training complete.")

# Example usage
if __name__ == "__main__":
    # Set random seed for reproducibility
    np.random.seed(42)

    # Define the neural network architecture
    input_size = 2
    hidden_size = 4
    output_size = 1

    # Create a neural network
    neural_network = NeuralNetwork(input_size, hidden_size, output_size)

    # Define training data
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([[0], [1], [1], [0]])

    # Train the neural network
    neural_network.train(inputs, targets, learning_rate=0.1, epochs=10000)

    # Test the trained network
    test_input = np.array([[0, 0]])
    predicted_output = neural_network.forward(test_input)

    print("Predicted Output:", predicted_output)
