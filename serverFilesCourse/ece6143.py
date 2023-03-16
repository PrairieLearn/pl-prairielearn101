import numpy as np
import itertools

def solarized_colors():
    return {'base03': '#002b36', 'base02': '#073642', 'base01': '#586e75', 'base00': '#657b83',
            'base0': '#839496', 'base1': '#93a1a1', 'base2': '#eee8d5', 'base3': '#fdf6e3',
            'yellow': '#b58900', 'orange': '#cb4b16', 'red': '#dc322f', 'magenta': '#d33682', 
            'violet': '#6c71c4', 'blue': '#268bd2', 'cyan': '#2aa198', 'green': '#859900'}

def generate_linear_regression_data_n(n=100, d=1, coef=[5], intercept=1, sigma=0):
  x = np.random.randn(n,d)
  y = (np.dot(x, coef) + intercept).squeeze() + sigma * np.random.randn(n)
  return x, y

def generate_linear_regression_data_int(n=100, xrange=[0,10], d=1, coef=[5], intercept=1, sigma=0):
    x = np.random.randint(xrange[0], xrange[1], size=(n,d))
    y = (np.dot(x, coef) + intercept).squeeze() + sigma * np.random.randn(n)
    return x, np.round(y).astype('int')

def generate_linear_regression_data(n=100, d=1, coef=[5], intercept=1, sigma=0, uninformative=0, collinear=0, collinear_sigma = 0):
  x = np.random.uniform(-1,1,size=(n,d-uninformative-collinear))
  y = (np.dot(x, coef) + intercept).squeeze() + sigma * np.random.randn(n)
  if collinear:
    # select random columns from x
    collinear_cols = np.random.choice(d-uninformative-collinear,size=collinear, replace=True)
    # generate some random coefficients for the new collinear columns
    collinear_coefs = np.random.uniform(1, 10, collinear)
    # generate noise so new columns are not exactly collinear
    collinear_noise = collinear_sigma*np.random.normal(size=(n,collinear))
    # value of new collinear columns
    collinear_features = collinear_coefs * x[:, collinear_cols] + collinear_noise
    x = np.column_stack((x, collinear_features))
  if uninformative:
    x = np.column_stack((x, sigma*np.random.randn(n,uninformative)))

  return x, y

def generate_linear_basis_data(n=100, d=2, coef=[1,1,0.5,0.5,1], intercept=1, sigma=0):
  x = np.random.randn(n,d)
  x = np.column_stack((x, x**2 ))
  for pair in list(itertools.combinations(range(d), 2)):
    x = np.column_stack((x, x[:,pair[0]]*x[:,pair[1]]))
  y = (np.dot(x, coef) + intercept).squeeze() + sigma * np.random.randn(n)
  return x[:,:d], y

def generate_polynomial_regression_data(n=100, xrange=[-1,1], coefs=[1,0.5,0,2], sigma=0.5):
  x = np.random.uniform(xrange[0], xrange[1], n)
  y = np.polynomial.polynomial.polyval(x,coefs) + sigma * np.random.randn(n)

  return x.reshape(-1,1), y


def generate_polynomial_classifier_data(n=100, xrange=[-1,1], coefs=[1,0.5,0,2], sigma=0.5):
    x = np.random.uniform(xrange[0], xrange[1], size=(n, 2))
    ysep = np.polynomial.polynomial.polyval(x[:,0],coefs)
    y = (x[:,1]>ysep).astype(int)
    x[:,0] = x[:,0] + sigma * np.random.randn(n)
    x[:,1] = x[:,1] + sigma * np.random.randn(n)
    return x, y

