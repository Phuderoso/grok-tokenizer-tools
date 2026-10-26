---
name: tokenizer-inspector
description: "Inspect real token IDs from public tokenizers (Grok-1/2, Llama-3, Mistral). Use when user asks for token IDs, tokenization comparison, or how models split text. Download public files and run locally. No inventing IDs."
type: tool
lifecycle: active
---

# Tokenizer Inspector

Get real token IDs. Do not invent them.

## When to use
- User asks "what tokens does X produce for Y"
- Compare tokenizers
- Debug why a word splits a certain way

## Workflow
1. Identify the model (Grok-1, Grok-2, Llama-3, Mistral).
2. Download or load the public tokenizer.
3. Run encode. Show IDs + decode.
4. If gated or missing, say so and give the exact command to fix.

## Quick commands
```bash
# Grok-1
curl -L -o tokenizer.model https://github.com/xai-org/grok-1/raw/main/tokenizer.model
python3 -c "
import sentencepiece as spm
sp = spm.SentencePieceProcessor()
sp.load('tokenizer.model')
print(sp.encode('TEXT', out_type=int))
"

# Grok-2
python3 -c "
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained('alvarobartt/grok-2-tokenizer')
print(tok.encode('TEXT'))
"
```

## Rules
- Never invent IDs.
- Prefer public files over approximations.
- Claude has no public tokenizer. State that.
- Show the exact command that produced the numbers.
