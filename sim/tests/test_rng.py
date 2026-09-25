from pfs_sim import rng


def test_rng_is_reproducible():
    assert (rng().random(5) == rng().random(5)).all()
