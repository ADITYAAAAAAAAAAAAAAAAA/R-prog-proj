library(magick)
library(httr)
library(jsonlite)
library(rpy2)

cohere_api_key <- "7HpPc5ghLeUjTWUHljnX8Y7xgxRcRhdOUg2bv9Px"

generate_caption <- function(image_path) {

  return("A generated caption for the uploaded image.")
}

query_cohere <- function(caption, user_question) {
  prompt <- paste("Image Caption:", caption, "\nUser Question:", user_question, "\nAnswer:")
  
  response <- POST(
    url = "https://api.cohere.ai/v1/generate",
    add_headers(Authorization = paste("Bearer", cohere_api_key), `Content-Type` = "application/json"),
    body = toJSON(list(
      model = "command-xlarge",
      prompt = prompt,
      max_tokens = 100,
      temperature = 0.75
    ), auto_unbox = TRUE)
  
st.title("VisioNiX - Image Captioning and Q&A")
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_image:
    image = Image.open(uploaded_image)
    #st.image(image, caption="Uploaded Image", use_column_width=True)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    user_question = st.text_input("Ask a question about the image")
    
    if st.button("Get Answer") and user_question:
        caption = generate_caption(image)
        answer = query_cohere(caption, user_question)
        
        st.write("### Answer:", answer)
  
  content <- content(response, as = "text", encoding = "UTF-8")
  parsed_content <- fromJSON(content)
  return(parsed_content$generations[[1]]$text)
}
