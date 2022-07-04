from src.extractors import extract_full_cag_tract


def test_extract_full_cag_tract():
    assert "CAG" * 7 == extract_full_cag_tract(f"GGGTATA{'CAG' * 7}CAA")
