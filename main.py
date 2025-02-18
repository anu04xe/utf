def utf8_encode(code_point):
    if code_point <= 0x7F:
        return bytes([code_point])
    elif code_point <= 0x7FF:
        return bytes([0xC0 | (code_point >> 6), 0x80 | (code_point & 0x3F)])
    elif code_point <= 0xFFFF:
        return bytes([0xE0 | (code_point >> 12), 0x80 | ((code_point >> 6) & 0x3F), 0x80 | (code_point & 0x3F)])
    elif code_point <= 0x10FFFF:
        return bytes([0xF0 | (code_point >> 18), 0x80 | ((code_point >> 12) & 0x3F), 0x80 | ((code_point >> 6) & 0x3F), 0x80 | (code_point & 0x3F)])
    else:
        raise ValueError("Code point out of range")

def utf8_decode(byte_sequence):
    if byte_sequence[0] <= 0x7F:
        return byte_sequence[0], 1
    elif (byte_sequence[0] & 0xE0) == 0xC0:
        return ((byte_sequence[0] & 0x1F) << 6) | (byte_sequence[1] & 0x3F), 2
    elif (byte_sequence[0] & 0xF0) == 0xE0:
        return ((byte_sequence[0] & 0x0F) << 12) | ((byte_sequence[1] & 0x3F) << 6) | (byte_sequence[2] & 0x3F), 3
    elif (byte_sequence[0] & 0xF8) == 0xF0:
        return ((byte_sequence[0] & 0x07) << 18) | ((byte_sequence[1] & 0x3F) << 12) | ((byte_sequence[2] & 0x3F) << 6) | (byte_sequence[3] & 0x3F), 4
    else:
        raise ValueError("Invalid UTF-8 sequence")