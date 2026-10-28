# Kata Tres en Raya (TDD)

Python 3, solo librería estándar.

- `src/tres_en_raya.py` — programa
- `tests/test_tres_en_raya.py` — pruebas escritas a mano
- `ia/prompt.md` — prompt para generar pruebas con IA; `ia/test_tres_en_raya_ia.py` — resultado
- `docs/comparacion.pdf` — presentación comparativa

```
python -m unittest discover -s tests -v
python -m unittest discover -s ia -p "test_*_ia.py" -v
```
