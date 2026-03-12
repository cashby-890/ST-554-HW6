# ST 554 Homework Six Part II by Cody Ashby
# Started on March 9, 2026
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

    def __init__(self, beta_0: int, beta_1: int, x: list, sigma: int, seed: int): #this initializes the class
        self.beta_0 = beta_0
        self.beta_1 = beta_1
        self.sigma = sigma
        self.x = x
        self.n = len(x)
        self.rng = default_rng(seed)
        self.slopes = np.zeros(shape=(10000,1)) #tried running this with an empty list, but couldn't get any sensible results

    def generate_data(self): #this will generate a dataset for a given list-type as defined by x
        """Generates a random dataset based on a list"""
        SLR_slope_simulator = self #I know these were defined when the class was inititalized, but the parameters defined in y below would not work unless they appeared again here.
        beta_0 = self.beta_0
        beta_1 = self.beta_1
        x = self.x
        sigma = self.sigma
        y = beta_0 + beta_1*x +np.random.normal(loc=beta_1,scale=sigma,size=len(x)) #line of best fit for the list-type x
        return x,y
        #As a precaution, I reiterated these returned arrays as x and y in the instance created below.

    def fit_slope(self,x: list, y: list): #allows us to estimate a slope from the generated data above
        """Estimates the slope from a generated dataset"""
        SLR_slope_simulator = self
        reg=linear_model.LinearRegression() #some tools from linear_model will be needed here
        beta_0 = self.beta_0
        beta_1 = self.beta_1
        x = self.x
        sigma = self.sigma
        y = beta_0 + beta_1*x +np.random.normal(loc=beta_1,scale=sigma,size=len(x))
        model=reg.fit(x.reshape(-1,1),y) #we can now fit our model here after a modification or two
        slope=model.coef_[0]
        return slope
        #this only give us one slope, though; we'll need to do this lots of times to get a better picture about the trends in the slope. 

    def run_simulations(self,int): #puts the two functions defined above into a for loop a specified number of times
        """Uses the methods from generate_data and fit_slope in a for loop; also adds elements to a list of sample slopes"""
        SLR_slope_simulator = self
        beta_0 = self.beta_0
        beta_1 = self.beta_1
        x = self.x
        sigma = self.sigma
        slopes = np.zeros(shape=(int,1)) #again, although this isn't technically an empty list,this was the only way I could get results.
        for i in range (int):
            y = beta_0 + beta_1*x +np.random.normal(loc=beta_1,scale=sigma,size=len(x))
            reg=linear_model.LinearRegression()
            model = reg.fit(x.reshape(-1,1),y)
            slopes[i] = model.coef_[0] #this replaces the array of zeros with estimated slope coefficients
        return slopes #I know nothing was supposed to be returned here, but again, this was for the sake of being able to produce results.
        #As a precaution, defining the array that comes from this as slopes comes in handy for the instance created below.

    def plot_sampling_distribution(self,slopes:list): #now we can get a visual representation from the sample slopes we got from the simulation above.
        """Will produce an error message if the length of the array of sample slopes is zero; otherwise, a histogram of the sample slopes will be plotted"""
        SLR_slope_simulator = self #probably not needed here, but again, done as a precaution
        if len(slopes) == 0:
            print("ERROR: Run a simulation first!") #possibly too simple of a message, but it's something?
        else:
            return plt.hist(slopes)

    def find_prob(self,value:float,sided:str): #finds the type of probability that the sample slope is either above, below, or different from a certain value
        """Finds the probability of the sample slope being larger, smaller, or different from a specified value; 
        also relies on the length of the array of sample slopes being larger than zero"""
        SLR_slope_simulator = self
        if len(slopes) == 0:
            print("ERROR: Run a simulation first!")
        else:
            if sided == "above":
                prob = sum(slopes>value)/len(slopes)
            elif sided == "below":
                prob = sum(slopes<value)/len(slopes)
            elif sided == "two-sided":
                if value > np.median(slopes):
                    prob = 2*(sum(slopes>value)/len(slopes))
                elif value < np.median(slopes):
                    prob = 2*(sum(slopes<value)/len(slopes))
            else:
                print("Please type in 'above', 'below', or 'two-sided'.")
        return prob
    
# Now that we've defined our class and a bunch of attributes to go with it; let's try it on some code!

example=SLR_slope_simulator(beta_0=12,beta_1=2,x=np.array(list(np.linspace(start=0,stop=10,num=11))*3),sigma=1,seed=10)
#As I warned many times before, I've defined a few variables utilizing this instance for the class and the appropriate attributes.
x=example.generate_data()[0]
y=example.generate_data()[1]
#From x and y as defined above, we'll estimate the sample slope.
example.fit_slope(x,y)
#Just in case we wanna skip to the end perhaps, let's try plotting the sampling distribution first.
example.plot_sampling_distribution(slopes) #Should produce the short, but sweet error message.
#Time for the "dirty work", repeat the process of generating data and fitting a sample slope in the simulation function below 10000 times.
example.run_simulations(10000) #Automatically saved as an array of sample slopes; it may be defined as slopes for ease of programming.
example.plot_sampling_distribution(slopes) #Now that we've run a simulation, we should get something that makes sense.
example.find_prob(2.1,"two-sided") #Finds the probability that the slope is different from 2.1.

#Thanks for bearing with me!
    