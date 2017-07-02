import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = y.shape[0]
  scores = X.dot(W)
  for i in range(num_train):
    eScore = np.exp(scores[i])
    eyScore = eScore[y[i]]
    loss -= np.log(eyScore / sum(eScore))
    for j in range(W.shape[1]):
      dW[:, j] += X[i] * eScore[j] / sum(eScore)
    dW[:, y[i]] -= X[i]

  loss = loss / num_train + 0.5 * reg * np.sum(W * W)
  dW = dW / num_train + reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = y.shape[0]
  scores = X.dot(W)
  eScore = np.exp(scores)
  eyScore = eScore[np.arange(num_train), y]
  sumOfEscore = np.sum(eScore, axis=1)
  lossMat = -np.log(eyScore / sumOfEscore)
  loss = np.sum(lossMat) / num_train + 0.5 * reg * np.sum(W * W)

  accuracy = eScore.T / sumOfEscore
  accuracy = accuracy.T
  accuracy[np.arange(num_train), y] -= 1
  dW = np.dot(X.T, accuracy) / num_train + reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

