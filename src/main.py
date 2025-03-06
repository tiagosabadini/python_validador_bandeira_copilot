def main():
    import argparse

    description = "Validador de bandeira de cartão de crédito"
    parser = argparse.ArgumentParser(description=description)
    
    args = parser.parse_args()
    
    print(f"Welcome to {description}")
    
    card_number = input("Digite o número do cartão de crédito: ")
    card_number = ''.join(filter(str.isdigit, card_number))
    if not card_number.isdigit():
        print("Por favor, insira apenas números.")
        return
    print(f"Número do cartão recebido: {card_number}")

    def validate_card(card_number):
        if card_number.startswith('4'):
            return "Visa"
        elif 51 <= int(card_number[:2]) <= 55 or 2221 <= int(card_number[:4]) <= 2720:
            return "MasterCard"
        elif card_number.startswith(('34', '37')):
            return "American Express"
        elif card_number.startswith('6011') or card_number.startswith('65') or 644 <= int(card_number[:3]) <= 649:
            return "Discover"
        elif card_number.startswith('6062'):
            return "Hipercard"
        else:
            return "Elo" # essa implementação não está boa, mas é só um exemplo

    card_type = validate_card(card_number)
    print(f"Tipo de cartão: {card_type}")

if __name__ == "__main__":
    main()