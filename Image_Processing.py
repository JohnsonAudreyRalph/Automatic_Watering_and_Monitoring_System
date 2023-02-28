import cv2
import time

# Mở camera
cap = cv2.VideoCapture(0)

# Đợi một giây để camera khởi động
time.sleep(1)

# Tạo vòng lặp chụp theo thời gian thực
while True:
    # Đọc ảnh từ camera
    ret, frame = cap.read()
    # Lưu ảnh vào file
    localtime = time.localtime(time.time())
    read_time = str(localtime.tm_mday) + '-' + str(localtime.tm_mon) + '-' + str(localtime.tm_year) + '--' + str(localtime.tm_hour) + 'h' + str(localtime.tm_min) + 'm' + str(localtime.tm_sec) + 's'
    File_name = 'IMG_CAM/image_' + read_time + '.jpg'
    cv2.imwrite(File_name, frame)
    # Đợi 6 giây trước khi chụp ảnh tiếp theo
    time.sleep(6)
    # Tạo trường hợp khi nhấn nút thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Giải phóng camera và đóng cửa sổ hiển thị ảnh
cap.release()
cv2.destroyAllWindows()


# import time
# filename = 'IMG_CAM/image_' + str(int(time.time())) + '.jpg'
# print('Kết quả 1 : ', filename)
# localtime = time.localtime(time.time())
# read_time = str(localtime.tm_mday) + '/' + str(localtime.tm_mon) + '/' + str(localtime.tm_year) + '__' + str(localtime.tm_hour) + ':' + str(localtime.tm_min) + ':' + str(localtime.tm_sec) + 's'
# File_name = 'IMG_CAM/image_' + read_time + '.jpg'
# print('Kết quả 2 : ', File_name)

# print('Loại 1: ', type(filename))
# print('Loại 2: ', type(File_name))