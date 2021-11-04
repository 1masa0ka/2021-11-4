import streamlit as st
from PIL import Image
import time

st.title('Streamlit入門')

st.write('Display Image')
'Start!'
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

if st.checkbox('Show image'):    
    img=Image.open('sample.jpg')   
    st.image(img,caption='cat',use_column_width=True)

option=st.selectbox('Favorite Num',
             list(range(1,11))            
             )
'You like',option,'!'

left_column,right_column=st.columns(2)
button1=left_column.button('left')
if button1:
    right_column.write('yes')

expander=st.expander('問い合わせ')
expander.write('come on!')


text=st.text_input('Your hobby')
condition=st.slider('Your condition',0,100,50)
'You love',text,'!'

'Your condition:',condition
