# Tokenizer Tools (Grok + Llama-3)

## Modelos suportados
- **Grok-1**: SentencePiece (`tokenizer.model`)
- **Grok-2**: `alvarobartt/grok-2-tokenizer`
- **Llama-3**: `meta-llama/Meta-Llama-3-8B`

## Uso
```bash
pip install transformers sentencepiece

# Individual
python scripts/grok1_example.py
python scripts/grok2_example.py
python scripts/llama3_example.py

# Comparar todos
python scripts/compare.py "tracking"
```

## Notas
- Llama-3 pode exigir aceite da licença no Hugging Face.
- Grok-1 precisa do arquivo `tokenizer.model` local.
- Vocab Llama-3: 128256 tokens.
