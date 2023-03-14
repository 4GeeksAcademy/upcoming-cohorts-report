import numpy as np
import pandas as pd


##### Values for inputs #####

# form_entry
first_name = ['First_1', 'First_2', 'First_3', 'First_4']
last_name = ['Last_1', 'Last_2', 'Last_3', 'Last_4']
email = ['email_1@mail.com', 'email_2@mail.com', 'email_3@mail.com', 'email_4@mail.com']
course = ['full-stack-ft', 'software-engineering', 'machine-learning', 'datascience-ml']
language = ['us', 'en', 'en', 'es']
location = [np.nan, 'Location_from_1', 'Wrong_academy', 'Location_from_2']
created_at = ['2023-03-01 21:00:00+00:00', '2023-01-11 11:00:00+00:00', '2023-03-01 21:00:00+00:00', '2023-02-01 22:00:00+00:00']
updated_at = ['2023-03-01 21:00:00+00:00', '2023-01-11 11:00:00+00:00', '2023-03-01 21:00:00+00:00', '2023-02-01 22:00:00+00:00']
academy_id = [np.nan, 11, 66, 33]
ac_expected_cohort_date = ['2023-06-01 12:00:00+00:00', '2023-07-01 12:00:00+00:00', '2023-08-01 12:00:00+00:00', '2023-09-01 12:00:00+00:00']

dict_form_entry = {'first_name':first_name, 'last_name':last_name, 'email':email, 'course':course,
                    'language':language, 'location':location, 'created_at':created_at, 'updated_at':updated_at,
                    'academy_id':academy_id, 'ac_expected_cohort_date':ac_expected_cohort_date}

# cohort_users
user_id = [111, 222, 333, 444, 555]
role = ['STUDENT', 'student', 'teacher', 'teacher', 'student']
created_at = ['2023-02-19 23:06:31.519727+00:00', '2023-02-20 22:06:31.519727+00:00', '2023-02-21 21:06:31.519727+00:00', '2023-02-22 20:06:31.519727+00:00', '2023-02-23 19:06:31.519727+00:00']
cohort_id = [1, 1, 2, 3, 4]

dict_cohort_users = {'user_id':user_id, 'role':role, 'created_at':created_at, 'cohort_id':cohort_id}

# auth
id_ = [111, 333, 444, 555]
email = ['email_2@mail.com', 'email_1@mail.com', 'other_email@mail.com', 'email_3@mail.com']

dict_auth = {'id':id_, 'email':email}

# academies_alias
slug = ['Location_from_1', 'Location_from_2', 'Location_from_1_other', 'Location_from_3', 'Location_from_4', 'Location_from_3_other', 'Location_from_5']
academy_id = [11, 22, 11, 33, 44, 33, 55]
name = ['Academy_1', 'Academy_2', 'Academy_1', 'Academy_3', 'Academy_4', 'Academy_3', 'Academy_5']
status = ['ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE']

dict_academies_alias = {'slug':slug, 'academy_id':academy_id, 'name':name, 'status':status}

### Expected inputs ###
expected_inputs = [pd.DataFrame(dict_form_entry), pd.DataFrame(dict_cohort_users), pd.DataFrame(dict_auth), pd.DataFrame(dict_academies_alias)]


##### Values for output #####

first_name = ['First_1', 'First_2', 'First_3', 'First_4']
last_name = ['Last_1', 'Last_2', 'Last_3', 'Last_4']
email = ['email_1@mail.com', 'email_2@mail.com', 'email_3@mail.com', 'email_4@mail.com']
course = ['full-stack-ft', 'software-engineering', 'machine-learning', 'datascience-ml']
language = ['us', 'en', 'en', 'es']
location = [np.nan, 'Location_from_1', 'Wrong_academy', 'Location_from_2']
form_created_at = ['2023-03-01 21:00:00', '2023-01-11 11:00:00', '2023-03-01 21:00:00', '2023-02-01 22:00:00']
updated_at = ['2023-03-01 21:00:00+00:00', '2023-01-11 11:00:00+00:00', '2023-03-01 21:00:00+00:00', '2023-02-01 22:00:00+00:00']
academy_id = [np.nan, 11, 66, 33]
ac_expected_cohort_date = ['2023-06-01 12:00:00+00:00', '2023-07-01 12:00:00+00:00', '2023-08-01 12:00:00+00:00', '2023-09-01 12:00:00+00:00']
datetime_form_entry_creation = [pd.to_datetime('2023-03-01 21:00:00'), pd.to_datetime('2023-01-11 11:00:00'), pd.to_datetime('2023-03-01 21:00:00'), pd.to_datetime('2023-02-01 22:00:00')]
role = [np.nan, 'STUDENT', 'student', np.nan]
cohort_user_created_at = [np.nan, '2023-02-19 23:06:31.519727', '2023-02-23 19:06:31.519727', np.nan]
cohort_id = [np.nan, 1, 4, np.nan]
datetime_cohort_user_creation = [pd.to_datetime(np.nan), pd.to_datetime('2023-02-19 23:06:31.519727'), pd.to_datetime('2023-02-23 19:06:31.519727'), pd.to_datetime(np.nan)]
in_cohort_user = [0, 1, 0, 0]

# Output dict
dict_output = {'first_name':first_name, 'last_name':last_name, 'email':email, 'course':course, 'language':language, 'location':location, 'form_created_at':form_created_at, 'updated_at':updated_at,
                'academy_id':academy_id, 'ac_expected_cohort_date':ac_expected_cohort_date, 'datetime_form_entry_creation':datetime_form_entry_creation,
                'role':role, 'cohort_user_created_at':cohort_user_created_at, 'cohort_id':cohort_id, 
                'datetime_cohort_user_creation':datetime_cohort_user_creation, 'in_cohort_user':in_cohort_user}

# Expected output
expected_output = pd.DataFrame(dict_output)



def run(form_entry, cohort_users, auth, academies_alias):

    # Merge cohort_users and auth based on user id
    cohort_users_auth = cohort_users.merge(auth, left_on='user_id', right_on='id', how='left')
    cohort_users_auth = cohort_users_auth[['email', 'role', 'created_at', 'cohort_id']]
    # Consider only users with student as role
    cohort_users_auth = cohort_users_auth[cohort_users_auth['role'].str.lower()=='student']

    # Function to delete "+00:00" from the date
    def correct_date(time):
        if pd.isna(time):
            return time
        else:
            sep = '+'
            stripped = time.split(sep, 1)[0]
            return stripped
    
    # Apply function
    cohort_users_auth['created_at'] = cohort_users_auth['created_at'].apply(correct_date)
    form_entry['created_at'] = form_entry['created_at'].apply(correct_date)

    # Convert to datetime
    cohort_users_auth['datetime_cohort_user_creation'] = pd.to_datetime(cohort_users_auth['created_at'])
    form_entry['datetime_form_entry_creation'] = pd.to_datetime(form_entry['created_at'])

    # Merge form_entry with cohort_users_auth based on user email
    form_entry = pd.merge(form_entry, cohort_users_auth, on='email', how='left')

    # Rename "created_at" columns to identify the source
    form_entry = form_entry.rename(columns={'created_at_x':'form_created_at', 'created_at_y':'cohort_user_created_at'})

    # Function to identify students who joined a cohort after the form creation
    def identify_cohort_users(row):
        cohort_user_creation = row['datetime_cohort_user_creation']
        form_entry_creation = row['datetime_form_entry_creation']

        if (pd.notnull(cohort_user_creation)) and (cohort_user_creation > form_entry_creation):
            return 1
        else:
            return 0
    
    # Apply function
    form_entry['in_cohort_user'] = form_entry.apply(identify_cohort_users, axis=1)

    # Delete cases of people who have the form several times for the same course (leave only the most recent)
    form_entry = form_entry.drop_duplicates(subset=['email', 'course', 'language'], keep='last')

    return form_entry