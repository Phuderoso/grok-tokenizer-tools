#!/usr/bin/env python3
"""Compara Grok-1 (SentencePiece) e Grok-2 (HF wrapper)."""
import sys

def try_grok1(text):
    try:
        import sentencepiece as spm
        sp = spm.SentencePieceProcessor()
        sp.load("tokenizer.model")
        ids = sp.encode(text, out_type=int)
        return ids, sp.decode(ids)
    except Exception as e:
        return None, str(e)

def try_grok2(text):
    try:
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained("alvarobartt/grok-2-tokenizer")
        ids = tok.encode(text)
        return ids, tok.decode(ids)
    except Exception as e:
        return None, str(e)

def main():
    text = sys.argv[1] if len(sys.argv) > 1 else "tracking"
    print(f"Texto: {text}\n")

    ids1, dec1 = try_grok1(text)
    if ids1:
        print(f"Grok-1: {ids1}")
        print(f"Decode: {dec1}")
    else:
        print(f"Grok-1 indisponível: {dec1}")
        print("Baixe tokenizer.model de https://github.com/xai-org/grok-1")

    print()
    ids2, dec2 = try_grok2(text)
    if ids2:
        print(f"Grok-2: {ids2}")
        print(f"Decode: {dec2}")
    else:
        print(f"Grok-2 indisponível: {dec2}")
        print("pip install transformers")
        print("Usa alvarobartt/grok-2-tokenizer")

if __name__ == "__main__":
    main()
