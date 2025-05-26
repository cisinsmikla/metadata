# metadata

Programma, kura tika izveidota praktiskajai daļai.

# Medicīnas datu harmonizācijas, anonimizācijas un metadatu ģenerēšanas rīki

Šis repozitorijs satur Python skriptus, kas izstrādāti bakalaura darba ietvaros ar mērķi **strukturēt, harmonizēt, anonimizēt** un sagatavot medicīnas datus pētniecībai un atvērtajai zinātnei.

## Saturs

- `01_import_and_preview.py` – CSV datu ielāde un priekšskatījuma tabulu attēlu ģenerēšana.
- `03_smart_harmonize.py` – Datu harmonizācija, kolonnu saskaņošana, dzimuma noteikšana pēc vārda.
- `fix_names.py` – Pacientu vārdu formatēšanas funkcija (pareizrakstība).
- `anonymize_auto.py` – Sensitīvo datu automātiska anonimizācija ar hash algoritmu.
- `05_generate_metadata.py` – Automātiska metadatu ģenerēšana JSON formātā.
- `datnes/` – Avotdatu mapes (nav publiski pievienotas).
- `output/` – Harmonizētie un anonimizētie rezultāti, ģenerētie metadati un tabulu attēli.

## Datu aizsardzība un anonimizācija

Repozitorijā iekļauts skripts `anonymize_auto.py`, kas automātiski atpazīst un aizvieto visus potenciāli sensitīvos personas datus (piemēram, vārdus, e-pastus, adreses, identifikatorus) ar neatgriezeniskiem kodiem, izmantojot SHA-256 hash funkciju. Rezultātā iegūtās datu kopas var droši izmantot pētniecībā un kopīgot atvērtajā zinātnē, jo tās vairs nav sasaistāmas ar konkrētu personu.

## Mākslīgā intelekta izmantošana

Daļa no šeit pieejamajiem skriptiem tika veidota ar mākslīgā intelekta rīka **ChatGPT** (OpenAI) atbalstu, izmantojot šādas uzvednes:

- “Izveido Python funkciju, kas harmonizē atšķirīgus kolonnu nosaukumus datu kopās”;
- “Kā no vārda kolonnas mēģināt noteikt dzimumu, izmantojot NLTK vārdu sarakstus?”;
- “Ģenerē JSON metadatus no pandas DataFrame ar datu tipu un aprakstu noteikšanu”;
- “Saglabā pandas DataFrame kā tabulas attēlu ar matplotlib”;
- “Kā veikt sensitīvu lauku anonimizāciju ar hash funkciju”.

Visa funkcionalitāte tika **pārskatīta, pārbaudīta un pielāgota manuāli**, nodrošinot tās atbilstību konkrētajām datu kopām un bakalaura darba mērķiem.

## Rezultātu izmantošana

Sagatavotie rezultāti (`output/` mapē) ietver harmonizētas, anonimizētas datu kopas un to metadatus (`metadata.json`). Šos datus var izmantot statistiskai analīzei, vizualizācijām, mašīnmācīšanās modeļiem vai publicēšanai atvērtajā zinātnē, ievērojot augstākos datu drošības standartus.

## Lietošana

Lai palaistu kādu no skriptiem, izmanto šādu komandu no projekta saknes mapes: 
python scripts/programma.py
Piemēram: python scripts/05_generate_metadata.py
Rezultātā `output/` mapē tiks izveidots attiecīgais rezultātu vai metadatu fails.
## Autors

**Jānis Bērziņš**  
Rīgas Tehniskā universitāte  
Bakalaura darbs – 2025
