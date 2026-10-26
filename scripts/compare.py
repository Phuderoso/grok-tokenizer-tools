#!/usr/bin/env python3
"""Compara Grok-1, Grok-2, Llama-3 e Mistral."""
import sys

def try_model(name, loader):
    try:
        ids, dec = loader()
        return ids, dec
    except Exception as e:
        return None, str(e)

def main():
    text = sys.argv[1] if len(sys.argv) > 1 else "tracking"
    print(f"Texto: {text}\n")

    models = [
        ("Grok-1", lambda: __import__('sentencepiece').SentencePieceProcessor().load('tokenizer.model') or None),
        ("Grok-2", lambda: __import__('transformers').AutoTokenizer.from_pretrained('alvarobartt/grok-2-tokenizer')),
        ("Llama-3", lambda: __import__('transformers').AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3-8B')),
        ("Mistral", lambda: __import__('transformers').AutoTokenizer.from_pretrained('mistralai/Mistral-7B-v0.1')),
    ]

    # Versão mais limpa
    from transformers import AutoTokenizer
    import sentencepiece as spm

    # Grok-1
    try:
        sp = spm.SentencePieceProcessor()
        sp.load("tokenizer.model")
        ids = sp.encode(text, out_type=int)
        print(f"Grok-1: {ids}\nDecode: {sp.decode(ids)}\n")
    except Exception as e:
        print(f"Grok-1 indisponível: {e}\n")

    # Grok-2
    try:
        tok = AutoTokenizer.from_pretrained("alvarobartt/grok-2-tokenizer")
        ids = tok.encode(text)
        print(f"Grok-2: {ids}\nDecode: {tok.decode(ids)}\n")
    except Exception as e:
        print(f"Grok-2 indisponível: {e}\n")

    # Llama-3
    try:
        tok = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
        ids = tok.encode(text)
        print(f"Llama-3: {ids}\nDecode: {tok.decode(ids)}\n")
    except Exception as e:
        print(f"Llama-3 indisponível: {e}\n")

    # Mistral
    try:
        tok = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
        ids = tok.encode(text)
        print(f"Mistral: {ids}\nDecode: {tok.decode(ids)}\n")
    except Exception as e:
        print(f"Mistral indisponível: {e}\n")

if __name__ == "__main__":
    main()
