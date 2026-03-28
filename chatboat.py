
#Importing Libraries
import streamlit as st 
import ollama



#Function(This function sends the user’s prompt to the LLM,Default model is "llama3.2".)
def llmresponds (prompt, model = "llama3.2"):
    
    messages = [
        {
            'role':'user',
            'content':'prompt'
        }
    ]
    
    
    #Sends request to the modelExtracts and returns the generated tex
    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']
    

#streamlitr layout

#set The Title And Discription
st.title("LLM Text Generator")
st.write("Interact With A large Language modeling (llm)")


#user input 
user_prompt = st.text_area("Enter Your Text")


#Button interaction
if st.button("Generate Responds"):
    if user_prompt.strip()!= "":
        
        #Loading Spinner
        with st.spinner ("loading......"):
            try:
                
                
                #Calling the llm
                responds = llmresponds(user_prompt)
                
                
                #Display Output
                st.success("Responds Genarator")
                st.text_area("llmresponds",value = responds,height=200 )
            #Error Handling    
            except Exception as e:
                st.error(f"Error : {str(e)}")
    #Empty Out Put Handling           
    else:
        st.warning("pleas enter a pormpt")
    
