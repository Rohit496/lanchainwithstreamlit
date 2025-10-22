from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o")

# Simple prompt template for Salesforce release information
salesforce_prompt_template = PromptTemplate(
    input_variables=["release_season", "year"],
    template="""You are a Salesforce expert with comprehensive knowledge of Salesforce releases and updates.
    
    Provide detailed information about the Salesforce {release_season} {year} release including:
    
    1. Release Overview - Brief summary and key themes
    2. Major New Features - Most important features and enhancements
    3. Key Changes - What users and admins need to know
    4. Latest Features - Include any recent innovations and trending capabilities
    
    If the specific release information is not available, provide general guidance about Salesforce release cycles and the latest available features.
    
    Keep the response well-organized and practical.
    """,
)

# Streamlit UI
st.title("🌟 Salesforce Release Information")
st.markdown("Get information about Salesforce seasonal releases")

# Simple input options
release_season = st.selectbox("Select Release Season:", ["Winter", "Summer", "Spring"])

current_year = 2025
year = st.selectbox(
    "Select Year:",
    list(range(current_year - 2, current_year + 1)),
    index=2,  # Default to current year
)

if st.button("Get Release Information", type="primary"):
    if release_season and year:
        with st.spinner(f"Fetching {release_season} {year} release information..."):
            try:
                # Format the prompt with user inputs
                formatted_prompt = salesforce_prompt_template.format(
                    release_season=release_season, year=year
                )

                # Get response from LLM
                response = llm.invoke(formatted_prompt)

                # Display the response
                st.markdown(f"### 📋 {release_season} {year} Release Information")
                st.markdown(response.content)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please check your API configuration and try again.")
    else:
        st.warning("Please select both release season and year.")

# Additional helpful information
st.markdown("---")
st.markdown("### 💡 Helpful Links")
st.markdown(
    """
- [Official Salesforce Release Notes](https://help.salesforce.com/s/articleView?id=release-notes.salesforce_release_notes.htm)
- [Trailhead Release Modules](https://trailhead.salesforce.com/)
- [Salesforce Developers](https://developer.salesforce.com/)
"""
)

# Sidebar with information
st.sidebar.markdown("### About Salesforce Releases")
st.sidebar.info(
    """
🌨️ **Winter** - February
☀️ **Summer** - June  
🌸 **Spring** - October

Each release includes hundreds of new features and improvements.
"""
)

st.sidebar.markdown("### Tips")
st.sidebar.success(
    """
- Check release notes before updates
- Test in Sandbox first
- Plan user training
"""
)
