#!/usr/bin/env python3
"""Exemplo para o tokenizer do Grok-2.

Opção 1 (recomendada): usar o wrapper HF
  pip install transformers
  from transformers import AutoTokenizer
  tok = AutoTokenizer.from_pretrained("alvarobartt/grok-2-tokenizer")

Opção 2: tokenizer.tok.json direto + tiktoken (formato interno)
  Baixe de https://huggingface.co/xai-org/grok-2
"""

def main():
    text = "tracking"
    print(f"Texto: {text}")
    print("---")
    try:
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained("alvarobartt/grok-2-tokenizer")
        ids = tok.encode(text)
        print(f"Grok-2 IDs (via HF wrapper): {ids}")
        print(f"Decode: {tok.decode(ids)}")
    except Exception as e:
        print(f"HF wrapper não disponível ou erro: {e}")
        print("Instale: pip install transformers")
        print("Ou baixe tokenizer.tok.json de https://huggingface.co/xai-org/grok-2")
    print("---")
    print("Vocab size: 131072")

if __name__ == "__main__":
    main()
