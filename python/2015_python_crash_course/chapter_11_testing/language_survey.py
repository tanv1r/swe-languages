from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#Show question and store responses to the survey.
my_survey.show_questions()
print("Enter 'q' to quit.")

while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)

#Show the survey results.
print("Thanks for participating in the survey.")
my_survey.show_results()
