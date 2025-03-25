'''
Created by Snoolie K (0xilis) on 2025 March 18.
Licensed under MIT. Please credit if using.
'''

import struct

# make a .aar of one contexts.plist file
def wrap_in_aar(input_file, input_mov, output_file):
    # Since I only need to care about a contents.plist (and in the future the mov file), I am hardcoding the header...
    header = bytearray.fromhex("4141303125005459503146504154500E00636F6E74656E74732E706C697374444154418E13")
    
    with open(input_file, 'rb') as f:
        file_data = f.read()
    
    file_size = len(file_data)
    
    if file_size <= 0xFFFF:
        # Our size can fit in a 2 byte AA_FIELD_TYPE_BLOB, yay
        header[-2:] = struct.pack('<H', file_size)
    else:
        '''
        Our contents.plist is over 64KB. This means it won't fit in a uint16_t.
        Instead, we update the A subtype for our DAT (2 byte AA_FIELD_TYPE_BLOB)
        To be a B subtype (4 byte AA_FIELD_TYPE_BLOB). This also means we will
        need to change the header size to 0x27 since we are adding 2 bytes by doing this.
        '''
        header[-3] = 0x42
        header[-2:] = struct.pack('<I', file_size)
        header[4] = 0x27
    # Hardcoded settlingEffect.mov header
    header2 = bytearray.fromhex("4141303129005459503146504154501200736574746C696E674566666563742E6D6F7644415441F4B8")
    
    if isinstance(input_mov, bytes):
        file_data2 = input_mov
    else:
        with open(input_mov, 'rb') as f:
            file_data2 = f.read()
    
    file_size2 = len(file_data2)
    
    if file_size2 <= 0xFFFF:
        # Our size can fit in a 2 byte AA_FIELD_TYPE_BLOB, yay
        header2[-2:] = struct.pack('<H', file_size2)
    else:
        '''
        Our settlingEffect.mov is over 64KB. This means it won't fit in a uint16_t.
        Instead, we update the A subtype for our DAT (2 byte AA_FIELD_TYPE_BLOB)
        To be a B subtype (4 byte AA_FIELD_TYPE_BLOB). This also means we will
        need to change the header size to 0x27 since we are adding 2 bytes by doing this.
        '''
        header2[-3] = 0x42
        header2[-2:] = struct.pack('<I', file_size2)
        header2[4] = 0x2B
    
    # Write the header and file data to the output file
    with open(output_file, 'wb') as f:
        f.write(header)
        f.write(file_data)
        f.write(header2)
        f.write(file_data2)

