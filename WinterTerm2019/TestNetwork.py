import numpy as np

#Generate the spiral data set
N = 100
D = 2
K = 3
X = np.zeros((N*K, D))
y = np.zeros(N*K, dtype='uint8')
for j in range(K):
    ix = range(N*j, N*(j+1))
    r = np.linspace(0.0,1,N)
    t = np.linspace(j*4,(j+1)*4,N) + np.random.randn(N)*0.2
    X[ix] = np.c_[r*np.sin(t),r*np.cos(t)]
    y[ix] = j
#plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
#plt.show()

#initialize parameters to be random numbers
h = 100 #size of the hidden layer
W = 0.01*np.random.randn(D,h)
b = np.zeros((1,h))
W2 = 0.01*np.random.randn(h,K)
b2 = np.zeros((1,K))

step_size = 1
reg = 10**-3

#gradient descent loop
num_examples = X.shape[0]
for i in range(10000):

    #get scores, N x K matrix
    hidden_layer = np.maximum(0,np.dot(X,W)+b)
    scores = np.dot(hidden_layer,W2) + b2

    #get the class probabilities
    exp_scores = np.exp(scores)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    #compute the loss
    correct_logprobs = -np.log(probs[range(num_examples),y])

    data_loss = np.sum(correct_logprobs)/num_examples
    reg_loss = 0.5*reg*np.sum(W*W) + 0.5*reg*np.sum(W2*W2)
    loss = data_loss + reg_loss
    if i%1000 == 0:
        #print(W)
        print("iteration %d: loss%f" % (i,loss))

    #compute the gradient on scores
    dscores = probs
    dscores[range(num_examples),y]-= 1
    dscores /= num_examples

    #backprop the gradeitn to the parameters, W2, b2 first
    dW2 = np.dot(hidden_layer.T, dscores)
    db2 = np.sum(dscores,axis=0,keepdims=True)
    #now backprop the hidden layer
    dhidden = np.dot(dscores, W2.T)
    #backprop the ReLU non linearity
    dhidden[hidden_layer <= 0] = 0
    #Now into W,b
    dW = np.dot(X.T, dhidden)
    db = np.sum(dhidden,axis=0, keepdims=True)

    dW2 += reg*W2
    dW += reg*W #reg gradient


    #parameter update
    W+= -step_size *dW
    b += -step_size * db
    W2 += -step_size * dW2
    b2 += -step_size * db2

#evaluates the training set accuracy
hidden_layer = np.maximum(0,np.dot(X,W)+b)
scores = np.dot(hidden_layer,W2)+b2
predicted_class = np.argmax(scores, axis=1)
print("Training accuracy: %.2f" % (np.mean(predicted_class == y)))
