Project name: Omr sheet reader
first run this cmd 
poetry install 
poetry update
uvicorn response.api:app --reload
for store the cordinate in the file name {omr_data.json}

then run the cordinate_helper file by this cmd

after this add the question_no and option on the omr_data.json file

poetry run ./cordinate_helper.py

then run the main.py file for find the marking ans by this cmd 

poetry run ./main.py


workflow :

first find the cordinates of all options(circle)
this can download the img in cord_img with pageno
edit the omr_data.json according to the needed cordinates and add question_no and options
then using this data of cordinates and questions we can read the any omr 
