import numpy as np 
import pandas as pd 

##### Values for inputs #####

### form_entry ###
first_name = ['First_1', 'First_2', 'First_3', 'First_4', 'First_5',
        'First_6', 'First_7', 'First_8', 'First_9', 'First_10']
last_name = ['Last_1', 'Last_2', 'Last_3', 'Last_4', 'Last_5',
            'Last_6', 'Last_7', 'Last_8', 'Last_9', 'Last_10']
email = ['email_1@mail.com', 'email_2@mail.com', 'email_3@mail.com', 'email_4@mail.com', 'email_5@gmail.com',
            'email_6@mail.com', 'email_7@gmail.com', 'email8@gmail.com', 'email_9@gmail.com', 'email_10@gmail.com']
course = ['full-stack', 'full-stack', 'machine-learning-engineering', 'machine-learning-engineering', np.nan, 
        'full-stack', 'machine-learning-engineering', 'full-stack', 'full-stack', 'machine-learning-engineering']
ac_expected_cohort = ['Already assigned', np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan]
academy_id = [np.nan, 11, 66, np.nan, 66, 
        11, 66, 66, 66, 33]
ac_expected_cohort_date = ['2023-06-01 12:00:00', '2023-07-01 12:00:00', np.nan, '2023-09-01 12:00:00', '2023-02-01 22:00:00',
        '2023-02-01 22:00:00', '2023-02-01 22:00:00', '2023-08-01 21:00:00', '2023-05-01 21:00:00', '2023-04-15 21:00:00']
in_cohort_user = [0, 1, 0, 0, 0, 
        0, 0, 0, 0, 0]

dict_form_entry = {'first_name':first_name, 'last_name':last_name, 'email':email, 'course':course,
                    'ac_expected_cohort':ac_expected_cohort, 'academy_id':academy_id, 'ac_expected_cohort_date':ac_expected_cohort_date, 
                    'in_cohort_user':in_cohort_user}


### upcoming_cohorts ###
slug = ['cohort_4', 'cohort-ml-5', 'cohort-ml-6', 'cohort_7', 'cohort_8']
kickoff_date = ['2023-05-01 21:00:00', '2023-06-01 21:00:00', '2023-05-01 21:00:00', '2023-06-01 21:00:00', '2023-04-21 21:00:00']
academy_id = [3, 33, 33, 66, 33]
datetime_kickoff = ['2023-05-01 21:00:00', '2023-06-01 21:00:00', '2023-05-01 21:00:00', '2023-06-01 21:00:00', '2023-04-21 21:00:00']

dict_upcoming_cohorts = {'slug':slug, 'kickoff_date':kickoff_date, 'academy_id':academy_id, 'datetime_kickoff':datetime_kickoff}


### Expected inputs ###
expected_inputs = [pd.DataFrame(dict_form_entry), pd.DataFrame(dict_upcoming_cohorts)]



##### Values for output #####
first_name = ['First_1', 'First_2', 'First_3', 'First_4', 'First_5',
        'First_6', 'First_7', 'First_8', 'First_9', 'First_10']
last_name = ['Last_1', 'Last_2', 'Last_3', 'Last_4', 'Last_5',
            'Last_6', 'Last_7', 'Last_8', 'Last_9', 'Last_10']
email = ['email_1@mail.com', 'email_2@mail.com', 'email_3@mail.com', 'email_4@mail.com', 'email_5@gmail.com',
            'email_6@mail.com', 'email_7@gmail.com', 'email8@gmail.com', 'email_9@gmail.com', 'email_10@gmail.com']
course = ['full-stack', 'full-stack', 'machine-learning-engineering', 'machine-learning-engineering', np.nan, 
        'full-stack', 'machine-learning-engineering', 'full-stack', 'full-stack', 'machine-learning-engineering']
ac_expected_cohort = ['Already assigned', np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, 'cohort_7', 'cohort-ml-6']
academy_id = [np.nan, 11, 66, np.nan, 66, 
        11, 66, 66, 66, 33]
ac_expected_cohort_date = ['2023-06-01 12:00:00', '2023-07-01 12:00:00', np.nan, '2023-09-01 12:00:00', '2023-02-01 22:00:00',
        '2023-02-01 22:00:00', '2023-02-01 22:00:00', '2023-08-01 21:00:00', '2023-05-01 21:00:00', '2023-04-15 21:00:00']
in_cohort_user = [0, 1, 0, 0, 0, 
        0, 0, 0, 0, 0]
datetime_expected_cohort_date = [pd.to_datetime('2023-06-01 12:00:00'), pd.to_datetime('2023-07-01 12:00:00'), pd.to_datetime(np.nan), pd.to_datetime('2023-09-01 12:00:00'), pd.to_datetime('2023-02-01 22:00:00'),
        pd.to_datetime('2023-02-01 22:00:00'), pd.to_datetime('2023-02-01 22:00:00'), pd.to_datetime('2023-08-01 21:00:00'), pd.to_datetime('2023-05-01 21:00:00'), pd.to_datetime('2023-04-15 21:00:00')]
cohort_assignation_error = [np.nan, np.nan, np.nan, 'Missing academy', 'Missing course',
        'Missing upcoming cohort', 'Missing upcoming cohort', 'Missing upcoming cohort', np.nan, np.nan]

dict_output = {'first_name':first_name, 'last_name':last_name, 'email':email, 'course':course,
                    'ac_expected_cohort':ac_expected_cohort, 'academy_id':academy_id, 'ac_expected_cohort_date':ac_expected_cohort_date,
                    'in_cohort_user':in_cohort_user, 'datetime_expected_cohort_date':datetime_expected_cohort_date, 'cohort_assignation_error':cohort_assignation_error}

### Expected output ###
expected_output = pd.DataFrame(dict_output)



def run(form_entry, upcoming_cohorts):

    """Cohort assignation"""

    # Convert columns to datetime
    form_entry['datetime_expected_cohort_date'] = pd.to_datetime(form_entry['ac_expected_cohort_date'])
    upcoming_cohorts['datetime_kickoff'] = pd.to_datetime(upcoming_cohorts['datetime_kickoff'])

    # Select only necessary columns
    upcoming_cohorts = upcoming_cohorts[['slug', 'academy_id', 'datetime_kickoff']]

    def assign_expected_cohort(row, df=upcoming_cohorts):
        # Function to assign closest cohort in date from the expected start date (ac_expected_cohort_date)

        datetime_expected = row['datetime_expected_cohort_date']
        expected_date = row['ac_expected_cohort_date']
        ac_expected_cohort = row['ac_expected_cohort']
        fe_academy_id = row['academy_id']
        fe_course = row['course']
        in_cohort_user = row['in_cohort_user']

        if (pd.notnull(ac_expected_cohort)) or (in_cohort_user==1):
            # If there is already an expected cohort keep that value
            # If user is already in cohort_users, no need to assign cohort to user
            return ac_expected_cohort
        elif pd.isna(expected_date):
            return np.nan
        elif pd.isna(fe_academy_id):   
            return 'Missing academy'
        elif pd.isna(fe_course):    
            return 'Missing course'
        else:
            # Filter by cohorts that belong to the academy indicated in form_entry
            df_filtered = df[df['academy_id']==int(fe_academy_id)]

            # Provisional criteria to select cohorts of the course that is expected to take
            ######### Use syllabus instead ##########
            if fe_course == 'machine-learning-engineering':
                df_filtered = df_filtered[df_filtered['slug'].str.contains('-ml-')]
            else:
                df_filtered = df_filtered[~df_filtered['slug'].str.contains('-ml-')]  


            datetime_expected = datetime_expected.replace(tzinfo=None)
            # Consider only start dates after the one indicated as expected date
            df_filtered = df_filtered[df_filtered['datetime_kickoff'] >= datetime_expected]
            if df_filtered.empty:
                return 'Missing upcoming cohort'   
            else:
                # Calculate time delta and select the cohort with the least value as expected cohort
                df_filtered['time_diff'] = abs(df_filtered['datetime_kickoff'] - datetime_expected)    
                min_idx = df_filtered['time_diff'].idxmin()
                expected_cohort = df_filtered.loc[min_idx, 'slug']
                return expected_cohort

    # Apply function
    form_entry['date_assigned_cohort'] = form_entry.apply(assign_expected_cohort, axis=1)

    # Define error values
    error_values = ['Missing academy', 'Missing course', 'Missing upcoming cohort', 'Wrong date format']

    # If the function returns an error message, place it in a column dedicated to errors
    form_entry.loc[form_entry['date_assigned_cohort'].isin(error_values), 'cohort_assignation_error'] = form_entry['date_assigned_cohort']

    # If the function does not return an error message, place the returned value as expected cohort
    form_entry.loc[~form_entry['date_assigned_cohort'].isin(error_values), 'ac_expected_cohort'] = form_entry['date_assigned_cohort']

    # Remove auxiliary column
    form_entry = form_entry.drop(columns=['date_assigned_cohort'])

    return form_entry