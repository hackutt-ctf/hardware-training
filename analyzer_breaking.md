### Est ce que le logical analyzer est un menteur

Travail avec un Logic Analyzer générique: Analyzer 24MHz8CH


Signal envoyé avec une Arduino Leonardo.


Verification des résultats faite avec le logiciel Saleae Logic 2: https://www.saleae.com/pages/downloads

## Résultats:

Envoie du signal de la clock peu fiable à cause de la carte => Il serait préférable de tester avec une Uno ou une Micro.

Lorsque l'on send un signal carré avec ce snippet à 16MHz:

```
  pinMode(9, OUTPUT);  // Pin 9 = OC1A (Output Compare)

  TCCR1A = _BV(COM1A0);  // Toggle OC1A (Pin 9) on Compare Match
  TCCR1B = _BV(WGM12) | _BV(CS10);  // CTC Mode, No Prescaler
  OCR1A = 0;
```

On obtient une signal constant mais la partie haute est très wide (70% ~)


Le reste des fréquences est correct (<55%)