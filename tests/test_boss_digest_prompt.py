from src.ai.prompts import CONTENT_ANALYSIS_SYSTEM


def test_analysis_prompt_values_the_four_boss_digest_themes() -> None:
    prompt = CONTENT_ANALYSIS_SYSTEM.lower()

    for term in (
        "steel processing and distribution",
        "industrialized construction",
        "mic/mimep",
        "ai frontier",
        "rag",
        "mlops/llmops",
    ):
        assert term in prompt


def test_analysis_prompt_values_executive_business_signals() -> None:
    prompt = CONTENT_ANALYSIS_SYSTEM.lower()

    for term in (
        "demand",
        "price",
        "margin",
        "supply chain",
        "policy",
        "competitor",
        "opportunit",
        "reliability",
        "cost",
    ):
        assert term in prompt


def test_analysis_prompt_sets_a_guarded_floor_for_core_industry_news() -> None:
    prompt = CONTENT_ANALYSIS_SYSTEM.lower()

    assert "should score at least 7" in prompt
    assert "credible and directly relevant" in prompt
    assert "steel processing or distribution" in prompt
    assert "industrialized construction or smart-space" in prompt
    assert "concrete" in prompt
    assert "do not apply this floor" in prompt
    assert "vague" in prompt
    assert "off-topic" in prompt
