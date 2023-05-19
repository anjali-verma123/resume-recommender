# resume-recommender
Resume Recommender system using Machine Learning

**Introduction**

Company firms and recruitment organizations method several resumes each day. Going through the resumes of these human beings manually is time-consuming.
In the present system the candidate has to fill each and every information regarding their resume in a manual form which takes large amount of time and then also the candidates, are not satisfied
by the job which the present system prefers according to their skills. The present resume scanning systems without machine learning are not much flexible, inefficient
and not time saving.
To overcome the problem this project will,
1. saves the time of the candidate by providing suggested jobs on the basis of only skills
2. provided by the candidate.
3. help in getting the job in that company which really appreciates candidates skill and ability.
4. replace slow and expensive human processing of resumes with extremely fast and cost-effective.

**Objectives**
1. To develop HR analytics job recommender system using
machine learning system.
2. To analyse the resume of student and comparing it with
company’s requirements.
3. To select possible candidates for right job.

**Methodology**

HR Analytics, is the tool for HR to suggest the top 'n' jobs from the dataset based on the skills of the person. There are two versions of this tool. Pyresparser is used for
extracting the skills from the resume.
In the first version, candidate will manually provide the skills as input, and list of suggested jobs are rendered.
In the second version, pyresparser is used for extracting the skills from the resume in .pdf format. Cosine-similarity algorithm is used, for matching the job description
with the skills.
At last both the version is deployed using Flask and rendered using simple html templates. CSS is added for designing the website.
The dataset is created via scrapping of the Glassdoor website, and jobs are extracted. The predefined dataset contains only IT, ML, AI, & Data Science, related jobs, hence
the machine learning algorithm will only suggest IT related jobs.

**Modules Used**

1. K Nearest Neighbour - is a simple algorithm that stores all the available cases and classifies the new data based on a similarity measure. Mostly used to classifies a data
point based on how its neighbors are classified.
2. Pyresparser - A simple resume parser used for extracting information from resumes.
3. Cosine-Similarity - is a measure of similarity between two sequences of numbers.
4. CountVectorizer – A tool, used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text.


**References**

1. https://youtu.be/X83cDfwtFpw
2. https://github.com/pik1989/HRAnalytics-Project
3. https://www.researchgate.net/publication/361772014_RESUME_PARSER
4. https://core.ac.uk/download/pdf/55305289.pdf
5. https://www.researchgate.net/publication/340700219_A_Machine_Learning_approach_for_automation_of_Resume_Recommendation_system
6. https://www.analyticsvidhya.com/blog/2021/06/resume-screening-with-natural-language-processing-in-python/ -- Resume Screening with Natural Language Processing in Python using dataset
7. https://randerson112358.medium.com/resume-scanner-2c30f5baf92c
8. https://oindrilasen.com/2021/05/build-resume-scanner-using-python-nlp/
9. https://github.com/Vignesh0404/Resume-Scanner
