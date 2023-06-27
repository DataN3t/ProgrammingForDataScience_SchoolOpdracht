# ProgrammingForDataScience_SchoolOpdracht
## S&P 500 tradingbot met data transformatie

### Business understanding

Door de jaren heen is algoritmisch handelen een integraal onderdeel geworden van de financiële markten. Geautomatiseerde handel, met behulp van handelsalgoritmen en bots, is populair geworden vanwege het vermogen om transacties veel sneller uit te voeren dan menselijke handelaren en om potentiële marktinefficiënties of trends te benutten.

Dit project heeft als doel een handelsbot te creëren die een eenvoudige maar effectieve strategie gebruikt die bekend staat als Drie Voortschrijdende Gemiddelden. Deze strategie gebruikt drie Eenvoudige Voortschrijdende Gemiddelden (SMAs) van de slotkoersen met verschillende tijdvensters (kort, midden, lang) om koop- of verkoopsignalen te genereren. De bot neemt historische gegevens voor de S&P 500-index en past deze strategie toe om handelsbeslissingen te nemen.

De zakelijke doelstellingen van deze bot zijn:

•	Automatisering: 
Verminder de behoefte aan handmatige interventie in handelsbeslissingen, waardoor tijd en middelen worden vrijgemaakt.

•	Benutten van Markttrends: 
Gebruik voortschrijdende gemiddelden om potentiële markttrends te identificeren en dienovereenkomstig transacties uit te voeren om mogelijk winst te genereren.

•	Schaalbaarheid en Snelheid: 
De bot kan een groot aantal transacties snel en efficiënt uitvoeren.

•	Risicobeheer: 
Door de bot te implementeren als onderdeel van een gediversifieerde beleggingsstrategie, kan het helpen om risico's te beheren en mogelijk rendementen te verbeteren.


### Data understanding

Deze handelsbot maakt gebruik van historische datagegevens van de S&P 500-index. Hier is een uitleg van de gegevens:

•	Bron: Gegevens zijn afkomstig van Yahoo Finance en Kaggle(SP500 CSV dataset), dat is een gerenommeerde aanbieder van financiële marktgegevens.


•	Velden: De dataset bevat de volgende velden:
o	            Open: De openingskoers van de index voor de handelsdag.
o	            High: De hoogste koers van de index tijdens de handelsdag.
o	            Low: De laagste koers van de index tijdens de handelsdag.
o	            Close: De slotkoers van de index voor de handelsdag.
o	            Adj Close: De aangepaste slotkoers die rekening houdt met dividenden en aandelensplitsingen.
o	            Volume: Het aantal verhandelde aandelen tijdens de handelsdag.

•	Afgeleide Velden: Daarnaast zijn er enkele aangemaakte kenmerken:

__Log_Returns:__ Vertegenwoordigt de logaritmische rendementen die worden gebruikt om relatieve veranderingen in de waarde van de index te analyseren.
__Normalized_Adj_Close:__ Dit is de aangepaste slotkoers genormaliseerd door de maximale aangepaste slotkoers. __Rolling_Mean:__ Het voortschrijdend gemiddelde van de aangepaste slotkoers over een periode van 21 dagen. __Tijdsbereik:__ De gegevens beslaan de periode van 1 januari 2000 tot 20 juni 2023. Het is belangrijk om voldoende gegevens te hebben om de strategie te backtesten in verschillende marktomstandigheden.

### Wat Maakt Deze Trading Bot Uniek
Hoewel de kernstrategie (Drie Voortschrijdende Gemiddelden) op zichzelf niet uniek is, aangezien het een veelgebruikte strategie is onder handelaren, kan de implementatie en combinatie van verschillende elementen deze bot onderscheiden:

Aanpasbare Parameters: De bot staat aanpassing van de perioden voor de korte, middellange en lange SMAs toe. Hiermee kan de strategie worden verfijnd op basis van verschillende marktomstandigheden.
Data Engineering: De bot bevat aanvullende stappen voor data-engineering, zoals normalisatie en berekening van logaritmische rendementen, die kunnen worden gebruikt om complexere strategieën te ontwikkelen.
Logging en Notificaties: De bot gebruikt logging om real-time informatie te geven over de uitvoering van transacties, en meldingen voor wijzigingen in de orderstatus. Dit helpt bij monitoring en probleemoplossing.
Flexibiliteit in Gegevensbronnen: De bot kan gegevens ophalen van Yahoo Finance als alternatief voor het geval de primaire CSV-gegevensbron niet werkt, wat zorgt voor robuustheid in het ophalen van gegevens.

