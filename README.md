# Sistem Keamanan Jaringan - Project Based Learning - Topik 38


## Command for install Docker in Kali
- sudo apt-get update
- sudo apt install -y docker.io
- sudo systemctl enable docker --now
- sudo usermod -aG docker $USER
- docker --version
- sudo systemctl status docker


## Command for install GNU Radio v3.7 on Docker
for transmitter
- git clone https://github.com/muhammadghalib/Docker-GNURadio
- cd Docker-GNURadio
- cd gnuradio-v37-transmitter
- sudo docker build -t ubuntu:gnuradio-v37-transmitter .
- sudo docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --privileged --device=/dev/bus/usb:/dev/bus/usb -v /dev/bus/usb:/dev/bus/usb --device=/dev/snd -v persistent-37-transmitter:/home/gnuradio-transmitter/persistent --group-add=audio -it ubuntu:gnuradio-v37-transmitter bash
- gnuradio-companion

for receiver
- cd Docker-GNURadio
- cd gnuradio-v37-receiver
- sudo docker build -t ubuntu:gnuradio-v37-receiver .
- sudo docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --privileged --device=/dev/bus/usb:/dev/bus/usb -v /dev/bus/usb:/dev/bus/usb --device=/dev/snd -v persistent-37-receiver:/home/gnuradio-receiver/persistent --group-add=audio -it ubuntu:gnuradio-v37-receiver bash
- gnuradio-companion

## Basic command in Docker
Melihat Daftar Container
- docker ps  
  Melihat daftar container yang sedang berjalan.
- docker ps -a  
  Melihat semua container, baik yang sedang berjalan maupun yang sudah berhenti.

Mengelola Container
- docker stop <container_id_or_name>  
  Menghentikan container yang sedang berjalan.
- docker rm <container_id_or_name>  
  Menghapus container yang sudah berhenti.

Melihat Daftar Images
- docker images  
  Melihat daftar image Docker yang tersimpan di sistem lokal.

Menghapus Images
- docker rmi <image_id_or_name>  
  Menghapus image dari sistem lokal.  
Contoh lain:
- docker rmi <repository_name>:<image_id_or_name>

Membersihkan Docker
- docker system df  
  Melihat seluruh penggunaan memori di Docker.
- docker system prune -a --volumes -f  
  Menghapus semua data Docker secara menyeluruh, termasuk container, images, network, dan volume yang tidak terpakai.

Mengelola Volume
- docker volume ls  
  Melihat daftar volume
- docker volume rm <nama_volume>
  Menghapus volume tertentu  

Copy file dari container ke direktori Downloads  
- docker cp CONTAINER_ID:/home/gnuradio-transmitter/persistent/NAMA_FILE ~/Downloads/  
  Transmitter  
- docker cp CONTAINER_ID:/home/gnuradio-receiver/persistent/NAMA_FILE ~/Downloads/  
  Receiver  
  
Copy file dari direktori Downloads ke container  
- docker cp ~/Downloads/NAMA_FILE CONTAINER_ID:/home/gnuradio-transmitter/persistent/  
  Transmitter  
- docker cp ~/Downloads/NAMA_FILE CONTAINER_ID:/home/gnuradio-receiver/persistent/  
  Receiver  


### Referensi
Install Docker on Ubuntu
- https://phoenixnap.com/kb/install-docker-on-ubuntu-20-04

Install Docker on Kali
- https://www.kali.org/docs/containers/installing-docker-on-kali/

Repository GNU Radio on Docker from git-artes
- https://github.com/git-artes/docker-gnuradio

Onnocenter GNU Radio
- http://onnocenter.or.id/wiki/index.php/GNURadio












