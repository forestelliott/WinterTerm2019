
import numpy as np
#First create test traing set of 100 images that are each 2x2 for a total dim
#of 12. Start with 10 catagories
X_train = np.random.randint(0, 255, size=(12,100))
Y_train = np.random.randint(0,9,size=100)

def L_i(x, y, W):

    delta = 1.0
    #Calculate the score

    scores = W.dot(x)
    correct_class_score = scores[y]
    #Get the dim of W

    D = W.shape[0]
    loss_i = 0.0
    for j in range(D):
        if (j == y):
            continue
        loss_i += max(0, scores[j] - correct_class_score + delta)
    return loss_i

#computes total loss over the entire training set
def L(X,Y,W):
    loss = 0
    for i in range(100):
        #print(Y[i])
        loss += L_i(X[:,i], Y[i], W)
    loss = loss/100
    return loss

def eval_numerical_gradient(f,x):
    '''

    :param f: loss function to calculate gradient from
    :param x: vector that gradient is calculated at
    :return: gradient matrix of f
    '''

    #evaluate function at original point
    fx = f(x)
    grad = np.zeros(x.shape)
    h = 0.00001

    #iterate over all indexes in x
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:

        #evaluate function at x+h
        ix = it.multi_index
        old_value = x[ix]
        x[ix] = old_value + h #increment by h
        fxh = f(x) #evaluate f(x+h)
        x[ix] = old_value

        #compute derivative
        grad[ix] = (fxh-fx)/h
        it.iternext() #go to next dimension
    return grad

def Test_loss_fun(W):
    return L(X_train, Y_train, W)

def main():
    W = np.random.rand(10,12)*0.001 #start with random W
    df = eval_numerical_gradient(Test_loss_fun, W) #compute gradient at that W
    loss_original = Test_loss_fun(W) #get loss
    print("Original loss: %f" % (loss_original, ))
    step_size = 10 ** (-6)
    W_new = W - step_size*df #change W using the gradient
    new_loss = Test_loss_fun(W_new) #get new loss
    print("Loss with step size 1.00e-06: %f" % (new_loss,))

main()