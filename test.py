from ut8decoder import utf8_encode, utf8_decode

if __name__ == "__main__":
    # Test cases
    test_strings = [
        "Hello, World!",  # Basic ASCII
        "こんにちは",      # Japanese
        "🌟 Stars ✨",    # Emojis and special characters
        "Café",          # Accented characters
    ]
    
    print("UTF-8 Encoder/Decoder Test\n")
    
    for test_str in test_strings:
        print(f"Original string: {test_str}")
        
        # Encode each character
        encoded_bytes = bytearray()
        for char in test_str:
            encoded_bytes.extend(utf8_encode(ord(char)))
            
        print(f"UTF-8 bytes: {encoded_bytes}")
        
        # Decode back to string
        decoded_chars = []
        i = 0
        while i < len(encoded_bytes):
            code_point, bytes_used = utf8_decode(encoded_bytes[i:])
            decoded_chars.append(chr(code_point))
            i += bytes_used
            
        decoded_str = ''.join(decoded_chars)
        print(f"Decoded string: {decoded_str}")
        print(f"Roundtrip successful: {test_str == decoded_str}\n")