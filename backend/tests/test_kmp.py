from algorithms.kmp import kmp_steps

def test_kmp_finds_match():
    steps = kmp_steps("ABABDABACDABABCABAB", "ABABCABAB")
    match_steps = [step for step in steps if step.get("phase") == "match"]

    assert len(match_steps) == 1
    assert match_steps[0]["matches"] == [10]