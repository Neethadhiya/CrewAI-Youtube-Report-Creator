from crewai import Agent, Task, Crew, Process
from tools import yt_tool
from agents import blog_resercher, blog_writer
from tasks import research_task, write_task

crew = Crew(
    agents=[blog_resercher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew = True,
    verbose=2
)
result = crew.kickoff(inputs={'topic': 'MCQ'})
print(result)
