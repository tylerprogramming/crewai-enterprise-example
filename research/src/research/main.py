#!/usr/bin/env python
import sys
from crew import ResearchCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs'
    }
    ResearchCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
