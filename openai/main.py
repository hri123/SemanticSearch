import os
from embedchain import Pipeline as App

# os.environ["OPENAI_API_KEY"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# load llm configuration from opensource.yaml file
# app = App.from_config(yaml_path="opensource.yaml")
app = App.from_config(yaml_path="openai.yaml")
# app = App()
app.config.collect_metrics = False

# Add different data sources
# app.add("https://en.wikipedia.org/wiki/Elon_Musk")
# app.add("https://www.forbes.com/profile/elon-musk")
# app.add("https://www.youtube.com/watch?v=RcYjXbSJBN8")
# You can also add local data sources such as pdf, csv files etc.
# app.add("/path/to/file.pdf")
# app.add("/Users/hrishikesh/Downloads/EXAMREVIEW-AWSCertifiedSolutionArchitectAssociate.pdf", data_type='pdf_file')
# app.add("/Users/hrishikesh/Downloads/Kubernetes-Patterns-2nd-Edition.pdf", data_type='pdf_file')
# app.add('https://arxiv.org/pdf/1706.03762.pdf', data_type='pdf_file')
app.add("/Users/hrishikesh/C/SandBoxes/AWS-SAA-C03/AWS Certified Solutions Architect Slides v26 My Notes.pdf", data_type='pdf_file')


# print(app.get_data_sources())

# response = app.query("What is the net worth of Elon Musk today?")
# print(response)
# Answer: The net worth of Elon Musk today is $258.7 billion.

# All set. Now start asking questions related to your data
while (True):
  question = input("Enter question: ")
  if question in ['q', 'exit', 'quit']:
    break
  answer = app.query(question)
  print(answer)
  # answer = app.search(question)
  # print(answer)
  # answer = app.chat(question)
  # print(answer)
  
