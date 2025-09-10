import re
import getpass
from datetime import datetime

class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password
        self.strength = 0
        self.feedback = []
    
    def check_length(self):
        """Verifica o comprimento da senha"""
        if len(self.password) >= 12:
            self.strength += 2
            self.feedback.append("✓ Senha longa (12+ caracteres)")
        elif len(self.password) >= 8:
            self.strength += 1
            self.feedback.append("✓ Comprimento adequado (8+ caracteres)")
        else:
            self.feedback.append("✗ Senha muito curta (mínimo 8 caracteres recomendado)")
    
    def check_uppercase(self):
        """Verifica se contém letras maiúsculas"""
        if re.search(r'[A-Z]', self.password):
            self.strength += 1
            self.feedback.append("✓ Contém letras maiúsculas")
        else:
            self.feedback.append("✗ Adicione letras maiúsculas")
    
    def check_lowercase(self):
        """Verifica se contém letras minúsculas"""
        if re.search(r'[a-z]', self.password):
            self.strength += 1
            self.feedback.append("✓ Contém letras minúsculas")
        else:
            self.feedback.append("✗ Adicione letras minúsculas")
    
    def check_numbers(self):
        """Verifica se contém números"""
        if re.search(r'[0-9]', self.password):
            self.strength += 1
            self.feedback.append("✓ Contém números")
        else:
            self.feedback.append("✗ Adicione números")
    
    def check_special_chars(self):
        """Verifica se contém caracteres especiais"""
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', self.password):
            self.strength += 1
            self.feedback.append("✓ Contém caracteres especiais")
        else:
            self.feedback.append("✗ Adicione caracteres especiais (!@#$% etc.)")
    
    def check_common_passwords(self):
        """Verifica se é uma senha comum"""
        common_passwords = ['password', '123456', 'qwerty', 'admin', 'welcome']
        if self.password.lower() not in common_passwords:
            self.strength += 1
            self.feedback.append("✓ Não é uma senha comum")
        else:
            self.feedback.append("✗ Esta senha é muito comum e fácil de adivinhar")
    
    def check_sequential_chars(self):
        """Verifica sequências óbvias"""
        sequences = ['123', 'abc', 'qwe', 'asd', 'xyz']
        for seq in sequences:
            if seq in self.password.lower():
                self.feedback.append("✗ Evite sequências óbvias como '123' ou 'abc'")
                return
        self.strength += 1
        self.feedback.append("✓ Não contém sequências óbvias")
    
    def analyze(self):
        """Executa todas as verificações"""
        self.check_length()
        self.check_uppercase()
        self.check_lowercase()
        self.check_numbers()
        self.check_special_chars()
        self.check_common_passwords()
        self.check_sequential_chars()
        
        # Classifica a força da senha
        if self.strength >= 6:
            rating = "FORTE"
        elif self.strength >= 4:
            rating = "MEDIANA"
        else:
            rating = "FRACA"
        
        return self.strength, rating, self.feedback

def main():
    print("=== ANALISADOR DE FORÇA DE SENHAS ===")
    print("Este programa analisa a força da sua senha baseado em critérios de segurança")
    print("\nDica: Use uma senha que você não utiliza em nenhum serviço real!")
    
    password = input("\nDigite a senha para análise: ")
    
    analyzer = PasswordAnalyzer(password)
    strength, rating, feedback = analyzer.analyze()
    
    print(f"\nPontuação: {strength}/7")
    print(f"Classificação: {rating}")
    
    print("\nDetalhes:")
    for item in feedback:
        clean_item = item.replace("✓", "[OK]").replace("✗", "[X]")
        print(f"  {clean_item}")
    
    # Gera relatorio
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("relatorio_senha.txt", "a", encoding="utf-8") as f:
            f.write(f"\n--- Análise em {timestamp} ---\n")
            f.write(f"Senha: {'*' * len(password)}\n")
            f.write(f"Pontuação: {strength}/7\n")
            f.write(f"Classificação: {rating}\n")
            f.write("Feedback:\n")
            for item in feedback:
                clean_item = item.replace("✓", "[OK]").replace("✗", "[X]")
                f.write(f"  {clean_item}\n")
    except Exception as e:
        print(f"Erro ao salvar relatório: {e}")

if __name__ == "__main__":
    main()