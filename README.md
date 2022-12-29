# ProjectWeb
## Project web này được thực hiện bởi:
- Tống Đức Thành Nam. 
- Trần Thanh Vinh. 
### Để Chạy trang web này: Hãy bấm vào đường link sau: 
tymwork.com

#Để chạy trang Flask web này trên máy cá nhân:
- Bước 1: Clone project này về máy cá nhân:
- Bước 2: Mở terminal cmd và chạy lệnh: 
```sh
git clone https://github.com/TongDucThanhNam/ProjectWeb.git
```
- Bước 3. Cài đặt virtualenv
```sh
    python -m pip install --user virtualenv
```
- Bước 4. Mở Terminal -> trỏ đến thử mục project, Tạo virtualenv venv (Lưu Ý nếu đã tồn tại thư mục env thì phải xóa đi trước khi tạo mới): 
```sh
    python -m venv venv
```
- Bước 5. Kích hoạn virtual env:
```sh
    .\venv\Scripts\activate
```
- Bước 6. Tải các thư viện liệt kê trong requirements.txt: 
```sh
python -m pip install -r requirements.txt
```
- Bước 7. Chạy file web flask: 
```sh
set FLASK_APP=flaskapp.py
```
```sh
flask run
```

# Chạy ứng dụng bằng Docker 
- Bước 1: Cài đặt Docker
- Bước 2: Tạo docker network:
```sh
docker network create --driver myproject-network
```
- Bước 3: Tạo build docker:
```sh
docker-compose build
```
- Bước 4: Chạy docker:
```sh
docker-compose up -d
```

# Web Server docker ubuntu
- Bước 1: Cài đặt Docker
git clone git@github.com:TongDucThanhNam/ProjectWeb.git