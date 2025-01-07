# Sistem Keamanan Jaringan - Project Based Learning - Topik 26

## Deskripsi proyek
Proyek ini bertujuan untuk mengimplementasikan Virtual Private Network (VPN) pada jaringan Software-Defined Radio (SDR) berbasis USRP B210 untuk mengamankan transmisi data telekomunikasi. Dalam proyek ini, OpenVPN akan digunakan untuk membangun dan mengkonfigurasi VPN yang melindungi jalur komunikasi SDR, sehingga mencegah penyadapan dan manipulasi data. Penggunaan USRP B210 sebagai transceiver SDR memungkinkan transmisi data dengan fleksibilitas tinggi, sementara GNU Radio akan digunakan untuk memproses sinyal. Dengan mengintegrasikan OpenVPN, proyek ini bertujuan untuk meningkatkan keamanan komunikasi data dalam jaringan SDR yang sensitif terhadap potensi ancaman. Metodologi yang diterapkan mencakup konfigurasi VPN menggunakan OpenVPN pada sistem berbasis Kali Linux, di mana VPN ini akan memastikan bahwa transmisi data tetap aman dan terlindungi dari gangguan luar.

## 🔌 Hardware yang Digunakan
- 1x USRP B210 sebagai transmitter
- 1x USRP B210 sebagai receiver
  
## 💻 Software yang Digunakan
- Ubuntu 24.04
- Docker
- GNU Radio v3.7

## 📦 Instalasi Docker
Berikut adalah langkah-langkah lengkap untuk menginstal Docker pada distribusi Ubuntu:

1. Perbarui daftar paket sistem:
   ```bash
   sudo apt-get update
   ```
2. Pasang Docker dengan perintah berikut:
   ```bash
   sudo apt install -y docker.io
   ```
3. Aktifkan layanan Docker agar berjalan otomatis saat sistem dinyalakan:
   ```bash
   sudo systemctl enable docker --now
   ```
4. Tambahkan pengguna Anda ke grup Docker untuk menghindari penggunaan `sudo` saat menjalankan perintah Docker:
   ```bash
   sudo usermod -aG docker $USER
   ```
   **Catatan:** Setelah menjalankan perintah ini, Anda perlu keluar dan masuk kembali agar perubahan grup diterapkan.

5. Verifikasi instalasi Docker dengan mengecek versinya:
   ```bash
   docker --version
   ```
6. Periksa status layanan Docker untuk memastikan bahwa Docker berjalan dengan benar:
   ```bash
   sudo systemctl status docker
   ```
   ![](./Documentation/Images/Instalasi%20Docker/1.png)

## 📡 Instalasi GNU Radio v3.7 di Docker

### **Transmitter**
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
5. Keluar dari container dan tutup terminal:
   ```bash
   exit
   ```

### **Receiver**
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
4. Keluar dari container dan tutup terminal:
   ```bash
   exit
   ```

## </> Instalasi Visual Studio Code dan Ekstensi
1. Unduh dan pasang **Visual Studio Code** dari [halaman resmi VS Code](https://code.visualstudio.com/) atau melalui **AppCenter** di ubuntu.
2. Buka Visual Studio Code, lalu navigasikan ke tab **Extensions** di panel kiri.
3. Cari dan pasang ekstensi **Docker**. Ekstensi ini memungkinkan Anda untuk mengelola container secara langsung dari dalam Visual Studio Code.
    ![](./Documentation/Images/Instalasi%20Visual%20Studio%20Code%20dan%20Ekstensi/1.png)
4. Cari dan pasang ekstensi **Dev Containers**. Ekstensi ini berguna untuk mengembangkan aplikasi di dalam container yang terisolasi dan telah dikonfigurasi sebelumnya.
    ![](./Documentation/Images/Instalasi%20Visual%20Studio%20Code%20dan%20Ekstensi/2.png)
5. Setelah ekstensi terpasang, buka tab **Docker** di panel kiri.
6. Periksa pada bagian **Containers** di panel tersebut dan pastikan terdapat dua container aktif:
   - **ubuntu:gnuradio-v37-transmitter**
   - **ubuntu:gnuradio-v37-receiver**  
   ![](./Documentation/Images/Instalasi%20Visual%20Studio%20Code%20dan%20Ekstensi/3.png)

## 🚀 Memulai Proyek dengan Visual Studio Code

### **Transmitter**
1. Menjalankan Container
   - Klik kanan pada container `ubuntu:gnuradio-v37-transmitter` lalu pilih **Start** untuk menjalankan container.
   - Setelah container aktif, klik kanan kembali pada container yang sama dan pilih **Attach Visual Studio Code** untuk terhubung dengan Visual Studio Code.

2. Membuka Terminal di Visual Studio Code
   - Tekan `Ctrl + Shift + P` untuk membuka Command Palette.
   - Ketikkan `View: Toggle Terminal` dan tekan `Enter`.
   - Pastikan Anda berada di terminal dengan path `gnuradio-transmitter@muhammad-ghalib`.

3. Membuat dan Mengisi File Pesan
   - Di dalam folder `persistent`, buat file baru bernama `send_message.txt`.
   - Tambahkan pesan yang akan dikirimkan ke **USRP B210 receiver** ke dalam file tersebut.

4. Memasang Library PyCryptodome
   - Di terminal, jalankan perintah berikut untuk memasang library **PyCryptodome**:
     ```bash
     pip install pycryptodome
     ```

5. Membuat File Python untuk Enkripsi
   - Buat file baru bernama `aes_encryptor_ecb.py`.
   - Salin dan tempel kode berikut ke dalam file tersebut:
     ```python
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
   - File ini akan mengenkripsi pesan dalam file `send_message.txt` menggunakan algoritma **AES** dengan mode **ECB** dan kunci rahasia `1111111111111111`.

6. Membuat File Output Enkripsi
   - Buat file baru bernama `encrypted_send_message.txt` di dalam folder `persistent`.
   - File ini akan digunakan untuk menyimpan hasil enkripsi dalam format HEX.

7. Membuat Skrip untuk Menjalankan Transmisi
   - Buat file baru bernama `run_transmitter.sh`.
   - Salin dan tempel kode berikut ke dalam file tersebut:
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
   - Skrip ini akan:
     - Menjalankan file `aes_encryptor_ecb.py` untuk enkripsi.
     - Menjalankan file `top_block.py` untuk memulai transmisi.

8. Memberikan Izin Eksekusi pada Skrip
   - Di terminal, masuk ke direktori `persistent`:
     ```bash
     cd persistent
     ```
   - Berikan izin eksekusi ke file `run_transmitter.sh`:
     ```bash
     chmod +x run_transmitter.sh
     ```

9. Membuka GNU Radio
   - Jalankan perintah berikut di terminal untuk membuka **GNU Radio Companion**:
     ```bash
     gnuradio-companion
     ```
   - Anda dapat mulai menggambar **flowgraph** seperti dibawah ini atau mengimpor file `transmitter.grc` ke dalam folder `persistent`.
   ![](./Documentation/Images/Memulai%20Proyek%20dengan%20Visual%20Studio%20Code/Transmitter/3.png)

10. Memastikan USRP B210 Terhubung
    - Jalankan perintah berikut untuk memeriksa koneksi dengan perangkat **USRP B210**:
      ```bash
      uhd_find_devices
      ```

      ![](./Documentation/Images/Memulai%20Proyek%20dengan%20Visual%20Studio%20Code/Transmitter/4.png)  

      **Catatan**: Setelah mengetahui alamat serial USRP B210 untuk transmitter maka masukkan alamat serial tersebut ke flowgraph transmitter pada block **UHD: USRP Sink** di Device Address.

11. Menjalankan dan Menghentikan Flowgraph
    - Jalankan **flowgraph** untuk menghasilkan file `top_block.py`.
    - Setelah selesai, hentikan **flowgraph**.

12. Menjalankan Skrip Transmisi
    - Di terminal, jalankan perintah berikut untuk memulai transmisi:
      ```bash
      ./run_transmitter.sh
      ```
    - Jika berhasil, Anda akan melihat **Transmitter FFT Plot** dengan grafik sinyal seperti yang diharapkan.  
    ![](./Documentation/Images/Memulai%20Proyek%20dengan%20Visual%20Studio%20Code/Transmitter/1.jpg)

### **Receiver**
1. Menjalankan Container
   - Klik kanan pada container `ubuntu:gnuradio-v37-receiver` lalu pilih **Start** untuk menjalankan container.
   - Setelah container aktif, klik kanan kembali pada container yang sama dan pilih **Attach Visual Studio Code** untuk terhubung dengan Visual Studio Code.

2. Membuka Terminal di Visual Studio Code
   - Tekan `Ctrl + Shift + P` untuk membuka Command Palette.
   - Ketikkan `View: Toggle Terminal` dan tekan `Enter`.
   - Pastikan Anda berada di terminal dengan path `gnuradio-receiver@muhammad-ghalib`.

3. Membuat File Pesan
   - Di dalam folder `persistent`, buat file baru bernama `receiver_message.txt`.

4. Memasang Library PyCryptodome
   - Di terminal, jalankan perintah berikut untuk memasang library **PyCryptodome**:
     ```bash
     pip install pycryptodome
     ```

5. Membuat File Python untuk Dekripsi
   - Buat file baru bernama `aes_decryptor_ecb.py`.
   - Salin dan tempel kode berikut ke dalam file tersebut:
     ```python
     from Crypto.Cipher import AES
     import binascii
     import time
     import os
     
     def decrypt_aes_ecb(hex_string, secret_key):
        cipher = AES.new(secret_key, AES.MODE_ECB)
        encrypted_bytes = binascii.unhexlify(hex_string)
        decrypted_bytes = cipher.decrypt(encrypted_bytes)
        return decrypted_bytes.strip()
     
     def read_and_decrypt_file(file_name, secret_key):
          with open(file_name, 'r') as f:
            for index, line in enumerate(f):
                hex_value = line.strip()
                try:
                    decrypted_value = decrypt_aes_ecb(hex_value, secret_key)
                    print("Baris {}: {}".format(index + 1, decrypted_value))
                except Exception:
                    print("Baris {}: HEX not valid".format(index + 1))
                time.sleep(0.2)

     if __name__ == "__main__":
        file_name = "receive_message.txt"

        # Kunci rahasia untuk dekripsi (harus sepanjang 16 byte)
        secret_key = "1111111111111111"

        read_and_decrypt_file(file_name, secret_key)
      ```

    - File ini akan mengdekripsi pesan dalam file `receive_message.txt` menggunakan algoritma **AES** dengan mode **ECB** dan kunci rahasia `1111111111111111`.

6. Membuat Skrip untuk Menjalankan Penerima
   - Buat file baru bernama `run_receiver.sh`.
   - Salin dan tempel kode berikut ke dalam file tersebut:
     ```bash
     echo "Step 1 = Menjalankan top_block.py..."
     python top_block.py &
     if [ $? -ne 0 ]; then
        echo "Eksekusi top_block.py gagal."
        exit 1
     fi

     sleep 3
     
     echo -e "\nStep 2 = Menjalankan aes_decryptor_ecb.py..."
     python aes_decryptor_ecb.py
     if [ $? -ne 0 ]; then
        echo "Eksekusi aes_decryptor_ecb.py gagal."
        exit 1
     fi
     ```
    - Skrip ini akan:
        - Menjalankan file `top_block.py` untuk memulai penerima.
        - Menjalankan file `aes_decryptor_ecb.py` untuk enkripsi.

7. Memberikan Izin Eksekusi pada Skrip
   - Di terminal, masuk ke direktori `persistent`:
     ```bash
     cd persistent
     ```
   - Berikan izin eksekusi ke file `run_receiver.sh`:
     ```bash
     chmod +x run_receiver.sh
     ```

8. Membuka GNU Radio
   - Jalankan perintah berikut di terminal untuk membuka **GNU Radio Companion**:
     ```bash
     gnuradio-companion
     ```
   - Anda dapat mulai menggambar **flowgraph** atau mengimpor file `receiver.grc` ke dalam folder `persistent`.
   ![](./Documentation/Images/Memulai%20Proyek%20dengan%20Visual%20Studio%20Code/Receiver/2.png)

9. Memastikan USRP B210 Terhubung
    - Jalankan perintah berikut untuk memeriksa koneksi dengan perangkat **USRP B210**:
      ```bash
      uhd_find_devices
      ```

      ![](./Documentation/Images/Memulai%20Proyek%20dengan%20Visual%20Studio%20Code/Transmitter/4.png)

      **Catatan**: Setelah mengetahui alamat serial USRP B210 untuk receiver maka masukkan alamat serial tersebut ke flowgraph transmitter pada block **UHD: USRP Source** di Device Address.

10. Menjalankan dan Menghentikan Flowgraph
    - Jalankan **flowgraph** untuk menghasilkan file `top_block.py`.
    - Setelah selesai, hentikan **flowgraph**.

11. Menjalankan Skrip Transmisi
    - Di terminal, jalankan perintah berikut untuk memulai transmisi:
      ```bash
      ./run_transmitter.sh
      ```
    - Jika berhasil, Anda akan melihat **Transmitter FFT Plot** dengan grafik sinyal seperti yang diharapkan.  
    ![](./Documentation/Images/Memulai%20Proyek%20dengan%20Visual%20Studio%20Code/Receiver/1.jpg)

## 🔗 Referensi
- **Instalasi Docker di Ubuntu:** [PhoenixNAP](https://phoenixnap.com/kb/install-docker-on-ubuntu-20-04)
- **Instalasi Docker di Kali Linux:** [Kali Docs](https://www.kali.org/docs/containers/installing-docker-on-kali/)
- **Instalasi GNU Radio:** [GNU Radio Wiki](https://wiki.gnuradio.org/index.php/InstallingGR)
- **Instalasi UHD:** [GNU Radio UHD](https://wiki.gnuradio.org/index.php?title=Draft-AN-445#Building_and_installing_UHD_from_source_code)
- **Repository Docker GNU Radio:** [Git Artes](https://github.com/git-artes/docker-gnuradio)
- **Onnocenter GNU Radio:** [Onnocenter](http://onnocenter.or.id/wiki/index.php/GNURadio)
- **Essential Docker Images:** [OpenVerso Docker Hub](https://hub.docker.com/u/openverso)

---

# 💡 STAY CURIOUS #
