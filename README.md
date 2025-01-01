# Sistem Keamanan Jaringan - Project Based Learning - Topik 38

## 📦 Instalasi Docker di Kali atau Ubuntu
Berikut adalah langkah-langkah untuk menginstal Docker pada distribusi Kali atau Ubuntu:

```bash
sudo apt-get update
sudo apt install -y docker.io
sudo systemctl enable docker --now
sudo usermod -aG docker $USER
docker --version
sudo systemctl status docker
```

---

## 📡 Instalasi GNU Radio v3.7 di Docker

### **Untuk Transmitter:**
1. Clone repository:
   ```bash
   git clone https://github.com/muhammadghalib/Docker-GNURadio
   ```
2. Masuk ke direktori transmitter:
   ```bash
   cd Docker-GNURadio/gnuradio-v37-transmitter
   ```
3. Build image Docker:
   ```bash
   sudo docker build -t ubuntu:gnuradio-v37-transmitter .
   ```
4. Jalankan container:
   ```bash
   sudo docker run --net=host \
      --env="DISPLAY" \
      --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
      --privileged \
      --device=/dev/bus/usb:/dev/bus/usb \
      -v /dev/bus/usb:/dev/bus/usb \
      --device=/dev/snd \
      -v persistent-37-transmitter:/home/gnuradio-transmitter/persistent \
      --group-add=audio \
      -it ubuntu:gnuradio-v37-transmitter bash
   ```
5. Jalankan GNU Radio:
   ```bash
   gnuradio-companion
   ```

### **Untuk Receiver:**
1. Masuk ke direktori receiver:
   ```bash
   cd Docker-GNURadio/gnuradio-v37-receiver
   ```
2. Build image Docker:
   ```bash
   sudo docker build -t ubuntu:gnuradio-v37-receiver .
   ```
3. Jalankan container:
   ```bash
   sudo docker run --net=host \
      --env="DISPLAY" \
      --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
      --privileged \
      --device=/dev/bus/usb:/dev/bus/usb \
      -v /dev/bus/usb:/dev/bus/usb \
      --device=/dev/snd \
      -v persistent-37-receiver:/home/gnuradio-receiver/persistent \
      --group-add=audio \
      -it ubuntu:gnuradio-v37-receiver bash
   ```
4. Jalankan GNU Radio:
   ```bash
   gnuradio-companion
   ```

---

## 🛠️ Perintah Dasar Docker

### **Melihat Daftar Container**
- Container yang sedang berjalan:
  ```bash
  docker ps
  ```
- Semua container (berjalan dan berhenti):
  ```bash
  docker ps -a
  ```

### **Mengelola Container**
- Menghentikan container:
  ```bash
  docker stop <container_id_or_name>
  ```
- Menghapus container:
  ```bash
  docker rm <container_id_or_name>
  ```

### **Melihat dan Mengelola Images**
- Daftar image yang tersimpan:
  ```bash
  docker images
  ```
- Menghapus image:
  ```bash
  docker rmi <image_id_or_name>
  ```
  Contoh:
  ```bash
  docker rmi <repository_name>:<image_id_or_name>
  ```

### **Membersihkan Docker**
- Melihat penggunaan memori Docker:
  ```bash
  docker system df
  ```
- Menghapus data yang tidak terpakai:
  ```bash
  docker system prune -a --volumes -f
  ```

### **Mengelola Volume**
- Melihat daftar volume:
  ```bash
  docker volume ls
  ```
- Menghapus volume:
  ```bash
  docker volume rm <nama_volume>
  ```

### **Mengelola File**
- Menyalin file dari container ke direktori Downloads:
  - **Transmitter:**
    ```bash
    docker cp CONTAINER_ID:/home/gnuradio-transmitter/persistent/NAMA_FILE ~/Downloads/
    ```
  - **Receiver:**
    ```bash
    docker cp CONTAINER_ID:/home/gnuradio-receiver/persistent/NAMA_FILE ~/Downloads/
    ```

- Menyalin file dari Downloads ke container:
  - **Transmitter:**
    ```bash
    docker cp ~/Downloads/NAMA_FILE CONTAINER_ID:/home/gnuradio-transmitter/persistent/
    ```
  - **Receiver:**
    ```bash
    docker cp ~/Downloads/NAMA_FILE CONTAINER_ID:/home/gnuradio-receiver/persistent/
    ```

---

## 🌐 Perintah Dasar UHD
- **Menemukan perangkat UHD:**
  ```bash
  uhd_find_devices
  ```
- **Memeriksa detail perangkat UHD:**
  ```bash
  uhd_usrp_probe
  ```

---

## ⚙️ Instalasi dan Penghapusan GNU Radio & UHD

### **Menginstal GNU Radio versi terbaru**
```bash
sudo apt-get install gnuradio
```

### **Menghapus GNU Radio**
```bash
sudo apt-get remove --purge gnuradio
sudo apt-get autoremove
sudo apt-get autoclean
```

### **Menginstal UHD versi terbaru**
```bash
sudo add-apt-repository ppa:ettusresearch/uhd
sudo apt install uhd-host
```

### **Menghapus UHD**
```bash
sudo apt remove uhd-host
```

---

## 🔗 Referensi
- **Instalasi Docker di Ubuntu:** [PhoenixNAP](https://phoenixnap.com/kb/install-docker-on-ubuntu-20-04)
- **Instalasi Docker di Kali Linux:** [Kali Docs](https://www.kali.org/docs/containers/installing-docker-on-kali/)
- **Instalasi GNU Radio:** [GNU Radio Wiki](https://wiki.gnuradio.org/index.php/InstallingGR)
- **Instalasi UHD:** [GNU Radio UHD](https://wiki.gnuradio.org/index.php?title=Draft-AN-445#Building_and_installing_UHD_from_source_code)
- **Repository Docker GNU Radio:** [Git Artes](https://github.com/git-artes/docker-gnuradio)
- **Onnocenter GNU Radio:** [Onnocenter](http://onnocenter.or.id/wiki/index.php/GNURadio)
- **Essential Docker Images:** [OpenVerso Docker Hub](https://hub.docker.com/u/openverso)

---

💡 **Catatan:** Pastikan semua langkah dijalankan dengan hak akses yang memadai dan ikuti panduan sesuai kebutuhan proyek Anda.

