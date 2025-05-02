from Crypto.Cipher import AES
import base64

# 去除补齐的字符
def unpad(text):
    padding_len = text[-1]
    return text[:-padding_len]

# 主解密函数
def aes_decrypt(encrypted_text, key):
    encrypted_data = base64.b64decode(encrypted_text)
    key = key.encode('utf-8')[:16]
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted).decode('utf-8')

# 示例
if __name__ == "__main__":
    encrypted = input("请输入加密后的文本：")
    key = "mysecretpassword"
    decrypted = aes_decrypt(encrypted, key)
    print("解密结果：", decrypted)
