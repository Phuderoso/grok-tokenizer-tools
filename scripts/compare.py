#!/usr/bin/env python3
"""Compara Grok-1 e Grok-2 no mesmo texto."""
import sys
import sentencepiece as spm
from transformers import AutoTokenizer

def main():
    text = sys.argv[1] if len(sys.argv) > 1 else "gato"
    print(f"Texto: {text}\n")

    # Grok-1
    try:
        sp = spm.SentencePieceProcessor()
        sp.load("tokenizer.model")
        ids = sp.encode(text, out_type=int)
        print(f"Grok-1: {ids}")
        print(f"Decode: {sp.decode(ids)}\n")
    except Exception as e:
        print(f"Grok-1: {e}\n(Baixe tokenizer.model do Grok-1 primeiro)\n")

    # Grok-2
    try:
        tok = AutoTokenizer.from_pretrained("alvarobartt/grok-2-tokenizer")
        ids = tok.encode(text)
        print(f"Grok-2: {ids}")
        print(f"Decode: {tok.decode(ids)}")
    except Exception as e:
        print(f"Grok-2: {e}")

if __name__ == "__main__":
    main()
