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