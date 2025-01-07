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