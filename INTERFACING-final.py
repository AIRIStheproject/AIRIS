
# coding: utf-8

# In[9]:


import getpass 
import pandas as pd
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
#Loading the contact and ztf data files
b=pd.read_csv('~/Desktop/contact.csv')
aa=pd.read_csv('~/Desktop/ztfdata.csv', index_col= None)
b1 = b['INTEREST']
b2=b['LAST UPDATED']
bthresh=b['THRESHOLD']
#Converting  the username and passwords to a list, for comparison
user = b['NAME'].tolist()
pwd=b['PASSWORD'].tolist()
username = input("Please enter your username. This is case insensitive: ").upper()                     
#IF the username exists in the contact file, the user is prompted for the password.
#If it doesnt exist, the individual is prompted to sign up by contacting the admin 
if username in user:
    password = getpass.getpass('Hello '+username+',' "please enter your password. This is case sensitive: ")
    
    u=pd.Index(user)
    l= u.get_loc(username)
    if password==pwd[l]:
        
        
        obj=aa[aa.objectId==b1[l]]
        a1 = obj['objectId']
        a2 = obj['time']
        a3=obj['magpsf']
        a4=obj['Δmaglatest']

#The light curve and datasets corresponding to the objectId of user is displayed     
        print('Hi '+ username)
        print('Following is the light curve of the object of your interest '+b1[l]+' and the all data entries of the same, in the reverse chronological order: ')
        y_med = [np.median(a3)]*len(a2)
        med_line = plt.plot(a2,y_med, linestyle='--')
        plt.title(b1[l])
        plt.plot(a2, a3) 
        plt.xticks(rotation=90, fontsize=10)
        plt.rcParams['figure.figsize'] = [15, 5]
        plt.gca().invert_xaxis()
        plt.show()
        print('You were last updated about these notifications on '+b2[l])
        display(obj)
#Giving an option to update the value of threshold to user
        yes=int(input(print('Do you want to change the threshold value for Δmaglatest? Enter 1 if you want to change, otherwise enter 0')))
        
        if yes==1:
            bthresh[l]=float(input(print('Enter the new value of threshold')))
        b['THRESHOLD'] = bthresh
        b.to_csv('~/Desktop/contact.csv',index=False)
    else:
        print('Wrong password')
else:
    print('You are not registered in our database. Please contact the admin to register and recieve updates about transient stars')

