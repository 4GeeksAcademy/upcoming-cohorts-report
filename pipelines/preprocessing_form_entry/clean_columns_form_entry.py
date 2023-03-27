import numpy as np
import pandas as pd 

# Values for inputs

first_name = ['First_1', 'First_2', 'First_3', 'First_4']
last_name = ['Last_1', 'Last_2', 'Last_3', 'Last_4']
email = ['email_1@mail.com', 'email_2@mail.com', 'email_3@mail.com', 'email_4@mail.com']
course = ['full-stack-ft', 'software-engineering', 'machine-learning', 'datascience-ml']
language = ['us', 'en', 'en', 'es']
location = [np.nan, 'Location_from_1', 'Wrong_academy', 'Location_from_2']
form_created_at = ['2023-03-01 21:00:00', '2023-01-11 11:00:00', '2020-03-01 21:00:00', '2023-02-01 22:00:00']
updated_at = ['2023-03-01 21:00:00+00:00', '2023-01-11 11:00:00+00:00', '2020-03-02 21:00:00+00:00', '2023-02-01 22:00:00+00:00']
academy_id = [np.nan, 11, 66, 33]
ac_expected_cohort_date = ['2023-06-01 12:00:00+00:00', '2023-07-01 12:00:00+00:00', '2023-08-01 12:00:00+00:00', '2023-09-01 12:00:00+00:00']
datetime_form_entry_creation = ['2023-03-01 21:00:00', '2023-01-11 11:00:00', '2020-03-01 21:00:00', '2023-02-01 22:00:00']
role = ['teacher', 'STUDENT', 'student', np.nan]
cohort_user_created_at = ['2023-02-21 21:06:31.519727', '2023-02-19 23:06:31.519727', '2023-02-23 19:06:31.519727', np.nan]
cohort_id = [2, 1, 4, np.nan]
in_cohort_user = [0, 1, 0, 0]

# Inputs dict
dict_inputs = {'first_name':first_name, 'last_name':last_name, 'email':email, 'course':course,
                    'language':language, 'location':location, 'form_created_at':form_created_at, 'updated_at':updated_at,
                    'academy_id':academy_id, 'ac_expected_cohort_date':ac_expected_cohort_date, 'datetime_form_entry_creation':datetime_form_entry_creation,
                    'role':role, 'cohort_user_created_at':cohort_user_created_at, 'cohort_id':cohort_id, 
                    'in_cohort_user':in_cohort_user}

# Expected inputs
expected_inputs = pd.DataFrame.from_dict(dict_inputs)



# Values for output

first_name = ['First_1', 'First_2', 'First_3', 'First_4']
last_name = ['Last_1', 'Last_2', 'Last_3', 'Last_4']
email = ['email_1@mail.com', 'email_2@mail.com', 'email_3@mail.com', 'email_4@mail.com']
course = ['full-stack', 'full-stack', 'machine-learning-engineering', 'machine-learning-engineering']
language = ['en', 'en', 'en', 'es']
location = [np.nan, 'Location_from_1', 'Wrong_academy', 'Location_from_2']
form_created_at = ['2023-03-01 21:00:00', '2023-01-11 11:00:00', '2020-03-01 21:00:00', '2023-02-01 22:00:00']
updated_at = ['2023-03-01 21:00:00', '2023-01-11 11:00:00', '2020-03-02 21:00:00', '2023-02-01 22:00:00']
academy_id = [np.nan, 11, 66, 33]
ac_expected_cohort_date = ['2023-06-01 12:00:00', '2023-07-01 12:00:00', '2023-08-01 12:00:00', '2023-09-01 12:00:00']
datetime_form_entry_creation = ['2023-03-01 21:00:00', '2023-01-11 11:00:00', '2020-03-01 21:00:00', '2023-02-01 22:00:00']
role = ['teacher', 'STUDENT', 'student', np.nan]
cohort_user_created_at = ['2023-02-21 21:06:31.519727', '2023-02-19 23:06:31.519727', '2023-02-23 19:06:31.519727', np.nan]
cohort_id = [2, 1, 4, np.nan]
in_cohort_user = [0, 1, 0, 0]
fullname = ['First_1 Last_1', 'First_2 Last_2', 'First_3 Last_3', 'First_4 Last_4']

# Output dict
dict_output = {'first_name':first_name, 'last_name':last_name, 'email':email, 'course':course,
                    'language':language, 'location':location, 'form_created_at':form_created_at, 'updated_at':updated_at,
                    'academy_id':academy_id, 'ac_expected_cohort_date':ac_expected_cohort_date, 'datetime_form_entry_creation':datetime_form_entry_creation,
                    'role':role, 'cohort_user_created_at':cohort_user_created_at, 'cohort_id':cohort_id, 
                    'in_cohort_user':in_cohort_user, 'fullname':fullname}

# Expected output
expected_output = pd.DataFrame(dict_output)


def run(form_entry):

    # Group courses under a single name per program
    form_entry['course'] = form_entry['course'].replace(['full-stack-ft', 'software-engineering',
                                         'coding-introduction', 'outcomes', 'Full Stack'], 'full-stack')
    form_entry['course'] = form_entry['course'].replace(['machine-learning', 'machine-learning-enginnering', 'datascience-ml', 'datascience'], 
                                        'machine-learning-engineering')

    # Create full name column
    form_entry['fullname'] = form_entry['first_name'].fillna('') + str(' ') + form_entry['last_name'].fillna('')

    # Consider 'us' as 'en' in language
    form_entry['language'] = form_entry['language'].replace('us', 'en')

    # Function to delete "+00:00" from the date
    def correct_date(time):
        if pd.isna(time):
             return time
        else:
            sep = '+'
            stripped = time.split(sep, 1)[0]
            return stripped

    # Apply function
    form_entry['updated_at'] = form_entry['updated_at'].apply(correct_date)
    form_entry['ac_expected_cohort_date'] = form_entry['ac_expected_cohort_date'].apply(correct_date)

    return form_entry