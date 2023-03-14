import numpy as np 
import pandas as pd 

##### Values for inputs #####

# cohorts
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

dict_cohorts = {'id':id_, 'slug':slug, 'name':name, 'kickoff_date':kickoff_date, 'ending_date':ending_date,
                'stage':stage, 'language':language, 'created_at':created_at, 'updated_at':updated_at,
                'academy_id':academy_id, 'never_ends':never_ends}

# academies_alias
slug = ['a', 'b', 'c', 'd', 'e', 'f']
academy_id = [1, 3, 2, 1, 1, 2]
name = ['Academy_1', 'Academy_3', 'Academy_2', 'Academy_1', 'Academy_1', 'Academy_2']
status = ['ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE']

dict_academies_alias = {'slug':slug, 'academy_id':academy_id, 'name':name, 'status':status}

### Expected inputs ###
expected_inputs = [pd.DataFrame(dict_cohorts), pd.DataFrame(dict_academies_alias)]


##### Values for output #####

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

dict_output = {'id':id_, 'slug':slug, 'name':name, 'kickoff_date':kickoff_date, 'ending_date':ending_date,
                'stage':stage, 'language':language, 'created_at':created_at, 'updated_at':updated_at,
                'academy_id':academy_id, 'never_ends':never_ends, 'academy':academy}

### Expected output ###
expected_output = pd.DataFrame(dict_output)


def run(cohorts, academies_alias):

    # Rename column from academies_alias
    academies_alias = academies_alias.rename(columns={'name':'academy'})
    
    # Remove unnecessary columns 
    academies_alias = academies_alias.drop(columns=['slug', 'status'])
    
    # Remove duplicates, so there is only one row for each academy
    academies_alias = academies_alias.drop_duplicates()

    # Merge both dataframes so now cohorts has the academy name
    cohorts = cohorts.merge(academies_alias, how='left', on='academy_id')

    return cohorts