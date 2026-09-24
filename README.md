# beercomparer

Vergleicht den Durchschnittspreis für ein Bier (0,5 l) zwischen zwei deutschen Städten.
Die Preise stammen aus dem Lebenshaltungskosten-Vergleich von [Numbeo](https://www.numbeo.com/cost-of-living/).

## Installation

```bash
pip install -r requirements.txt
```

## Aufruf

```bash
python compare.py
```

Das Skript fragt nacheinander nach zwei Städten und gibt die Preise aus, zum Beispiel:

```
Stadt 1: Berlin
Stadt 2: Munich
In Berlin kostet ein Bier (0,5 L) derzeit: ø 4.50€ und in Munich ø 5.00€
```

Die Städtenamen müssen so geschrieben sein, wie Numbeo sie führt (meist englisch, etwa `Munich`, `Cologne`).

## Lizenz

MIT, siehe [LICENSE](LICENSE).
