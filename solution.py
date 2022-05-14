def solution(s):
    # Your code here
    # build a text to Braille encoder dictionary from the example given
    # enter variable information from the provided sample data 
    sample_text = "The quick brown fox jumps over the lazy dog"
    sample_output = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    
    # establish and remove the Braille capitalization mark
    cap_mark = sample_output[:6]
    sample_chars_code = sample_output[6:]
    
    # match the characters to their code to complete the dictionary
    encoder_dict = {}
    for char in sample_text:
        encoder_dict[char.lower()] = str(sample_chars_code[:6])
        sample_chars_code = sample_chars_code[6:]
        
    # use the Braille encoder to transform the signage
    encoded = ''
    for char in s:
        if char.isupper():
            encoded += cap_mark
        encoded += encoder_dict[char.lower()]
        
    return encoded

sign = input('What does the sign say? ')
print('Here is the message, encoded for Braille: {}'.format(solution(sign)))
