import pandas as pd

lang1 = pd.read_table('slk_sentences.tsv')
lang2 = pd.read_table('pol_sentences.tsv')
links = pd.read_table('links.csv')

lang1.columns = ['id', 'language', 'sentence']
lang2.columns = ['id', 'language', 'sentence']
links.columns = ['original_id', 'translation_id']

lang1_name = lang1.iloc[0]['language']
lang2_name = lang2.iloc[0]['language']

lang1.drop('language', axis=1, inplace=True)
lang2.drop('language', axis=1, inplace=True)

output = pd.DataFrame(columns=(lang1_name, lang2_name))

for id_1, sentence_1 in zip(lang1['id'], lang1['sentence']):
    translations = links.loc[links['original_id'] == id_1]
    for trans_id in translations['translation_id']:
        sentence_2_df = lang2.loc[lang2['id'] == trans_id]
        if not sentence_2_df.empty:
            sentence_2 = sentence_2_df.iloc[0]['sentence']
            output = output.append({lang1_name: sentence_1, lang2_name: sentence_2},
                                   ignore_index=True)


output.to_csv('output.tsv', sep='\t')
