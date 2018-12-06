# ARNEKT-NER-TASK


# This read me file details how to prepare the submission file for IECSIL - 2018 tasks.

## The base line model created using Term Document Matrix as a representation method and Multinomial Naive Bayes as a classifier

## download the data

#### run sh download_files.sh for downloading the training and test corpus

###### sh download_files.sh
#####Used C-DAC pos taggers
## Make Submission File

#### run python code/get_submission.py for creating submission files

##### change the "lang_code" parameter in "get_submission.py" for switching the language

#Trained models were already attached in code foleder.
#No need to train models again.
#Just change the language code and test set number for results and execute get_submission.py in python3
