import numpy as np 
import pandas as pd 

##### Values for inputs #####
in_cohort_user = [1, 0, 0, 0, 0, 0, 0, 0, 0]
deal_status = [np.nan, 'LOST', 'WON', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
ac_expected_cohort = [np.nan, np.nan, np.nan, 'Expected_cohort', np.nan, np.nan, np.nan, np.nan, np.nan]
email = ['email_1@mail.com', 'email_2@mail.com', 'email_3@mail.com', 'email_4@mail.com', 'email_5@4geeksacademy.com',
        'email_6@mail.com', 'email_7@mail.com', 'email_8@mail.com', 'email_9@mail.com']
tags = ['website-lead', 'website-lead', 'utec-uruguay', 'utec-uruguay', 'utec-uruguay',
        'other', 'utec-uruguay', 'contact-us', np.nan]

dict_inputs = {'in_cohort_user':in_cohort_user, 'deal_status':deal_status, 'ac_expected_cohort':ac_expected_cohort,
                'email':email, 'tags':tags}

expected_inputs = pd.DataFrame(dict_inputs)

##### Values for output #####
in_cohort_user = [0, 0]
deal_status = [np.nan, np.nan]
ac_expected_cohort = [np.nan, np.nan]
email = ['email_7@mail.com', 'email_8@mail.com']
tags = ['utec-uruguay', 'contact-us']
lead_type = ['STRONG', 'SOFT']

dict_output = {'in_cohort_user':in_cohort_user, 'deal_status':deal_status, 'ac_expected_cohort':ac_expected_cohort,
                'email':email, 'tags':tags, 'lead_type':lead_type}

expected_output = pd.DataFrame(dict_output)



def run(form_entry):

    # Consider only people who did not enter a cohort after the form entry creation date
    form_entry = form_entry[form_entry['in_cohort_user']==0]

    # The status should not be won or lost
    not_lost_or_won = form_entry[(form_entry['deal_status']!='LOST') & (form_entry['deal_status']!='WON')]

    # Those who do not have an expected cohort are considered unassigned
    unassigned = not_lost_or_won[not_lost_or_won['ac_expected_cohort'].isnull()]

    # Filter to not consider 4geeks emails 
    unassigned = unassigned[unassigned['email'].str.contains('@4geeks') == False]

    # Assign lead_type according to tags
    unassigned.loc[unassigned['tags'] == 'request_more_info', 'lead_type'] = 'SOFT'
    unassigned.loc[unassigned['tags'] == 'contact-us', 'lead_type'] = 'SOFT'
    unassigned.loc[unassigned['tags'] == 'website-lead', 'lead_type'] = 'STRONG'
    unassigned.loc[unassigned['tags'] == 'utec-uruguay', 'lead_type'] = 'STRONG'
    unassigned.loc[unassigned['tags'] == 'jobboard-lead', 'lead_type'] = 'STRONG'
    unassigned.loc[unassigned['tags'] == 'website-lead,blacks-in-technology', 'lead_type'] = 'STRONG'
    
    # Filter by lead type
    unassigned = unassigned[(unassigned['lead_type']=='STRONG') | (unassigned['lead_type']=='SOFT')]

    return unassigned