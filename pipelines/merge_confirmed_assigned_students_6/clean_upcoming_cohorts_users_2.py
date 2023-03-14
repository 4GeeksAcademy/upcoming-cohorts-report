import numpy as np 
import pandas as pd 


##### Values for inputs #####
id_ = [1, 1, 2, 3, 3]
slug = ['cohort_1', 'cohort_1', 'cohort_2', 'cohort_3', 'cohort_3']
name = ['Cohort_1', 'Cohort_1', 'Cohort_2', 'Cohort_3', 'Cohort_3']
stage = ['INACTIVE', 'INACTIVE', 'INACTIVE', 'INACTIVE', 'INACTIVE']
language = ['en', 'en', 'es', 'es', 'es']
academy_id = [11, 11, 22, 33, 33]
academy = ['Academy_1', 'Academy_1', 'Academy_2', 'Academy_3', 'Academy_3']
datetime_kickoff = [pd.to_datetime('2023-06-01 15:00:00'), pd.to_datetime('2023-06-01 15:00:00'), 
                    pd.to_datetime('2023-05-15 15:00:00'), pd.to_datetime('2023-05-01 15:00:00'),
                    pd.to_datetime('2023-05-01 15:00:00')]
email = ['user_1@mail.com', 'user_2@mail.com', np.nan, 'user_3@mail.com', 'user4@mail.com']
location = [np.nan, 'Location_user_2', np.nan, np.nan, np.nan]
deal_id = [1111, np.nan, np.nan, 3333, 4444]
deal_owner = ['Owner_1', np.nan, np.nan, 'Owner_3', 'Owner_4']
form_created_at = ['2023-01-01 15:16:00', np.nan, np.nan, '2023-01-02 15:16:00', '2023-01-03 15:16:00']
assigned = [1, 0, np.nan, 1, 1]
confirmed = [1, 1, np.nan, 0, 1]
educational_status = ['ACTIVE', 'ACTIVE', np.nan, np.nan, 'ACTIVE']
inscription_created_at = ['2023-01-11 15:16:00', '2023-01-12 15:16:00', np.nan, np.nan, '2023-01-15 15:16:00']

dict_inputs = {'id':id_, 'slug':slug, 'name':name, 'stage':stage, 'language':language, 'academy_id':academy_id,
                'academy':academy, 'datetime_kickoff':datetime_kickoff, 'email':email, 'location':location,
                'deal_id':deal_id, 'deal_owner':deal_owner, 'form_created_at':form_created_at, 'assigned':assigned,
                'confirmed':confirmed, 'educational_status':educational_status, 'inscription_created_at':inscription_created_at}

### Expected inputs ###
expected_inputs = pd.DataFrame(dict_inputs)



##### Values for output #####
id_ = [3, 3, 2, 1, 1]
slug = ['cohort_3', 'cohort_3', 'cohort_2', 'cohort_1', 'cohort_1']
name = ['Cohort_3', 'Cohort_3', 'Cohort_2', 'Cohort_1', 'Cohort_1']
stage = ['INACTIVE', 'INACTIVE', 'INACTIVE', 'INACTIVE', 'INACTIVE']
language = ['es', 'es', 'es', 'en', 'en']
academy_id = [33, 33, 22, 11, 11]
academy = ['Academy_3', 'Academy_3', 'Academy_2', 'Academy_1', 'Academy_1']
datetime_kickoff = [pd.to_datetime('2023-05-01 15:00:00'), pd.to_datetime('2023-05-01 15:00:00'), pd.to_datetime('2023-05-15 15:00:00'),
                    pd.to_datetime('2023-06-01 15:00:00'), pd.to_datetime('2023-06-01 15:00:00')]
days_until_kickoff = [(pd.to_datetime('2023-05-01 15:00:00')-pd.Timestamp.now()).days,
                    (pd.to_datetime('2023-05-01 15:00:00')-pd.Timestamp.now()).days,
                    (pd.to_datetime('2023-05-15 15:00:00')-pd.Timestamp.now()).days,
                    (pd.to_datetime('2023-06-01 15:00:00')-pd.Timestamp.now()).days,
                    (pd.to_datetime('2023-06-01 15:00:00')-pd.Timestamp.now()).days]
email = ['user_3@mail.com', 'user4@mail.com', np.nan, 'user_1@mail.com', 'user_2@mail.com']
assigned = [1, 1, np.nan, 1, 0]
location = [np.nan, np.nan, np.nan, np.nan, 'Location_user_2']
ac_deal_link = ['https://4geeks.activehosted.com/app/deals/3333', 'https://4geeks.activehosted.com/app/deals/4444',
                np.nan, 'https://4geeks.activehosted.com/app/deals/1111', np.nan]
deal_owner = ['Owner_3', 'Owner_4', np.nan, 'Owner_1', np.nan]
datetime_form_entry_creation = [pd.to_datetime('2023-01-02 15:16:00'), pd.to_datetime('2023-01-03 15:16:00'),
                pd.to_datetime(np.nan), pd.to_datetime('2023-01-01 15:16:00'), pd.to_datetime(np.nan)]
days_since_form_creation = [(pd.Timestamp.now()-pd.to_datetime('2023-01-02 15:16:00')).days,
                            (pd.Timestamp.now()-pd.to_datetime('2023-01-03 15:16:00')).days, np.nan, 
                            (pd.Timestamp.now()-pd.to_datetime('2023-01-01 15:16:00')).days, np.nan]
unconfirmed = [1, 0, np.nan, 0, 0]
confirmed = [0, 1, np.nan, 1, 1]
educational_status = [np.nan, 'ACTIVE', np.nan, 'ACTIVE', 'ACTIVE']
inscription_created_at = [pd.to_datetime(np.nan), pd.to_datetime('2023-01-15 15:16:00'), pd.to_datetime(np.nan),
                        pd.to_datetime('2023-01-11 15:16:00'), pd.to_datetime('2023-01-12 15:16:00')]
days_since_inscription = [np.nan, (pd.Timestamp.now()-pd.to_datetime('2023-01-15 15:16:00')).days,
                        np.nan, (pd.Timestamp.now()-pd.to_datetime('2023-01-11 15:16:00')).days,
                        (pd.Timestamp.now()-pd.to_datetime('2023-01-12 15:16:00')).days]

dict_output = {'id':id_, 'slug':slug, 'name':name, 'stage':stage, 'language':language, 'academy_id':academy_id,
                'academy':academy, 'datetime_kickoff':datetime_kickoff, 'days_until_kickoff':days_until_kickoff,
                'email':email, 'assigned':assigned, 'location':location, 'ac_deal_link':ac_deal_link, 'deal_owner':deal_owner, 'datetime_form_entry_creation':datetime_form_entry_creation, 
                'days_since_form_creation':days_since_form_creation, 'unconfirmed':unconfirmed, 'confirmed':confirmed, 
                'educational_status':educational_status, 'inscription_created_at':inscription_created_at, 'days_since_inscription':days_since_inscription}

### Expected output ###
expected_output = pd.DataFrame(dict_output)



def run(upcoming_cohorts_users):

    # Define function to delete "+00:00" from dates
    def correct_date(time):
        if pd.isna(time):
             return time
        else:
            sep = '+'
            stripped = time.split(sep, 1)[0]
            return stripped

    # Apply function
    upcoming_cohorts_users['inscription_created_at'] = upcoming_cohorts_users['inscription_created_at'].apply(correct_date)

    # Convert columns to datetime
    upcoming_cohorts_users['datetime_kickoff'] = pd.to_datetime(upcoming_cohorts_users['datetime_kickoff'])
    upcoming_cohorts_users['datetime_form_entry_creation'] = pd.to_datetime(upcoming_cohorts_users['form_created_at'])
    upcoming_cohorts_users['inscription_created_at'] = pd.to_datetime(upcoming_cohorts_users['inscription_created_at'])

    # Create column that calculates the days remaining until the start of the cohort
    upcoming_cohorts_users['days_until_kickoff'] = (upcoming_cohorts_users['datetime_kickoff'] - pd.Timestamp.now()).dt.days

    # Create column that calculates the days since the form was completed/registration was made
    upcoming_cohorts_users['days_since_form_creation'] = (pd.Timestamp.now()- upcoming_cohorts_users['datetime_form_entry_creation']).dt.days
    upcoming_cohorts_users['days_since_inscription'] = (pd.Timestamp.now()- upcoming_cohorts_users['inscription_created_at']).dt.days

    # Create function to obtain link from deal_id
    def create_link(row):
        if pd.isnull(row['deal_id']):
            return np.nan
        else:
            return 'https://4geeks.activehosted.com/app/deals/' + str(int(row['deal_id']))

    # Apply function
    upcoming_cohorts_users['ac_deal_link'] = upcoming_cohorts_users.apply(create_link, axis=1)

    # Create a column whose value is 1 only when a student is assigned but not confirmed in a cohort
    upcoming_cohorts_users.loc[upcoming_cohorts_users['assigned'] == 1, 'unconfirmed'] = 1
    upcoming_cohorts_users.loc[upcoming_cohorts_users['confirmed'] == 1, 'unconfirmed'] = 0

    # Select columns in preferred order
    upcoming_cohorts_users = upcoming_cohorts_users[['id', 'slug', 'name', 'stage', 'language', 'academy_id', 'academy', 'datetime_kickoff', 
                            'days_until_kickoff', 'email', 'assigned', 'location', 'ac_deal_link', 'deal_owner', 'datetime_form_entry_creation', 
                            'days_since_form_creation', 'unconfirmed', 'confirmed', 'educational_status', 'inscription_created_at', 
                            'days_since_inscription']]

    # Drop duplicates
    upcoming_cohorts_users = upcoming_cohorts_users.drop_duplicates(subset=['id', 'email'], keep='last')

    # Sort so that cohorts that start before are shown first
    upcoming_cohorts_users = upcoming_cohorts_users.sort_values(by=['days_until_kickoff'], ascending=True)

    return upcoming_cohorts_users