# Contents

- model.py: Collection of models and parameters to use on imputed data:
	- running instructions: 
	```
	python model.py /home/egwebber/ML-Programing-Assignments/PA-02/Output/conditional_transformed.csv
	```
	- the models used in each run can be changed by manually altering the list in main()
	- The recall threshold K can be by changed manually in the function magic_loop()
	- The magic_loop() function is set to pick the top ten models with the highest precision at the given level of K, and these are reported in Output/Final_table.txt.
		- Either 'precision' or 'auc' can be used as the preferred metric, this can be done in magic_loop() line 81

- Output
	- Collection of logs and results
	- Images: 
		- Precision and Recall curvers for various classifiers