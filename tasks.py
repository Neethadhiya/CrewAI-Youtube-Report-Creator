from crewai import Task
from tools import yt_tool
from agents import blog_resercher, blog_writer

research_task = Task(
    description=(
        'Identify the video {topic}'
        'Get detailed information about the video from the channel'),
    agent=blog_resercher,
    tools = [yt_tool],
    expected_output='A comprehensive 3 paragraph long report based on the {topic} of the video content',
)

write_task = Task(
    description=(
        'get the info from the youtube channel on the topic {topic}'),
    agent=blog_writer,
    tools=[yt_tool],
    async_execution = False,
    expected_output='Summarize the info from the youtube channel video on the topic{topic}',
    output_file = 'new-blog-post.md'
)