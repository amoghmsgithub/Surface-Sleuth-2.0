import torch.nn.functional as F

def deep_similarity(e1, e2):
    return F.cosine_similarity(e1, e2).item()

def final_score(orb_score, deep_score):
    return 0.6 * orb_score + 0.4 * (deep_score * 100)