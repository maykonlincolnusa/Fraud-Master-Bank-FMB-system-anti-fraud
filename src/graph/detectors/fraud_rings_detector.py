import networkx as nx

def detect_fraud_rings(G):

    communities = nx.algorithms.community.greedy_modularity_communities(G)

    suspicious_groups = []

    for community in communities:
        if len(community) > 5:
            suspicious_groups.append(list(community))

    return suspicious_groups