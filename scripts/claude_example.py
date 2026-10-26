#!/usr/bin/env python3
"""Notas e aproximação para o tokenizer do Claude.

Anthropic não publica o tokenizer oficial do Claude.
Não existe arquivo de vocabulário público equivalente ao Grok ou Llama.

Opções disponíveis (aproximações):
- Xenova/claude-tokenizer (HF) — baseado em tokenizer antigo
- ctok (sanderland) — reconstrução offline de contagem
- API oficial da Anthropic (count_tokens) — só contagem, sem IDs

Este script tenta o Xenova se disponível e avisa sobre as limitações.
"""

def main():
    text = "tracking"
    print(f"Texto: {text}")
    print("---")
    print("Claude: tokenizer oficial NÃO é público.")
    print()
    try:
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained("Xenova/claude-tokenizer")
        ids = tok.encode(text)
        print(f"Aproximação (Xenova/claude-tokenizer): {ids}")
        print(f"Decode: {tok.decode(ids)}")
        print("AVISO: isto NÃO é o tokenizer atual do Claude 3/4.")
    except Exception as e:
        print(f"Xenova não disponível: {e}")
    print()
    print("Alternativas:")
    print("- https://github.com/sanderland/ctok (contagem offline)")
    print("- API Anthropic count_tokens (só número, sem boundaries)")
    print("- https://huggingface.co/Xenova/claude-tokenizer (legado)")

if __name__ == "__main__":
    main()
