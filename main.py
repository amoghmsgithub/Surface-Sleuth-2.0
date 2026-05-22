import os
from preprocessing.preprocess import preprocess_image
from models.embeddings import get_embedding
from matching.orb_match import orb_match
from matching.fusion import deep_similarity, final_score
from security.pqc_crypto import generate_keys
from database.db_handler import save_db, load_db

TRAIN_PATH = "data/fingerprints/train"

# Generate keys once (in real system store securely)
public_key, secret_key = generate_keys()

def build_database():
    db = {}

    for file in os.listdir(TRAIN_PATH):
        path = os.path.join(TRAIN_PATH, file)

        # Skip non-files
        if not os.path.isfile(path):
            continue

        img = preprocess_image(path)

        # Skip invalid/corrupted images
        if img is None:
            print(f"Skipping invalid image: {file}")
            continue

        emb = get_embedding(img)

        db[file] = {
            "image": img,
            "embedding": emb
        }

    save_db(db, public_key)
    return "Database built & encrypted successfully"

def match_fingerprint(test_image_path):
    db = load_db(secret_key)

    test_img = preprocess_image(test_image_path)

    # Handle invalid uploaded image
    if test_img is None:
        return []

    test_emb = get_embedding(test_img)

    results = []

    for name, data in db.items():
        orb_score = orb_match(test_img, data["image"])
        deep_score = deep_similarity(test_emb, data["embedding"])
        score = final_score(orb_score, deep_score)

        results.append((name, score))

    # Sort best match first
    results.sort(key=lambda x: x[1], reverse=True)

    return results