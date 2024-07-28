import cohere
import streamlit as st

# Set Cohere API key
api_key = 'cv2iT1eJhSikUq7HcUeIjiCSKUQdOH1dsvE9HgTB'  # Replace with your actual API key
cohere_client = cohere.Client(api_key)

# Streamlit app framework
st.title('🦜🔗 YouTube GPT Creator')
prompt = st.text_input('Plug in your prompt here')

def generate_text(prompt, model='command-xlarge-nightly'):
    try:
        response = cohere_client.generate(
            model=model,
            prompt=prompt,
            max_tokens=500
        )
        return response.generations[0].text.strip()
    except Exception as e:
        st.error(f"Error in generating text: {e}")
        return None

# Process user input and generate results
if prompt:
    with st.spinner('Generating title...'):
        try:
            title_prompt = f"Write me a YouTube video title about {prompt}"
            title = generate_text(title_prompt)
        except Exception as e:
            st.error(f"Error generating title: {e}")
            title = None

    if title:
        with st.spinner('Generating script...'):
            try:
                script_prompt = f"Write me a YouTube video script based on this title TITLE: {title}"
                script = generate_text(script_prompt)
            except Exception as e:
                st.error(f"Error generating script: {e}")
                script = None

        # Display results
        if title:
            st.write("*Title:*", title)

        if script:
            st.write("*Script:*", script)

        # Expandable sections for history
        if title:
            st.expander('Title History').info(title)

        if script:
            st.expander('Script History').info(script)
