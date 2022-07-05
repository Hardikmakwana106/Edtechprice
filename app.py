import pickle
import numpy as np
import sklearn
import streamlit as st


  
# load the model from disk
final_model = pickle.load(open('Edtech_project_pickle.pkl', 'rb'))





def main():
    
    st.title('Cost Prediction of the Edtech Product')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Course_duration = st.text_input("Course duration")
    
    Mentor_Experience = st.text_input("Mentor experience")
    
    No_of_projects = st.text_input("Number of projects")
    
    No_of_enrollment = st.text_input("Number of enrollment")
    
    Type_of_Session_Online = st.selectbox("Type of Session", ['Online', 'Offline'])
    if (Type_of_Session_Online =='Online'):
        Type_of_Session_Online = 1
    else:
        Type_of_Session_Online = 0
        
    Assitance_and_support_yes = st.selectbox("Assitance and support", ['yes', 'no'])
    if(Assitance_and_support_yes =='yes'):
        Assitance_and_support_yes = 1
    else:
        Assitance_and_support_yes = 0
    
    Life_time_access_yes = st.selectbox("Life time access", ['yes', 'no'])
    if(Life_time_access_yes =='yes'):
        Life_time_access_yes = 1
    else:
        Life_time_access_yes = 0
    
    
    Classroom_class_yes = st.selectbox("Classroom" , ['yes', 'no'] )
    if(Classroom_class_yes =='yes'):
        Classroom_class_yes = 1
    else:
        Classroom_class_yes = 0    
    
    
    Marketing_yes = st.selectbox("Marketing" , ['yes', 'no'])
    if(Marketing_yes =='yes'):
        Marketing_yes = 1
    else:
        Marketing_yes = 0
        
        
    Course_level_Intermediate = st.selectbox("Course_level", ['Beginner', 'Intermediate', 'Advanced'])
    if (Course_level_Intermediate == 'Intermediate'):
        Course_level_Intermediate = 1
        Course_level_Beginner= 0
        
    elif(Course_level_Intermediate == 'Beginner'):
        Course_level_Intermediate = 0
        Course_level_Beginner= 1
    
    else:
        Course_level_Intermediate = 0
        Course_level_Beginner= 0
        
        
         

    
    result=""
    if st.button("Predict"):
        result= final_model.predict([[Course_duration, Mentor_Experience ,No_of_projects , No_of_enrollment , Type_of_Session_Online , Assitance_and_support_yes ,Life_time_access_yes , Classroom_class_yes , Marketing_yes, Course_level_Beginner,Course_level_Intermediate]])
        output =round(result[0])
        st.success('The product price is {}'.format(output))
   






if __name__=="__main__":
    main()
