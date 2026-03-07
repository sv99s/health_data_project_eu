import pandas as pd
from pathlib import Path

# ===========================
# Mappings English → Italian
# ===========================
country_map = {
    'AT': 'Austria', 'BE': 'Belgio', 'BG': 'Bulgaria', 'CY': 'Cipro',
    'CZ': 'Repubblica Ceca', 'DE': 'Germania', 'DK': 'Danimarca', 'EE': 'Estonia',
    'EL': 'Grecia', 'ES': 'Spagna', 'FI': 'Finlandia', 'FR': 'Francia',
    'HR': 'Croazia', 'HU': 'Ungheria', 'IE': 'Irlanda', 'IT': 'Italia',
    'LT': 'Lituania', 'LU': 'Lussemburgo', 'LV': 'Lettonia', 'MT': 'Malta',
    'NL': 'Paesi Bassi', 'PL': 'Polonia', 'PT': 'Portogallo', 'RO': 'Romania',
    'SE': 'Svezia', 'SI': 'Slovenia', 'SK': 'Slovacchia'
}

disease_map = {
    # Prevalence chronic diseases
    'Allergy': 'Allergia',
    'Arthrosis': 'Artrosi',
    'Asthma': 'Asma',
    'Coronary heart disease or angina pectoris': 'Cardiopatia coronarica o angina pectoris',
    'Chronic lower respiratory diseases (excluding asthma)': 'Malattie croniche delle vie respiratorie inferiori (escl. asma)',
    'Cirrhosis of the liver': 'Cirrosi epatica',
    'Diabetes': 'Diabete',
    'Chronic depression': 'Depressione cronica',
    'High blood lipids': 'Alti lipidi nel sangue',
    'High blood pressure': 'Ipertensione',
    'Heart attack or chronic consequences of heart attack': 'Infarto o conseguenze croniche dell\'infarto',
    'Kidney problems': 'Problemi renali',
    'Low back disorder or other chronic back defect': 'Disturbi lombari o altri difetti cronici della schiena',
    'Neck disorder or other chronic neck defect': 'Disturbi del collo o altri difetti cronici del collo',
    'Stroke or chronic consequences of stroke': 'Ictus o conseguenze croniche dell\'ictus',
    'Urinary incontinence, problems in controlling the bladder': 'Incontinenza urinaria, problemi di controllo della vescica',

    # Mortality causes
    'Tuberculosis': 'Tubercolosi',
    'Accidents (V01-X59, Y85, Y86)': 'Incidenti (V01-X59, Y85, Y86)',
    'Other accidents (W20-W64, W75-X39, X50-X59, Y86)': 'Altri incidenti (W20-W64, W75-X39, X50-X59, Y86)',
    'Certain infectious and parasitic diseases (A00-B99)': 'Alcune malattie infettive e parassitarie (A00-B99)',
    'Other infectious and parasitic diseases (remainder of A00-B99)': 'Altre malattie infettive e parassitarie (resto di A00-B99)',
    'Viral hepatitis and sequelae of viral hepatitis': 'Epatite virale e sequele dell\'epatite virale',
    'Chronic viral hepatitis B and C': 'Epatite virale cronica B e C',
    'Human immunodeficiency virus [HIV] disease': 'Malattia da virus dell\'immunodeficienza umana [HIV]',
    'Malignant neoplasms (C00-C97)': 'Neoplasie maligne (C00-C97)',
    'Malignant neoplasm of lip, oral cavity, pharynx': 'Neoplasia maligna di labbra, cavità orale, faringe',
    'Neoplasms': 'Neoplasie',
    'Malignant neoplasm of oesophagus': 'Neoplasia maligna dell\'esofago',
    'Malignant neoplasm of stomach': 'Neoplasia maligna dello stomaco',
    'Malignant neoplasm of colon, rectosigmoid junction, rectum, anus, and anal canal': 'Neoplasia maligna del colon, retto, giunzione rettosigmoidea, ano e canale anale',
    'Malignant neoplasm of liver and intrahepatic bile ducts': 'Neoplasia maligna del fegato e dei dotti biliari intraepatici',
    'Malignant neoplasm of pancreas': 'Neoplasia maligna del pancreas',
    'Malignant neoplasm of larynx': 'Neoplasia maligna della laringe',
    'Malignant neoplasm of trachea, bronchus and lung': 'Neoplasia maligna di trachea, bronchi e polmoni',
    'Malignant melanoma of skin': 'Melanoma maligno della pelle',
    'Malignant neoplasm of breast': 'Neoplasia maligna della mammella',
    'Malignant neoplasm of cervix uteri': 'Neoplasia maligna della cervice uterina',
    'Malignant neoplasm of other parts of uterus': 'Neoplasia maligna di altre parti dell\'utero',
    'Malignant neoplasm of ovary': 'Neoplasia maligna dell\'ovaio',
    'Malignant neoplasm of prostate': 'Neoplasia maligna della prostata',
    'Malignant neoplasm of kidney, except renal pelvis': 'Neoplasia maligna del rene, escluso il bacinetto renale',
    'Malignant neoplasm of bladder': 'Neoplasia maligna della vescica',
    'Malignant neoplasm of brain and central nervous system': 'Neoplasia maligna del cervello e del sistema nervoso centrale',
    'Malignant neoplasm of thyroid gland': 'Neoplasia maligna della tiroide',
    'Hodgkin disease and lymphomas': 'Malattia di Hodgkin e linfomi',
    'Other malignant neoplasm of lymphoid, haematopoietic and related tissue': 'Altre neoplasie maligne del tessuto linfoide, ematopoietico e correlato',
    'Leukaemia': 'Leucemia',
    'Other malignant neoplasms (remainder of C00-C97)': 'Altre neoplasie maligne (resto C00-C97)',
    'Non-malignant neoplasms (benign and uncertain)': 'Neoplasie non maligne (benigne e incerte)',
    'Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism': 'Malattie del sangue e degli organi emopoietici e alcuni disturbi del sistema immunitario',
    'Endocrine, nutritional and metabolic diseases (E00-E90)': 'Malattie endocrine, nutrizionali e metaboliche (E00-E90)',
    'Diabetes mellitus': 'Diabete mellito',
    'Other endocrine, nutritional and metabolic diseases (remainder of E00-E90)': 'Altre malattie endocrine, nutrizionali e metaboliche (resto E00-E90)',
    'Mental and behavioural disorders (F00-F99)': 'Disturbi mentali e comportamentali (F00-F99)',
    'Dementia': 'Demenza',
    'Mental and behavioural disorders due to use of alcohol': 'Disturbi mentali e comportamentali dovuti all\'uso di alcol',
    'Other mental and behavioural disorders (remainder of F00-F99)': 'Altri disturbi mentali e comportamentali (resto F00-F99)',
    'Parkinson disease': 'Morbo di Parkinson',
    'Alzheimer disease': 'Malattia di Alzheimer',
    'Diseases of the nervous system and the sense organs (G00-H95)': 'Malattie del sistema nervoso e degli organi di senso (G00-H95)',
    'Other diseases of the nervous system and the sense organs (remainder of G00-H95)': 'Altre malattie del sistema nervoso e degli organi di senso (resto G00-H95)',
    'Diseases of the circulatory system (I00-I99)': 'Malattie del sistema circolatorio (I00-I99)',
    'Ischaemic heart diseases': 'Cardiopatie ischemiche',
    'Other ischaemic heart diseases': 'Altre cardiopatie ischemiche',
    'Acute myocardial infarction including subsequent myocardial infarction': 'Infarto miocardico acuto incluso infarto successivo',
    'Other heart diseases': 'Altre malattie cardiache',
    'Cerebrovascular diseases': 'Malattie cerebrovascolari',
    'Other diseases of the circulatory system (remainder of I00-I99)': 'Altre malattie del sistema circolatorio (resto I00-I99)',
    'Diseases of the respiratory system (J00-J99)': 'Malattie del sistema respiratorio (J00-J99)',
    'Influenza (including swine flu)': 'Influenza (inclusa influenza suina)',
    'Pneumonia': 'Polmonite',
    'Other lower respiratory diseases': 'Altre malattie respiratorie inferiori',
    'Chronic lower respiratory diseases': 'Malattie croniche delle vie respiratorie inferiori',
    'Asthma and status asthmaticus': 'Asma e status asthmaticus',
    'Other diseases of the respiratory system (remainder of J00-J99)': 'Altre malattie del sistema respiratorio (resto J00-J99)',
    'Diseases of the digestive system (K00-K93)': 'Malattie del sistema digestivo (K00-K93)',
    'Ulcer of stomach, duodenum and jejunum': 'Ulcera di stomaco, duodeno e digiuno',
    'Chronic liver disease': 'Malattie croniche del fegato',
    'Chronic liver disease (excluding alcoholic and toxic liver disease)': 'Malattie croniche del fegato (escl. alcoliche e tossiche)',
    'Other diseases of the digestive system (remainder of K00-K93)': 'Altre malattie del sistema digestivo (resto K00-K93)',
    'Diseases of the skin and subcutaneous tissue (L00-L99)': 'Malattie della pelle e del tessuto sottocutaneo',
    'Diseases of the musculoskeletal system and connective tissue (M00-M99)': 'Malattie del sistema muscoloscheletrico e del tessuto connettivo',
    'Other diseases of the musculoskeletal system and connective tissue (remainder of M00-M99)': 'Altre malattie del sistema muscoloscheletrico e del tessuto connettivo (resto M00-M99)',
    'Diseases of the genitourinary system (N00-N99)': 'Malattie del sistema genitourinario (N00-N99)',
    'Diseases of kidney and ureter': 'Malattie del rene e dell\'uretere',
    'Other diseases of the genitourinary system (remainder of N00-N99)': 'Altre malattie del sistema genitourinario (resto N00-N99)',
    'Pregnancy, childbirth and the puerperium (O00-O99)': 'Gravidanza, parto e puerperio (O00-O99)',
    'Certain conditions originating in the perinatal period (P00-P96)': 'Alcune condizioni del periodo perinatale (P00-P96)',
    'Congenital malformations, deformations and chromosomal abnormalities (Q00-Q99)': 'Malformazioni congenite, deformazioni e anomalie cromosomiche (Q00-Q99)',
    'Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified (R00-R99)': 'Sintomi, segni e risultati clinici e di laboratorio anomali (R00-R99)',
    'Sudden infant death syndrome': 'Sindrome della morte improvvisa infantile',
    'Ill-defined and unknown causes of mortality': 'Cause di mortalità non definite e sconosciute',
    'Rheumatoid arthritis and arthrosis (M05-M06,M15-M19)': 'Artrite reumatoide e artrosi (M05-M06,M15-M19)',
    'Other symptoms, signs and abnormal clinical and laboratory findings (remainder of R00-R99)': 'Altri sintomi, segni e risultati clinici e di laboratorio anomali (resto R00-R99)',
    'Total': 'Totale',
    'Drug dependence, toxicomania (F11-F16, F18-F19)': 'Dipendenza da droghe, tossicodipendenza (F11-F16, F18-F19)',
    'COVID-19, virus identified': 'COVID-19, virus identificato',
    'COVID-19, virus not identified': 'COVID-19, virus non identificato',
    'COVID-19, other': 'COVID-19, altro',
    'External causes of morbidity and mortality (V01-Y89)': 'Cause esterne di morbidità e mortalità (V01-Y89)',
    'Other external causes of morbidity and mortality (remainder of V01-Y89)': 'Altre cause esterne di morbidità e mortalità (resto V01-Y89)',
    'Transport accidents (V01-V99, Y85)': 'Incidenti stradali (V01-V99, Y85)',
    'Falls': 'Cadute',
    'Accidental drowning and submersion': 'Annegamento accidentale e sommersione',
    'Accidental poisoning by and exposure to noxious substances': 'Avvelenamento accidentale da sostanze nocive',
    'Intentional self-harm': 'Autolesionismo intenzionale',
    'Assault': 'Aggressione',
    'Event of undetermined intent': 'Evento di intento indeterminato'
}

# ===========================
# Paths
# ===========================
PROCESSED_IT_PATH = Path("data/processed_it")

# ===========================
# Translation Functions
# ===========================
def translate_to_italian(df: pd.DataFrame, col_country='country', col_disease='disease') -> pd.DataFrame:
    if col_country in df.columns:
        df[col_country] = df[col_country].map(country_map).fillna(df[col_country])
    if col_disease in df.columns:
        df[col_disease] = df[col_disease].map(disease_map).fillna(df[col_disease])
    return df

def translate_csv_to_it(input_csv: Path, output_subfolder=None) -> Path:
    df = pd.read_csv(input_csv)
    df = translate_to_italian(df)

    if output_subfolder is None:
        output_subfolder = input_csv.parent.name

    save_folder = PROCESSED_IT_PATH / output_subfolder
    save_folder.mkdir(parents=True, exist_ok=True)

    save_path = save_folder / input_csv.name.replace(".csv", "_it.csv")
    df.to_csv(save_path, index=False, encoding='utf-8')
    print(f"Translated CSV saved: {save_path}")
    return save_path

def translate_all(csv_list):
    for csv_file in csv_list:
        translate_csv_to_it(csv_file)