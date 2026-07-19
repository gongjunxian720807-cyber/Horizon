"""Standalone HTML rendering for the Chinese boss industry digest."""

from __future__ import annotations

import base64
import html
from collections import defaultdict
from pathlib import Path
from typing import Mapping, Sequence

from ..models import CategoryGroupConfig, ContentItem
from .summarizer import _safe_url


_MONTHS = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")
_IMAGE_MEDIA_TYPES = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
}


def _text(value: object) -> str:
    return html.escape(str(value), quote=True)


class BossDigestHtmlRenderer:
    """Render a portable blue-and-gold morning brief from structured items."""

    def render(
        self,
        items: Sequence[ContentItem],
        *,
        date: str,
        total_fetched: int,
        category_groups: Mapping[str, CategoryGroupConfig],
        default_group: str,
        hero_path: Path,
    ) -> str:
        year, month, day = self._date_parts(date)
        hero_data_uri = self._hero_data_uri(hero_path)
        grouped = self._group_items(items, category_groups, default_group)
        focus_items = "".join(self._focus_item(item, index) for index, item in enumerate(items[:3], 1))
        sections = "".join(
            self._category_section(
                group_key,
                group.name or group_key,
                grouped.get(group_key, []),
            )
            for group_key, group in category_groups.items()
        )
        if default_group not in category_groups and grouped.get(default_group):
            sections += self._category_section(
                default_group,
                default_group,
                grouped[default_group],
            )

        if items:
            focus = f'<ol class="focus-list">{focus_items}</ol>'
        else:
            focus = (
                '<div class="empty-state"><strong>今日暂无达到重要性门槛的资讯</strong>'
                f'<span>已分析 {total_fetched} 条内容，请稍后查看下一期。</span></div>'
            )

        return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>老板行业早报 · {_text(date)}</title>
  <style>
    :root {{ --navy:#18366f; --navy-2:#254b8f; --gold:#efb84d; --paper:#fffdfa; --ink:#24314a; --muted:#6f7889; --line:#d8e0ee; }}
    * {{ box-sizing:border-box; }}
    html {{ background:#eaf2fb; }}
    body {{ margin:0; color:var(--ink); background:#eaf2fb; font-family:"Microsoft YaHei","PingFang SC","Noto Sans CJK SC",Arial,sans-serif; line-height:1.75; }}
    a {{ color:inherit; }}
    .page {{ width:min(900px,calc(100% - 40px)); margin:40px auto; background:var(--paper); border-top:7px solid var(--navy); border-bottom:7px solid var(--navy); box-shadow:0 22px 55px rgba(35,67,108,.20); }}
    .masthead {{ position:relative; padding:38px 56px 26px; }}
    .masthead::before {{ content:""; position:absolute; left:56px; top:0; width:150px; height:8px; background:var(--gold); }}
    .brand {{ margin:0 128px 0 0; color:var(--navy); font-size:clamp(38px,7vw,68px); font-weight:900; letter-spacing:.08em; line-height:1.1; }}
    .brand-en {{ margin:10px 0 0 4px; color:#64769b; font-size:12px; letter-spacing:.45em; text-transform:uppercase; }}
    .date-card {{ position:absolute; right:56px; top:0; width:94px; padding:10px 12px 14px; color:white; background:var(--gold); text-align:center; font-family:Georgia,serif; }}
    .date-card span {{ display:block; }}
    .date-card .year {{ font-size:21px; }}
    .date-card .month {{ margin:3px 0; padding-bottom:5px; border-bottom:1px solid rgba(255,255,255,.9); font-size:20px; }}
    .date-card .day {{ font-size:38px; line-height:1; }}
    .rule {{ height:4px; margin:0 56px 26px; background:var(--navy); }}
    .hero {{ margin:0 56px; border:1px solid #aabbd7; background:#dbe7f6; }}
    .hero img {{ display:block; width:100%; height:clamp(210px,34vw,330px); object-fit:cover; }}
    .summary-strip {{ display:flex; justify-content:space-between; gap:20px; margin:22px 56px 0; padding:15px 18px; color:#fff; background:var(--navy); }}
    .summary-strip strong {{ color:#ffd77c; }}
    .summary-strip span:last-child {{ white-space:nowrap; }}
    main {{ padding:28px 56px 48px; }}
    .section-kicker {{ margin:0 0 12px; color:var(--navy); font-size:17px; letter-spacing:.08em; }}
    .focus-list {{ margin:0 0 34px; padding:0; list-style:none; }}
    .focus-list li {{ display:grid; grid-template-columns:32px 1fr auto; align-items:start; gap:10px; padding:13px 0; border-bottom:1px dashed #bdc9dc; }}
    .focus-list .number {{ width:28px; height:28px; border-radius:50%; color:#fff; background:var(--gold); text-align:center; line-height:28px; font-weight:700; }}
    .focus-list a {{ color:var(--navy); font-weight:700; text-decoration:none; }}
    .article-card h3,.article-summary,.focus-list a,details,.meta {{ overflow-wrap:anywhere; word-break:break-word; }}
    .score {{ color:#9a6b13; font-weight:700; white-space:nowrap; }}
    .category {{ margin-top:34px; }}
    .category-heading {{ display:flex; align-items:center; gap:12px; margin:0 0 12px; color:var(--navy); font-size:24px; }}
    .category-heading::before {{ content:""; width:7px; height:28px; background:var(--gold); }}
    .category-count {{ margin-left:auto; color:var(--muted); font-size:13px; font-weight:400; }}
    .empty-category {{ margin:0; padding:14px 18px; color:var(--muted); background:#f5f7fb; border-left:3px solid #d8e0ee; }}
    .article-card {{ position:relative; margin:0 0 18px; padding:22px 24px; border:1px solid var(--line); border-left:4px solid var(--navy-2); background:#fff; box-shadow:0 5px 14px rgba(40,66,102,.06); break-inside:avoid; }}
    .article-card h3 {{ margin:0 70px 10px 0; color:var(--navy); font-size:20px; line-height:1.45; }}
    .article-card h3 a {{ text-decoration:none; }}
    .article-card h3 a:hover,.article-card h3 a:focus {{ text-decoration:underline; }}
    .article-score {{ position:absolute; right:22px; top:22px; color:#9a6b13; font-weight:800; }}
    .article-summary {{ margin:0; color:#414b5d; }}
    .meta {{ display:flex; flex-wrap:wrap; gap:7px 16px; margin-top:13px; color:var(--muted); font-size:13px; }}
    .tags {{ display:flex; flex-wrap:wrap; gap:6px; margin-top:13px; }}
    .tag {{ padding:2px 9px; border-radius:999px; color:#365487; background:#edf3fb; font-size:12px; }}
    details {{ margin-top:14px; padding-top:10px; border-top:1px dashed var(--line); color:#566175; }}
    summary {{ color:var(--navy-2); cursor:pointer; font-weight:700; }}
    .references {{ margin:8px 0 0; padding-left:20px; }}
    .empty-state {{ display:grid; gap:4px; margin-bottom:32px; padding:24px; color:var(--navy); background:#f2f6fb; border:1px solid var(--line); text-align:center; }}
    .empty-state span {{ color:var(--muted); }}
    footer {{ padding:20px 56px; color:#718099; background:#f2f5fa; border-top:1px solid var(--line); font-size:12px; text-align:center; }}
    @media (max-width: 680px) {{
      .page {{ width:100%; margin:0; border-top-width:5px; box-shadow:none; }}
      .masthead {{ padding:28px 22px 20px; }}
      .masthead::before {{ left:22px; width:95px; height:6px; }}
      .brand {{ margin-right:84px; font-size:36px; letter-spacing:.03em; }}
      .brand-en {{ max-width:220px; letter-spacing:.18em; }}
      .date-card {{ right:22px; width:72px; }}
      .date-card .year,.date-card .month {{ font-size:16px; }}
      .date-card .day {{ font-size:30px; }}
      .rule,.hero,.summary-strip {{ margin-left:22px; margin-right:22px; }}
      .hero img {{ height:210px; }}
      .summary-strip {{ display:block; }}
      .summary-strip span {{ display:block; }}
      main {{ padding:24px 22px 38px; }}
      .focus-list li {{ grid-template-columns:28px 1fr; }}
      .focus-list .score {{ grid-column:2; }}
      .article-card {{ padding:19px 18px; }}
      .article-card h3 {{ margin-right:0; padding-right:0; }}
      .article-score {{ position:static; display:block; margin-bottom:6px; }}
      footer {{ padding:18px 22px; }}
    }}
    @media print {{
      html,body {{ background:#fff; }}
      .page {{ width:100%; margin:0; border:0; box-shadow:none; }}
      .hero img {{ height:240px; }}
      .article-card {{ box-shadow:none; }}
      a {{ text-decoration:none; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <header class="masthead">
      <h1 class="brand">老板行业早报</h1>
      <p class="brand-en">STEEL · CONSTRUCTION · AI · EDF</p>
      <time class="date-card" datetime="{_text(date)}"><span class="year">{year}</span><span class="month">{_MONTHS[month - 1]}</span><span class="day">{day}</span></time>
    </header>
    <div class="rule"></div>
    <figure class="hero"><img src="{hero_data_uri}" alt="钢结构、工业化建造与人工智能主题视觉"></figure>
    <div class="summary-strip" aria-label="从 {total_fetched} 条内容中筛选出 {len(items)} 条重要资讯"><span>从 <strong>{total_fetched}</strong> 条内容中筛选出 <strong>{len(items)}</strong> 条重要资讯</span><span>报告日期 {_text(date)}</span></div>
    <main>
      <section aria-labelledby="focus-heading">
        <h2 class="section-kicker" id="focus-heading">老板重点 · QUICK READ</h2>
        {focus}
      </section>
      {sections}
    </main>
    <footer>Horizon AI 新闻雷达 · 每日自动生成 · 重要决策请核对原始来源</footer>
  </div>
</body>
</html>
"""

    @staticmethod
    def _date_parts(date: str) -> tuple[str, int, str]:
        parts = date.split("-")
        if len(parts) != 3:
            raise ValueError("date must use YYYY-MM-DD format")
        year, month, day = parts
        month_number = int(month)
        if month_number < 1 or month_number > 12:
            raise ValueError("date month must be between 01 and 12")
        return _text(year), month_number, _text(str(int(day)))

    @staticmethod
    def _hero_data_uri(hero_path: Path) -> str:
        media_type = _IMAGE_MEDIA_TYPES.get(hero_path.suffix.lower())
        if media_type is None:
            raise ValueError("hero image must be JPEG, PNG, or WebP")
        encoded = base64.b64encode(hero_path.read_bytes()).decode("ascii")
        return f"data:{media_type};base64,{encoded}"

    @staticmethod
    def _group_items(
        items: Sequence[ContentItem],
        category_groups: Mapping[str, CategoryGroupConfig],
        default_group: str,
    ) -> dict[str, list[ContentItem]]:
        category_to_group = {
            category: group_key
            for group_key, group in category_groups.items()
            for category in group.categories
        }
        grouped: dict[str, list[ContentItem]] = defaultdict(list)
        for item in items:
            category = item.metadata.get("category")
            group_key = category_to_group.get(category, default_group)
            grouped[group_key].append(item)
        return grouped

    def _focus_item(self, item: ContentItem, index: int) -> str:
        title = _text(item.metadata.get("title_zh") or item.title)
        url = _safe_url(item.url)
        label = f'<a href="{url}" target="_blank" rel="noopener noreferrer">{title}</a>' if url else title
        score = _text(item.ai_score if item.ai_score is not None else "—")
        return f'<li><span class="number">{index}</span>{label}<span class="score">{score}/10</span></li>'

    def _category_section(
        self,
        group_key: str,
        group_name: str,
        items: Sequence[ContentItem],
    ) -> str:
        if items:
            body = "".join(self._article_card(item) for item in items)
        else:
            body = '<p class="empty-category">今天没有达到质量门槛的资讯，不为凑数而收录。</p>'
        return (
            f'<section class="category" data-group="{_text(group_key)}">'
            f'<h2 class="category-heading">{_text(group_name)}'
            f'<span class="category-count">{len(items)} 条</span></h2>{body}</section>'
        )

    def _article_card(self, item: ContentItem) -> str:
        meta = item.metadata
        title = _text(meta.get("title_zh") or item.title)
        url = _safe_url(item.url)
        title_html = (
            f'<a href="{url}" target="_blank" rel="noopener noreferrer">{title}</a>'
            if url
            else title
        )
        summary = _text(
            meta.get("detailed_summary_zh")
            or meta.get("detailed_summary")
            or item.ai_summary
            or "暂无摘要。"
        )
        background = meta.get("background_zh") or meta.get("background") or ""
        discussion = meta.get("community_discussion_zh") or meta.get("community_discussion") or ""
        source = meta.get("feed_name") or item.author or item.source_type.value
        published = item.published_at.strftime("%m月%d日 %H:%M") if item.published_at else ""
        score = _text(item.ai_score if item.ai_score is not None else "—")
        tags = "".join(f'<span class="tag">#{_text(tag)}</span>' for tag in item.ai_tags)
        references = []
        for reference in meta.get("sources") or []:
            reference_title = _text(reference.get("title") or "参考资料")
            reference_url = _safe_url(reference.get("url", ""))
            if reference_url:
                references.append(
                    f'<li><a href="{reference_url}" target="_blank" rel="noopener noreferrer">{reference_title}</a></li>'
                )

        detail_parts = []
        if background:
            detail_parts.append(f'<p><strong>背景：</strong>{_text(background)}</p>')
        if discussion:
            detail_parts.append(f'<p><strong>社区讨论：</strong>{_text(discussion)}</p>')
        if references:
            detail_parts.append(f'<ul class="references">{"".join(references)}</ul>')
        details = (
            f'<details><summary>背景与参考资料</summary>{"".join(detail_parts)}</details>'
            if detail_parts
            else ""
        )

        return (
            '<article class="article-card">'
            f'<span class="article-score">{score}/10</span>'
            f'<h3>{title_html}</h3>'
            f'<p class="article-summary">{summary}</p>'
            f'<div class="meta"><span>来源：{_text(source)}</span><time>{_text(published)}</time></div>'
            f'<div class="tags">{tags}</div>{details}</article>'
        )
