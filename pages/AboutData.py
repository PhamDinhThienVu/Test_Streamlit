import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Manage page link - nav bar to move on another pages

with st.sidebar:

  st.header('Outline', divider='rainbow')

  st.page_link(page = "pages/Problems.py", 
             label="Problems")

  st.page_link(page = "pages/AboutData.py", 
             label="About Data")

  st.page_link(page = "pages/AnalysData.py", 
             label="Data Analysis")
  
  st.page_link(page = "pages/TestYourHealth.py", 
             label="Test Your Health")
  

# Content
data = pd.read_csv("./data/HepatitisCdata.csv")  
st.title("Về bộ dữ liệu")
st.write(data)
  
st.subheader("Kích thước: ")
shape = data.shape
st.write(shape)
st.text(f"Bộ dữ liệu gồm {shape[0]} bản ghi, mỗi bản ghi có {shape[1]} trường")

st.write("""
### Ý nghĩa các trường dữ liệu
- **Albumin Blood Test (ALB)** g/L: Albumin là một loại protein do gan sản xuất. Mức albumin thấp có thể là dấu hiệu của tổn thương gan do viêm gan C.
- **Alkaline Phosphatase Test (ALP) IU/L**: Phosphatase kiềm là một enzyme có trong gan, xương và các mô khác. Mức ALP tăng cao có thể do nhiều nguyên nhân, bao gồm cả viêm gan C và các vấn đề về đường mật.
- **Alanine Transaminase Test (ALT) U/L**: Alanine aminotransferase (ALT) là một enzyme có trong gan. Nồng độ ALT tăng cao là dấu hiệu cho thấy gan đang bị tổn thương. Xét nghiệm ALT thường được sử dụng cùng với AST để đánh giá tình trạng gan.
- **Aspartate Transaminase Test (AST) U/L**: Aspartate aminotransferase (AST) là một enzyme có trong gan, tim, cơ bắp và các mô khác. Nồng độ AST tăng cao có thể do viêm gan C hoặc các bệnh lý khác về gan. Xét nghiệm AST thường được sử dụng cùng với ALT để đánh giá tình trạng gan.
- **Bilirubin Blood Test (BIL) µmol/L**: Bilirubin là một chất được tạo ra từ sự phân hủy của hồng cầu. Bilirubin được gan xử lý và thải ra mật. Mức bilirubin cao có thể gây ra bệnh vàng da và có thể là dấu hiệu của tổn thương gan do viêm gan C.
- **Cholinesterase (CHE) kU/L**: Cholinesterase là một enzyme quan trọng cho hệ thần kinh. Xét nghiệm CHE thường không được sử dụng để chẩn đoán viêm gan C, nhưng đôi khi có thể được thực hiện để đánh giá chức năng gan بشكل عام (be dang tong quat - tổng thể).
- **Cholesterol (CHOL) mmol/L**: Cholesterol là một chất béo quan trọng trong cơ thể. Mức cholesterol cao có thể là yếu tố nguy cơ mắc các bệnh về tim mạch. Viêm gan C có thể ảnh hưởng đến nồng độ cholesterol trong máu.
- **Creatinine Blod Test (CREA) µmol/L**: Creatinine là một chất thải được tạo ra từ quá trình chuyển hóa cơ bắp. Creatinine được lọc qua thận và thải ra nước tiểu. Xét nghiệm creatinine thường được sử dụng để đánh giá chức năng thận, nhưng đôi khi cũng có thể được thực hiện để đánh giá tình trạng tổng thể của bệnh nhân.
- **Gamma-Glutamyl Transpeptidase Test (GGT) U/L**: Gamma-glutamyl transferase (GGT) là một enzyme có trong gan, đường mật và thận. Nồng độ GGT tăng cao có thể do nhiều nguyên nhân, bao gồm cả viêm gan C và nghiện rượu.
- **Protein Blood Test (PROT) g/L**: Protein tổng hợp là một phép đo của tất cả các protein trong máu. Gan sản xuất nhiều loại protein khác nhau. Mức protein tổng hợp thấp có thể là dấu hiệu của tổn thương gan do viêm gan C.

### Các biên mục tiêu [Category]

- **0=Blood Donor** : Người bình thường
- **1=Hepatitis (Viêm gan)**: Viêm gan. Viêm gan C là một trong những loại viêm gan có thể được xét nghiệm thông qua các chỉ số enzyme 
- **2=Fibrosis (Xơ gan)**: Xơ gan. Xơ gan là giai đoạn cuối cùng của sẹo gan, có thể do nhiều nguyên nhân gây ra, bao gồm viêm gan C mạn tính. Trong xơ gan, các mô gan bị tổn thương được thay thế bằng mô sẹo, làm giảm chức năng gan.
- **3=Cirrhosis (Cứng hóa)**:Gan cứng hóa ( cirrhosis) là** giai đoạn nặng nhất của xơ gan**, khi gan bị xơ hóa nghiêm trọng và chức năng gan bị suy giảm đáng kể.
""")

st.subheader("Describe của tập dữ liệu: ")
st.write(data.describe())

st.subheader("Nguồn gốc")
st.write("""
         https://www.kaggle.com/datasets/fedesoriano/hepatitis-c-dataset
Context
The data set contains laboratory values of blood donors and Hepatitis C patients and demographic values like age. The data was obtained from UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/HCV+data

Content
All attributes except Category and Sex are numerical.
Attributes 1 to 4 refer to the data of the patient:
1. X (Patient ID/No.)
2. Category (diagnosis) (values: '0=Blood Donor', '0s=suspect Blood Donor', '1=Hepatitis', '2=Fibrosis', '3=Cirrhosis')
3. Age (in years)
4. Sex (f,m)
Attributes 5 to 14 refer to laboratory data:
5. ALB
6. ALP
7. ALT
8. AST
9. BIL
10. CHE
11. CHOL
12. CREA
13. GGT
14. PROT

The target attribute for classification is Category (2): blood donors 
         vs. 
         Hepatitis C patients (including its progress ('just' Hepatitis C, Fibrosis, Cirrhosis).

**Acknowledgements**
- Creators: Ralf Lichtinghagen, Frank Klawonn, Georg Hoffmann
- Donor: Ralf Lichtinghagen: Institute of Clinical Chemistry; Medical University Hannover (MHH); Hannover, Germany; lichtinghagen.ralf '@' mh-hannover.de
- Donor: Frank Klawonn; Helmholtz Centre for Infection Research; Braunschweig, Germany; frank.klawonn '@' helmholtz-hzi.de
- Donor: Georg Hoffmann; Trillium GmbH; Grafrath, Germany; georg.hoffmann '@' trillium.de

**Relevant Papers**
- Lichtinghagen R et al. J Hepatol 2013; 59: 236-42
- Hoffmann G et al. Using machine learning techniques to generate laboratory diagnostic pathways â€“ a case study. J Lab Precis Med 2018; 3: 58-67

**Other Datasets**
- Stroke Prediction Dataset: LINK
- Wind Speed Prediction Dataset: LINK
- Spanish Wine Quality Dataset: LINK
""")