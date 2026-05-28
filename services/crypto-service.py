class CryptoService():


    def monitorate_crypto(self, crypto_obj, current_price):
        if crypto_obj.previous_price is None:
            crypto_obj.previous_price = current_price
        
