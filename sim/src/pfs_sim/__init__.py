"""点なし時空の考察に関する数値実験。"""

import numpy as np

DEFAULT_SEED = 0


def rng(seed: int = DEFAULT_SEED) -> np.random.Generator:
    """再現性のため、シードを固定した乱数生成器を返す。"""
    return np.random.default_rng(seed)
