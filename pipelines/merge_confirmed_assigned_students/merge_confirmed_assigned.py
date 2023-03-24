import numpy as np 
import pandas as pd 

##### Values for inputs #####

### form_entry ###
email = ['email_1@mail.com', 'email_2@mail.com', 'email_3@mail.com', 'email_4@mail.com']
ac_expected_cohort = ['cohort_1', np.nan, 'cohort_2', 'cohort_1']
updated_at = ['2023-01-01 15:16:00', '2023-01-02 15:16:00', '2023-01-03 15:16:00', '2023-01-04 15:16:00']
location = ['location_1', 'location_2', np.nan, np.nan]
ac_deal_id = [1111, 2222, 3333, 4444]
ac_deal_owner_full_name = ['Owner_1', np.nan, np.nan, 'Owner_4']
form_created_at = ['2023-01-01 15:16:00', '2023-01-02 15:16:00', '2023-01-03 15:16:00', '2023-01-04 15:16:00']

dict_form_entry = {'email':email, 'ac_expected_cohort':ac_expected_cohort, 'updated_at':updated_at,
                    'location':location, 'ac_deal_id':ac_deal_id, 'ac_deal_owner_full_name':ac_deal_owner_full_name,
                    'form_created_at':form_created_at}

### confirmed ###
email = ['email_1@mail.com', 'email_5@mail.com', 'email_6@mail.com']
slug = ['cohort_1', 'cohort_5', 'cohort_6']
updated_at = ['2023-02-01 20:30:00', '2023-02-05 20:30:00', '2020-11-11 20:30:00']
educational_status = ['status_1', 'status_5', 'status_6']
created_at = ['2023-02-01 20:30:00', '2023-02-05 20:30:00', '2020-11-11 20:30:00']

dict_confirmed = {'email':email, 'slug':slug, 'updated_at':updated_at, 'educational_status':educational_status,
                'created_at':created_at}

### upcoming_cohorts ###
slug = ['cohort_1', 'cohort_2', 'cohort_3', 'cohort_4', 'cohort_5']

dict_upcoming_cohorts = {'slug':slug}

### Expected inputs ###
expected_inputs = [pd.DataFrame(dict_form_entry), pd.DataFrame(dict_confirmed), pd.DataFrame(dict_upcoming_cohorts)]


##### Values for output ####
slug = ['cohort_1', 'cohort_1', 'cohort_2', 'cohort_3', 'cohort_4', 'cohort_5']
email = ['email_1@mail.com', 'email_4@mail.com', 'email_3@mail.com', np.nan, np.nan, 'email_5@mail.com']
assigned = [1, 1, 1, np.nan, np.nan, 0]
confirmed = [1, 0, 0, np.nan, np.nan, 1]
location = ['location_1', np.nan, np.nan, np.nan, np.nan, np.nan]
deal_id = [1111, 4444, 3333, np.nan, np.nan, np.nan]
deal_owner = ['Owner_1', 'Owner_4', np.nan, np.nan, np.nan, np.nan]
form_created_at = ['2023-01-01 15:16:00', '2023-01-04 15:16:00', '2023-01-03 15:16:00', np.nan, np.nan, np.nan]
educational_status = ['status_1', np.nan, np.nan, np.nan, np.nan, 'status_5']
inscription_created_at = ['2023-02-01 20:30:00', np.nan, np.nan, np.nan, np.nan, '2023-02-05 20:30:00']

dict_output = {'slug':slug, 'email':email, 'assigned':assigned, 'confirmed':confirmed, 'location':location,
                'deal_id':deal_id, 'deal_owner':deal_owner, 'form_created_at':form_created_at, 'educational_status':educational_status, 'inscription_created_at':inscription_created_at}

### Expected output ###
expected_output = pd.DataFrame(dict_output)



def run(form_entry, confirmed, upcoming_cohorts):

    # Create auxiliary dataframe with the email of each assigned student and their expected cohort
    assigned = form_entry.loc[form_entry['ac_expected_cohort'].notnull()]
    assigned_short = assigned[['ac_expected_cohort', 'email']].rename(columns={'ac_expected_cohort': 'slug'})
    # Since these are assigned students, create a column that identifies them as such 
    assigned_short['assigned'] = 1
    # Also create a column for confirmed, since they will later be concatenated
    assigned_short['confirmed'] = 0

    # Create auxiliary dataframe with the email of each confirmed student and their cohort
    confirmed_short = confirmed[['slug', 'email']]
    # Create a column for assigned, since they will later be concatenated
    confirmed_short['assigned'] = 0
    # Since these are confirmed students, create a column that identifies them as such 
    confirmed_short['confirmed'] = 1

    # Concatenate both auxiliary dataframes, in order to have all students associated with upcoming cohorts identified as assigned or confirmed
    concatenated_df = pd.concat([confirmed_short, assigned_short])
    confirmed_and_assigned = concatenated_df.groupby(['slug', 'email']).sum().reset_index()

    # Merge the auxiliary dataframe with the complete one, to add more information about the assigned students
    assigned = pd.merge(assigned_short, assigned, left_on=['slug', 'email'], right_on=['ac_expected_cohort', 'email'])
    assigned['datetime_update'] = pd.to_datetime(assigned['updated_at'])
    grouped_assigned = assigned.groupby(['slug', 'email']).agg({'datetime_update': 'max', 'location': 'last', 'ac_deal_id':'last', 'ac_deal_owner_full_name':'last', 'form_created_at': 'last'})
    grouped_assigned = grouped_assigned.reset_index()
    confirmed_and_assigned = confirmed_and_assigned.merge(grouped_assigned, on='email', how='left').drop(columns=['slug_y', 'datetime_update'])
    confirmed_and_assigned = confirmed_and_assigned.rename(columns={'slug_x':'slug', 'ac_deal_id':'deal_id', 'ac_deal_owner_full_name':'deal_owner'})

    # Merge the auxiliary dataframe with the complete one, to add more information about the confirmed students
    confirmed = pd.merge(confirmed_short, confirmed, on=['slug', 'email'])
    confirmed['datetime_update'] = pd.to_datetime(confirmed['updated_at'])
    grouped_confirmed = confirmed.groupby(['slug', 'email']).agg({'datetime_update': 'max', 'educational_status': 'last', 'created_at': 'last'})
    grouped_confirmed = grouped_confirmed.reset_index()
    confirmed_and_assigned = confirmed_and_assigned.merge(grouped_confirmed, on='email', how='left').drop(columns=['datetime_update'])
    confirmed_and_assigned = confirmed_and_assigned.rename(columns={'slug_x':'slug', 'created_at':'inscription_created_at'}).drop(columns=['slug_y'])

    # Merge the above information with upcoming cohorts, so that each row corresponds to a student from an upcoming cohort
    upcoming_cohorts_users = upcoming_cohorts.merge(confirmed_and_assigned, on='slug', how='left')
    upcoming_cohorts_users = upcoming_cohorts_users.fillna(value=np.nan)

    return upcoming_cohorts_users