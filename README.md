# Sistem Keamanan Jaringan - Project Based Learning - Topik 38

## Deskripsi proyek
Proyek ini bertujuan untuk mengimplementasikan Virtual Private Network (VPN) pada jaringan Software-Defined Radio (SDR) berbasis USRP B210 untuk mengamankan transmisi data telekomunikasi. Dalam proyek ini, OpenVPN akan digunakan untuk membangun dan mengkonfigurasi VPN yang melindungi jalur komunikasi SDR, sehingga mencegah penyadapan dan manipulasi data. Penggunaan USRP B210 sebagai transceiver SDR memungkinkan transmisi data dengan fleksibilitas tinggi, sementara GNU Radio akan digunakan untuk memproses sinyal. Dengan mengintegrasikan OpenVPN, proyek ini bertujuan untuk meningkatkan keamanan komunikasi data dalam jaringan SDR yang sensitif terhadap potensi ancaman. Metodologi yang diterapkan mencakup konfigurasi VPN menggunakan OpenVPN pada sistem berbasis Kali Linux, di mana VPN ini akan memastikan bahwa transmisi data tetap aman dan terlindungi dari gangguan luar.

## 🔌 Hardware yang Digunakan
- 1x USRP B210 sebagai transmitter
- 1x USRP B210 sebagai receiver
  
## 💻 Software yang Digunakan
- Ubuntu
- Docker
- GNU Radio v3.7

## 📦 Instalasi Docker
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

### **Untuk Transmitter**
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

### **Untuk Receiver**
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

## </> Instalasi Visual Studio Code dan Ekstensi

### **Memasang Ekstensi**
1. Install Visual Studio Code dari AppCenter.
2. Install ekstensi Docker.
3. Install ekstensi Dev Containers.
4. Buka ekstensi Docker di panel kiri VSCode.
5. Pastikan ada 2 container di panel Container, yaitu Transmitter dan Receiver.

## Memulai Bekerja dengan Visual Studio Code

### **Transmitter**
1. Klik kanan pada container ubuntu:gnuradio-v37-transmitter lalu start.
2. Klik kanan lagi pada container ubuntu:gnuradio-v37-transmitter lalu Attach Visual Studio Code.
3. Buka terminal dengan cara menekan ctrl+shift+p lalu ketikkan View:Toggle Terminal dan pastikan anda berada di gnuradio-transmitter@muhammad-ghalib.
4. Didalam folder persistent buat file `send_message.txt` dan berikan pesan yang akan dikirimkan ke USRP B210 receiver didalam file tersebut.
5. Di terminal jalankan perintah ini untuk memasang library pycryptodome.
   ```bash
   pip install pycryptodome
   ```
6. Buat file `aes_encryptor_ecb.py` dan masukkan kode dibawah ini. kode ini berguna untuk mengenkripsi pesan yang ada didalam file send_message.txt dengan algoritma enkripsi AES dengan mode ECB menggunakan secret key 1111111111111111.
   ```bash
   from Crypto.Cipher import AES
   from Crypto.Util.Padding import pad
   import binascii

   input_file = "send_message.txt"
   output_file = "encrypted_send_message.txt"

   # Secret Key (harus 16, 24, atau 32 byte)
   secret_key = b"1111111111111111"[:16]

   with open(input_file, "r") as file:
       plaintext = file.read()

   cipher = AES.new(secret_key, AES.MODE_ECB)
   ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))

   with open(output_file, "w") as file:
       file.write(binascii.hexlify(ciphertext).decode('utf-8') + "\n")

   print("Pesan dari '{}' telah berhasil dienkripsi dan disimpan di '{}'.".format(input_file, output_file))
   ```
7. Buat file `encrypted_send_message.txt`. file ini berguna untuk menyimpan hasil enkripsi dalam bentuk HEX.
8. Buat file `run_transmitter.sh`. file ini berguna untuk menjalankan perintah enkripsi dan memulai transmisi pesan.
   ```bash
   echo "Step 1 = Menjalankan aes_encryptor_ecb.py ..."
   python aes_encryptor_ecb.py
   if [ $? -ne 0 ]; then
       echo "Eksekusi aes_encryptor_ecb.py gagal."
       exit 1
   fi

   echo -e "\nStep 2 = Menjalankan top_block.py..."
   python top_block.py
   if [ $? -ne 0 ]; then
       echo "Eksekusi top_block.py gagal."
       exit 1
   fi
   ```
9. Di terminal jalankan perintah ini lalu enter.
    ```bash
    chmod +x run_transmitter.sh
    ```
10. Jalankan GNU Radio di terminal.
    ```bash
    gnuradio-companion
    ```
11. Mulai menggambar flowgraph atau import file `transmitter.grc` ke dalam folder persistent.
12. Di terminal jalankan perintah ini untuk memastikan USRP B210 apakah terhubung.
    ```bash
    uhd_find_devices
    ```
13. Run flowgraph untuk menghasilkan file `top_block.py` setelah itu stop flowgraph.
14. Di terminal jalankan perintah ini lalu enter.
    ```bash
    ./run_transmitter.sh
    ```
15. Anda akan melihat Transmitter FFT Plot dengan grafik sinyal seperti ini.

### **Receiver**
1. Klik kanan pada container ubuntu:gnuradio-v37-receiver lalu start.
2. Klik kanan lagi pada container ubuntu:gnuradio-v37-receiver lalu Attach Visual Studio Code.
3. Buka terminal dengan cara menekan ctrl+shift+p lalu ketikkan View:Toggle Terminal dan pastikan anda berada di gnuradio-receiver@muhammad-ghalib.
4. Didalam folder persistent buat file receive_message.txt. File ini berguna untuk menyimpan pesan yang diterima dari USRP B210 transmitter.
5. Buat file aes_decryptor_ecb.py dan masukkan kode dibawah ini. kode ini berguna untuk mengdekripsi pesan yang ada didalam file receive_message.txt dengan algoritma enkripsi AES dengan mode ECB menggunakan secret key 1111111111111111 dan menampilkan hasil dari dekripsinya diterminal.
6. Buat file run_receiver.sh. file ini berguna untuk menjalankan perintah menerima tranmisi pesan dan dekripsi.
7. Di terminal ketikkan chmod +x run_receiver.sh lalu enter.
8. Jalankan GNU Radio dengan cara ketikkan gnuradio-companion di terminal.
9. Mulai menggambar flowgraph atau import file receiver.grc ke dalam folder persistent.
10. Pastikan USRP B210 sudah terhubung.
11. Run flowgraph untuk menghasilkan file top_block.py setelah itu stop flowgraph.
12. Di terminal ketikkan ./run_receiver.sh lalu enter.
13. Anda akan melihat Transmitter FFT Plot dengan grafik sinyal seperti ini dan pesan asli yang sudah didekripsi di terminal.

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

💡 **STAY CURIOUS**

