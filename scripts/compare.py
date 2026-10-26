#!/usr/bin/env python3
"""Compara tokenização entre Grok-1 (SentencePiece) e notas sobre Grok-2.
Coloque tokenizer.model na mesma pasta para o Grok-1.
"""
import sys

def main():
    text = sys.argv[1] if len(sys.argv) > 1 else "tracking"
    print(f"Texto: {text}")
    print("---")
    try:
        import sentencepiece as spm
        sp = spm.SentencePieceProcessor()
        sp.load("tokenizer.model")
        ids = sp.encode(text, out_type=int)
        print(f"Grok-1 IDs: {ids}")
        print(f"Grok-1 tokens: {sp.encode(text, out_type=str)}")
        print(f"Decode: {sp.decode(ids)}")
    except Exception as e:
        print(f"Grok-1: tokenizer.model não encontrado ou erro ({e})")
        print("Baixe de https://github.com/xai-org/grok-1")
    print("---")
    print("Grok-2: use tokenizer.tok.json + tiktoken ou o wrapper HF")
    print("https://huggingface.co/xai-org/grok-2")

if __name__ == "__main__":
    main()
