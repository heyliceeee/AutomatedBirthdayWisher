# 🎉 Automated Birthday Wisher

Sistema automático que envia mensagens de aniversário personalizadas por email, utilizando dados de um ficheiro CSV e templates de cartas.

---

## 📌 Funcionalidades

- Verifica diariamente se alguém faz anos.
- Calcula automaticamente a idade com base no ano de nascimento.
- Seleciona aleatoriamente um template de mensagem.
- Substitui placeholders como **[NAME]** e **[AGE]**.
- Envia emails personalizados através de SMTP.
- Suporta caracteres especiais (UTF‑8).

---

## 📁 Estrutura dos dados

### **birthdays.csv**
Contém:
- Nome  
- Email  
- Dia  
- Mês  
- Ano de nascimento  

### **letter_templates/**
Pasta com mensagens de aniversário contendo placeholders:
- `[NAME]`
- `[AGE]`

---

## 🔧 Configuração

As credenciais SMTP são carregadas a partir de variáveis de ambiente:

- `SMTP_HOST`  
- `SMTP_PORT`  
- `SMTP_EMAIL`  
- `SMTP_PASSWORD`

---

## 🚀 Funcionamento

1. Carrega os dados de aniversário.
2. Compara a data atual com as datas do ficheiro.
3. Para cada aniversariante:
   - Escolhe um template aleatório.
   - Substitui os placeholders.
   - Envia o email personalizado.
4. Caso não haja aniversários, informa no terminal.

---

## 📨 Objetivo

Automatizar o envio de mensagens de aniversário, garantindo que ninguém fica sem uma palavra especial no seu dia.
