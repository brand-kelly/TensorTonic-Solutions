def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = set(recommended[:k])
    rel_set = set(relevant)
    
    precision = len(top_k.intersection(rel_set)) / k
    recall = len(top_k.intersection(rel_set)) / len(relevant)

    return [precision, recall]