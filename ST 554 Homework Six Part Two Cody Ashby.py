# ST 554 Homework Six Part II by Cody Ashby
# Creating a Class from our SLR sample slope simulator

# In the previous homework assignment, we created a simulation of a sampling distribution for the sample slope of a SLR model.
# Here, we'll utilize the concepts of creating a Python class to accomplish this same goal.
# Before we begin though, let's import the appropriate modules:

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import default_rng
from sklearn import linear_model

# Now, let's start defining our class!

class SLR_slope_simulator:
    
    def __init__(self, beta_0:int, beta_1:int, x:np.array, sigma:int, seed:int):
        self.beta_0 = beta_0
        self.beta_1 = beta_1
        self.sigma = sigma
        self.x = x
        self.n = len(x)
        self.rng = rng.normal(loc=beta_1,scale=sigma)
        self.slopes = []
        
    def generate_data:
        """Generates a dataset"""
        y = beta_0 + beta_1*x +rng.normal(loc=beta_1,scale=sigma)
        return x,y
    
    def fit_slope(x,y):
        model=reg.fit(x.reshape(-1,1),y)
        slope=model.coef_[0]
        return slope
    
    def run_simulations(int):
        """Uses generate_data and fit_slope in a for loop; also adds to list of slopes"""
        slopes = np.zeros(shape(int,1))
        for i in range (1,int):
            y = beta_0 + beta_1*x +rng.normal(loc=beta_1,scale=sigma)
            model = reg.fit(x.reshape(-1,1),y)
            slopes[i] = model.coef_[0]
        return None
            
        
    def plot_sampling_distribution():
        """Will produce an error message if the length of slopes is zero; otherwise, a histogram of the slopes will be plotted"""
        if len(slopes) = 0:
            print("ERROR: Run a simulation first!")
        else:
            plt.hist(slopes)
            
    def find_prob(value:float,sided:str):
        """Finds the probability of the sample slope being larger, smaller, or different from a specified value; also relies on the length of slopes being larger than zero"""
        if len(slopes) = 0:
            print("ERROR: Run a simulation first!")
        else:
            if sided = "above":
                prob = sum(slopes>value)/len(slopes)
            elif sided = "below":
                prob = sum(slopes<value)/len(slopes)
            elif sided = "two-sided":
                if value > np.median(slopes):
                    prob = 2*(sum(slopes>value)/len(slopes))
                elif value < np.median(slopes):
                    prob = 2*(sum(slopes<value)/len(slopes))
        return prob
    
    