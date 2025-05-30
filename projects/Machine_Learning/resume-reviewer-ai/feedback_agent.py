from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Use Falcon model with Hugging Face Hub
llm = HuggingFaceHub(
    repo_id="mrm8488/t5-base-finetuned-question-generation-ap",
    model_kwargs={"temperature": 0.7, "max_new_tokens": 512}
)

# Prompt template for feedback
prompt = PromptTemplate(
    input_variables=["resume", "job_description"],
    template="""
    You are an expert resume reviewer. Compare the following resume with the job description and give 3 detailed suggestions for improving the resume:

    Resume:
    {resume}

    Job Description:
    {job_description}
    """
)

# Create the chain
chain = LLMChain(llm=llm, prompt=prompt)

def generate_feedback(resume, job_description):
    return chain.run(resume=resume, job_description=job_description)