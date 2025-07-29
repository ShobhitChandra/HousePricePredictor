# -------------------- Imports --------------------
import numpy as np
import sys
import statistics as stats
import copy, math

X_train = np.array([[2104, 5, 1, 45],[1416, 3, 2, 40],[852, 2, 1, 35]])
y_train = np.array([460, 232, 178])

#intialized parameters with some values.
b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])

# x_vec = X_train[0,:]

# def s_predict (w, x, b):
#     p = np.dot(x,w) + b
#     return p

# def compute_cost (X, y, w, b):
#     m = X.shape[0]
#     cost = 0
#     for i in range(m):
#         f_wb_i = np.dot(X[i], w) + b
#         cost = cost + (f_wb_i - y[i]) ** 2
#     cost = cost / (2 * m)
#     return cost

# def compute_gradient (X, y, w, b):
#     m,n = X.shape
#     dj_dw = np.zeros((n,))
#     dj_db = 0.
    
#     for i in range(m) :
#         err = ((np.dot(X[i], w) + b) - y[i])
#         for j in range (n) :
#             dj_dw[j] = dj_dw[j] + err * X[i, j]
#         dj_db = dj_db + err
#     dj_dw = dj_dw / m
#     dj_db = dj_db / m
    
#     return dj_dw, dj_db

# #Compute and display gradient 
# tmp_dj_db, tmp_dj_dw = compute_gradient(X_train, y_train, w_init, b_init)

# def calculate_gradient (X, y, w_in, b_in, cost_function, gradient_function, alpha, nums_iter):
#     J_history = []
#     w = copy.deepcopy(w_in)
#     b = b_in
    
#     for i in range(nums_iter):
#         dj_dw , dj_db = gradient_function(X, y, w, b)
        
#         w = w - alpha * dj_dw
#         b = b - alpha *dj_db
        
#         if i < 100000:
#             J_history.append(cost_function(X, y, w, b))
        
#         if i% math.ceil(nums_iter / 10) == 0:
#             print(f"Iteration {i:4d}: Cost {J_history[-1]:8.2f}   ")
        
#     return w, b, J_history 

# # initialize parameters
# initial_w = np.zeros_like(w_init)
# initial_b = 0.
# # some gradient descent settings
# iterations = 1000
# alpha = 5.0e-7
# # run gradient descent 
# w_final, b_final, J_hist = calculate_gradient(X_train, y_train, initial_w, initial_b,
#                                                     compute_cost, compute_gradient, 
#                                                     alpha, iterations)


# makeing a function to predict the value of y
def predict (x, w, b):
    return np.dot(x, w) + b 

if __name__ == "__main__":
    area = float(sys.argv[1])
    bedrooms = float(sys.argv[2])
    floors = float(sys.argv[3])
    age = float(sys.argv[4])

    x = np.array([area, bedrooms, floors, age])
    price = predict(x, w_init, b_init)
    print(round(price, 2), flush=True)

