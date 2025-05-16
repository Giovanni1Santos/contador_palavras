# 📝 Analisador de Frequência de Palavras em Textos

Um script Python simples que analisa arquivos de texto, conta a frequência de palavras e gera relatórios estatísticos.

## ✨ Funcionalidades

- Extrai texto de arquivos .txt
- Processa o texto (remove pontuação, padroniza capitalização)
- Conta a ocorrência de cada palavra
- Gera relatórios ordenados por frequência
- Exporta resultados para arquivos .txt 

## 🛠️ Como Usar

### Pré-requisitos
- Python 3.x

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/analisador-palavras.git
```
2. Acesse o diretório:
```bash
cd analisador-palavras
```

### Execução
1. Coloque seu arquivo de texto na pasta do projeto (ex.: `documento.txt`)
2. Execute o script:
```bash
python analisador.py
```

### Parâmetros Opcionais
- `-a` ou `--arquivo`: Especifica o arquivo de entrada
```bash
python analisador.py -a documento.txt
```
- `-l` ou `--limite`: Define o número de palavras no ranking
```bash
python analisador.py -a documento.txt -l 20
```

## 📂 Estrutura de Arquivos
```
📁 analisador-palavras/
├── 📄 analisador.py       # Script principal
├── 📄 texto.txt     # Arquivo de exemplo
├── 📄 estatisticas.txt    # Saída gerada
└── 📄 README.md           # Este arquivo
```

## 📊 Exemplo de Saída
```
=== PALAVRAS MAIS FREQUENTES ===
python: 15
programação: 12
dados: 10
análise: 8
texto: 5
```

## 🤝 Contribuição
Contribuições são bem-vindas! Siga estes passos:
1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

