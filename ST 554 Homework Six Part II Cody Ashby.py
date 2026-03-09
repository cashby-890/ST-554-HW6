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
        return x,y
    
    def fit_slope(x,y):
        
    def run_simulations(int):
        """Uses generate_data and fit_slope in a for loop; also adds to list of slopes"""
        
    def plot_sampling_distribution():
        """Will produce an error message if the length of slopes is zero; otherwise, a histogram of the slopes will be plotted"""
        
    def find_prob(value:int,sided:str):
        """Finds the probability of the sample slope being larger, smaller, or different from a specified value; also relies on the length of slopes being larger than zero"""