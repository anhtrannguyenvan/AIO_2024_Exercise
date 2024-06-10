##Question 1
def calc_f1_score(tp,fp,fn):
    #calculate precision
    if tp + fp == 0:
        precision = 0
    else:
        precision = tp / (tp+fp)
        
    #Calculate Recall
    if tp + fn == 0:
        recall = 0
    else:
        recall = tp / (tp + fn)
        
    #Calculate F1-score
    if precision + recall == 0:
        f1_score = 0
    else:
        f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score
#test 
assert round(calc_f1_score(tp=2, fp=3, fn=5), 2) == 0.33
print(round(calc_f1_score(tp=2, fp=4, fn=5), 2))

##Question2:
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

# Test function
assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print(is_number(1))  # Should print True
print(is_number('n'))  # Should print False

##Question 4:
import math

def calc_sig(x):
    return 1/ (1+math.exp(-x))
#test function
assert round(calc_sig(3),2)==0.95
print(round(calc_sig(2),2))


##Question 5: 
def calc_elu(x, alpha =0.01):
    if x >0:
        return x
    else:
        return alpha * (math.exp(x)-1)
#Test function:
assert round(calc_elu(1), 2) == 1
print(round(calc_elu(-1), 2))

##Question 6:
import math
def calc_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif act_name == 'relu':
        return max(0, x)
    elif act_name == 'elu':
        alpha = 0.01
        if x > 0:
            return x
        else:
            return alpha * (math.exp(x) - 1)
    else:
        raise ValueError("Unsupported activation function")

# Test function
assert calc_activation_func(x=1, act_name='relu') == 1
print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))

##Question 7:
def calc_ae(y, y_hat):
    return abs(y - y_hat)

# Test function
y = 1
y_hat = 6
assert calc_ae(y, y_hat) == 5

y = 2
y_hat = 9
print(calc_ae(y, y_hat))

##Question 8:
def calc_se(y, y_hat):
    return (y - y_hat) ** 2

# Test function
y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4

print(calc_se(2, 1))

##Question 9
import math

def approx_cos(x, n):
    result = 0
    for i in range(n):
        coef = (-1) ** i
        num = x ** (2 * i)
        denom = math.factorial(2 * i)
        result += coef * (num / denom)
    return result

# Test function
assert round(approx_cos(x=1, n=10), 2) == 0.54
print(round(approx_cos(x=3.14, n=10), 2))

##Question 10:
import math

def approx_sin(x, n):
    result = 0
    for i in range(n):
        coef = (-1) ** i
        num = x ** (2 * i + 1)
        denom = math.factorial(2 * i + 1)
        result += coef * (num / denom)
    return result

# Test function
assert round(approx_sin(x=1, n=10), 4) == 0.8415
print(round(approx_sin(x=3.14, n=10), 4))

##Question 11:
import math

def approx_sinh(x, n):
    result = 0
    for i in range(n):
        num = x ** (2 * i + 1)
        denom = math.factorial(2 * i + 1)
        result += num / denom
    return result

# Test function
assert round(approx_sinh(x=1, n=10), 2) == 1.18
print(round(approx_sinh(x=3.14, n=10), 2))

##Question 12:
import math

def approx_cosh(x, n):
    result = 0
    for i in range(n):
        num = x ** (2 * i)
        denom = math.factorial(2 * i)
        result += num / denom
    return result

# Test function
assert round(approx_cosh(x=1, n=10), 2) == 1.54
print(round(approx_cosh(x=3.14, n=10), 2))
