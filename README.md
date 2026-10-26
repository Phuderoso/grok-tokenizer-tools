# Tokenizer Tools

## Modelos com tokenizer público
- Grok-1 (SentencePiece)
- Grok-2 (`alvarobartt/grok-2-tokenizer`)
- Llama-3 (`meta-llama/Meta-Llama-3-8B`)
- Mistral (`mistralai/Mistral-7B-v0.1`)

## Claude
Anthropic **não publica** o tokenizer.
- Script: `scripts/claude_example.py` (explica limitações + tenta aproximação Xenova)
- Contagem oficial: API `count_tokens` da Anthropic
- Aproximações comunitárias: ctok, Xenova/claude-tokenizer (legado)

## Uso geral
```bash
pip install transformers sentencepiece
python scripts/compare.py "tracking"
```
