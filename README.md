# Tokenizer Tools

Ferramentas práticas para inspecionar tokenizers públicos.

## O que tem
- Grok-1: baixar `tokenizer.model` e usar SentencePiece
- Grok-2: `alvarobartt/grok-2-tokenizer` via transformers
- Skill: `skills/tokenizer-inspector/SKILL.md` (workflow direto, sem inventar IDs)

## Uso
```bash
# Grok-1
curl -L -o tokenizer.model https://github.com/xai-org/grok-1/raw/main/tokenizer.model
python3 -c "
import sentencepiece as spm
sp = spm.SentencePieceProcessor()
sp.load('tokenizer.model')
print(sp.encode('gato', out_type=int))
"

# Grok-2
pip install transformers
python3 -c "
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained('alvarobartt/grok-2-tokenizer')
print(tok.encode('gato'))
"
```

Resultados reais testados:
- `tracking` → Grok-1: [9618], Grok-2: [63377]
- `gato` → Grok-1: [382, 4707], Grok-2: [231, 2502]
