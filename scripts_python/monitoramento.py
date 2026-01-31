import subprocess

def verificar_servidores():
    print("--- 🤖 Iniciando Sistema de Automação ---")
    print("Verificando status do Target 2 (Windows)...")
    
    # Comando que o Python vai executar
    comando = ["ansible", "win2", "-i", "hosts.ini", "-m", "win_ping"]
    
    try:
        # Executa o comando e captura a saída
        resultado = subprocess.run(comando, capture_output=True, text=True)
        
        if "SUCCESS" in resultado.stdout:
            print("✅ Status: Servidor Online e Pronto!")
            print(f"Retorno do Windows: {resultado.stdout}")
        else:
            print("⚠️ Status: Servidor respondeu com erro.")
            print(resultado.stderr)
            
    except Exception as e:
        print(f"❌ Erro ao tentar rodar a automação: {e}")

if __name__ == "__main__":
    verificar_servidores()

 