# Grok Tokenizer Tools

## Suporte
- **Grok-1**: SentencePiece (`tokenizer.model`)
- **Grok-2**: tiktoken-style / HF wrapper (`alvarobartt/grok-2-tokenizer`)

## Scripts
```bash
# Grok-1 (precisa do tokenizer.model na pasta)
python scripts/grok1_example.py

# Grok-2 (precisa transformers)
pip install transformers
python scripts/grok2_example.py

# Comparar
python scripts/compare.py "tracking"
```

## Visualizador
Abra `visualizer.html`.

## Links
- Grok-1: https://github.com/xai-org/grok-1
- Grok-2: https://huggingface.co/xai-org/grok-2
- Wrapper Grok-2: https://huggingface.co/alvarobartt/grok-2-tokenizer
