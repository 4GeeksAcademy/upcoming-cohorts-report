import numpy as np 
import pandas as pd 

##### Values for inputs #####

id_ = [111, 222, 333, 444]
slug = ['cohort_1', 'cohort_2', 'cohort_3', 'cohort_4']
name = ['Cohort 1', 'Cohort 2', 'Cohort_3', 'Cohort_4']
kickoff_date = ['2023-02-01 21:00:00+00:00', '2023-04-01 21:00:00+00:00', '2023-04-01 21:00:00+00:00', '2023-05-01 21:00:00+00:00']
ending_date = ['2024-02-01 21:00:00+00:00', '2024-04-01 21:00:00+00:00', '2024-04-01 21:00:00+00:00', '2024-05-01 21:00:00+00:00']
stage = ['INACTIVE', 'INACTIVE', 'DELETED', 'INACTIVE']
language = ['en', 'en', 'es', 'es']
created_at = ['2022-02-01 21:00:00+00:00', '2022-04-01 21:00:00+00:00', '2022-04-01 21:00:00+00:00', '2022-05-01 21:00:00+00:00']
updated_at = ['2022-02-01 21:00:00+00:00', '2022-04-01 21:00:00+00:00', '2022-04-01 21:00:00+00:00', '2022-05-01 21:00:00+00:00']
academy_id = [1, 2, 1, 3]
never_ends = [False, True, False, False]
academy = ['Academy_1', 'Academy_2', 'Academy_1', 'Academy_3']

dict_inputs = {'id':id_, 'slug':slug, 'name':name, 'kickoff_date':kickoff_date, 'ending_date':ending_date,
                'stage':stage, 'language':language, 'created_at':created_at, 'updated_at':updated_at,
                'academy_id':academy_id, 'never_ends':never_ends, 'academy':academy}

### Expected inputs ###
expected_inputs = pd.DataFrame(dict_inputs)


##### Values for output #####

id_ = [444]
slug = ['cohort_4']
name = ['Cohort_4']
kickoff_date = ['2023-05-01 21:00:00']
ending_date = ['2024-05-01 21:00:00']
stage = ['INACTIVE']
language = ['es']
created_at = ['2022-05-01 21:00:00']
updated_at = ['2022-05-01 21:00:00']
academy_id = [3]
never_ends = [False]
academy = ['Academy_3']
datetime_kickoff = [pd.to_datetime('2023-05-01 21:00:00')]

dict_output = {'id':id_, 'slug':slug, 'name':name, 'kickoff_date':kickoff_date, 'ending_date':ending_date,
                'stage':stage, 'language':language, 'created_at':created_at, 'updated_at':updated_at,
                'academy_id':academy_id, 'never_ends':never_ends, 'academy':academy, 'datetime_kickoff':datetime_kickoff}

### Expected output ###
expected_output = pd.DataFrame(dict_output)

def run(cohorts):

    # Function to delete "+00:00" from the date
    def correct_date(time):
        if pd.isna(time):
            return time
        else:
            sep = '+'
            stripped = time.split(sep, 1)[0]
            return stripped

    # Apply function
    cohorts['kickoff_date'] = cohorts['kickoff_date'].apply(correct_date)
    cohorts['ending_date'] = cohorts['ending_date'].apply(correct_date)
    cohorts['created_at'] = cohorts['created_at'].apply(correct_date)
    cohorts['updated_at'] = cohorts['updated_at'].apply(correct_date)

    # Create column for kickoff date in datetime
    cohorts['datetime_kickoff'] = pd.to_datetime(cohorts['kickoff_date'])

    # Define current time
    current_time = pd.Timestamp.now()

    # Consider only the cohorts whose kickoff datetime is greater than the current one
    upcoming_cohorts = cohorts[cohorts['datetime_kickoff']>current_time]

    # Consider only the cohorts that end and are not deleted
    upcoming_cohorts = upcoming_cohorts[upcoming_cohorts['never_ends']==False]
    upcoming_cohorts = upcoming_cohorts[(upcoming_cohorts['stage']!='DELETED')]

    return upcoming_cohorts