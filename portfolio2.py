import streamlit as st
#from info import profile_picture, about_me, linkedin_image_url, github_image_url, email_image_url, my_linkedin_url, my_github_url, my_email_address, education_data, course_data
import pandas as pd

#COPIED FROM INFO FILE
profile_picture = "BenzProfilePicture.jpg"
about_me = "I'm Will Nicholson. I am a first year Industrial Engineering major studying here at Georgia Tech. I plan to graduate in three years and then pursue my masters in either analystics."


#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/william-nicholson-6190a62a2/"
my_github_url = "https://github.com/willnicholson"
my_email_address = "wwnicholson4@gmail.com"


education_data ={
    'Degree': 'Bachelor of Science in Industrial Engineering',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': "Spring 2026",
    'GPA': '4.0'
}
course_data = {
    "code":["CS 1301", "ISyE 2027", "ISyE 3030", "CS 2316"], 
    "names":["Intro to CS", "Probability with Applications", "Basic Statistical Methods", "Data Manipulation for Science and Industry"], 
    "semester_taken":["1st", "1st", "2nd", "2nd"],
    "skills":["Fully competent in Python (Couldn't tell you what recursion is)", "Can model scenarios using probability functions (There are 6 sides to a die)", "Will know confidcence intervals (Still can't predict anything)", "Will learn SQL, software development, and more"],
    }
experience_data = {
    "Leader in Band": (["- Served on the Roswell High School Leadership team for 3 years",
                                                                          "- Became woodwind captain and drum major", "- Led band to first place finish for first time in 5 years"],"DrumMajorChampPicture.jpg"),
    "Proficient in Probability":(["- Got 6th place at the Georgia Tech International Probability Competition",
                                                           "- Plans to become a TA in ISyE 2027"],"ProbabilityAchievementPicture.jpg"),
    "Future Intern":(["- Plans to complete an internship this upcoming Summer of 2024"],"InternPicture.jpg")

}

projects_data = {
    "Personal Profile": "Created this personal profile while taking CS1301",
    "Fantasy Football Pages": "Created info page on NFL receivers and a miniquiz on fantasy football from scratch",
    "Fantasy Football Draft Guide Web App": "Created a Web App through Streamlit on a brief guide to how to draft based on draft position, draft strategy, and commitment to fantasy fooball",
}

programming_data = {
    "Python": 100,
    "SQL": 20,
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": "🐍",
    "SQL": "🔍",
}
spoken_icons = {"English": "🇬🇧",
    "Spanish":"🇪🇸"
}

#CHANGE BELOW
spoken_data = {
    "English": "Fluent",
    "Spanish": "Almost Fluent",
}
leadership_data = {
    "Band Leadership": (["- Served as woodwind captain and drum major in final two years at Roswell"],"DrumMajorPicture.jpg"),
}
activity_data={
    "United Sound": ["- Taught special needs students how to play instruments", 
            "- Held a concert featuring the students playing pieces all together"],
    "Help a Hornet": ["- Help underpriveledged children by buying them presents for Christmas"],
    "Veterinarian Volunteer": ["- Volunteered at PetVet Inc., a veterinary clinic in Cumming, GA",
            "- Helped spay and neuter stray cats and dogs and shadowed surgeon in clinic"]
}
#END OF IMPORTED INFO FILE

#About Me Section
def aboutMeSection():
    st.header("About Me")
    st.image(profile_picture, width = 200)
    st.write(about_me)
    st.write('---')
aboutMeSection()
    
#Sidebar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link=f'<a href="{my_linkedin_url}"><img src="{linkedin_image_url}" alt="LinkedIn" width = "75" height = "75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link=f'<a href="{my_github_url}"><img src="{github_image_url}" alt="Github" width = "65" height = "65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html=f'<a href="{my_email_address}"><img src="{email_image_url}" alt="Email" width = "75" height = "75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()

#Education
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
                "code": "Course Code",
                "names": "Course Names",
                "semester_taken": "Semester Taken",
                "skills": "What I Learned"},
                 hide_index = True
                 )
    st.write("---")  
    
education_section(education_data, course_data)

#Professional Experience

def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experience_section(experience_data)

#Projects

def project_section(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
project_section(projects_data)

#Skills

def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{programming_icons.get(skill, '')}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{spoken_icons.get(spoken,'')}: {proficiency}")

        st.write("---")
skills_section(programming_data, spoken_data)

#Activities

def activities_section(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
                
    st.write("---")
activities_section(leadership_data, activity_data)
        
