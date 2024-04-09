import streamlit as st
from PIL import Image
from PIL.ImageFilter import *
from PIL import ImageEnhance
#import cv2
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from base64 import b64encode
##############################################################################################################
st.set_option('deprecation.showPyplotGlobalUse', False)
##############################################################################################################
@st.cache_data
def display_histogram(img):
        img = np.array(img)
        fig, ax = plt.subplots(1, 2, figsize=(15, 5))
        ax[0].imshow(img)
        ax[0].axis("off")
        ax[0].set_title("Image")
        ax[1].hist(img.ravel(), bins=256, histtype="step", color="black")
        ax[1].set_title("Histogram")
        plt.suptitle("Image and its Histogram")
        st.pyplot(fig)
@st.cache_data
def luminosite(img, pourcentage):
    return ImageEnhance.Brightness(img).enhance(1 + pourcentage)
@st.cache_data
def get_image_download_link(img,filename,text):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href
##############################################################################################################
st.markdown('<h1 style="color: #7ED957; text-align: center;">cveditor</h1>', unsafe_allow_html=True)
st.markdown('---')
image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="file_uploader")
if image:
    img = Image.open(image)
    final_img = img
    old = img
    gray_img = img.convert("L")
##############################################################################################################
### Image Info ###
    st.markdown("<h4 style='text-align: center;'>Image Info ℹ️</h4>", unsafe_allow_html=True)
    img_info = {
        "Format": img.format,
        "Size": img.size,
        "Mode": img.mode,
    }
    table_html = "<table><tbody>"
    for key, value in img_info.items():
        table_html += f"<tr><td><b>{key}</b></td><td>{value}</td></tr>"
    table_html += "</tbody></table>"
    st.write(table_html, unsafe_allow_html=True)
### Change Format ###
    st.markdown("<h4 style='text-align: center;'>Change Format 🔄🔧</h4>", unsafe_allow_html=True)
    format = st.selectbox("Select a Format", ["JPEG", "PNG"])
    if format:
        if format == "JPEG":
            img = img.convert("RGB")
        elif format == "PNG":
            img = img.convert("RGBA")

### Resize ###
    st.markdown("<h4 style='text-align: center;'>Resizing 🖼️📏</h4>", unsafe_allow_html=True)
    colWH, colSubmit = st.columns(2)
    with colWH:
        width = st.number_input("Width", value=img.width)
        height = st.number_input("Height", value=img.height)
    with colSubmit:
        #center the button vertically and horizontally
        for i in range(5):
            st.write("")
        submit = st.button("Resize")

    if submit:
        img = img.resize((int(width), int(height)))
        gray_img = gray_img.resize((int(width), int(height)))
### Rotate ###
    st.markdown("<h4 style='text-align: center;'>Rotation and Flip 🔄🔃</h4>", unsafe_allow_html=True)
    colR, colF = st.columns(2)
    with colR:
        degree = st.slider("Degree", 0.0, 360.0, 0.0, 0.01)
    img = img.rotate(degree)
    gray_img = gray_img.rotate(degree)
    with colF:
        flipH = st.checkbox("Flip Horizontally")
        flipV = st.checkbox("Flip Vertically")
    if flipH:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        gray_img = gray_img.transpose(Image.FLIP_LEFT_RIGHT)
    if flipV:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        gray_img = gray_img.transpose(Image.FLIP_TOP_BOTTOM)
### TO Name ###
    st.markdown("<h4 style='text-align: center;'>☀️🖌️</h4>", unsafe_allow_html=True)
    colB, colC = st.columns(2)
    with colB:
        brightness = st.slider("Brightness", -1.0, 1.0, 0.0, 0.01)
        blur = st.slider("Blur", 0.0, 10.0, 0.0, 0.01)
    img = ImageEnhance.Brightness(img).enhance(1 + brightness)
    gray_img = ImageEnhance.Brightness(gray_img).enhance(1 + brightness)
    img = img.filter(GaussianBlur(blur))
    gray_img = gray_img.filter(GaussianBlur(blur))
    with colC:
        contrast = st.slider("Contrast", -1.0, 1.0, 0.0, 0.01)
        sharpen = st.slider("Sharpen", 0.0, 10.0, 0.0, 0.01)
    img = ImageEnhance.Contrast(img).enhance(1 + contrast)
    gray_img = ImageEnhance.Brightness(gray_img).enhance(1 + contrast)
    img = img.filter(UnsharpMask(sharpen))
    gray_img = gray_img.filter(UnsharpMask(sharpen))
### Covert to Grayscale ###
    st.markdown("<h4 style='text-align: center;'>Grayscale 🎨➡️🔳</h4>", unsafe_allow_html=True)
    colGS,colIGS = st.columns(2)
    with colGS:
        grayscale = st.checkbox("Grayscale")
    if grayscale:
        img = gray_img
    with colIGS:
        inversed_grayscale = st.checkbox("Inversed Grayscale")
    if inversed_grayscale:
        img = gray_img.point(lambda x: 255 - x)
### Channels ###
    if not grayscale and not inversed_grayscale and format == "JPEG":
        st.markdown("<h4 style='text-align: center;'>Channels 🌈</h4>", unsafe_allow_html=True)
        colR, colG, colB = st.columns(3)
        try :
            r, g, b = img.split()
        except:
            st.write("Image is not in RGB mode")
        with colR:
            red = st.checkbox("Red", value=True)
        with colG:
            green = st.checkbox("Green", value=True)
        with colB:
            blue = st.checkbox("Blue", value=True)
        img = Image.merge("RGB", (r if red else r.point(lambda x: 0), g if green else g.point(lambda x: 0), b if blue else b.point(lambda x: 0)))
### Filters ###
    st.markdown("<h4 style='text-align: center;'>Filters 📸</h4>", unsafe_allow_html=True)
    NameF,ValueF = st.columns(2)
    with NameF:
        Reset = st.button("Reset")
        BW = st.checkbox("Black and white")
        contour = st.checkbox("Contour")
        edge_enhance = st.checkbox("Edge Enhance")
        edge_enhance_more = st.checkbox("Edge Enhance More")
        emboss = st.checkbox("Emboss")
        find_edges = st.checkbox("Find Edges")
        smooth = st.checkbox("Smooth")
        Med = st.checkbox("Median Filter")
    with ValueF:
         Max_BW = st.slider("threshold",0.0,255.0,190.0,0.01)
    if Filter:
        if Reset:
            img = old
        elif BW:
            img = gray_img.point(lambda x: 0 if x < Max_BW else 255, '1')
        elif Med:
            img = img.filter(MedianFilter)
        elif contour:
            img = img.filter(CONTOUR)
        elif edge_enhance:
            img = img.filter(EDGE_ENHANCE)
        elif edge_enhance_more:
            img = img.filter(EDGE_ENHANCE_MORE)
        elif emboss:
            img = img.filter(EMBOSS)
        elif find_edges:
            img = img.filter(FIND_EDGES)
        elif smooth:
            img = img.filter(SMOOTH)
### Histogram ###
    if not BW and not grayscale and not inversed_grayscale:
        st.markdown("<h4 style='text-align: center;'>Histogram 📊</h4>", unsafe_allow_html=True)
        display_histogram(img)
        ##histogram egalisation
        #egalisation = st.checkbox("Egalisation d'histogramme")
        #if egalisation:
            #img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            #img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
            #img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
            #img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
            #img = Image.fromarray(img)
            #display_histogram(img)
### Download ###
    st.markdown("<h4 style='text-align: center;'>Download 📥</h4>", unsafe_allow_html=True)
    colD, colP = st.columns(2)
    with colD:
        download = st.button("Download")
    with colP:
        preview = st.checkbox("Preview")
    if download:
#TO DO : solve the of png format
        st.markdown(get_image_download_link(img, "img.png", 'Download ' + "image"), unsafe_allow_html=True)
    if preview:
        st.image(img)
### Display Image ###
    #st.image(img)
    with st.sidebar:
        slider_value = st.slider("Zoom", 0.1, 2.0, 1.0, 0.1)
        st.image(img, width=int(slider_value * 300))  # Adjust 300 to your desired initial width

