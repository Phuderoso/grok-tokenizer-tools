#!/usr/bin/env python3
"""Compara Grok-1, Grok-2 e Llama-3."""
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

def try_llama3(text):
    try:
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
        ids = tok.encode(text)
        return ids, tok.decode(ids)
    except Exception as e:
        return None, str(e)

def main():
    text = sys.argv[1] if len(sys.argv) > 1 else "tracking"
    print(f"Texto: {text}\n")

    for name, fn in [("Grok-1", try_grok1), ("Grok-2", try_grok2), ("Llama-3", try_llama3)]:
        ids, dec = fn(text)
        if ids:
            print(f"{name}: {ids}")
            print(f"Decode: {dec}\n")
        else:
            print(f"{name} indisponível: {dec}\n")

if __name__ == "__main__":
    main()
