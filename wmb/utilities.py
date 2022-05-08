import pandas as pd


def transfer_cluster_annot(prev_cluster,
                           cur_cluster,
                           confident=0.9,
                           less_confident=0.5,
                           null_name=''):
    table = pd.DataFrame({'cur': cur_cluster, 'prev': prev_cluster})
    counts = table.value_counts().unstack().fillna(0).astype(int)
    ratio = counts / counts.sum(axis=1).values[:, None]

    cluster_map = {}
    for cur, row in ratio.iterrows():
        max_ratio = row.max()
        max_cluster = row.index[row.argmax()]
        if max_ratio > confident:
            cluster_map[cur] = max_cluster
        elif max_ratio > less_confident:
            cluster_map[cur] = max_cluster + f'_{int(max_ratio*100)}'
        else:
            cluster_map[cur] = null_name
    return cluster_map
