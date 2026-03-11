import networkx as nx

def build_transaction_graph(transactions):

    G = nx.DiGraph()

    for tx in transactions:
        sender = tx["account_id"]
        receiver = tx["counterparty_id"]
        amount = tx["amount"]

        G.add_edge(sender, receiver, weight=amount)

    return G