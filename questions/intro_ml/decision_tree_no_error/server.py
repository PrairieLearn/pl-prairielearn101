import matplotlib.pyplot as plt
import io
import random, copy
import numpy as np


def file(data):

    if data['filename']=='figure.png':
        
        if data['params']['problem']=="checkerboard":

            n_points = 300
            n_classes = 2
    
            x = np.random.uniform(-1,1, size=(n_points, n_classes))
            mask = np.logical_or(np.logical_and(x[:,0] > 0.0, x[:,1] > 0.0), \
                np.logical_and(x[:,0] < 0.0, x[:,1] < 0.0))
            y = np.eye(n_classes)[1*mask][:,0]
            X = x[np.all(np.abs(x) > 0.03, axis=1),:]
            Y = y[np.all(np.abs(x) > 0.03, axis=1)]
    
            plt.scatter(X[:,0], X[:,1], c=Y, cmap="bwr", alpha=0.5)
            plt.xlabel(r"$x$")
            plt.xlabel(r"$x_1$")
            plt.ylabel(r"$x_2$")
            
            # Save the figure and return it as a buffer
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            return buf

        elif data['params']['problem']=="diagonal":

            n_points = 300
            n_classes = 2
            
            s = random.sample([-1,1], k=2)
            
            x = np.random.uniform(-1,1, size=(n_points, n_classes))
            z = np.random.uniform(-0.05, 0.05) + np.random.uniform(0.6, 0.2)*x[:,0] + s[1]*np.random.uniform(0.2, 0.6)*x[:,1]
            y = (z > 0).astype('int')
            X = x[(np.abs(z) > 0.01),:]
            Y = y[(np.abs(z) > 0.01)].astype('int')
            
            scatter  = plt.scatter(X[:,0], X[:,1], c=Y, cmap="bwr", alpha=0.5, label=Y)
            plt.xlabel(r"$x_1$")
            plt.ylabel(r"$x_2$")
                        
            # Save the figure and return it as a buffer
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            return buf
            
        elif data['params']['problem']=="circle":

            n_points = 300
            n_classes = 2
            
            x = np.random.uniform(-1,1, size=(n_points, n_classes))
            r = np.random.uniform(0.2, 0.4) 
            z = ( x[:,0] )**2 + ( x[:, 1] )**2 
            y = (z > r ).astype('int')
            X = x[(np.abs(z-r) > 0.05),:]
            Y = y[(np.abs(z-r) > 0.05)]
            scatter  = plt.scatter(X[:,0], X[:,1], c=Y, cmap="bwr", alpha=0.5, label=Y)
            plt.xlabel(r"$x_1$")
            plt.ylabel(r"$x_2$")
            
            # Save the figure and return it as a buffer
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            return buf


def generate(data):


    data['params']['problem'] = random.choice(["checkerboard", "diagonal", "circle"])
    if data['params']['problem']=="checkerboard":
        data['params']['checkerboard'] = True
        data['params']['diagonal'] = False
        data['params']['circle'] = False
    elif data['params']['problem']=="diagonal":
        data['params']['checkerboard'] = False
        data['params']['diagonal'] = True
        data['params']['circle'] = False
    elif data['params']['problem']=="circle":
        data['params']['checkerboard'] = False
        data['params']['diagonal'] = False
        data['params']['circle'] = True
