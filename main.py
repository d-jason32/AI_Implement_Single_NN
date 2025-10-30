import sys

'''
Using the code provided in the PPT for Single NN. 
Implement the solution for the following equation

y= 3x+2.3

Train the algorithm with 20 data units and run the epoch for 100000 iterations.

Please provide your documentation for the implementation 
'''
def main():

    # Add the 20 data units
    x0 = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5]
    x1 = [5.2, 6.9, 8.2 , 9.9, 11.2, 12.9, 14.2, 15.8, 17.2, 18.9, 20.2, 21.9, 23.2, 24.9, 26.2, 27.9, 29.2, 30.9, 32.2, 33.9 ]
    # Expected outputs
    # 0 means the point is below the expected
    # 1 means the point is above the expected
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