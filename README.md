# practice-docker-flaskpython-project

# 2. Thực hành

## Deploy Python by Docker

#### Cài đặt thư viện và các gói servervice cho python.

``` sh
sudo apt-get install -y python3-pip
sudo apt-get install libssl-dev libffi-dev python-dev
sudo apt-get install -y python3-venv
sudo apt install python3-virtualenv
```

#### Tạo thư mục project Python

``` sh
mkdir flaskpy_project
cd flaskpy_project
```

#### Tạo file app.py để chạy project
``` sh
touch app.py
nano app.py     
```

```bash
import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'thuy',
                    'email': 'thuy@gmail.com',
                    'message': 'Xin chào!!!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
```

#### Tạo môi trường ảo

``` sh
python -m venv
```

#### Kích hoạt môi trường ảo

``` sh
source venv/bin/activate
```

#### Tải về thư viện framework FlaskAPI

```sh
touch requirements.txt
nano requirements.txt
```

```bash
flask==2.0.1
```

```sh
pip install requirements.txt
```

#### Tạo file Dockerfile để khai báo image mà chúng ta muốn Docker tạo cho mình.

``` bash
FROM python:3.7

WORKDIR /UniCloud/Docker/FlaskWeb/flaskpy_project

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt



CMD [ "python", "app.py"]
```


#### Build image của project python từ Dockerfile. Lưu ý dấu chấm cuối được gọi là "build context", được xem là toàn bộ nội dung bên trong thư mục chứa Dockerfile bao gồm cả Dockerfile sẽ được gửi đến Docker Daemon để chạy và build image.

``` sh
docker build -t flaskpy_project:latest .
```

#### Kiểm tra image đã tạo

``` sh
docker images
```

#### Từ image run để tạo ra một container và chạy project

``` sh
docker run -it --name flaskpy_project -p 8888:8000 flaskpy_project:latest
```

#### Truy cập vào đường dẫn http://điền_ip_address:8888 hoặc http://localhost:8888 để xem trang web


### Sử dụng docker-compose để tạo ra container (thay vì dùng lệnh dokcer run thì ta dùng docker-compsoe up để tạo 1 container)

#### Tạo file docker-compsoe.yml để config các services của project cho container

``` sh
touch docker-compose.yml
```

``` bash
version: "4.7"
services:
  flaskpy_project:
    image: flaskpy_project:latest       
    ports:
      #cổng ngoài:cổng trong container
      - 8888:8000
```

```sh
docker-compose up
```
#### Truy cập vào đường dẫn http://điền_ip_address:8888 hoặc http://localhost:8888 để xem trang web

#### Đăng nhập vào Docker Hub

```sh
docker login
Username: username_dockerhub
Pasword:
```

#### Tạo tag cho image flaskpy_project (tạo ra một bản sao của image)

``` sh
docker tag flaskpy_project whiteb3ar99/flaskpy_project:latest
```

#### Push image đã tạo lên Docker Hub để lưu trữ

``` sh
docker push username_dockerhub/flaskpy_project:latest
```

#### Pull image vừa push lên Docker Hub về để chạy (docker stop id_containeđang chạy)

``` sh
docker pull whiteb3ar99/flaskpy_project:latest
```

#### Run image thành container mới

``` sh
docker run -it --name flaskpy_project_1 -p 8888:8000 -d whiteb3ar99/flaskpy_project
```
