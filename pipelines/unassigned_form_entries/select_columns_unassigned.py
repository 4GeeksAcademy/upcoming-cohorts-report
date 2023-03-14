import numpy as np 
import pandas as pd 

##### Values for inputs #####

email = ['email_1@mail.com', 'email_2@mail.com']
course = ['course_1', 'course_2']
language = ['en', 'es']
country = ['Country_1', 'Country_2']
city = ['City_1', 'City_2']
created_at = ['2020-09-22 05:27:37.584999', '2022-11-23 12:24:36.586999']
lead_type = ['STRONG', 'SOFT']
location = ['Location_1', 'Location_2']
ac_deal_owner_full_name = ['Owner_1', 'Owner_2']
fullname = ['Fullname_1', 'Fullname_2']
cohort_assignation_error = ['Missing academy', np.nan]
academy = [np.nan, 'Academy_2']

dict_inputs = {'email':email, 'course':course, 'language':language, 'country':country, 'city':city,
                'created_at':created_at, 'lead_type':lead_type, 'location':location, 'ac_deal_owner_full_name':ac_deal_owner_full_name,
                'fullname':fullname, 'cohort_assignation_error':cohort_assignation_error, 'academy':academy}

expected_inputs = pd.DataFrame(dict_inputs)


##### Values for output #####

fullname = ['Fullname_1', 'Fullname_2']
email_u = ['email_1@mail.com', 'email_2@mail.com']
created_at = ['2020-09-22 05:27:37.584999', '2022-11-23 12:24:36.586999']
course = ['course_1', 'course_2']
language = ['en', 'es']
academy = [np.nan, 'Academy_2']
location = ['Location_1', 'Location_2']
country = ['Country_1', 'Country_2']
city = ['City_1', 'City_2']
cohort_assignation_error = ['Missing academy', np.nan]
lead_type = ['STRONG', 'SOFT']
ac_deal_owner_full_name = ['Owner_1', 'Owner_2']
datetime_creation = [pd.to_datetime('2020-09-22 05:27:37.584999'), pd.to_datetime('2022-11-23 12:24:36.586999')]
days_since_creation = [(pd.Timestamp.now()-pd.to_datetime('2020-09-22 05:27:37.584999')).days, (pd.Timestamp.now()-pd.to_datetime('2022-11-23 12:24:36.586999')).days]

dict_output = {'fullname':fullname, 'email_u':email_u, 'created_at':created_at, 'course':course,
                'language':language, 'academy':academy, 'location':location, 'country':country, 'city':city, 'cohort_assignation_error':cohort_assignation_error, 'lead_type':lead_type,
                'ac_deal_owner_full_name':ac_deal_owner_full_name, 'datetime_creation':datetime_creation, 'days_since_creation':days_since_creation}

expected_output = pd.DataFrame(dict_output)


def run(unassigned):

    # Select only needed columns
    unassigned = unassigned[['fullname', 'email', 'created_at', 'course', 'language', 'academy',  
                            'location', 'country', 'city', 'cohort_assignation_error', 'lead_type', 'ac_deal_owner_full_name']]

    # Create column for creation time in datetime
    unassigned['datetime_creation'] = pd.to_datetime(unassigned['created_at'])

    # Create column that shows how many days have passed since creation
    unassigned['days_since_creation'] = (pd.Timestamp.now() - unassigned['datetime_creation']).dt.days

    # Rename the email column, so it doesn't mix with the emails from upcoming cohorts in the dashboard
    unassigned = unassigned.rename(columns={'email':'email_u'})

    # Show least recent first
    unassigned = unassigned.sort_values(by=['days_since_creation'], ascending=False)

    return unassigned