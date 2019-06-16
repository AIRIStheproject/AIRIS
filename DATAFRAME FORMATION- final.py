
# coding: utf-8

# In[ ]:


import pandas as pd
import datetime
import numpy as np
import time
import schedule
import matplotlib.pyplot as plt 
import smtplib
from IPython.display import display

#contact is the contact csv file. aa is an empty csv file, to which we will be saving the ZTF DATA. We give an option of adding to,removing from or editing the contact database
try:
    b=pd.read_csv('~/Desktop/contact.csv')
    aa=pd.read_csv('~/Desktop/ztfdata.csv')
    display(b)
    delrows=[]
    l=len(b)
    u= input(print('Do you want to add/delete/edit any data from the contact database? Press 0 if you do not want any changes, 1 to add, 2 to delete,3 to edit'))
    if u== '1':
        size1 =int(input(print ('How many new data rows do you want to add?')))
    
        for i in range(0,size1):
            print('You will now be entering details of the ',i+1,'th new row')
            col=input(print('Enter the name in caps:'))
            siz=input(print('Enter the email address: '))
            mas=input(print('Enter the objectId of interest. Please use objectIds in confirmation with the ZTF datasets'))
            tim=input(print('Enter the last updated date and time in the following format - MM/DD/YY HH:MM:SS  '))
            pas=input(print('Enter the password to be alloted'))
            b.loc[l+i]= [ col, siz, mas, tim,pas]
            
    elif u=='2':
        num= int(input(print('Enter the number of rows you want to delete from the contact database')))
        delrows=[None]*num
        for i in range(0,num):
            
            delrows[i]=int(input(print('Enter the row numbers you want to delete')))
            b=b.drop([delrows[i]])

    elif u=='3':
        num1=int(input(print('Enter the number of cells that have to be changed')))
        for i in range(0,num1):
            row=int(input(print('Enter the row number that has to be edited')))
            column=input(print('Enter the name of the column in caps under which the data to be edited is'))
            data_new=input(print('Enter the new data that has to be entered'))
            b.loc[row,column]=data_new
        
    print('The updated database is as :')
    display(b)
#In case such files dont exist, the admin manually enters the contacts,which is then saved to filename contact.csv and aa    
except IOError:
    column1=['NAME', 'CONTACT','INTEREST','LAST UPDATED','PASSWORD']
    b=pd.DataFrame(columns=column1)
    size1 =int(input(print ('How many new data rows do you want to add to the contact database?')))
    l=0
    for i in range(0,size1):
        print('You will now be entering details of the ',i+1,'th new row')
        col=input(print('Enter the name in caps:'))
        siz=input(print('Enter the email address: '))
        mas=input(print('Enter the objectId of interest. Please use objectIds in confirmation with the ZTF datasets'))
        tim=input(print('Enter the last updated date and time in the following format - MM/DD/YY HH:MM:SS  '))
        pas=input(print('Enter the password to be alloted'))
        b.loc[l+i]= [ col, siz, mas, tim,pas]
    export1 = b.to_csv (r'~/Desktop/contact.csv', index = None, header=True) 
    column2=['id','objectId','time','filter','ra','dec','magpsf','magap','distnr','Δmaglatest','Δmagref','rb']
    aa=pd.DataFrame(columns=column2)
    export2 = aa.to_csv (r'~/Desktop/ztfdata.csv', index = None, header=True)
    

# Pandas dataframe b has the columns of Name, Interested Object ID and Last Updated 
contact=len(b)
b1 = b['INTEREST']
b2 = b['LAST UPDATED']
b3 = b['NAME']
bcont=b['CONTACT']
bthresh=b['THRESHOLD']
date=0
#ZTF data is downloaded and saved in the aa dataframe. Only those entries are downloaded to which contacts have shown interest in.
#This is the first run
for  i in range(0, 1):
    link='https://mars.lco.global/?sort_value=jd&sort_order=desc&objectId='+b1[i]+'&candid=&time__gt=&time__lt=&time__since=&jd__gt=&jd__lt=&filter=&cone=&objectcone=&objectidps=&ra__gt=&ra__lt=&dec__gt=&dec__lt=&l__gt=&l__lt=&b__gt=&b__lt=&magpsf__gte=&magpsf__lte=&sigmapsf__lte=&magap__gte=&magap__lte=&distnr__gte=&distnr__lte=&deltamaglatest__gte=&deltamaglatest__lte=&deltamagref__gte=&deltamagref__lte=&elong__lte=&nbad__lte=&rb__gte=&classtar__gte=&classtar__lte=&fwhm__lte='
    tblist = pd.read_html(link)
    aa= tblist[0]
                
for  i in range(1, contact):
    link='https://mars.lco.global/?sort_value=jd&sort_order=desc&objectId='+b1[i]+'&candid=&time__gt=&time__lt=&time__since=&jd__gt=&jd__lt=&filter=&cone=&objectcone=&objectidps=&ra__gt=&ra__lt=&dec__gt=&dec__lt=&l__gt=&l__lt=&b__gt=&b__lt=&magpsf__gte=&magpsf__lte=&sigmapsf__lte=&magap__gte=&magap__lte=&distnr__gte=&distnr__lte=&deltamaglatest__gte=&deltamaglatest__lte=&deltamagref__gte=&deltamagref__lte=&elong__lte=&nbad__lte=&rb__gte=&classtar__gte=&classtar__lte=&fwhm__lte='
    tblist = pd.read_html(link)
    df= tblist[0]
    f=[aa,df]
    re=pd.concat(f)
    aa=re
date=datetime.date.today()
date=str(date)
#ZTF website is checked by this function and any data after the day of first run, is downloaded and saved in the aa dataframe. Only those entries are downloaded to which contacts have shwn interest in. 

def job():
    
    l=0
    #Updating the contact database, if the user wishes to do so
    u= input(print('Do you want to enter any new data into the contact database? Press 1 for yes, 0 for no.'))
    if u== '1':
        size1 =int(input(print ('How many new data rows do you want to add?')))
    
        for i in range(0,size1):
            print('You will now be entering details of the ',i+1,'th new row')
            col=input(print('Enter the name in caps:'))
            siz=input(print('Enter the email address: '))
            mas=input(print('Enter the objectId of interest. Please use objectIds in confirmation with the ZTF datasets'))
            tim=input(print('Enter the last updated date and time in the following format - MM/DD/YY HH:MM:SS  '))
            pas=input(print('Enter the password to be alloted'))
            b.loc[l+i]= [ col, siz, mas, tim,pas]
    print('The updated database is as :')
    display(b)
    #Invoking the variables date amd dataframe 'aa' as a local variable
    d=date
    
    a=aa
    #Appending any new data to the aa dataframe from ZTF site
    if l==0:
        for i in range (0,contact):
            link='https://mars.lco.global/?sort_value=jd&sort_order=desc&objectId='+b1[i]+'&candid=&time__gt='+d+'&time__lt=&time__since=&jd__gt=&jd__lt=&filter=&cone=&objectcone=&objectidps=&ra__gt=&ra__lt=&dec__gt=&dec__lt=&l__gt=&l__lt=&b__gt=&b__lt=&magpsf__gte=&magpsf__lte=&sigmapsf__lte=&magap__gte=&magap__lte=&distnr__gte=&distnr__lte=&deltamaglatest__gte=&deltamaglatest__lte=&deltamagref__gte=&deltamagref__lte=&elong__lte=&nbad__lte=&rb__gte=&classtar__gte=&classtar__lte=&fwhm__lte='
            tblist=pd.read_html(link)
            df1=tblist[0]
            f1=[a,df1]
            re1= pd.concat(f1)
            a=re1
            l+=1
            dates=datetime.date.today()
            dates=str(dates)
    else:
         for i in range (0,contact):
            link='https://mars.lco.global/?sort_value=jd&sort_order=desc&objectId='+b1[i]+'&candid=&time__gt='+dates+'&time__lt=&time__since=&jd__gt=&jd__lt=&filter=&cone=&objectcone=&objectidps=&ra__gt=&ra__lt=&dec__gt=&dec__lt=&l__gt=&l__lt=&b__gt=&b__lt=&magpsf__gte=&magpsf__lte=&sigmapsf__lte=&magap__gte=&magap__lte=&distnr__gte=&distnr__lte=&deltamaglatest__gte=&deltamaglatest__lte=&deltamagref__gte=&deltamagref__lte=&elong__lte=&nbad__lte=&rb__gte=&classtar__gte=&classtar__lte=&fwhm__lte='
            tblist=pd.read_html(link)
            df1=tblist[0]
            f1=[a,df1]
            re1= pd.concat(f1)
            a=re1
            
            dates=datetime.date.today()
            dates=str(dates)
    
    
        
    print('\n')
    obj=[]
    b4=[]
    cont=[]
    error=[]
    for j in range(0,contact):
    #Taking only relevant rows for each objectID and other parameters corresponding to that objectID
        error=bthresh[j]
        cont=str(bcont[j])
        obj=a[a.objectId==b1[j]]
        a1 = obj['objectId']
        a2 = obj['time']
        a3=obj['magpsf']
        a4=obj['Δmaglatest']
    #Taking the median value of magnitudes and maximum of dates,for a specific object. 
        med=np.median(a3)
        size=len(obj)
        b4=max(a2)
        for i in range(0,size):
    #If the last updated time is lesser than the new data, then we print results that are outside the percentage range.        
            if a2[i]>b2[j]:
                abso=a3[i]-med
                if (abso<(-error)
                    or(
                        abso>(error)
                       )
                    ):
    #If all criteria are met, we send an email to the user
                    gmail_user = 'youremail@gmail.com'  
                    gmail_password = 'yourpassword'

                    sent_from = gmail_user  
                    to = cont
                    subject = 'NEW TRANSIENT SIGHTING OF'+a1[i]  
                    body = b3[j],', you have a new hit of ', a1[i],'. The timestamp for the same is '+a2[i]+'\n\n- AIRIS TEAM'

                    email_text = """\  
                    From: %s  
                    To: %s  
                    Subject: %s

                    %s
                    """ % (sent_from, "".join(to), subject, body)
        
                    try:  
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server.login(gmail_user, gmail_password)
                        server.sendmail(sent_from, to, email_text)
                        server.close()
    
                        print ('Email sent!')
                    except:  
                        print ('Something went wrong...')
                
                else:
                    
                    print('No new hits outside the permissible limits')
                
       
            
            else:
                print('Already updated')
        
    #We update the last updated  time with the latest time         
        b2[j]=b4
        a.to_csv('~/Desktop/ztfdata.csv',index=False)
        b.to_csv('~/Desktop/contact.csv',index=False)
schedule.every(1).day.at("18:00").do(job)



while True:
    schedule.run_pending()
    time.sleep(1)


