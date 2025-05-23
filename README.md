# metadata
Programma, kura tika izveidota praktiskajai daļai.
# Medicīnas datu harmonizācijas un metadatu ģenerēšanas rīki

Šis repozitorijs satur Python skriptus, kas izstrādāti bakalaura darba ietvaros ar mērķi strukturēt, harmonizēt un sagatavot medicīnas datus pētniecībai un atvērtajai zinātnei.

## Saturs

- `01_import_and_preview.py` – CSV datu ielāde un priekšskatījuma tabulu attēlu ģenerēšana.
- `03_smart_harmonize.py` – Datu harmonizācija, kolonnu saskaņošana, dzimuma noteikšana pēc vārda.
- `fix_names.py` – Pacientu vārdu formatēšanas funkcija (pareizrakstība).
- `05_generate_metadata.py` – Automātiska metadatu ģenerēšana JSON formātā.
- `datnes/` – Avotdatu mapes (nav publiski pievienotas).
- `output/` – Harmonizētie rezultāti un attēli.

## Mākslīgā intelekta izmantošana

Daļa no šeit pieejamajiem skriptiem tika veidota ar mākslīgā intelekta rīka **ChatGPT** (OpenAI) atbalstu, izmantojot šādas uzvednes:

- “Izveido Python funkciju, kas harmonizē atšķirīgus kolonnu nosaukumus datu kopās”;
- “Kā no vārda kolonnas mēģināt noteikt dzimumu, izmantojot NLTK vārdu sarakstus?”;
- “Ģenerē JSON metadatus no pandas DataFrame ar datu tipu un aprakstu noteikšanu”;
- “Saglabā pandas DataFrame kā tabulas attēlu ar matplotlib”.

Visa funkcionalitāte tika **pārskatīta, pārbaudīta un pielāgota manuāli**, nodrošinot tās atbilstību konkrētajām datu kopām un bakalaura darba mērķiem.

## Autors

**Jānis Bērziņš**  
Rīgas Tehniskā universitāte  
Bakalaura darbs – 2025
