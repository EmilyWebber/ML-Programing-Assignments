# ML-Programming-Assignments
Repository for Machine Learning 01

Output
	- gender_transformed.csv
		- The csv with missing gender values gathered from genderize.io
	- mean_transformed.csv
		- The csv with missing Age, GPA, Days_Missing fields imputed as attribute mean
	- conditional_transformed.csv
		- The csv with missing Age, GPA, Days_Missing fields imputed as attribute mean conditional on class: Graduation
	- student_summaries.txt
		- summary statistics

Images
	- Histograms for Age, Days_Missing, Gender, GPA, Graduated, and State

summary.py
	- generates summary statistics

transform_gender.py
	- gets gender from genderize.io and adds a new csv

transform_means.py
	- hard-coded means and conditional means from summary statistics
	- adds two new csvs