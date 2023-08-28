#importations 
import numpy as np
import pandas as pd
import pickle


#loading the model

with open('models/model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Creating features

def get_name_length(name):
    name = str(name)
    return len(name)

def get_first_letter(name):
    name = str(name)
    return name[0]

def get_last_letter(name):
    name = str(name)
    return name[-1]

def get_number_of_occurs(letter,name):
    return name.count(letter)

# processing function

def process(text):
  # extracting the first name
  name_parts = text.split()

  if len(name_parts) > 0:
    first_name = name_parts[0]
  else:
    first_name = text

  # create an empty dataframe with a column with the name "Name"
  Dataset = pd.DataFrame(columns=['Name'])
  
  # Add a row with 'Name' = 'Mohamed'
  Dataset.loc[0] = first_name
  
  # Define your list of column names
  column_names = ['name length', 'first letter', 'last letter']  # Modify this with your own column names

  # Add empty columns to the DataFrame
  for column_name in column_names:
    Dataset[column_name] = "A"

  arabic_alphabets = [
    'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض',
    'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي', 'آ', 'ء',
    'أ','آ', 'إ', 'ئ']
  dict_letters_rank = {}
  for i in range(len(arabic_alphabets)):
    dict_letters_rank.update({arabic_alphabets[i] : i+1})

  dict_letters_rank.update({'ة' : 4 ,'ى' : 1})
  for column_name in arabic_alphabets:
    Dataset[column_name] = None
  # Extract features
  for i in range(len(Dataset)):
    Dataset.loc[i, 'name length'] = get_name_length(Dataset.loc[i, 'Name'])
    Dataset.loc[i, 'first letter'] = dict_letters_rank[get_first_letter(Dataset.loc[i, 'Name'])]
    Dataset.loc[i, 'last letter'] =  dict_letters_rank[get_last_letter(Dataset.loc[i, 'Name'])]
    for j in arabic_alphabets :
      Dataset.loc[i,j] = get_number_of_occurs(j,Dataset.loc[i, 'Name'])
  return Dataset.drop('Name',axis = 1)

#predicting function

def predict(model,data):
  probabilites = model.predict_proba(data)
  max_probability = probabilites.max()
  if max_probability >= 0.65 :
    max_index = np.argmax(probabilites)
    if max_index == 0 :
      label ='female'
    else :
      label='male'
  else :
    label='indefined'
  return label

def predict_pipeline(data):
    processed_data = process(data)
    return predict(loaded_model,processed_data)
  
