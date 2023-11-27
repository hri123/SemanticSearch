import openai
import time

from openai import OpenAI
client = OpenAI()

# Upload a file with an "assistants" purpose
file = client.files.create(
  file=open("/Users/hrishikesh/C/SandBoxes/AWS-SAA-C03/AWS Certified Solutions Architect Slides v26 My Notes.pdf", "rb"),
  purpose='assistants'
)

# Add the file to the assistant
assistant = client.beta.assistants.create(
  instructions="You are a customer support chatbot. Use your knowledge base to best respond to customer queries.",
  model="gpt-4-1106-preview",
  tools=[{"type": "retrieval"}],
  file_ids=[file.id]
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="what is the difference between NAT Gateway and NAT instance.",
  file_ids=[file.id]
)


run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id
)
print(run)

def poll_run(run, thread):
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id, run_id=run.id,
        )
        time.sleep(0.5)
    return run

# waiting for the run to be completed
run = poll_run(run, thread)

messages = client.beta.threads.messages.list (thread_id=thread. id)
for m in messages:
    print(f"{m.role}: {m.content[0].text.value}")

file_deletion_status = client.beta.assistants.files.delete(
  assistant_id=assistant.id,
  file_id=file.id
)