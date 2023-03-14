import numpy as np 
import pandas as pd 

##### Values for inputs #####

# form_entry
email = ['user_1@mail.com', 'user_2@mail.com', 'user_3@mail.com']
academy_id = [1, np.nan, 3]

dict_form_entry = {'email':email, 'academy_id':academy_id}

# academies_alias
slug = ['a', 'b', 'c', 'd', 'e', 'f']
academy_id = [1, 3, 2, 1, 1, 2]
name = ['Academy_1', 'Academy_3', 'Academy_2', 'Academy_1', 'Academy_1', 'Academy_2']
status = ['ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE']

dict_academies_alias = {'slug':slug, 'academy_id':academy_id, 'name':name, 'status':status}

### Expected inputs ###
expected_inputs = [pd.DataFrame(dict_form_entry), pd.DataFrame(dict_academies_alias)]


##### Values for output #####
email = ['user_1@mail.com', 'user_2@mail.com', 'user_3@mail.com']
academy_id = [1, np.nan, 3]
academy = ['Academy_1', np.nan, 'Academy_3']

dict_output = {'email':email, 'academy_id':academy_id, 'academy':academy}

### Expected output ###
expected_output = pd.DataFrame(dict_output)


def run(form_entry, academies_alias):

    # Rename column from academies_alias
    academies_alias = academies_alias.rename(columns={'name':'academy'})
    
    # Remove unnecessary columns 
    academies_alias = academies_alias.drop(columns=['slug', 'status'])
    
    # Remove duplicates, so there is only one row for each academy
    academies_alias = academies_alias.drop_duplicates()

    # Merge both dataframes so now form_entry has the academy name
    form_entry = form_entry.merge(academies_alias, how='left', on='academy_id')

    return form_entry