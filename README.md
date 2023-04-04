# ProjectWeb
## Project web này được thực hiện bởi:
- Tống Đức Thành Nam. 
- Trần Thanh Vinh. 
- Nguyễn Võ Công Huy.
### Để Chạy trang web này: Hãy bấm vào đường link sau: 
### [https://tymwork.live](https://tymwork.live)

# Để chạy trang Flask web này trên máy cá nhân:
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

# Chạy ứng dụng bằng Docker Desktop (Docker và Docker Compose):
- Bước 1: Cài đặt Docker
- Bước 2: Tạo docker network:
```sh
docker network create myproject-network
```
- Bước 3: Tạo build docker:
```sh
docker-compose build
```
- Bước 4: Chạy docker:
```sh
docker-compose up -d
```

# Deploy lên server Ubuntu 20.04:
- Bước 1: Cài đặt Docker
- Login vào github bằng SSH
- Clone project này về server.
```sh
git clone git@github.com:TongDucThanhNam/ProjectWeb.git
```
- Bước 2: Cài Docker và Docker Compose:
- Tạo docker network:
```sh
docker network create --driver myproject-network
```
- Build docker:
```sh
docker-compose build
```
- Chạy docker:
```sh
docker-compose up -d
```
Nhớ chọn port 5000 để chạy web server
```sh
Your_app_IP:5000 (Your_app_IP là địa chỉ IP của server)
```



