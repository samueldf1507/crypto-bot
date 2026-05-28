class CryptoService():


    def calculate_variation (self, crypto_obj, current_price, current_volume):
        if crypto_obj.previous_price is None:
            
            return
        
        difference_price = current_price - crypto_obj.previous_price
        diferenca_volume = current_volume - crypto_obj.previous_volume

        crypto_obj.previous_price = current_price
        crypto_obj.previous_volume = current_volume

        return {
            "variacao_preco": difference_price,
            "variacao_volume": diferenca_volume
        }

        
        

        
