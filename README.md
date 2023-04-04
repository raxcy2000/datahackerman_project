# Datahackerman Project

GOAL: Query and extract information from Game of Thrones API.

- Note:
    - use version control and virtual environments. 
    - create a requirements file.
    - End result should be scripts (suitably commented) written in Python 3.
 
Data needed is in "data" folder with 3 files: `csv_file.csv`, `json_file.json`, and `txt_file.txt`

The Project is divided into 4 parts:

Part 1 - **_API Access_**

This project will involve querying an API and extracting information from it. The API in question provides information on Game of Thrones, allowing one to access information on the houses, characters and books.

* API URL: http://anapioficeandfire.com/api/{SECTION}/{INDEX}

Where **SECTION** can be either 'books', 'characters', or 'houses' and **INDEX** is an integer to a certain entry in a section.

For example, to access the character Peter Baelish, the full request would be http://anapioficeandfire.com/api/characters/823, where 823 is the index corresponding to that character. 
It's recommended to read the full documentation, which can be found here: https://anapioficeandfire.com/Documentation

- We would like you to answer the following:
    - a) What index corresponds to the house "House Breakstone"?
    - b) How many males, females and unknown genders are there in the first 40 characters? Note, index 0 does not correspond to a character, so full range is 1 - 40 both ends inclusive. 
    - c) How many books can be accessed from this API?
    - d) How many books does the character 'High Septon' appear in? (ignoring 'povcharacters') 
