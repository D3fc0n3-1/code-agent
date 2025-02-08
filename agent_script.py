from smolagents import CodeAgent, TransformersModel
import os

model_id = os.environ.get("MODEL_ID", "meta-llama/Llama-3.2-3B-Instruct") #Get from env variable

model = TransformersModel(model_id=model_id) #If you use a local model path, change this
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

result = agent.run("can you make all the scripts and instructions to fine tune a DistilBERT model LLM including splitting and formatting the data correctly")
print(result)
