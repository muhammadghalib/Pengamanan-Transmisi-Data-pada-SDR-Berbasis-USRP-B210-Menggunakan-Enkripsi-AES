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





