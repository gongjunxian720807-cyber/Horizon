"""Tests for the standalone Chinese boss digest HTML renderer."""

from datetime import datetime, timezone
from pathlib import Path

from src.ai.html_digest import BossDigestHtmlRenderer
from src.models import CategoryGroupConfig, ContentItem, SourceType


def _make_item(
    idx: int,
    *,
    category: str = "ai",
    title: str | None = None,
    url: str | None = None,
) -> ContentItem:
    item = ContentItem(
        id=f"rss:item-{idx}",
        source_type=SourceType.RSS,
        title=title or f"Important Item {idx}",
        url=url or f"https://example.com/items/{idx}",
        content="content",
        author="tester",
        published_at=datetime(2026, 7, 19, 8, 0, tzinfo=timezone.utc),
        metadata={
            "category": category,
            "title_zh": title or f"重要资讯 {idx}",
            "detailed_summary_zh": f"第 {idx} 条资讯摘要。",
            "background_zh": f"第 {idx} 条背景资料。",
            "feed_name": "测试信息源",
            "sources": [
                {
                    "title": "参考资料",
                    "url": f"https://docs.example.com/items/{idx}",
                }
            ],
        },
    )
    item.ai_score = 8.0
    item.ai_tags = ["AI", "部署"]
    return item


def _groups() -> dict[str, CategoryGroupConfig]:
    return {
        "steel": CategoryGroupConfig(name="钢材加工配送", limit=4, categories=["steel"]),
        "construction": CategoryGroupConfig(
            name="工业化建造与智能空间", limit=4, categories=["construction"]
        ),
        "ai": CategoryGroupConfig(
            name="AI 前沿", limit=4, categories=["ai", "ai-tools"]
        ),
        "edf": CategoryGroupConfig(
            name="EDF AI 前沿部署工程", limit=3, categories=["edf"]
        ),
    }


def _hero(tmp_path: Path) -> Path:
    path = tmp_path / "hero.jpg"
    path.write_bytes(b"\xff\xd8\xff\xe0test-jpeg")
    return path


def test_html_digest_is_self_contained_responsive_and_printable(tmp_path: Path) -> None:
    result = BossDigestHtmlRenderer().render(
        [_make_item(1, category="steel"), _make_item(2, category="edf")],
        date="2026-07-19",
        total_fetched=173,
        category_groups=_groups(),
        default_group="ai",
        hero_path=_hero(tmp_path),
    )

    assert result.startswith("<!doctype html>")
    assert '<meta charset="utf-8">' in result
    assert "老板行业早报" in result
    assert "从 173 条内容中筛选出 2 条重要资讯" in result
    assert "2026" in result and "JUL" in result and ">19<" in result
    assert "钢材加工配送" in result
    assert "工业化建造与智能空间" in result
    assert "AI 前沿" in result
    assert "EDF AI 前沿部署工程" in result
    assert "重要资讯 1" in result
    assert "第 1 条资讯摘要。" in result
    assert "https://example.com/items/1" in result
    assert "data:image/jpeg;base64," in result
    assert "@media (max-width: 680px)" in result
    assert "@media print" in result
    assert ".article-card h3,.article-summary,.focus-list a,details,.meta { overflow-wrap:anywhere; word-break:break-word; }" in result
    assert "background:#eaf2fb;" in result
    assert "linear-gradient" not in result
    assert "<style>" in result
    assert "<script" not in result.lower()
    assert "<link" not in result.lower()
    assert "@import" not in result.lower()
    assert "url(http" not in result.lower()


def test_html_digest_escapes_text_and_rejects_unsafe_links(tmp_path: Path) -> None:
    item = _make_item(1, title='<script>alert("title")</script>')
    item.metadata["detailed_summary_zh"] = '<img src=x onerror="alert(1)">'
    item.metadata["feed_name"] = '<svg onload="alert(1)">'
    item.metadata["sources"] = [
        {"title": '<b onclick="alert(1)">参考</b>', "url": "javascript:alert(1)"}
    ]
    item.ai_tags = ['tag"><script>alert(1)</script>']

    result = BossDigestHtmlRenderer().render(
        [item],
        date="2026-07-19",
        total_fetched=1,
        category_groups=_groups(),
        default_group="ai",
        hero_path=_hero(tmp_path),
    )

    assert "<script>alert" not in result
    assert "<img src=x" not in result
    assert "<svg onload" not in result
    assert "<b onclick" not in result
    assert 'href="javascript:' not in result
    assert "&lt;script&gt;" in result
    assert "&lt;img src=x onerror=&quot;alert(1)&quot;&gt;" in result


def test_html_digest_uses_default_group_and_renders_empty_state(tmp_path: Path) -> None:
    renderer = BossDigestHtmlRenderer()
    result = renderer.render(
        [_make_item(1, category="unmapped")],
        date="2026-07-19",
        total_fetched=1,
        category_groups=_groups(),
        default_group="ai",
        hero_path=_hero(tmp_path),
    )
    empty = renderer.render(
        [],
        date="2026-07-19",
        total_fetched=12,
        category_groups=_groups(),
        default_group="ai",
        hero_path=_hero(tmp_path),
    )

    assert 'data-group="ai"' in result
    assert "今日暂无达到重要性门槛的资讯" in empty
    assert "已分析 12 条内容" in empty
