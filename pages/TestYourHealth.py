import streamlit as st
import pickle
import numpy as np
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
  
  
def load_data():
  with open('models/model_binary.pkl', 'rb') as file:
    data = pickle.load(file)
    return data
def load_data2():
  with open('models/model_multiclass.pkl', 'rb') as file:
    data = pickle.load(file)
    return data
data = load_data();
model = data["model"]
data2 = load_data2()
model2 = data2["model"]


def predict():
  st.title("Kiểm tra sức khỏe của bạn - Dự đoán bệnh viêm gan C")
  st.write("""### Cung cấp thông tin để dự đoán""")

#Get data from user
  age = st.slider("Tuổi của bạn", 6, 100, 54)

  gender = (
  "Nam",
  "Nữ"
)
  gender = st.selectbox("Giới tính",gender)


# - **Albumin Blood Test (ALB)** g/L: Albumin là một loại protein do gan sản xuất. Mức albumin thấp có thể là dấu hiệu của tổn thương gan do viêm gan C.
  st.write("""### Chỉ số Albumin trong máu (Albumin Blood Test - ALB)
         - Albumin là một loại protein do gan sản xuất. Mức albumin thấp có thể là dấu hiệu của tổn thương gan do viêm gan C.
         """)
  alb = st.slider("ALB", 14.9, 82.2, 31.95)
# - **Alkaline Phosphatase Test (ALP) IU/L**: Phosphatase kiềm là một enzyme có trong gan, xương và các mô khác. Mức ALP tăng cao có thể do nhiều nguyên nhân, bao gồm cả viêm gan C và các vấn đề về đường mật.
  st.write("""### Alkaline Phosphatase Test (ALP) IU/L
         - Phosphatase kiềm là một enzyme có trong gan, xương và các mô khác. Mức ALP tăng cao có thể do nhiều nguyên nhân, bao gồm cả viêm gan C và các vấn đề về đường mật.
         """)
  alp = st.slider("ALP", 11.3, 416.6, 93.22)
# - **Alanine Transaminase Test (ALT) U/L**: Alanine aminotransferase (ALT) là một enzyme có trong gan. Nồng độ ALT tăng cao là dấu hiệu cho thấy gan đang bị tổn thương. Xét nghiệm ALT thường được sử dụng cùng với AST để đánh giá tình trạng gan.
  st.write("""### Alanine Transaminase Test (ALT) U/L
         - Alanine aminotransferase (ALT) là một enzyme có trong gan. Nồng độ ALT tăng cao là dấu hiệu cho thấy gan đang bị tổn thương. Xét nghiệm ALT thường được sử dụng cùng với AST để đánh giá tình trạng gan.
         """)
  alt = st.slider("ALT", 0.9, 325.3, 8.12)
# - **Aspartate Transaminase Test (AST) U/L**: Aspartate aminotransferase (AST) là một enzyme có trong gan, tim, cơ bắp và các mô khác. Nồng độ AST tăng cao có thể do viêm gan C hoặc các bệnh lý khác về gan. Xét nghiệm AST thường được sử dụng cùng với ALT để đánh giá tình trạng gan.
  st.write("""### Aspartate Transaminase Test (AST) U/L
         - Aspartate aminotransferase (AST) là một enzyme có trong gan, tim, cơ bắp và các mô khác. Nồng độ AST tăng cao có thể do viêm gan C hoặc các bệnh lý khác về gan. Xét nghiệm AST thường được sử dụng cùng với ALT để đánh giá tình trạng gan.
         """)
  ast = st.slider("AST", 10.6, 324.0, 114.69)
# - **Bilirubin Blood Test (BIL) µmol/L**: Bilirubin là một chất được tạo ra từ sự phân hủy của hồng cầu. Bilirubin được gan xử lý và thải ra mật. Mức bilirubin cao có thể gây ra bệnh vàng da và có thể là dấu hiệu của tổn thương gan do viêm gan C.
  st.write("""### Bilirubin Blood Test (BIL) µmol/L
         - Bilirubin là một chất được tạo ra từ sự phân hủy của hồng cầu. Bilirubin được gan xử lý và thải ra mật. Mức bilirubin cao có thể gây ra bệnh vàng da và có thể là dấu hiệu của tổn thương gan do viêm gan C.
         """)
  bil = st.slider("BIL", 0.8, 209.0, 60.5)
# - **Cholinesterase (CHE) kU/L**: Cholinesterase là một enzyme quan trọng cho hệ thần kinh. Xét nghiệm CHE thường không được sử dụng để chẩn đoán viêm gan C, nhưng đôi khi có thể được thực hiện để đánh giá chức năng gan بشكل عام (be dang tong quat - tổng thể).
  st.write("""### Cholinesterase (CHE) kU/L
         - Cholinesterase là một enzyme quan trọng cho hệ thần kinh. Xét nghiệm CHE thường không được sử dụng để chẩn đoán viêm gan C, nhưng đôi khi có thể được thực hiện để đánh giá chức năng gan بشكل عام (be dang tong quat - tổng thể).
         """)
  che = st.slider("CHE", 1.42, 16.41, 3.40)
# - **Cholesterol (CHOL) mmol/L**: Cholesterol là một chất béo quan trọng trong cơ thể. Mức cholesterol cao có thể là yếu tố nguy cơ mắc các bệnh về tim mạch. Viêm gan C có thể ảnh hưởng đến nồng độ cholesterol trong máu.
  st.write("""### Cholesterol (CHOL) mmol/L
         - Cholesterol là một chất béo quan trọng trong cơ thể. Mức cholesterol cao có thể là yếu tố nguy cơ mắc các bệnh về tim mạch. Viêm gan C có thể ảnh hưởng đến nồng độ cholesterol trong máu.
         """)
  chol = st.slider("CHOL", 1.43, 9.67, 3.90)
# - **Creatinine Blod Test (CREA) µmol/L**: Creatinine là một chất thải được tạo ra từ quá trình chuyển hóa cơ bắp. Creatinine được lọc qua thận và thải ra nước tiểu. Xét nghiệm creatinine thường được sử dụng để đánh giá chức năng thận, nhưng đôi khi cũng có thể được thực hiện để đánh giá tình trạng tổng thể của bệnh nhân.
  st.write("""### Creatinine Blod Test (CREA) µmol/L
         - Creatinine là một chất thải được tạo ra từ quá trình chuyển hóa cơ bắp. Creatinine được lọc qua thận và thải ra nước tiểu. Xét nghiệm creatinine thường được sử dụng để đánh giá chức năng thận, nhưng đôi khi cũng có thể được thực hiện để đánh giá tình trạng tổng thể của bệnh nhân.
         """)
  crea = st.slider("CREA", 8.0, 1079.0, 155.19)
# - **Gamma-Glutamyl Transpeptidase Test (GGT) U/L**: Gamma-glutamyl transferase (GGT) là một enzyme có trong gan, đường mật và thận. Nồng độ GGT tăng cao có thể do nhiều nguyên nhân, bao gồm cả viêm gan C và nghiện rượu.
  st.write("""### Gamma-Glutamyl Transpeptidase Test (GGT) U/L
         - Gamma-glutamyl transferase (GGT) là một enzyme có trong gan, đường mật và thận. Nồng độ GGT tăng cao có thể do nhiều nguyên nhân, bao gồm cả viêm gan C và nghiện rượu.
         """)
  ggt = st.slider("GGT", 4.5, 650.0, 135.59)
# - **Protein Blood Test (PROT) g/L**: Protein tổng hợp là một phép đo của tất cả các protein trong máu. Gan sản xuất nhiều loại protein khác nhau. Mức protein tổng hợp thấp có thể là dấu hiệu của tổn thương gan do viêm gan C.
  st.write("""### Protein Blood Test (PROT) g/L
         - Protein tổng hợp là một phép đo của tất cả các protein trong máu. Gan sản xuất nhiều loại protein khác nhau. Mức protein tổng hợp thấp có thể là dấu hiệu của tổn thương gan do viêm gan C.
         """)
  prot = st.slider("PROT", 44.8, 86.5, 70.0)

  ok = st.button("Dự đoán bệnh")
  if ok:
    if(gender == "Nam"):
      gender = 1.0
    else:
      gender = 0.0
    x = np.array([[age, gender,alb, alp, alt, ast, bil, che, chol, crea, ggt, prot]])
    y = model.predict(x)
    if(y[0] == 0.0):
      st.subheader(f"Tình trạng của bạn: Khỏe mạnh")
    else:
      st.subheader(f"Tình trạng của bạn: Có bệnh!")

    y2 = model2.predict(x)
    if(y2[0] == 0.0):
      st.subheader(f"Hãy giữ gìn sức khỏe và kiểm tra thường sức khỏe thường xuyên!")
    elif y2[0] == 1.0:
      st.subheader(f"Bạn có khả năng mắc viêm gan C, cần đi khám ngay!")
    elif y2[0] == 2.0:
      st.subheader(f"Bạn có khả năng mắc xơ gan, trở nặng của viêm gan C, cần đi khám ngay!")
    else:
      st.subheader(f"Bạn có khả năng xơ cứng gan, giai đoạn cuối của viêm gan C, cần đi khám ngay!")
predict()  
