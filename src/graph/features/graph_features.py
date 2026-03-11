def compute_graph_features(G):

    features = {}

    features["pagerank"] = nx.pagerank(G)
    features["degree"] = dict(G.degree())

    return features