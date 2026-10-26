#!/usr/bin/env python3
"""Exemplo para o tokenizer do Llama-3.

Usa o tokenizer público via Hugging Face.
Requer: pip install transformers
Modelo de referência: meta-llama/Meta-Llama-3-8B (ou 70B)
"""

def main():
    text = "tracking"
    print(f"Texto: {text}")
    print("---")
    try:
        from transformers import AutoTokenizer
        # Tokenizer público do Llama-3
        tok = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
        ids = tok.encode(text)
        print(f"Llama-3 IDs: {ids}")
        print(f"Decode: {tok.decode(ids)}")
        print(f"Vocab size: {tok.vocab_size}")
    except Exception as e:
        print(f"Erro: {e}")
        print("Instale: pip install transformers")
        print("Pode precisar de acesso ao modelo no Hugging Face (aceitar licença).")
        print("Alternativa: use um tokenizer Llama-3 já baixado localmente.")

if __name__ == "__main__":
    main()
