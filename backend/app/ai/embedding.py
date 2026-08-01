from sentence_transformers import SentenceTransformer, util

_model = None


def get_model() -> SentenceTransformer:
    global _model

    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")

    return _model


def create_embedding(text: str):
    model = get_model()

    return model.encode(text)


def similarity(text1: str, text2: str):

    model = get_model()

    emb1 = model.encode(text1)

    emb2 = model.encode(text2)

    score = util.cos_sim(emb1, emb2)

    return float(score)
