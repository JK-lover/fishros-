import face_recognition 
import cv2
from ament_index_python.packages import get_package_share_directory
import os

def main():
    default_image_path = os.path.join(get_package_share_directory('demo_python_service'),'resource/default.jpg')
    print(f"真实路径：{default_image_path}") 
    
    #加载图片，使用cv2
    image = cv2.imread(default_image_path)

    
    #人脸位置
    face_locations = face_recognition.face_locations(image,number_of_times_to_upsample =1,model='hog')
    
    #绘制人脸框
    for top,right,bottom,left in face_locations:
        cv2.rectangle(image,(left,top),(right,bottom),(0,0,255),5)
    
    #结果显示
    cv2.imshow('RESULT',image)
    cv2.waitKey(0)