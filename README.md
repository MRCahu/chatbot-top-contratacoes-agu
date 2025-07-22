# 🤖 Chatbot para Consulta do Instrumento de Padronização AGU

Este projeto demonstra uma abordagem simples de RAG (Retrieval-Augmented Generation) aplicada ao documento **"Instrumento de Padronização dos Procedimentos de Contratação - AGU (Fev 2024)"**. A solução utiliza LangChain, embeddings locais e ChromaDB para responder perguntas com base no conteúdo do PDF.

---

## 📚 Visão Geral

1. O PDF é carregado e dividido em páginas.
2. Cada página é convertida em embeddings com Hugging Face.
3. Os vetores são armazenados em uma base ChromaDB local.
4. Um modelo da OpenAI é utilizado para gerar as respostas.

---

## 🚀 Tecnologias Utilizadas

- Python 3.11
- [LangChain](https://github.com/langchain-ai/langchain)
- [ChromaDB](https://github.com/chroma-core/chroma)
- [Hugging Face Transformers](https://github.com/huggingface/transformers)

---

## 🛠️ Como Rodar

1. Instale as dependências em um ambiente virtual:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Defina a variável `OPENAI_API_KEY` com sua chave da OpenAI.
3. Execute o script de exemplo:
   ```bash
   python chatbot_pdf.py --pdf inputs/Instrumento_AGU.pdf
   ```
4. Envie suas perguntas no prompt e digite `sair` para finalizar.

---

## 📄 Estrutura

```
chatbot-top-contratacoes-agu/
├── chatbot_pdf.py       # Script de linha de comando
├── chatbot_pdf.ipynb    # Notebook original
├── inputs/
│   └── Instrumento_AGU.pdf
├── requirements.txt
└── README.md
```
