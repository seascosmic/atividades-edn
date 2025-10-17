# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.

senha = input("Digite sua senha: ")

tem_maiuscula = any(c.isupper() for c in senha)
tem_minuscula = any(c.islower() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
tem_caractere_especial = any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|\\`~" for c in senha)
tamanho_valido = len(senha) >= 8

if all([tem_maiuscula, tem_minuscula, tem_numero, tem_caractere_especial, tamanho_valido]):
    print("✅ Senha forte! Todos os critérios foram atendidos.")
else:
    print("⚠️ Senha fraca. Verifique os critérios abaixo:")
    if not tamanho_valido:
        print("- Deve ter pelo menos 8 caracteres.")
    if not tem_maiuscula:
        print("- Deve conter pelo menos uma letra maiúscula.")
    if not tem_minuscula:
        print("- Deve conter pelo menos uma letra minúscula.")
    if not tem_numero:
        print("- Deve conter pelo menos um número.")
    if not tem_caractere_especial:
        print("- Deve conter pelo menos um caractere especial (!, @, #, $, etc.)")
