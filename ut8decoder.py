def utf8_encode(code_point):
    if not isinstance(code_point, int):
        raise TypeError("Code point must be an integer")
    
    if code_point < 0:
        raise ValueError("Code point cannot be negative")
        
    if code_point <= 0x7F:
        return bytes([code_point])
    elif code_point <= 0x7FF:
        return bytes([0xC0 | (code_point >> 6), 
                     0x80 | (code_point & 0x3F)])
    elif code_point <= 0xFFFF:
        return bytes([0xE0 | (code_point >> 12),
                     0x80 | ((code_point >> 6) & 0x3F),
                     0x80 | (code_point & 0x3F)])
    elif code_point <= 0x10FFFF:
        return bytes([0xF0 | (code_point >> 18),
                     0x80 | ((code_point >> 12) & 0x3F),
                     0x80 | ((code_point >> 6) & 0x3F),
                     0x80 | (code_point & 0x3F)])
    else:
        raise ValueError("Code point out of range (maximum is 0x10FFFF)")

def utf8_decode(byte_sequence):
    if not byte_sequence:
        raise ValueError("Empty byte sequence")
        
    if not isinstance(byte_sequence, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")

    # Determine sequence length based on first byte
    first_byte = byte_sequence[0]
    if first_byte <= 0x7F:
        return first_byte, 1
    elif (first_byte & 0xE0) == 0xC0:
        if len(byte_sequence) < 2:
            raise ValueError("Incomplete 2-byte UTF-8 sequence")
        if not (0x80 <= byte_sequence[1] <= 0xBF):
            raise ValueError("Invalid continuation byte")
        return ((first_byte & 0x1F) << 6) | (byte_sequence[1] & 0x3F), 2
    elif (first_byte & 0xF0) == 0xE0:
        if len(byte_sequence) < 3:
            raise ValueError("Incomplete 3-byte UTF-8 sequence")
        if not all(0x80 <= b <= 0xBF for b in byte_sequence[1:3]):
            raise ValueError("Invalid continuation byte")
        return ((first_byte & 0x0F) << 12) | ((byte_sequence[1] & 0x3F) << 6) | (byte_sequence[2] & 0x3F), 3
    elif (first_byte & 0xF8) == 0xF0:
        if len(byte_sequence) < 4:
            raise ValueError("Incomplete 4-byte UTF-8 sequence")
        if not all(0x80 <= b <= 0xBF for b in byte_sequence[1:4]):
            raise ValueError("Invalid continuation byte")
        return ((first_byte & 0x07) << 18) | ((byte_sequence[1] & 0x3F) << 12) | ((byte_sequence[2] & 0x3F) << 6) | (byte_sequence[3] & 0x3F), 4
    else:
        raise ValueError("Invalid UTF-8 first byte")