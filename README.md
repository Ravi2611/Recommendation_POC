
# Product Recoomandation

_**ONE STOP SOLUTION FOR ALL YOUR Product Recommandation Solutions**_ 
## Introduction 




_📌 **Data Upload**_ <br/>

This module deals with the data upload. It can take csv and excel files. As soon as the data is uploaded, it creates a copy of the data to ensure that we don't have to read the data multiple times. It also saves the columns and their data types along with displaying them for the user. This is used to upload and save the data and it's column types which will be further needed at a later stage. 

_📌 **Change Metadata**_ <br/>

Once the column types are saved in the metadata, we need to give the user the option to change the type. This is to ensure that the automatic column tagging can be overridden if the user wishes. For example a binary column with 0 and 1s can be tagged as numerical and the user might have to correct it. The three data types available are:

* Numerical 
* Categorical 
* Object

The correction happens immediately and is saved at that moment. 

_📌 **Machine Learning**_ <br/>


_📌 **Data Visualization**_ <br/>

_📌 **Y-Parameter Optimization**_ <br/>

## Technology Stack 

1. Python 
2. Streamlit 
3. Pandas
4. Scikit-Learn
5. Seaborn

# How to Run 

- Clone the repository
- Setup Virtual environment
```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
- Run Streamlit
```
$ streamlit run app.py
```
