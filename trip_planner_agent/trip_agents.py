from crewai import Agent
import streamlit as st
from langchain_community.llms import OpenAI

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from langchain_community.tools import DuckDuckGoSearchRun
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)
from utilities import getLLM



def streamlit_callback(step_output, agent_name: str = 'Generic call'):
    # This function will be called after each step of the agent's execution
    st.markdown("---")
    st.markdown(f"in callback with: {agent_name}\n")
    for step in step_output:
        if isinstance(step, tuple) and len(step) == 2:
            action, observation = step
            if isinstance(action, dict) and "tool" in action and "tool_input" in action and "log" in action:
                st.markdown(f"# Agent Name: {agent_name}")
                st.markdown(f"# Action")
                st.markdown(f"**Tool:** {action['tool']}")
                st.markdown(f"**Tool Input** {action['tool_input']}")
                st.markdown(f"**Log:** {action['log']}")
                st.markdown(f"**Action:** {action['Action']}")
                st.markdown(
                    f"**Action Input:** ```json\n{action['tool_input']}\n```")
            elif isinstance(action, str):
                st.markdown(f"**Action:** {action}")
            else:
                st.markdown(f"**Action:** {str(action)}")

            st.markdown(f"**Observation**")
            if isinstance(observation, str):
                observation_lines = observation.split('\n')
                for line in observation_lines:
                    if line.startswith('Title: '):
                        st.markdown(f"**Title:** {line[7:]}")
                    elif line.startswith('Link: '):
                        st.markdown(f"**Link:** {line[6:]}")
                    elif line.startswith('Snippet: '):
                        st.markdown(f"**Snippet:** {line[9:]}")
                    elif line.startswith('-'):
                        st.markdown(line)
                    else:
                        st.markdown(line)
            else:
                st.markdown(str(observation))
        else:
            st.markdown(step)


class TripAgents():
    
    
    def city_selection_agent(self):
        return Agent(
            role='City Selection Expert',
            goal='Select the best city based on weather, season, and prices',
            backstory='An expert in analyzing travel data to pick ideal destinations',
            tools=[
                DuckDuckGoSearchRun(),
                WebsiteSearchTool(),
            ],
            verbose=True,
            llm=getLLM("GOOGLE_API_KEY"),
            #step_callback=streamlit_callback,
            step_callback=lambda x: streamlit_callback(x, "city_selection_agent")
        )

    def local_expert(self):
        return Agent(
            role='Local Expert at this city',
            goal='Provide the BEST insights about the selected city',
            backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
            tools=[
                DuckDuckGoSearchRun(),
                WebsiteSearchTool(),
            ],
            verbose=True,
            llm=getLLM("GOOGLE_API_KEY"),
            #step_callback=streamlit_callback,
            step_callback=lambda x: streamlit_callback(x, "local_expert")
        )

    def travel_concierge(self):
        return Agent(
            role='Amazing Travel Concierge',
            goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
            backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
            tools=[
                DuckDuckGoSearchRun(),
                WebsiteSearchTool(),
                CalculatorTools.calculate,
            ],
            verbose=True,
            llm=getLLM("GOOGLE_API_KEY"),
            #step_callback=streamlit_callback,
            step_callback=lambda x: streamlit_callback(x, "travel_concierge")
        )
