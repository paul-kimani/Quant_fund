import streamlit as st
# REMOVED: from st_pages import ... (This library conflicts with native navigation)

# 1. PAGE TITLE & HEADER
st.title("💻 DE Zoomcamp")
st.markdown("### 👨‍🔧 Data Engineering Zoomcamp by [DataTalksClub](https://datatalks.club/)")

st.image("https://pbs.twimg.com/media/FmmYA2YWYAApPRB.png")

st.info("Original Course Repository on [Github](https://github.com/DataTalksClub/data-engineering-zoomcamp)")

st.markdown("---")

# 2. SIGN UP SECTION
with st.expander("Sign up here for 2024 Cohort"):
    st.markdown("""
   
    #

    - Register in [DataTalks.Club's Slack](https://datatalks.club/slack.html)
    - Join the [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG) channel
    - Join the [course Telegram channel with announcements](https://t.me/dezoomcamp)
    - The videos are published on [DataTalks.Club's YouTube channel](https://www.youtube.com/c/DataTalksClub) in [the course playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
    - [Frequently asked technical questions](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing)
    #""", unsafe_allow_html=True)

# 3. OVERVIEW SECTION
st.markdown("""
### 👨‍🎓 Taking the course

##### 👨‍👦‍👦 2024 Cohort

* **Start**: 15 January 2024 (Monday) at 17:00 CET
* [Cohort folder](cohorts/2024/) with homeworks and deadlines 

##### 👨‍🔧 Self-paced mode
All the materials of the course are freely available, so that you
can take the course at your own pace

* Follow the suggested syllabus (see below) week by week
* You don't need to fill in the registration form. Just start watching the videos and join Slack
* Check [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing) if you have problems
* If you can't find a solution to your problem in FAQ, ask for help in Slack

### 🔎 Overview""", unsafe_allow_html=True)

st.image("https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/architecture/photo1700757552.jpeg")

# 4. INSTRUCTORS & FOOTER
st.markdown("""
### 📓 Prerequisites

To get the most out of this course, you should feel comfortable with coding and command line
and know the basics of SQL. Prior experience with Python will be helpful, but you can pick
Python relatively fast if you have experience with other programming languages.

Prior experience with data engineering is not required.

### 👨‍🏫 Instructors

- [Ankush Khanna](https://linkedin.com/in/ankushkhanna2)
- [Victoria Perez Mola](https://www.linkedin.com/in/victoriaperezmola/)
- [Alexey Grigorev](https://linkedin.com/in/agrigorev)
- [Matt Palmer](https://www.linkedin.com/in/matt-palmer/)
- [Luis Oliveira](https://www.linkedin.com/in/lgsoliveira/)
- [Michael Shoemaker](https://www.linkedin.com/in/michaelshoemaker1/)

Past instructors:
- [Sejal Vaidya](https://www.linkedin.com/in/vaidyasejal/)
- [Irem Erturk](https://www.linkedin.com/in/iremerturk/)

### ❔ Asking for help in Slack
The best way to get support is to use [DataTalks.Club's Slack](https://datatalks.club/slack.html). Join the [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG) channel.

---
            
           
##### 🖼️ Course UI was made by [Paul Kimani](https://github.com/paul-kimani)
""", unsafe_allow_html=True)

# CSS HACK (Optional: Hides footer if desired)
hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)