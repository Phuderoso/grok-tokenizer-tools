#!/usr/bin/env python3
"""Exemplo mínimo para o tokenizer SentencePiece do Grok-1.
Baixe tokenizer.model de https://github.com/xai-org/grok-1
"""
import sentencepiece as spm

sp = spm.SentencePieceProcessor()
sp.load("tokenizer.model")  # coloque o arquivo na mesma pasta

text = "tracking"
ids = sp.encode(text, out_type=int)
print(f"Texto: {text}")
print(f"IDs: {ids}")
print(f"Decode: {sp.decode(ids)}")
