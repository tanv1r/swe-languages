class AnonymousSurvey():
	"""Collect anonymous answers to survey question."""
	
	def __init__(self, question):
		"""Store a question and prepare to store responses."""
		self.question = question
		self.responses = []
		
	def show_questions(self):
		"""Show the survey question."""
		print(self.question)
	
	def store_response(self, response):
		"""Store one response to the survey question."""
		self.responses.append(response)
		
	def show_results(self):
		"""Show all the responses that have been given."""
		print("Survey results for the question " + "'" + self.question + "': ")
		for response in self.responses:
			print("- " + response)
		
