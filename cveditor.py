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
st.set_page_config(page_title="cveditor", page_icon="🎨", layout="centered", initial_sidebar_state="collapsed")
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
st.markdown("""<div style="display: flex; align-items: center; justify-content: center;">
<svg width="683.851" height="108.602" viewBox="0 0 683.851 108.602" xmlns="http://www.w3.org/2000/svg">
	<g id="svgGroup" stroke-linecap="round" fill-rule="evenodd" font-size="9pt" stroke="#FF4B4B" stroke-width="0.25mm" fill="none" style="stroke:#FF4B4B;stroke-width:0.25mm;fill:none">
		<path d="M 73.351 5.401 L 69.001 17.401 Q 64.351 15.151 59.476 13.801 Q 54.601 12.451 48.001 12.451 A 31.759 31.759 0 0 0 36.144 14.634 A 29.971 29.971 0 0 0 30.826 17.401 A 31.75 31.75 0 0 0 21.278 27.273 A 40.467 40.467 0 0 0 18.901 31.651 Q 14.891 40.224 14.578 52.112 A 77.389 77.389 0 0 0 14.551 54.151 A 62.794 62.794 0 0 0 15.475 65.184 A 46.394 46.394 0 0 0 18.826 76.201 A 38.516 38.516 0 0 0 24.206 84.943 A 32.134 32.134 0 0 0 30.676 90.901 A 29.555 29.555 0 0 0 47.394 96.146 A 35.842 35.842 0 0 0 48.001 96.151 A 50.573 50.573 0 0 0 53.957 95.818 Q 56.975 95.46 59.574 94.715 A 28.92 28.92 0 0 0 60.751 94.351 Q 66.151 92.551 71.251 89.701 L 75.601 101.551 A 56.342 56.342 0 0 1 68.859 104.617 A 71.841 71.841 0 0 1 62.926 106.576 Q 56.26 108.47 47.56 108.592 A 86.123 86.123 0 0 1 46.351 108.601 A 48.576 48.576 0 0 1 32.363 106.649 A 41.941 41.941 0 0 1 22.201 102.076 A 42.901 42.901 0 0 1 7.386 86.408 A 52.374 52.374 0 0 1 5.851 83.476 Q 0.001 71.401 0.001 54.751 A 74.058 74.058 0 0 1 1.482 39.62 A 58.118 58.118 0 0 1 5.926 26.326 A 47.453 47.453 0 0 1 16.394 11.879 A 44.791 44.791 0 0 1 22.726 6.976 A 44.057 44.057 0 0 1 41.747 0.359 A 55.938 55.938 0 0 1 48.151 0.001 A 68.458 68.458 0 0 1 55.739 0.403 A 52.8 52.8 0 0 1 61.801 1.426 A 57.336 57.336 0 0 1 73.013 5.242 A 53.419 53.419 0 0 1 73.351 5.401 Z" id="0" vector-effect="non-scaling-stroke"/>
		<path d="M 137.701 106.801 L 121.651 106.801 L 83.101 5.551 L 97.051 0.151 L 130.051 91.201 L 163.201 0.601 L 176.101 5.551 L 137.701 106.801 Z" id="1" vector-effect="non-scaling-stroke"/>
		<path d="M 254.101 106.801 L 191.101 106.801 L 191.101 1.801 L 254.101 1.801 L 254.101 14.101 L 205.351 14.101 L 205.351 46.051 L 247.351 46.051 L 247.351 58.051 L 205.351 58.051 L 205.351 94.501 L 254.101 94.501 L 254.101 106.801 Z" id="2" vector-effect="non-scaling-stroke"/>
		<path d="M 274.351 106.501 L 274.351 2.101 Q 281.401 1.351 288.151 0.976 Q 294.901 0.601 303.601 0.601 A 72.912 72.912 0 0 1 314.617 1.39 Q 321.361 2.422 326.926 4.801 Q 336.751 9.001 343.126 16.351 Q 349.501 23.701 352.576 33.376 A 66.384 66.384 0 0 1 355.534 49.869 A 77.259 77.259 0 0 1 355.651 54.151 A 67.963 67.963 0 0 1 353.429 71.697 A 62.703 62.703 0 0 1 352.501 74.851 Q 349.351 84.601 342.826 92.026 Q 336.301 99.451 326.176 103.726 A 51.535 51.535 0 0 1 315.057 106.932 Q 309.853 107.85 303.914 107.98 A 90.289 90.289 0 0 1 301.951 108.001 A 280.47 280.47 0 0 1 295.844 107.937 Q 292.823 107.872 290.134 107.737 A 152.251 152.251 0 0 1 287.026 107.551 Q 280.651 107.101 274.351 106.501 Z M 288.601 13.651 L 288.601 94.801 A 65.35 65.35 0 0 0 293.495 95.307 A 73.924 73.924 0 0 0 295.201 95.401 Q 298.651 95.551 302.401 95.551 Q 315.901 95.551 324.451 90.301 Q 333.001 85.051 337.051 75.676 A 48.437 48.437 0 0 0 340.433 63.565 A 63.753 63.753 0 0 0 341.101 54.151 A 50.858 50.858 0 0 0 337.051 33.901 Q 333.001 24.451 324.601 18.676 Q 316.736 13.269 304.795 12.924 A 57.012 57.012 0 0 0 303.151 12.901 A 147.347 147.347 0 0 0 298.989 12.957 A 111.296 111.296 0 0 0 295.201 13.126 Q 291.601 13.351 288.601 13.651 Z" id="3" vector-effect="non-scaling-stroke"/>
		<path d="M 390.901 106.801 L 376.651 106.801 L 376.651 1.801 L 390.901 1.801 L 390.901 106.801 Z" id="4" vector-effect="non-scaling-stroke"/>
		<path d="M 452.401 106.801 L 438.151 106.801 L 438.151 14.401 L 405.901 14.401 L 405.901 1.801 L 484.651 1.801 L 484.651 14.401 L 452.401 14.401 L 452.401 106.801 Z" id="5" vector-effect="non-scaling-stroke"/>
		<path d="M 527.263 107.464 A 54.765 54.765 0 0 0 538.651 108.601 Q 550.351 108.601 559.501 104.326 Q 568.651 100.051 575.101 92.626 A 48.958 48.958 0 0 0 577.088 90.184 A 52.102 52.102 0 0 0 584.926 75.301 A 60.733 60.733 0 0 0 586.149 71.255 Q 588.28 63.213 588.301 54.326 A 74.892 74.892 0 0 0 588.301 54.151 A 72.323 72.323 0 0 0 588.182 49.985 A 62.159 62.159 0 0 0 584.926 33.151 Q 581.551 23.401 575.101 15.901 Q 568.651 8.401 559.426 4.201 A 44.888 44.888 0 0 0 550.588 1.257 A 54.63 54.63 0 0 0 538.651 0.001 A 59.024 59.024 0 0 0 529.31 0.714 A 44.491 44.491 0 0 0 512.101 7.126 Q 501.001 14.251 495.076 26.476 A 56.983 56.983 0 0 0 490.823 38.645 A 69.272 69.272 0 0 0 489.151 54.151 A 73.37 73.37 0 0 0 489.204 56.942 A 64.153 64.153 0 0 0 492.526 75.301 A 59.064 59.064 0 0 0 493.185 77.135 A 51.529 51.529 0 0 0 502.276 92.626 Q 508.651 100.051 517.801 104.326 A 43.713 43.713 0 0 0 527.263 107.464 Z M 538.651 96.301 A 39.775 39.775 0 0 0 547.573 95.349 A 28.974 28.974 0 0 0 558.001 90.751 A 33.705 33.705 0 0 0 568.989 77.445 A 40.877 40.877 0 0 0 569.776 75.676 A 51.161 51.161 0 0 0 573.26 62.282 A 65.255 65.255 0 0 0 573.751 54.151 Q 573.751 46.051 571.351 38.551 A 44.602 44.602 0 0 0 565.141 26.061 A 42.179 42.179 0 0 0 564.451 25.126 Q 559.951 19.201 553.426 15.751 A 29.882 29.882 0 0 0 542.301 12.478 A 36.867 36.867 0 0 0 538.651 12.301 Q 527.701 12.301 519.826 17.851 Q 511.951 23.401 507.826 32.851 A 49.189 49.189 0 0 0 504.145 46.633 A 61.885 61.885 0 0 0 503.701 54.151 Q 503.701 62.251 506.026 69.826 A 44.069 44.069 0 0 0 512.297 82.645 A 41.885 41.885 0 0 0 512.851 83.401 Q 517.351 89.401 523.876 92.851 A 29.882 29.882 0 0 0 535.001 96.124 A 36.867 36.867 0 0 0 538.651 96.301 Z" id="6" vector-effect="non-scaling-stroke"/>
		<path d="M 683.851 102.301 L 670.501 108.601 L 657.451 80.101 Q 653.542 71.689 648.041 67.114 A 24.316 24.316 0 0 0 645.001 64.951 A 29.478 29.478 0 0 0 636.75 61.647 Q 633.063 60.75 628.748 60.526 A 56.771 56.771 0 0 0 625.801 60.451 L 623.551 60.451 L 623.551 106.801 L 609.301 106.801 L 609.301 2.101 A 371.851 371.851 0 0 1 620.846 1.187 A 323.669 323.669 0 0 1 624.526 0.976 A 281.911 281.911 0 0 1 634.001 0.653 A 339.402 339.402 0 0 1 640.051 0.601 Q 659.251 0.601 668.926 8.401 Q 678.581 16.185 678.601 28.45 A 31.288 31.288 0 0 1 678.601 28.501 A 29.82 29.82 0 0 1 677.625 36.331 A 22.008 22.008 0 0 1 672.076 46.126 A 31.534 31.534 0 0 1 664.69 51.642 Q 659.785 54.348 653.251 56.101 A 35.485 35.485 0 0 1 658.394 58.895 A 30.641 30.641 0 0 1 660.451 60.376 Q 663.404 62.696 666.159 66.466 A 43.941 43.941 0 0 1 666.526 66.976 A 46.667 46.667 0 0 1 668.73 70.418 Q 670.576 73.576 672.451 77.701 L 683.851 102.301 Z M 623.551 13.201 L 623.551 48.451 L 640.051 48.451 Q 650.851 48.451 657.601 43.651 Q 664.351 38.851 664.351 29.851 A 14.717 14.717 0 0 0 659.441 18.654 A 19.909 19.909 0 0 0 658.051 17.476 A 20.884 20.884 0 0 0 651.505 14.143 Q 646.632 12.601 640.051 12.601 A 298.818 298.818 0 0 0 635.5 12.634 Q 633.053 12.671 630.901 12.751 Q 626.851 12.901 623.551 13.201 Z" id="7" vector-effect="non-scaling-stroke"/>
	</g>
</svg>
</div>
""", unsafe_allow_html=True)
st.markdown('---')
image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="file_uploader")
if image:
    img = Image.open(image)
    final_img = img
    old = img
    gray_img = img.convert("L")
### Image Info ###
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center;">
<svg xmlns="http://www.w3.org/2000/svg" width="11" height="24" viewBox="0 0 11 24"><path fill="currentColor" d="M8.436.006a2.24 2.24 0 0 1 2.408 2.354v-.006a3.156 3.156 0 0 1-3.151 3.01l-.065-.001h.003a2.151 2.151 0 0 1-2.367-2.398l-.001.01A3.087 3.087 0 0 1 8.44.004h-.005zM3.489 24c-1.268 0-2.199-.783-1.311-4.226l1.456-6.108c.254-.978.295-1.369 0-1.369a9.57 9.57 0 0 0-3.035 1.359l.033-.021l-.633-1.057c3.086-2.622 6.638-4.159 8.158-4.159c1.268 0 1.48 1.526.845 3.874l-1.666 6.421c-.296 1.135-.168 1.526.126 1.526a6.553 6.553 0 0 0 2.863-1.456l-.008.007l.72.979c-3.004 3.052-6.281 4.232-7.549 4.232z"/></svg>
            <h4 style="text-align: center;">Image Info</h4>
            </div>
    """,unsafe_allow_html=True)
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
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: center;">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.5"><path stroke-linejoin="round" d="M4.5 15v-3m0 0V9h3v3zm6 3V9l3 6V9m6 0h-3v6h3v-2.4"/><path d="M4 6V3.6a.6.6 0 0 1 .6-.6h14.8a.6.6 0 0 1 .6.6V6M4 18v2.4a.6.6 0 0 0 .6.6h14.8a.6.6 0 0 0 .6-.6V18"/></g></svg>
    <h4 style='text-align: center;'>Change Format</h4>
    </div>
    """, unsafe_allow_html=True)
    format = st.selectbox("Select a Format", ["JPEG", "PNG"])
    if format:
        if format == "JPEG":
            img = img.convert("RGB")
        elif format == "PNG":
            img = img.convert("RGBA")

### Resize ###
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: center;">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 512 512"><path fill="currentColor" d="m29 30l1 90h36V66h26V30zm99 0v36h72V30zm108 0v36h72V30zm108 0v36h72V30zm102 0v78h36V30zm-206 80v36h100.543l-118 118H30v218h218V289.457l118-118V272h36V110zm206 34v72h36v-72zM30 156v72h36v-72zm416 96v72h36v-72zm0 108v72h36v-72zm-166 86v36h72v-36zm108 0v36h72v-36z"/></svg>
    <h4 style='text-align: center;'>Resizing</h4>
    </div>
    """, unsafe_allow_html=True)
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
    st.markdown("""
                <div style="display: flex; align-items: center; justify-content: center;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 100 100"><g fill="currentColor" stroke-linejoin="round" color="currentColor"><path d="M79.85 4.386a1 1 0 0 0-.564.153L62.189 16.224a1 1 0 0 0-.352 1.315l8.425 18.717c.426.803 1.615.668 1.85-.209l2.932-10.871c7.894 2.498 13.883 8.977 15.514 17.152c1.698 8.512-.779 16.792-7.658 22.084a1 1 0 0 0-.184 1.402l3.474 9.41a1 1 0 0 0 1.402.182c9.579-7.368 14.159-22.987 11.794-34.838C97.087 29.048 88.584 19.8 77.39 16.416l3.394-10.77a1 1 0 0 0-.934-1.26M24.064 33.683a3.5 3.5 0 0 0-3.006 1.973l-20.71 42.8a3.5 3.5 0 0 0 2.63 4.985l75.015 11.275a3.5 3.5 0 0 0 3.846-4.55L67.573 46.672a3.5 3.5 0 0 0-2.431-2.293l-40.04-10.584a3.5 3.5 0 0 0-1.038-.113m2.039 7.617l35.412 9.363L73.419 86.95l-64.7-9.724z"/><path d="m41.797 11.014l1.558 4.752l9.502-3.118L51.3 7.896zm10.781 7.564l4.943.744l1.487-9.888l-4.944-.745zM27.545 15.69l1.559 4.752l9.501-3.117l-1.558-4.752zM13.29 20.365l1.559 4.75l9.502-3.117l-1.559-4.75zm37.057 13.047l4.945.742l1.486-9.888l-4.945-.743zM7.1 35.924l4.834 1.277l2.556-9.668l-4.834-1.277Zm41.02 12.322l4.943.742l1.486-9.888l-4.944-.743Zm-44.854 2.18L8.1 51.703l2.556-9.668l-4.834-1.277Zm42.623 12.652l4.945.744l1.486-9.888l-4.945-.745ZM.082 62.465l.303 1.969l1.025.92l2.295 1.109l2.178-4.5l-.44-.213l1.38-5.213l-4.835-1.277Zm8.123 6.176l9.002 4.355l2.178-4.5l-9.002-4.355zm35.453 9.271l4.946.744l1.486-9.89l-4.945-.743zm-21.951-2.738l9.002 4.355l2.178-4.5l-9.002-4.355zm13.502 6.533l9.002 4.356l1.09-2.25l2.472.37l.088-.583l-2.293-.344l.82-1.693l-9.001-4.356z"/></g></svg>
                    <h4 style='text-align: center;'>Rotation and Flip</h4>
                </div>
                """, unsafe_allow_html=True)
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
### Settings ###
    st.markdown("""<div style="display: flex; align-items: center; justify-content: center;">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><g fill="none" fill-rule="evenodd"><path d="M24 0v24H0V0zM12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035c-.01-.004-.019-.001-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427c-.002-.01-.009-.017-.017-.018m.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093c.012.004.023 0 .029-.008l.004-.014l-.034-.614c-.003-.012-.01-.02-.02-.022m-.715.002a.023.023 0 0 0-.027.006l-.006.014l-.034.614c0 .012.007.02.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01z"/><path fill="currentColor" d="M18 4a1 1 0 1 0-2 0v1H4a1 1 0 0 0 0 2h12v1a1 1 0 1 0 2 0V7h2a1 1 0 1 0 0-2h-2zM4 11a1 1 0 1 0 0 2h2v1a1 1 0 1 0 2 0v-1h12a1 1 0 1 0 0-2H8v-1a1 1 0 0 0-2 0v1zm-1 7a1 1 0 0 1 1-1h12v-1a1 1 0 1 1 2 0v1h2a1 1 0 1 1 0 2h-2v1a1 1 0 1 1-2 0v-1H4a1 1 0 0 1-1-1"/></g></svg>
    <h4 style='text-align: center;'>Settings</h4> 
    </div>""", unsafe_allow_html=True)
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
    st.markdown("""<div style="display: flex; align-items: center; justify-content: center;">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 72 72"><defs><path id="openmojiOverlappingWhiteAndBlackSquares0" d="M60 12H28v32h32z"/></defs><use href="#openmojiOverlappingWhiteAndBlackSquares0"/><path fill="#fff" stroke="#fff" stroke-width="2" d="M44 28H12v32h32z"/><path fill="#3f3f3f" d="M60 12H28v32h32z"/><g fill="none" stroke="#000" stroke-linejoin="round" stroke-width="2"><path stroke-linecap="round" d="M24.5 28H12v32h32V48"/><use href="#openmojiOverlappingWhiteAndBlackSquares0"/></g></svg>
    <h4 style='text-align: center;'>Grayscale</h4>
    </div>""", unsafe_allow_html=True)
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
        st.markdown("""<div style="display: flex; align-items: center; justify-content: center;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 16 16"><g fill="none"><g clip-path="url(#gravityUiLayers3Diagonal0)"><path fill="currentColor" fill-rule="evenodd" d="M6.702 3.013L8 3.5V2.386A2 2 0 0 1 10.702.513l3.351 1.257A3 3 0 0 1 16 4.579v4.035a2 2 0 0 1-2.702 1.873L12 10v1.114a2 2 0 0 1-2.702 1.873L8 12.5v1.114a2 2 0 0 1-2.702 1.873L1.947 14.23A3 3 0 0 1 0 11.421V7.386a2 2 0 0 1 2.702-1.873L4 6V4.886a2 2 0 0 1 2.702-1.873M5.5 6.563l.553.207A3 3 0 0 1 8 9.579v1.319l1.824.684a.5.5 0 0 0 .676-.468V7.079a1.5 1.5 0 0 0-.973-1.405L6.176 4.418a.5.5 0 0 0-.676.468zm4.553-2.293L9.5 4.062V2.386a.5.5 0 0 1 .676-.468l3.35 1.256c.586.22.974.78.974 1.405v4.035a.5.5 0 0 1-.676.468L12 8.398V7.079a3 3 0 0 0-1.947-2.809M1.5 11.421V7.386a.5.5 0 0 1 .676-.468l3.35 1.257c.586.219.974.779.974 1.404v4.035a.5.5 0 0 1-.676.468l-3.35-1.257a1.5 1.5 0 0 1-.974-1.404" clip-rule="evenodd"/></g><defs><clipPath id="gravityUiLayers3Diagonal0"><path fill="currentColor" d="M0 0h16v16H0z"/></clipPath></defs></g></svg>
        <h4 style='text-align: center;'>Channels
        </div>""", unsafe_allow_html=True)
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
    st.markdown("""<div style="display: flex; align-items: center; justify-content: center;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="24" viewBox="0 0 25 24"><path fill="currentColor" d="m20.888 2.27l-1.57.78l1.57.782l.78 1.569l.781-1.57l1.57-.78l-1.57-.781l-.78-1.569zm-12.93-.755l1.098 2.204l2.204 1.097l-2.204 1.097l-1.097 2.204l-1.097-2.204l-2.204-1.097l2.204-1.097zm9.28 1.887l5.15 5.149L7.297 23.64L2.15 18.491zm-2.004 4.833l2.32 2.32l2.005-2.004l-2.32-2.32zm.906 3.735l-2.32-2.32l-8.842 8.841l2.32 2.32z"/></svg>
                <h4 style='text-align: center;'>Filters</h4>
                </div>""", unsafe_allow_html=True)
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
        st.markdown("""<div style="display: flex; align-items: center; justify-content: center;">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 48 48"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M6 6v36h36M14 30v4m8-12v12m8-28v28m8-20v20"/></svg>
        <h4 style='text-align: center;'>Histogram</h4>
        </div>""", unsafe_allow_html=True)
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
### Object Detection ###

### Download ###
    st.markdown("""<div style="display: flex; align-items: center; justify-content: center;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 36 36"><path fill="currentColor" d="M30.92 8h-4.37a1 1 0 0 0 0 2H31v20H5V10h4.38a1 1 0 0 0 0-2h-4.3A2 2 0 0 0 3 10v20a2 2 0 0 0 2.08 2h25.84A2 2 0 0 0 33 30V10a2 2 0 0 0-2.08-2" class="clr-i-outline clr-i-outline-path-1"/><path fill="currentColor" d="m10.3 18.87l7 6.89a1 1 0 0 0 1.4 0l7-6.89a1 1 0 0 0-1.4-1.43L19 22.65V4a1 1 0 0 0-2 0v18.65l-5.3-5.21a1 1 0 0 0-1.4 1.43" class="clr-i-outline clr-i-outline-path-2"/><path fill="none" d="M0 0h36v36H0z"/></svg>
                <h4 style='text-align: center;'>Download</h4>
                </div>""", unsafe_allow_html=True)
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

### TO DO ###
#1. Add the Forier Transform
#2. Add Object Detection
