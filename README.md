# Welcome to my CS 5001 Project: Data Analysis of COVID-19

## Project Design:

Premise:
1. Ever since the start of pandemic, numbers and numbers everywhere. Want to know what they really mean? How are they calculated?
2. NEWS: All they ever do is spread fear: always reporting # of cases, deaths but no mention of recovery
    - **Number of cases is not the biggest concern, overwhelming health care facilities is the biggest concern**

Three Stage Project:
- **For presentation in CS5001 for December 14 and 16, will be working on Part 1**

1. Recreating British Columbia COVID-19 model and analyzing any correlation with confounding factors such as:
    - demographics (age, gender, residence) : main focus for projects
    - income : datasets were missing values, poor quality
    - hospitalization rate : datasets were missing values, poor quality

- If successful, plan to move to Part 2 and Part 3 *(Potential master's thesis?)*

2. Adding more confounding factors and performing a comparative study with different provinces in Canada
3. Performing a comparative study for COVID-19 response between developed and emerging nations (Maybe the top 10 nations in terms of numbers)

Main purpose of project:
1. Self development. Learn more about python and it's different libraries
2. Play with real datasets and perfrom analysis of data

Targeted audience for project:
1. Geared towards public health agencies managing pandemic response
    - what have we learned from the pandemic
    - preventing pandemics in the future

Process:
1. Data Analysis:
   - read multiple datasets, clean, merge them using Jupyter notebooks. Great that can use it in VSCode.
   - visualizations: charts, makes it easy to understand the data
   - learned so far: pandas, numpy, seaborn, matplot lib
   - *still need to learn how to use fastai*
   - *WANT TO EVENTUALLY CREATE A PREDICTIVE MODEL*

2. Presenting the output:
   - want to present the output in the form of a website made using bootstrap, flask libraries
   - HTML, CSS and Javascript (basic) will be used
   - want to add API with live COVID-19 data around the globe
   - website deployed on the web through heroku (similar to AWS)
   - *also want to upload a merged CSV file of all my cleaned data for future use*

Source of dataset collection:
1. John Hopkins World COVID-19 dataset
2. BC COVID-19 dataset (Last updated on November 23, 2020)
3. COVID-19 healthdata.org

### Latest Problems (November 29, 2020):
- How do I add my charts and plots from Jupyter notebooks to my website?
- what do need to do to make a predictive model, right now have a static data, eventually want something like a pivot table that a user can play with
- since using pandas, a lot of previously written functions are not needed anymore, use different ways to use functions
- want to have an output file, filter data


### Latest Update (Decemeber 2, 2020):
- How do I add my charts and plots from Jupyter notebooks to my website? 
   - Thinking about saving plots as images and uploading them on the website 
- since using pandas, a lot of previously written functions are not needed anymore, use different ways to use functions
   - Write the code for the filter data along with the pandas analysis
   - use the matplot lib for the graphs
   - In the final product will have own code as well as pandas code
- API about live covid data, news feed on the website homepage, write the python code, try/except (defensive coding), csv file
- Can I have something like an HTML form where a user can filter out the data they are interested in?
   - Filtered data, written to file
   - How do I get it to download
- Lastly, upload entire merged data (csv file) on the website that is for future purposes
- GOAL OF PROJECT: Able to use what is learnt in the course CS5001 and start something, not perfect it, **BE REALISTIC**

### Plan for (December 6, 2020):
- Work on the data analysis part: own code and working with pandas
- html forms? filter function when the user asks for some information?

### Latest Update (December 11, 2020):
-Successfully completed the filter function, unable to connect it to HTML
-Successfully build the API
-Have to abort the plan to connect with HTML **for now**
-Resolved the issue of images not showing up
-Only thing left: 
  - filter for datasets so that I do not need pandas
  - experimental: recursion(decision trees), classes
  - make list of course topics covered
  - libraries covered

### Latest Update (December 13, 2020):
-Successfully filtered datasets, do not need pandas
-decision tree using recursion built for CS5002 project
-images still a headache for the presentation: have screenshot and preloaded website
-finally done with the code, only powerpoint slides left

### Experience:
-I have not been able to achieve what I want to but it is a start, a foot in the right direction
**Always remember, it is worth doing things badly at first than not doing it at all since "the fool is the precursor to the master."**

## Winter Break and 2021 Plans
*- What do need to do to make a predictive model, right now have a static data, eventually want something like a pivot table that a user can play with*
   *- sample website: IHME covid-19 website*
   *- Predictive model out of scope right now for the next two weeks, presentation on Decmeber 16*
   *- Plan to learn it over the winter break!*
   *- Carry out the prject over the next year*
   *- Will be able to add the vaccine implementation as well in the future*
   *- Learn about the ML from fast ai*





