import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
from annoy import AnnoyIndex
import os 
import sys
import time
from tqdm import tqdm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.logger import get_logger

logger = get_logger('collaborative_filtering')

start = time.time()

def preprocessing(df):
    try:
        logger.info('data preprocessing has started')
        print(df.isna().sum())
        print(df.shape)
        print(df.dtypes)
        print(df.duplicated().sum())
        
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)
        print(df.shape)
        
        df.set_index('id', inplace=True)
        df_1 = df.copy()

        categorical_cols = df.select_dtypes(include=['object'])
        le = LabelEncoder()
        categorical_cols = categorical_cols.apply(le.fit_transform)
        df_1[categorical_cols.columns] = categorical_cols

        feature_cols = [
            'track_number','disc_number', 'danceability','energy','key','loudness','mode','speechiness',
            'acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature','year',
        ]
        
        scaler = MinMaxScaler()
        df_1[feature_cols] = scaler.fit_transform(df_1[feature_cols])
        
        logger.info('preprocessing completed')
        return df_1, df  # return both encoded/scaled and original for reference

    except Exception as e:
        logger.error('error in data preprocessing')
        print(e)


def cf(df_encoded, original_df):
    try:
        logger.info('Starting collaborative filtering using Annoy')
        
        f = df_encoded.shape[1]
        t = AnnoyIndex(f, 'angular')  # angular is similar to cosine

        index_to_track_id = list(df_encoded.index)
        track_id_to_index = {track_id: idx for idx, track_id in enumerate(index_to_track_id)}

        for i in range(len(df_encoded)):
            t.add_item(i, df_encoded.iloc[i].values.tolist())

        t.build(10)
        t.save('annoy_index.ann')
        logger.info('Annoy index built and saved')

        data = []

        for i in tqdm(range(len(df_encoded))):
            neighbors = t.get_nns_by_item(i, 21, include_distances=True)  # 21 to exclude self
            source_id = index_to_track_id[i]

            for neighbor_idx, dist in zip(*neighbors):
                if neighbor_idx == i:
                    continue  # skip self
                target_id = index_to_track_id[neighbor_idx]
                similarity = 1 - dist  # approximate cosine
                data.append((source_id, target_id, similarity))

        similarity_df = pd.DataFrame(data, columns=["source", "target", "similarity"])
        logger.info('Similarity dataframe created')

        return similarity_df

    except Exception as e:
        logger.error('error in collaborative filtering')
        print(e)


def recommend(similarity_df, original_df, track_name, top_n=5):
    try:
        name_to_id = dict(zip(original_df['name'], original_df.index))
        id_to_name = dict(zip(original_df.index, original_df['name']))

        if track_name not in name_to_id:
            return "Track not found"
        
        track_id = name_to_id[track_name]
        top_matches = similarity_df[similarity_df['source'] == track_id]
        top_matches = top_matches.sort_values(by='similarity', ascending=False).head(top_n)

        return [id_to_name.get(tid, f"Track {tid}") for tid in top_matches['target']]
    
    except Exception as e:
        logger.error('error in recommend function')
        print(e)


def main():
    try:
        logger.info('Pipeline started')
        df = pd.read_csv(r'C:\Users\palya\Desktop\spotify clone\spotify-waffle\models\data\tracks_features.csv')
        df_encoded, original_df = preprocessing(df)
        similarity_df = cf(df_encoded, original_df)
        print(recommend(similarity_df, original_df, 'Lemonade', top_n=5))
        
    except Exception as e:
        logger.error('error in main')
        print(e)


if __name__ == "__main__":
    main()
    end = time.time()
    print(f"Execution time: {end - start} seconds")