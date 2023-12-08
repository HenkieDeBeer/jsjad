# Gebruik van de code
Dit is Python code gemaakt als alternatief voor de site van de TU delft om poly-alfabetische vercijfering te ontcijferen. Hieronder staan de instructie over hoe _main.py_ gebruikt moet worden voor de oefening en opdrachten.

## Bepaal de sleutellengte
_Opzet:_ zet de variabele **TASK** naar "KEYLENGTH"

Plaats de tekst waarvan je de sleutel wilt bepalen in het bestand "vigciphertext.txt". Door de code vervolgens te runnen, krijg je op het console scherm een aantal cijfers te zijn. Dit ziet er ongeveer als volgt uit:

_mogelijkeKeyLengte_ : **aantalOffsetMatches**

Als je bij de mogelijke Keylengtes een patroon ziet, dan is de kleinste waarde van dat patroon waarschijnlijk de lengte van de sleutel. Die vul je in bij **SPLITSCONSTANT**

## Bepaal per subset de letter
_Opzet:_ zet de variabele **TASK** naar "SPLITANDSHIFT"

Als je de sleutellengte weet, dan kun je de letters die bij elkaar behoren splitsen. Voor een sleutellenge van 2 en het versleutelde woord _abcdef_ betekend dat de eerste subset de letters _ace_ bevat en de tweede subset _bdf_. 
Voor de variabele **SHOWSUBSET** vul je dan de nummer van de subset in die je wilt ziet. Als je een sleutellengte van 6 hebt, dan zijn je mogelijkheden: 1, 2, 3, 4, 5, en 6.

Je kunt nu per subset van letters zien hoe vaak de letters voor komt in de subset. Nu moet je door middel van het invullen van de **SHIFT** (0 <= **SHIFT** < 26 ) bepalen hoe veel verplaatsing er is geweest. Dit doe je door de letter die het vaak voor komt naar de E te krijgen. 
Als dit gelukt is, dan staat er bovenaan met welke letter die letters versleuteld zijn. Dit doe je voor iedere subset, waardoor je de sleuter krijgt.

## Ontcijferen
_Opzet:_ zet de variabele **TASK** naar "DECODE"

Als je de sleutel hebt, dan vul je die in bij **KEY**. Door het programma nu te runnen, krijg je ontsleutelde tekst.
