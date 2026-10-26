#!/usr/bin/env python3
"""Exemplo para o tokenizer do Mistral.

Usa modelo público via Hugging Face.
Requer: pip install transformers
Referência: mistralai/Mistral-7B-v0.1 (ou versões mais novas)
"""

def main():
    text = "tracking"
    print(f"Texto: {text}")
    print("---")
    try:
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
        ids = tok.encode(text)
        print(f"Mistral IDs: {ids}")
        print(f"Decode: {tok.decode(ids)}")
        print(f"Vocab size: {tok.vocab_size}")
    except Exception as e:
        print(f"Erro: {e}")
        print("Instale: pip install transformers")
        print("Modelo: mistralai/Mistral-7B-v0.1")

if __name__ == "__main__":
    main()
