import random, copy

def generate(data):


    opts = [
        {'txt': """<p>You are hired by a real estate website to develop a regression model to predict housing prices based on other characteristics of a home (like square footage, year of last renovation, number of bedrooms, etc.). Ultimately, they want to develop a tool that will allow homeowners to enter the properties of their home, then get an estimated sales price.</p>
            <p>You are given a dataset on which to train the model. The data has information about every home sale in the last 40 years in 5 selected neighborhoods, which were chosen so as to be representative of most neighborhood 'types'.</p>
            <p>The dataset is sorted by address, then by date of sale. You notice that many homes appear in the dataset more than once (i.e. they were sold several times in the last 40 years). But, when used 'in production' the model will be asked to predict sales price for "new" homes not in this dataset! Therefore, when training and evaluating your model,</p>""",
         'ansTrue': ["you should split the data into training and test by group, with address as the group ID. This way, each address appears either in the training or test set, but not both."],
         'ansFalse': ["you should split the data into training and test stratified by address, so that for all addresses, a fixed proportion of samples from each address appears in the training set.", "you should make sure the data is well shuffled, so that the data in both the training and test sets will be representative of the overall data distribution. This is especially important for sorted data!", "you should make sure that for each home that is going to be in both the training and test sets, the 'earlier' (in time) sales appear in the training set, and the 'later' sales appear in the test set."],
         'exp': ""
         },
        {'txt': """<p>You are hired by a real estate website to develop a regression model to predict a 'housing market score' based on characteristics like interest rates, inflation, local housing supply, and similar factors.</p>
            <p>You are given a dataset on which to train the model. The data has one row for every week in a 2-year period, for every major metro area in the U.S. It has key market factors as features and a 'housing market score' label that was computed based on the sales prices of houses sold that week. It is sorted by metro area, then by time.</p>
            <p>The model will eventually be deployed on their website, to help homeowners in major metro areas (the same metro areas as in the datasets!) decide whether or not it is a favorable time to sell their homes.</p>""",
         'ansTrue': ["you should split the data so that the 'earlier' (in time) samples appear in the training set, and the 'later' samples appear in the test set."],
         'ansFalse': ["you should make sure the data is randomly shuffled, so that the data in both the training and test sets will be representative of the overall data distribution. This is especially important for sorted data!",  "you should split the data into training and test by group, with metro area as the group ID. This way, each metro area appears either in the training or test set, but not both.", 
            "you should avoid shuffling the data - just use the first part of the (sorted) data for training, and the last part as the test set."],
         'exp': ""
         }

    ]

    data['params'] = random.choice(opts)


