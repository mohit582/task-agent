import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="Task Automation Agent", page_icon="🤖")
st.title("🤖 Task Automation Agent")
st.write("Tell me your goal and I'll break it down into an actionable plan!")

user_input = st.text_area("What do you need to accomplish?", height=100)

if st.button("Generate Plan ⚡"):
    if user_input:
        with st.spinner("Thinking..."):
            result = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": """You are a productivity assistant.
When given a task or goal, you:
1. Break it into clear steps
2. Prioritize them (High/Medium/Low)
3. Estimate time for each step
Be concise and practical."""},
                    {"role": "user", "content": user_input}
                ],
                model="llama-3.3-70b-versatile",
            )
        st.success("Here's your plan!")
        st.markdown(result.choices[0].message.content)
    else:
        st.warning("Please enter a task first!")
