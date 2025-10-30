import sys

'''
Using the code provided in the PPT for Single NN. 
Implement the solution for the following equation

y= 3x+2.3

Train the algorithm with 20 data units and run the epoch for 100000 iterations.

Please provide your documentation for the implementation 
'''



def main():
    x0 = [1, 2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    x1 = [5.2, 8.4, 11.2 , 14.4, 17.2, 20.4, 23.2, 26.4, 29.2, 32.4, 35.2, 38.4, 41.2, 44.4, 47.4, 50.2, 53.4, 56.2, 59.3, 62.2 ]
    # Expected outputs
    y = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

    # Initialize weights and biases
    w0 = 0.1
    w1 = -0.23
    b = 0.22

    # Epoch running for 100,000 iterations
    for i in range(0, 100000):
        loss = 0
        for j in range(0, len(y)):
            a = w0 * x0[j] + w1 * x1[j] + b

            loss += 0.5 * (y[j] - a)** 2

            dw0 = -(y[j] - a) * x0[j]
            dw1 = -(y[j] - a) * x1[j]
            db = -(y[j] - a)

            w0 = w0 - 0.001 * dw0
            w1 = w1 - 0.001 * dw1
            b = b - 0.001 * db

        print("loss = ", loss)

    x0_test = 2.7
    x1_test = 6.0
    output = x0_test * w0 + x1_test * w1 + b
    print("Output ", output)

if __name__ == "__main__":
    sys.exit(main() or 0)