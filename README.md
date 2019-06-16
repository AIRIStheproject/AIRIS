# AIRIS
The ZTF database, at its time of inception, had made available only the light
curves of individual transient events, in the general domain. For a researcher who
wants to study about a particular transient event, it would be a very tedious process
to sift through light curves, determine which transient event was being reported
and then search for individual readings. This is a very time consuming job and
forces an interested individual to actually spend more determining what transient
event he was looking at than in actual research. Thus, the main objective of the
project was to create a database, based on the daily report of light curves, as given
out by the ZTF.
The other objective of this project was to design a platform that would cater to
an individual interested in transient events. This platform would provide all alert
packets that this individual is interested in only, from the ZTF database.

The basic steps to be carried out are:

INFORMATION RETRIEVAL

1. Accept details from individuals who are interested to receive notifications.
Ideally, the admin must get the following details: Name, Transient event that the
individual is interested in, Email Address to send notifications to and Last Updated
time. When a person signs up for our platform, he is provided with a password,
using which the data will be accessed from the second program. Store this contact
data into a csv file, name it contact.csv.
2. Using the area of interested transient events as a filter, we filter out alerts from
the ZTF database. For example, if a particular individual wants data related to
event A, our program should filter the ZTF database, download alerts that are
relevant and save it to a csv file, say ztfdata.csv. During the first run, the entire
ZTF database is checked and saved to our database. Store the date of first run.
3. Now, a provision must be made so that the program can run everyday at a
designated time, to update the csv file with any new entries. Thus, in the
subsequent runs, datasets appearing after the date of first run is filtered and saved.

PROCESSING OF DOWNLOADED DATA

4. Now, all data in the ztfdata file can’t be presented to the user, as the chances of
redundancy are very high. Thus there is a need for different verticals, based on
which meaningful information regarding the transient events can be passed on to
the end user. A temporary dataframe with alerts of objectId corresponding to one
contact (from the contact database) is formed.
5. We select the following as verticals:
a. The last updated time of the individual in the contact file is compared
with the time of observation of the alert
b. The value of Δmaglatest should be compared with a threshold value given
by the user. Thus, we need to introduce a column ‘THRESHOLD’ which
will define the minimum value of Δmaglatest. If there are alerts with values
beyond the threshold, user must be notified.
6. Update the last updated time of the individual with the new time.
7. Send out notifications for alerts which satisfied all verticals that were set, via
email addresses provided by the user.
8. The program is designed to run once a day at particular time.

INTERFACING

Now, the user has got a notification email that tells him of a new alert that satisfies
the criteria. The second part of the program is designed as a front­end program.
Here, the user can log­in to the interface by using the username and password that
were allotted on sign­up. Once the user has logged in successfully, a light curve of
the object of interest and the all data entries corresponding to that object is to be
displayed. There should be, finally, a provision to change the threshold value, if
the user wants.
