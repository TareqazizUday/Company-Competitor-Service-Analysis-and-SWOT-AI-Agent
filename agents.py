from crewai import Agent

company_researcher = Agent(
    role='Company Researcher',
    goal='Extract company details from the given URL.',
    verbose=True,
    memory=True,
    tools=[], 
    allow_delegation=False
)

market_analyst = Agent(
    role='Market Analyst',
    goal='Analyze services and identify competitors from extracted data.',
    verbose=True,
    memory=True,
    tools=[],
    allow_delegation=False
)

business_analyst = Agent(
    role='Business Analyst',
    goal='Perform a SWOT analysis for the company based on extracted data.',
    verbose=True,
    memory=True,
    tools=[],
    allow_delegation=False
)
