from .caesar_cipher import CaesarCipher


class MessageVisualizer(CaesarCipher):
    
    def print_ticket(self):
        table_line = '+'+'='*70+'+'
        title= '|{:^70}|'.format('Caesar Cipher Algo')
        original_message = '|{:^70}|'.format('Original message: '+ self.get_message())
        encrypted_message = '|{:^70}|'.format('Encrypted message: '+ self.encrypted_message())
        decorator = '{:^70}'.format('~')
    
        return f"""
        {decorator}
        {table_line}
        {title}
        {table_line}
        {original_message}
        {encrypted_message}
        {table_line}
        {decorator}
        """


"""
Expected Output with shift == 3

                                          ~
        +======================================================================+
        |                          Caesar Cipher Algo                          |
        +======================================================================+
        |                        Original message: ciao                        |
        |                       Encrypted message: fldr                        |
        +======================================================================+
                                          ~
"""