import numpy as np 
import pandas as pd 


##### Values for inputs #####

### cohort_users ###
id_ = [11, 22, 33, 44]
role = ['student', 'STUDENT', 'teacher', 'student']
cohort_id = [444, 111, 888, 555]
user_id = [2, 7, 3, 4]

dict_cohort_users = {'id':id_, 'role':role, 'cohort_id':cohort_id, 'user_id':user_id}

### auth ###
id_ = [2, 3, 4]
first_name = ['First_2', 'First_3', 'First_4']
last_name = ['Last_2', 'Last_3', 'Last_4']

dict_auth = {'id':id_, 'first_name':first_name, 'last_name':last_name}

### upcoming_cohorts ###
id_ = [444, 555, 888]
slug = ['cohort_4', 'cohort_5', 'cohort_8']
name = ['Cohort_4', 'Cohort_5', 'Cohort_8']

dict_upcoming_cohorts = {'id':id_, 'slug':slug, 'name':name}

### Expected inputs ###
expected_inputs = [pd.DataFrame(dict_cohort_users), pd.DataFrame(dict_auth), pd.DataFrame(dict_upcoming_cohorts)]


##### Values for output #####

id_ = [11, 44]
role = ['student', 'student']
cohort_id = [444, 555]
user_id = [2, 4]
slug = ['cohort_4', 'cohort_5']
first_name = ['First_2', 'First_4']
last_name = ['Last_2', 'Last_4']

dict_output = {'id':id_, 'role':role, 'cohort_id':cohort_id, 'user_id':user_id, 'slug':slug, 
                'first_name':first_name, 'last_name':last_name}

### Expected output ###
expected_output = pd.DataFrame(dict_output)



def run(cohort_users, auth, upcoming_cohorts):

    """Function to obtain the users that are associated to an upcoming cohort as students"""

    # Associate each upcoming_cohort id with its slug
    upcoming_cohorts_slugs = upcoming_cohorts[['id', 'slug']]

    # Merge cohort_users with upcoming_cohorts_slugs, so cohort_users now has slug in addition to cohort id
    cohort_users = cohort_users.merge(upcoming_cohorts_slugs, left_on='cohort_id', right_on='id', how='left')
    cohort_users = cohort_users.rename(columns={'id_x':'id'})
    cohort_users = cohort_users.drop(columns=['id_y'])

    # Merge cohort_users with auth, so there is more information about the users
    cohort_users_auth = cohort_users.merge(auth, left_on='user_id', right_on='id', how='left')

    # Select only users who are associated with a cohort as students
    cohort_users_auth = cohort_users_auth[cohort_users_auth['role'].str.lower()=='student']
    cohort_users_auth = cohort_users_auth.rename(columns={'id_x':'id'})
    cohort_users_auth = cohort_users_auth.drop(columns=['id_y'])

    # Select only students who have an associated cohort
    confirmed = cohort_users_auth.loc[cohort_users_auth['slug'].notnull()]

    return confirmed