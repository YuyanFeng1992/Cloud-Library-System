For this homework, you are provided:

1. A basic simple project file structure to 
work from. The static contents of the frontend are provided in the templates.
But, you will need to create the small amount of code for variables and 
expressions in the templates to provide the dynamic content.
2. The database schema and stored proc creation code.
3. The root route code in the Python app. You are to implement two other routes
	that are described in section 1 below.
4. Screen shot of the resulting product.


For the homework, you are to:

0. Review the documentations, including the comments in the code to 
	gain all the spec.
	
1. Create the code for items A - I. They are all specified in the comments in 
	the respective files listed below:
	A - B: in studentAdmin.py
	C - H: in /templates/processRecord.html
	I : in /templates/studentRecords.html
	
2. Create the .wsgi file for this application

3. Create the /etc/apache2/sites-available/studentAdmin.conf with the proper
	configurations, disable the 000_default.config, 
	enable the studentAdmin.conf, and restart the apache server.
	(Use the Amazeriffic app as reference and adapt to your app's name 
	accordingly)
	
4. Use the code in the .sql files in folder sproc to set up the "school" 
	database and schema for this project.  Reminder: the database and tables must be 
	created first before you create the sprocs!

5. Create your dbconfig.txt file
	
6. Test your app:
	localhost:8080
	
	To help with debugging, you may want to test with localhost:5000 first since
	details of error are readily displayed in the console or on the web page. 
	Once debugged, and if you have completed correctly the apache config in 
	steps 2 and 3 above, localhost:8080 should work.
	
7. Please feel free to modify the .css to change the look of your front end 
	if you don't like the look form the baseline project.





	
	