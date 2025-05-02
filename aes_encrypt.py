from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# 补齐函数：使明文长度变为 16 的倍数（PKCS7）
def pad(text):
    padding_len = 16 - len(text) % 16
    return text + chr(padding_len) * padding_len

# 主加密函数
def aes_encrypt(plain_text, key):
    key = key.encode('utf-8')[:16]  # AES-128 使用 16 字节密钥
    iv = get_random_bytes(16)  # 生成随机 IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plain_text).encode('utf-8')
    encrypted = cipher.encrypt(padded_text)
    # 返回 IV + 密文，Base64 编码
    return base64.b64encode(iv + encrypted).decode('utf-8')

# 示例
if __name__ == "__main__":
    plaintext = "这是一段需要加密的文本。"
    key = "mysecretpassword"  # 自定义密钥
    encrypted = aes_encrypt(plaintext, key)
    print("加密结果：", encrypted)
