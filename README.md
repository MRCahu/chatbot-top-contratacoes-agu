# 🤖 Chatbot para Consulta do Instrumento de Padronização AGU

Projeto desenvolvido como prática de construção de um sistema de RAG (Retrieval-Augmented Generation) usando Python, LangChain, Hugging Face e ChromaDB.

---

## 📚 Visão Geral

Este chatbot foi projetado para responder perguntas baseadas no conteúdo do documento:

> **"Instrumento de Padronização dos Procedimentos de Contratação - AGU (Fev 2024)"**

Utiliza técnicas de:
- Extração de texto de PDFs
- Criação de embeddings locais com Hugging Face
- Busca vetorial inteligente usando ChromaDB
- Implementação de fluxo de perguntas e respostas simulando um assistente jurídico

---

## 🚀 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-orange)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow)

- Python 3.11
- LangChain
- LangChain-Community
- LangChain-Huggingface
- ChromaDB
- Sentence-Transformers
- Gradio (futuras melhorias)
- Jupyter Notebook

---

## 🛠️ Como Rodar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/chatbot-top-contratacoes-agu.git
cd chatbot-top-contratacoes-agu
