from __future__ import annotations

import argparse
import json
import re
import sqlite3
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DB_PATH = REPO_ROOT / "20_research" / "YouTubeTranscripts" / "analysis" / "woodcraft_research.sqlite"


HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Woodcraft Research Database</title>
  <style>
    :root {
      --bg: #f6f7f4;
      --ink: #20231f;
      --muted: #62685f;
      --line: #c9cec4;
      --accent: #1c6b5a;
      --accent-dark: #11483d;
      --panel: #ffffff;
      --mark: #eaf3ef;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: "Segoe UI", Arial, sans-serif;
      line-height: 1.4;
    }
    header {
      padding: 18px 22px 12px;
      border-bottom: 1px solid var(--line);
      background: var(--panel);
    }
    h1 {
      margin: 0 0 4px;
      font-size: 24px;
      font-weight: 700;
      letter-spacing: 0;
    }
    .subtle { color: var(--muted); font-size: 14px; }
    main { padding: 18px 22px 28px; max-width: 1440px; margin: 0 auto; }
    .toolbar {
      display: grid;
      grid-template-columns: minmax(220px, 1fr) 180px 110px;
      gap: 10px;
      margin-bottom: 14px;
    }
    input, select, button {
      min-height: 40px;
      border: 1px solid var(--line);
      border-radius: 6px;
      font: inherit;
    }
    input, select { padding: 8px 10px; background: var(--panel); color: var(--ink); }
    button {
      padding: 8px 12px;
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
      font-weight: 600;
      cursor: pointer;
    }
    button:hover { background: var(--accent-dark); }
    .stats {
      display: grid;
      grid-template-columns: repeat(6, minmax(120px, 1fr));
      gap: 8px;
      margin: 10px 0 16px;
    }
    .stat {
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 6px;
      padding: 10px;
    }
    .stat strong { display: block; font-size: 22px; line-height: 1.1; }
    .tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 10px 0 14px;
    }
    .tab {
      min-height: 34px;
      padding: 6px 10px;
      border: 1px solid var(--line);
      background: var(--panel);
      color: var(--ink);
      border-radius: 6px;
      cursor: pointer;
    }
    .tab.active {
      background: var(--mark);
      border-color: var(--accent);
      color: var(--accent-dark);
      font-weight: 700;
    }
    .result-meta {
      margin: 8px 0;
      color: var(--muted);
      font-size: 14px;
    }
    .view-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      margin: 8px 0;
    }
    .view-actions .result-meta {
      margin: 0;
    }
    .back-button {
      min-height: 32px;
      padding: 5px 10px;
      background: var(--panel);
      color: var(--accent-dark);
      border-color: #8fa99e;
      font-size: 13px;
      font-weight: 700;
    }
    .back-button:hover:not(:disabled) {
      background: var(--mark);
      color: var(--accent-dark);
    }
    .back-button:disabled {
      color: #8b9288;
      background: #eef1eb;
      border-color: var(--line);
      cursor: default;
      opacity: 0.75;
    }
    .column-controls {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin: 8px 0 12px;
      padding: 8px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #eef1eb;
      color: var(--muted);
      font-size: 13px;
    }
    .column-controls:empty { display: none; }
    .column-controls-title {
      font-weight: 700;
      color: var(--ink);
      margin-right: 2px;
    }
    .column-toggle {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      min-height: 28px;
      padding: 4px 8px;
      border: 1px solid #b8c3b4;
      border-radius: 6px;
      background: #f9faf7;
      color: var(--ink);
      cursor: pointer;
    }
    .column-toggle:hover {
      border-color: #8fa99e;
      background: #f4f8f5;
    }
    .column-toggle:has(input:checked) {
      border-color: #7ba396;
      background: var(--mark);
      color: var(--accent-dark);
      font-weight: 600;
    }
    .column-toggle input {
      min-height: 0;
      width: 14px;
      height: 14px;
      margin: 0;
      accent-color: var(--accent);
    }
    .column-action {
      min-height: 28px;
      padding: 3px 8px;
      border-radius: 6px;
      background: var(--panel);
      color: var(--accent-dark);
      border-color: #8fa99e;
      font-size: 13px;
      font-weight: 600;
    }
    .column-action:hover {
      background: var(--mark);
      color: var(--accent-dark);
    }
    .table-wrap {
      max-width: 100%;
      overflow-x: auto;
      overflow-y: visible;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: var(--panel);
    }
    .floating-scrollbar {
      position: fixed;
      bottom: 0;
      height: 18px;
      overflow-x: auto;
      overflow-y: hidden;
      border: 1px solid var(--line);
      border-bottom: 0;
      border-radius: 6px 6px 0 0;
      background: rgba(255, 255, 255, 0.96);
      box-shadow: 0 -3px 10px rgba(32, 35, 31, 0.12);
      display: none;
      z-index: 20;
    }
    .floating-scrollbar.visible {
      display: block;
    }
    .floating-scrollbar-inner {
      height: 1px;
    }
    table {
      width: max-content;
      min-width: 100%;
      border-collapse: collapse;
      font-size: 14px;
    }
    th, td {
      min-width: 130px;
      padding: 9px 10px;
      border-bottom: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
    }
    td {
      max-width: 320px;
    }
    th.col-tiny, td.col-tiny {
      width: 72px;
      min-width: 72px;
      max-width: 96px;
    }
    th.col-compact, td.col-compact {
      width: 120px;
      min-width: 96px;
      max-width: 150px;
    }
    th.col-medium, td.col-medium {
      width: 210px;
      min-width: 170px;
      max-width: 260px;
    }
    th.col-wide, td.col-wide {
      width: 320px;
      min-width: 240px;
      max-width: 380px;
    }
    th.col-xwide, td.col-xwide {
      width: 430px;
      min-width: 320px;
      max-width: 520px;
    }
    th {
      position: sticky;
      top: 0;
      background: #eef1eb;
      z-index: 1;
    }
    .sort-button {
      display: inline-flex;
      align-items: center;
      justify-content: flex-start;
      gap: 6px;
      width: 100%;
      min-height: 28px;
      padding: 0;
      border: 0;
      background: transparent;
      color: var(--ink);
      font-weight: 700;
      text-align: left;
    }
    .sort-button:hover {
      background: transparent;
      color: var(--accent-dark);
    }
    .sort-mark {
      color: var(--muted);
      font-size: 12px;
      min-width: 12px;
    }
    .column-filter {
      width: 100%;
      min-height: 30px;
      margin-top: 6px;
      padding: 5px 7px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 400;
    }
    tr:last-child td { border-bottom: 0; }
    code {
      background: #eef1eb;
      border: 1px solid var(--line);
      border-radius: 4px;
      padding: 1px 4px;
      font-family: Consolas, monospace;
      font-size: 13px;
    }
    a { color: var(--accent-dark); }
    @media (max-width: 760px) {
      main { padding: 14px; }
      .toolbar { grid-template-columns: 1fr; }
      .stats { grid-template-columns: repeat(2, minmax(120px, 1fr)); }
      h1 { font-size: 20px; }
    }
  </style>
</head>
<body>
  <header>
    <h1>Woodcraft Research Database</h1>
    <div class="subtle">Local SQLite search over transcripts, video research, current products, and cross-references.</div>
  </header>
  <main>
    <form class="toolbar" id="searchForm">
      <input id="query" name="q" placeholder="Search planter, Planter Box A, video 046, snowflake..." autocomplete="off">
      <select id="scope" name="scope">
        <option value="all">All</option>
        <option value="products">Products</option>
        <option value="videos">Videos</option>
        <option value="crossrefs">Crossrefs</option>
        <option value="ideas">Uncataloged Ideas</option>
      </select>
      <button type="submit">Search</button>
    </form>

    <section class="stats" id="stats"></section>

    <nav class="tabs" id="tabs">
      <button class="tab active" data-view="products" type="button">Products</button>
      <button class="tab" data-view="pricing" type="button">Pricing</button>
      <button class="tab" data-view="videos" type="button">Videos</button>
      <button class="tab" data-view="search" type="button">Search Results</button>
      <button class="tab" data-view="crossrefs" type="button">Crossrefs</button>
      <button class="tab" data-view="unmatched-products" type="button">Products Without Video</button>
      <button class="tab" data-view="unmatched-ideas" type="button">Ideas Not In Products</button>
    </nav>

    <div class="view-actions">
      <button class="back-button" id="backButton" type="button" disabled>Back</button>
      <div class="result-meta" id="meta"></div>
    </div>
    <div class="column-controls" id="columnControls"></div>
    <div class="table-wrap" id="results"></div>
  </main>
  <div class="floating-scrollbar" id="floatingScrollbar" aria-hidden="true">
    <div class="floating-scrollbar-inner" id="floatingScrollbarInner"></div>
  </div>
  <script>
    const hiddenColumnsStorageKey = "woodcraftResearchHiddenColumns";
    const results = document.getElementById("results");
    const backButton = document.getElementById("backButton");
    const floatingScrollbar = document.getElementById("floatingScrollbar");
    const floatingScrollbarInner = document.getElementById("floatingScrollbarInner");
    let syncingScrollbars = false;

    function loadHiddenColumns() {
      try {
        return JSON.parse(sessionStorage.getItem(hiddenColumnsStorageKey) || "{}");
      } catch {
        return {};
      }
    }

    const state = {
      view: "products",
      q: "",
      scope: "all",
      rows: [],
      columns: [],
      metaLabel: "rows",
      sort: {},
      filters: {},
      hiddenColumns: loadHiddenColumns(),
      history: []
    };

    function clone(value) {
      return JSON.parse(JSON.stringify(value));
    }

    function viewSnapshot() {
      return {
        view: state.view,
        q: state.q,
        scope: state.scope,
        filters: clone(state.filters)
      };
    }

    function sameSnapshot(left, right) {
      return JSON.stringify(left) === JSON.stringify(right);
    }

    function pushHistory() {
      const snapshot = viewSnapshot();
      const previous = state.history[state.history.length - 1];
      if (!previous || !sameSnapshot(previous, snapshot)) {
        state.history.push(snapshot);
      }
      updateBackButton();
    }

    function updateFormFromState() {
      document.getElementById("query").value = state.q;
      document.getElementById("scope").value = state.scope;
    }

    function updateBackButton() {
      backButton.disabled = state.history.length === 0;
    }

    function restoreSnapshot(snapshot) {
      state.view = snapshot.view;
      state.q = snapshot.q;
      state.scope = snapshot.scope;
      state.filters = clone(snapshot.filters);
      updateFormFromState();
      updateBackButton();
      loadView(state.view).catch(showError);
    }

    function saveHiddenColumns() {
      sessionStorage.setItem(hiddenColumnsStorageKey, JSON.stringify(state.hiddenColumns));
    }

    function escapeHtml(value) {
      return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
    }

    function linkify(value) {
      const text = escapeHtml(value);
      return text.replace(/https?:\\/\\/[^\\s)]+/g, url => `<a href="${url}" target="_blank" rel="noreferrer">${url}</a>`);
    }

    function viewSort() {
      if (!state.sort[state.view]) state.sort[state.view] = { key: "", direction: "asc" };
      return state.sort[state.view];
    }

    function viewFilters() {
      if (!state.filters[state.view]) state.filters[state.view] = {};
      return state.filters[state.view];
    }

    function viewHiddenColumns() {
      if (!state.hiddenColumns[state.view]) state.hiddenColumns[state.view] = {};
      return state.hiddenColumns[state.view];
    }

    function activeColumns(columns) {
      const hidden = viewHiddenColumns();
      return columns.filter(col => !hidden[col.key]);
    }

    function updateFloatingScrollbar() {
      const rect = results.getBoundingClientRect();
      const hasScrollableTable = results.querySelector("table") && results.scrollWidth > results.clientWidth + 1;
      const nativeScrollbarVisible = rect.bottom <= window.innerHeight;
      const tableInView = rect.top < window.innerHeight && rect.bottom > 0;
      const show = hasScrollableTable && tableInView && !nativeScrollbarVisible;

      floatingScrollbar.classList.toggle("visible", show);
      if (!show) return;

      const left = Math.max(rect.left, 0);
      const right = Math.max(window.innerWidth - rect.right, 0);
      floatingScrollbar.style.left = `${left}px`;
      floatingScrollbar.style.width = `${Math.max(window.innerWidth - left - right, 0)}px`;
      floatingScrollbarInner.style.width = `${results.scrollWidth}px`;

      if (floatingScrollbar.scrollLeft !== results.scrollLeft) {
        floatingScrollbar.scrollLeft = results.scrollLeft;
      }
    }

    function syncTableScroll(source, target) {
      if (syncingScrollbars) return;
      syncingScrollbars = true;
      target.scrollLeft = source.scrollLeft;
      syncingScrollbars = false;
      updateFloatingScrollbar();
    }

    function cellText(row, key) {
      return String(row[key] ?? "");
    }

    function compareCells(a, b, key, direction) {
      const left = cellText(a, key).trim();
      const right = cellText(b, key).trim();
      const leftNumber = Number(left);
      const rightNumber = Number(right);
      let result;
      if (left !== "" && right !== "" && Number.isFinite(leftNumber) && Number.isFinite(rightNumber)) {
        result = leftNumber - rightNumber;
      } else {
        result = left.localeCompare(right, undefined, { numeric: true, sensitivity: "base" });
      }
      return direction === "desc" ? -result : result;
    }

    function visibleRows(rows, columns) {
      const filters = viewFilters();
      const columnsForFilters = activeColumns(columns);
      const filtered = rows.filter(row => {
        return columnsForFilters.every(col => {
          if (col.filter === false) return true;
          const query = String(filters[col.key] ?? "").trim().toLowerCase();
          return !query || cellText(row, col.key).toLowerCase().includes(query);
        });
      });
      const sort = viewSort();
      if (sort.key && columnsForFilters.some(col => col.key === sort.key)) {
        filtered.sort((a, b) => compareCells(a, b, sort.key, sort.direction));
      }
      return filtered;
    }

    function sortMark(key) {
      const sort = viewSort();
      if (sort.key !== key) return "";
      return sort.direction === "asc" ? "ASC" : "DESC";
    }

    function renderCell(row, col) {
      const value = row[col.key];
      if (col.linksKey && Array.isArray(row[col.linksKey]) && row[col.linksKey].length) {
        return row[col.linksKey].map(link => {
          const label = link.label || link.title || link.url || "";
          const title = link.label && link.title ? ` title="${escapeHtml(link.title)}"` : "";
          if (link.view) {
            return `<a href="#" data-view-link="${escapeHtml(link.view)}" data-filter-key="${escapeHtml(link.filter_key || "")}" data-filter-value="${escapeHtml(link.filter_value || "")}">${escapeHtml(label)}</a>`;
          }
          if (!link.url) return escapeHtml(label);
          return `<a href="${escapeHtml(link.url)}" target="_blank" rel="noreferrer"${title}>${escapeHtml(label)}</a>`;
        }).join("; ");
      }
      if (col.linkKey && row[col.linkKey]) {
        return `<a href="${escapeHtml(row[col.linkKey])}" target="_blank" rel="noreferrer">${escapeHtml(value)}</a>`;
      }
      return col.html ? linkify(value) : escapeHtml(value);
    }

    function columnClass(col) {
      const allowed = ["tiny", "compact", "medium", "wide", "xwide"];
      return allowed.includes(col.size) ? ` class="col-${col.size}"` : "";
    }

    function table(rows, columns) {
      const columnsToShow = activeColumns(columns);
      if (!columnsToShow.length) return "<div style='padding: 14px;'>Choose at least one column.</div>";
      const filters = viewFilters();
      const displayRows = visibleRows(rows, columns);
      const head = columnsToShow.map(col => {
        const value = escapeHtml(filters[col.key] ?? "");
        const filter = col.filter === false ? "" : `<input class="column-filter" data-filter-key="${escapeHtml(col.key)}" value="${value}" placeholder="Filter">`;
        return `<th${columnClass(col)}><button class="sort-button" type="button" data-sort-key="${escapeHtml(col.key)}">${escapeHtml(col.label)} <span class="sort-mark">${sortMark(col.key)}</span></button>${filter}</th>`;
      }).join("");
      const body = displayRows.length ? displayRows.map(row => {
        return "<tr>" + columnsToShow.map(col => `<td${columnClass(col)}>${renderCell(row, col)}</td>`).join("") + "</tr>";
      }).join("") : `<tr><td colspan="${columnsToShow.length}">No rows found.</td></tr>`;
      return `<table><thead><tr>${head}</tr></thead><tbody>${body}</tbody></table>`;
    }

    function renderColumnControls() {
      const controls = document.getElementById("columnControls");
      if (!state.columns.length) {
        controls.innerHTML = "";
        return;
      }
      const hidden = viewHiddenColumns();
      const visibleCount = activeColumns(state.columns).length;
      const toggles = state.columns.map(col => {
        const checked = !hidden[col.key];
        const disabled = checked && visibleCount === 1 ? " disabled" : "";
        return `<label class="column-toggle"><input type="checkbox" data-column-key="${escapeHtml(col.key)}"${checked ? " checked" : ""}${disabled}>${escapeHtml(col.label)}</label>`;
      }).join("");
      controls.innerHTML = `<span class="column-controls-title">Columns</span>${toggles}<button class="column-action" type="button" data-column-action="show-all">Show all</button>`;
    }

    function renderCurrentTable() {
      const rows = visibleRows(state.rows, state.columns);
      const suffix = rows.length === state.rows.length ? "" : ` (${state.rows.length} before filters)`;
      document.getElementById("meta").textContent = `${rows.length} ${state.metaLabel}${suffix}`;
      renderColumnControls();
      results.innerHTML = table(state.rows, state.columns);
      updateBackButton();
      updateFloatingScrollbar();
    }

    function setTable(rows, columns, metaLabel) {
      state.rows = rows;
      state.columns = columns;
      state.metaLabel = metaLabel;
      renderCurrentTable();
    }

    async function getJson(url) {
      const response = await fetch(url);
      if (!response.ok) throw new Error(await response.text());
      return response.json();
    }

    async function loadStats() {
      const data = await getJson("/api/stats");
      const labels = {
        videos: "Videos",
        products: "Products",
        crossrefs: "Crossrefs",
        ideas: "Video Ideas",
        unmatched_products: "No Video Match",
        unmatched_ideas: "Ideas Not Cataloged"
      };
      document.getElementById("stats").innerHTML = Object.entries(labels).map(([key, label]) => {
        return `<div class="stat"><strong>${escapeHtml(data[key])}</strong><span>${escapeHtml(label)}</span></div>`;
      }).join("");
    }

    function setActiveTab(view) {
      document.querySelectorAll(".tab").forEach(tab => {
        tab.classList.toggle("active", tab.dataset.view === view);
      });
    }

    async function loadView(view) {
      state.view = view;
      setActiveTab(view);
      const meta = document.getElementById("meta");
      results.innerHTML = "<div style='padding: 14px;'>Loading...</div>";
      updateFloatingScrollbar();
      let data;
      if (view === "search") {
        const params = new URLSearchParams({ q: state.q, scope: state.scope });
        data = await getJson(`/api/search?${params.toString()}`);
        setTable(data.rows, [
          { key: "kind", label: "Type", size: "compact" },
          { key: "title", label: "Title / Product", linksKey: "title_links", size: "medium" },
          { key: "identifier", label: "ID", linksKey: "identifier_links", size: "compact" },
          { key: "reference_code", label: "Code", size: "compact" },
          { key: "result_links_text", label: "Links", linksKey: "result_links", size: "wide" },
          { key: "summary", label: "Summary", html: true, size: "xwide" }
        ], "search result rows");
      } else if (view === "videos") {
        data = await getJson("/api/videos");
        setTable(data.rows, [
          { key: "video_no", label: "#", size: "tiny" },
          { key: "title", label: "Video", linkKey: "url", size: "wide" },
          { key: "woodworking_relevance", label: "Relevance", size: "compact" },
          { key: "concept", label: "Concept", size: "xwide" },
          { key: "products_text", label: "Products", linksKey: "associated_product_links", size: "wide" },
          { key: "ideas_text", label: "Ideas", linksKey: "associated_idea_links", size: "wide" }
        ], "videos");
      } else if (view === "products") {
        data = await getJson("/api/products");
        setTable(data.rows, [
          { key: "catalog_id", label: "Catalog ID", size: "compact" },
          { key: "product_name", label: "Product", size: "medium" },
          { key: "reference_code", label: "Code", size: "compact" },
          { key: "product_id", label: "Product ID", size: "medium" },
          { key: "status", label: "Status", size: "compact" },
          { key: "primary_use_case", label: "Use Case", size: "wide" },
          { key: "associated_videos", label: "Associated Video", linksKey: "associated_video_links", size: "wide" },
          { key: "plans_source_ref", label: "Plan / Source", html: true, size: "xwide" }
        ], "current products");
      } else if (view === "pricing") {
        data = await getJson("/api/pricing");
        setTable(data.rows, [
          { key: "catalog_id", label: "Catalog ID", size: "compact" },
          { key: "product_name", label: "Product", size: "medium" },
          { key: "reference_code", label: "Code", size: "compact" },
          { key: "status", label: "Product Status", size: "compact" },
          { key: "materials_cost_amount", label: "Materials Cost $", size: "compact" },
          { key: "materials_cost_info", label: "Materials Cost Info", size: "medium" },
          { key: "materials_cost_status", label: "Materials Status", size: "compact" },
          { key: "target_price", label: "Sale Price", size: "compact" },
          { key: "sale_price_status", label: "Sale Price Status", size: "compact" },
          { key: "unit_cost_estimate", label: "Unit Cost", size: "compact" },
          { key: "pricing_strategy_1_price_floor", label: "Strategy 1 Floor", size: "compact" },
          { key: "pricing_strategy_2_price_floor", label: "Strategy 2 Floor", size: "compact" },
          { key: "recommended_price_floor", label: "Recommended Floor", size: "compact" },
          { key: "material_cost_percent_of_price", label: "Material % of Price", size: "compact" },
          { key: "margin_estimate", label: "Profit / Margin", size: "medium" },
          { key: "pricing_strategy_review", label: "Pricing Review", size: "wide" },
          { key: "pricing_validation", label: "Pricing Validation", size: "wide" },
          { key: "verification_status", label: "Verification", size: "compact" },
          { key: "build_time_estimate", label: "Build Time", size: "compact" },
          { key: "lead_time_estimate", label: "Lead Time", size: "compact" },
          { key: "cost_sheet_ref", label: "Cost Sheet", html: true, size: "medium" },
          { key: "product_id", label: "Product ID", size: "medium" }
        ], "pricing rows");
      } else if (view === "crossrefs") {
        data = await getJson("/api/crossrefs");
        setTable(data.rows, [
          { key: "section", label: "Section", size: "compact" },
          { key: "catalog_id", label: "Catalog ID", size: "compact" },
          { key: "product_id", label: "Product ID", size: "medium" },
          { key: "product_name", label: "Product", linkKey: "primary_video_url", size: "medium" },
          { key: "reference_code", label: "Code", size: "compact" },
          { key: "matched_videos", label: "Matched Videos", size: "medium" },
          { key: "confidence", label: "Confidence", size: "compact" },
          { key: "how_identified", label: "How Identified", size: "wide" }
        ], "cross-reference rows");
      } else if (view === "unmatched-products") {
        data = await getJson("/api/unmatched-products");
        setTable(data.rows, [
          { key: "catalog_id", label: "Catalog ID", size: "compact" },
          { key: "product_id", label: "Product ID", size: "medium" },
          { key: "product_name", label: "Product", size: "medium" },
          { key: "reference_code", label: "Code", size: "compact" },
          { key: "status", label: "Status", size: "compact" },
          { key: "notes", label: "Notes", size: "wide" }
        ], "products without direct saved-video match");
      } else if (view === "unmatched-ideas") {
        data = await getJson("/api/unmatched-ideas");
        setTable(data.rows, [
          { key: "idea", label: "Idea", size: "medium" },
          { key: "source_videos", label: "Source Videos", linksKey: "source_video_links", size: "compact" },
          { key: "current_product_record", label: "Current Product Record", size: "medium" },
          { key: "notes", label: "Notes", size: "wide" }
        ], "video ideas not in current products");
      }
    }

    document.getElementById("searchForm").addEventListener("submit", event => {
      event.preventDefault();
      pushHistory();
      state.q = document.getElementById("query").value.trim();
      state.scope = document.getElementById("scope").value;
      loadView("search").catch(showError);
    });

    document.getElementById("tabs").addEventListener("click", event => {
      const button = event.target.closest(".tab");
      if (button && button.dataset.view !== state.view) {
        pushHistory();
        loadView(button.dataset.view).catch(showError);
      }
    });

    backButton.addEventListener("click", () => {
      const snapshot = state.history.pop();
      if (snapshot) restoreSnapshot(snapshot);
    });

    results.addEventListener("click", event => {
      const linkedItem = event.target.closest("[data-view-link]");
      if (linkedItem) {
        event.preventDefault();
        const view = linkedItem.dataset.viewLink;
        const filterKey = linkedItem.dataset.filterKey;
        const filterValue = linkedItem.dataset.filterValue;
        if (view && filterKey) {
          pushHistory();
          state.filters[view] = {};
          state.filters[view][filterKey] = filterValue || "";
          loadView(view).catch(showError);
        }
        return;
      }
      const button = event.target.closest("[data-sort-key]");
      if (!button) return;
      const sort = viewSort();
      const key = button.dataset.sortKey;
      if (sort.key === key) {
        sort.direction = sort.direction === "asc" ? "desc" : "asc";
      } else {
        sort.key = key;
        sort.direction = "asc";
      }
      renderCurrentTable();
    });

    results.addEventListener("input", event => {
      const input = event.target.closest("[data-filter-key]");
      if (!input) return;
      const key = input.dataset.filterKey;
      const cursor = input.selectionStart;
      viewFilters()[input.dataset.filterKey] = input.value;
      renderCurrentTable();
      const replacement = Array.from(document.querySelectorAll("[data-filter-key]")).find(element => element.dataset.filterKey === key);
      if (replacement) {
        replacement.focus();
        replacement.setSelectionRange(cursor, cursor);
      }
    });

    document.getElementById("columnControls").addEventListener("change", event => {
      const input = event.target.closest("[data-column-key]");
      if (!input) return;
      const hidden = viewHiddenColumns();
      const key = input.dataset.columnKey;
      const visibleCount = activeColumns(state.columns).length;
      if (!input.checked && visibleCount <= 1) {
        input.checked = true;
        return;
      }
      if (input.checked) {
        delete hidden[key];
      } else {
        hidden[key] = true;
      }
      saveHiddenColumns();
      renderCurrentTable();
    });

    document.getElementById("columnControls").addEventListener("click", event => {
      const button = event.target.closest("[data-column-action]");
      if (!button) return;
      if (button.dataset.columnAction === "show-all") {
        state.hiddenColumns[state.view] = {};
        saveHiddenColumns();
        renderCurrentTable();
      }
    });

    function showError(error) {
      results.innerHTML = `<div style='padding: 14px;'>${escapeHtml(error.message)}</div>`;
      updateFloatingScrollbar();
    }

    results.addEventListener("scroll", () => syncTableScroll(results, floatingScrollbar));
    floatingScrollbar.addEventListener("scroll", () => syncTableScroll(floatingScrollbar, results));
    window.addEventListener("scroll", updateFloatingScrollbar, { passive: true });
    window.addEventListener("resize", updateFloatingScrollbar);

    loadStats().then(() => loadView("products")).catch(showError);
  </script>
</body>
</html>
"""


def dict_rows(cursor: sqlite3.Cursor) -> list[dict[str, object]]:
    return [dict(row) for row in cursor.fetchall()]


def clean_query(value: str) -> str:
    terms = re.findall(r"[A-Za-z0-9_'-]+", value)
    return " ".join(f'"{term}"' for term in terms[:8])


def connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def video_index(conn: sqlite3.Connection) -> dict[str, dict[str, object]]:
    return {
        f"{row['video_no']:03d}": {"title": row["title"], "url": row["url"]}
        for row in conn.execute("SELECT video_no, title, url FROM videos")
    }


def video_numbers(value: object) -> list[str]:
    text = str(value or "")
    backticked = re.findall(r"`(\d{3})`", text)
    if backticked:
        return backticked
    return re.findall(r"(?<!\$)\b\d{3}\b", text)


def product_video_links(conn: sqlite3.Connection) -> dict[str, dict[str, object]]:
    videos = video_index(conn)
    links: dict[str, dict[str, object]] = {}
    rows = conn.execute("SELECT product_id, matched_videos FROM product_crossrefs WHERE confidence <> 'Related only' ORDER BY id")
    for row in rows:
        product_id = row["product_id"]
        product_links = links.setdefault(
            product_id,
            {"primary_video_url": "", "associated_videos": "", "associated_video_links": []},
        )
        labels: list[str] = []
        seen: set[str] = set()
        for link in product_links["associated_video_links"]:
            if isinstance(link, dict) and link.get("video_no"):
                seen.add(str(link["video_no"]))
        for video_no in video_numbers(row["matched_videos"]):
            if video_no in seen or video_no not in videos:
                continue
            video = videos[video_no]
            labels.append(video["title"])
            product_links["associated_video_links"].append(
                {"video_no": video_no, "title": video["title"], "url": video["url"]}
            )
            seen.add(video_no)
            if not product_links["primary_video_url"] and video["url"]:
                product_links["primary_video_url"] = video["url"]
        if labels:
            existing = product_links["associated_videos"]
            product_links["associated_videos"] = "; ".join([part for part in [existing, "; ".join(labels)] if part])
    return links


def video_product_links(conn: sqlite3.Connection) -> dict[int, dict[str, object]]:
    links: dict[int, dict[str, object]] = {}
    rows = conn.execute(
        """
        SELECT product_id, catalog_id, product_name, matched_videos
        FROM product_crossrefs
        WHERE confidence <> 'Related only'
        ORDER BY id
        """
    )
    for row in rows:
        product_label = row["product_name"]
        filter_value = row["catalog_id"] or row["product_id"]
        for video_no in video_numbers(row["matched_videos"]):
            key = int(video_no)
            video_links = links.setdefault(key, {"products_text": "", "associated_product_links": []})
            seen = {
                link.get("filter_value")
                for link in video_links["associated_product_links"]
                if isinstance(link, dict)
            }
            if filter_value in seen:
                continue
            video_links["associated_product_links"].append(
                {
                    "title": product_label,
                    "view": "products",
                    "filter_key": "catalog_id",
                    "filter_value": filter_value,
                }
            )
    for video_links in links.values():
        video_links["products_text"] = "; ".join(link["title"] for link in video_links["associated_product_links"])
    return links


def video_idea_links(conn: sqlite3.Connection) -> dict[int, dict[str, object]]:
    links: dict[int, dict[str, object]] = {}
    rows = conn.execute(
        """
        SELECT idea, source_videos
        FROM video_ideas_without_product_record
        ORDER BY idea
        """
    )
    for row in rows:
        for video_no in video_numbers(row["source_videos"]):
            key = int(video_no)
            video_links = links.setdefault(key, {"ideas_text": "", "associated_idea_links": []})
            if any(link.get("filter_value") == row["idea"] for link in video_links["associated_idea_links"]):
                continue
            video_links["associated_idea_links"].append(
                {
                    "title": row["idea"],
                    "view": "unmatched-ideas",
                    "filter_key": "idea",
                    "filter_value": row["idea"],
                }
            )
    for video_links in links.values():
        video_links["ideas_text"] = "; ".join(link["title"] for link in video_links["associated_idea_links"])
    return links


def source_video_links(source_videos: object, videos: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    links: list[dict[str, object]] = []
    seen: set[str] = set()
    for video_no in video_numbers(source_videos):
        if video_no in seen:
            continue
        seen.add(video_no)
        video = videos.get(video_no)
        if not video:
            links.append({"title": video_no, "url": ""})
            continue
        links.append({"video_no": video_no, "label": video_no, "title": video["title"], "url": video["url"]})
    return links


def search_link_target(view: str, filter_key: str, filter_value: object, title: object, label: object | None = None) -> dict[str, object]:
    return {
        "label": str(label if label is not None else title),
        "title": str(title or ""),
        "view": view,
        "filter_key": filter_key,
        "filter_value": str(filter_value or ""),
    }


def enrich_search_rows(conn: sqlite3.Connection, rows: list[dict[str, object]]) -> list[dict[str, object]]:
    videos = video_index(conn)
    product_links = product_video_links(conn)
    video_links = video_product_links(conn)
    idea_links = video_idea_links(conn)
    product_labels = {
        row["product_id"]: {
            "catalog_id": row["catalog_id"],
            "product_id": row["product_id"],
            "product_name": row["product_name"],
        }
        for row in conn.execute("SELECT catalog_id, product_id, product_name FROM current_products")
    }

    for row in rows:
        kind = row.get("kind")
        identifier = str(row.get("identifier") or "")
        title = str(row.get("title") or "")
        row["title_links"] = []
        row["identifier_links"] = []
        row["result_links"] = []
        row["result_links_text"] = ""

        if kind == "video":
            video = videos.get(identifier)
            if video and video.get("url"):
                link = {"label": title, "title": title, "url": video["url"]}
                row["title_links"] = [link]
                row["identifier_links"] = [{"label": identifier, "title": title, "url": video["url"]}]
                row["result_links"].append({"label": "YouTube", "title": title, "url": video["url"]})
            linked_products = video_links.get(int(identifier), {}).get("associated_product_links", [])
            if isinstance(linked_products, list):
                row["result_links"].extend(linked_products)
            linked_ideas = idea_links.get(int(identifier), {}).get("associated_idea_links", [])
            if isinstance(linked_ideas, list):
                row["result_links"].extend(linked_ideas)
            row["result_links_text"] = "; ".join(str(link.get("label") or link.get("title") or "") for link in row["result_links"])
            continue

        if kind in {"product", "crossref"}:
            product_id = str(row.get("product_id") or "")
            product = product_labels.get(product_id, {})
            filter_value = product.get("catalog_id") or product_id or identifier
            product_name = product.get("product_name") or title
            product_link = search_link_target("products", "catalog_id", filter_value, product_name)
            row["title_links"] = [product_link]
            row["identifier_links"] = [
                search_link_target("products", "catalog_id", filter_value, product_name, identifier)
            ]
            row["result_links"].append(search_link_target("products", "catalog_id", filter_value, product_name, "Product row"))
            if kind == "crossref":
                row["result_links"].extend(source_video_links(row.get("matched_videos"), videos))
            else:
                associated_videos = product_links.get(product_id, {}).get("associated_video_links", [])
                if isinstance(associated_videos, list):
                    row["result_links"].extend(associated_videos)
            row["result_links_text"] = "; ".join(str(link.get("label") or link.get("title") or "") for link in row["result_links"])
            continue

        if kind == "idea":
            row["title_links"] = [search_link_target("unmatched-ideas", "idea", title, title)]
            row["identifier_links"] = source_video_links(identifier, videos)
            row["result_links"] = [
                search_link_target("unmatched-ideas", "idea", title, title, "Idea row"),
                *row["identifier_links"],
            ]
            row["result_links_text"] = "; ".join(str(link.get("label") or link.get("title") or "") for link in row["result_links"])

    return rows


def estimate_status(value: str | None) -> str:
    text = (value or "").lower()
    if not text:
        return ""
    if "owner-confirmed" in text or "confirmed" in text or "approved override" in text:
        return "Confirmed"
    if "assumption" in text or "estimate" in text or "guide" in text or "draft" in text or "reference" in text:
        return "Estimated"
    if "pending" in text or "blocked" in text or "not started" in text:
        return "Pending"
    return "Review"


def split_money_info(value: str | None) -> tuple[str, str]:
    text = (value or "").strip()
    if not text:
        return "", ""
    match = re.search(r"\$\d+(?:,\d{3})*(?:\.\d{2})?", text)
    if not match:
        return "", text
    amount = match.group(0)
    before = text[: match.start()].strip(" -–—:;,.")
    after = text[match.end() :].strip(" -–—:;,.")
    info = " ".join(part for part in [before, after] if part)
    return amount, info


def search_rows(conn: sqlite3.Connection, q: str, scope: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    fts_query = clean_query(q)
    like_query = f"%{q}%"

    def add_videos() -> None:
        if q:
            try:
                result = conn.execute(
                    """
                    SELECT 'video' AS kind, v.title, printf('%03d', v.video_no) AS identifier,
                           '' AS reference_code,
                           v.concept || ' Products: ' || v.products_text AS summary
                    FROM videos_fts f
                    JOIN videos v ON v.video_no = f.video_no
                    WHERE videos_fts MATCH ?
                    ORDER BY v.video_no
                    LIMIT 80
                    """,
                    (fts_query,),
                )
            except sqlite3.OperationalError:
                result = conn.execute(
                    """
                    SELECT 'video' AS kind, title, printf('%03d', video_no) AS identifier,
                           '' AS reference_code,
                           concept || ' Products: ' || products_text AS summary
                    FROM videos
                    WHERE title LIKE ? OR concept LIKE ? OR products_text LIKE ? OR transcript_text LIKE ?
                    ORDER BY video_no
                    LIMIT 80
                    """,
                    (like_query, like_query, like_query, like_query),
                )
        else:
            result = conn.execute(
                """
                SELECT 'video' AS kind, title, printf('%03d', video_no) AS identifier,
                       '' AS reference_code,
                       concept || ' Products: ' || products_text AS summary
                FROM videos
                ORDER BY video_no
                LIMIT 30
                """
            )
        rows.extend(dict_rows(result))

    def add_products() -> None:
        if q:
            try:
                result = conn.execute(
                    """
                    SELECT 'product' AS kind, p.product_name AS title,
                           COALESCE(NULLIF(p.catalog_id, ''), p.product_id) AS identifier,
                           p.reference_code,
                           p.product_id,
                           'Product ID: ' || p.product_id || '. ' || p.primary_use_case || ' Status: ' || p.status AS summary
                    FROM products_fts f
                    JOIN current_products p ON p.product_id = f.product_id
                    WHERE products_fts MATCH ?
                    ORDER BY p.product_name
                    LIMIT 80
                    """,
                    (fts_query,),
                )
            except sqlite3.OperationalError:
                result = conn.execute(
                    """
                    SELECT 'product' AS kind, product_name AS title,
                           COALESCE(NULLIF(catalog_id, ''), product_id) AS identifier,
                           reference_code,
                           product_id,
                           'Product ID: ' || product_id || '. ' || primary_use_case || ' Status: ' || status AS summary
                    FROM current_products
                    WHERE product_name LIKE ? OR product_id LIKE ? OR catalog_id LIKE ? OR reference_code LIKE ? OR source_links LIKE ? OR full_text LIKE ?
                    ORDER BY product_name
                    LIMIT 80
                    """,
                    (like_query, like_query, like_query, like_query, like_query, like_query),
                )
        else:
            result = conn.execute(
                """
                SELECT 'product' AS kind, product_name AS title,
                       COALESCE(NULLIF(catalog_id, ''), product_id) AS identifier,
                       reference_code,
                       product_id,
                       'Product ID: ' || product_id || '. ' || primary_use_case || ' Status: ' || status AS summary
                FROM current_products
                ORDER BY product_name
                LIMIT 30
                """
            )
        rows.extend(dict_rows(result))

    def add_crossrefs() -> None:
        if q:
            try:
                result = conn.execute(
                    """
                    SELECT 'crossref' AS kind, c.product_name AS title,
                           COALESCE(NULLIF(c.catalog_id, ''), c.product_id) AS identifier,
                           c.reference_code,
                           c.product_id,
                           c.matched_videos,
                           'Product ID: ' || c.product_id || '. ' || c.matched_videos || ' - ' || c.confidence || ': ' || c.how_identified AS summary
                    FROM crossrefs_fts f
                    JOIN product_crossrefs c ON c.id = f.row_id
                    WHERE crossrefs_fts MATCH ?
                    ORDER BY c.product_name
                    LIMIT 80
                    """,
                    (fts_query,),
                )
            except sqlite3.OperationalError:
                result = conn.execute(
                    """
                    SELECT 'crossref' AS kind, product_name AS title,
                           COALESCE(NULLIF(catalog_id, ''), product_id) AS identifier,
                           reference_code,
                           product_id,
                           matched_videos,
                           'Product ID: ' || product_id || '. ' || matched_videos || ' - ' || confidence || ': ' || how_identified AS summary
                    FROM product_crossrefs
                    WHERE product_name LIKE ? OR product_id LIKE ? OR catalog_id LIKE ? OR reference_code LIKE ? OR matched_videos LIKE ? OR how_identified LIKE ?
                    ORDER BY product_name
                    LIMIT 80
                    """,
                    (like_query, like_query, like_query, like_query, like_query, like_query),
                )
        else:
            result = conn.execute(
                """
                SELECT 'crossref' AS kind, product_name AS title,
                       COALESCE(NULLIF(catalog_id, ''), product_id) AS identifier,
                       reference_code,
                       product_id,
                       matched_videos,
                       'Product ID: ' || product_id || '. ' || matched_videos || ' - ' || confidence || ': ' || how_identified AS summary
                FROM product_crossrefs
                ORDER BY product_name
                LIMIT 30
                """
            )
        rows.extend(dict_rows(result))

    def add_ideas() -> None:
        if q:
            result = conn.execute(
                """
                SELECT 'idea' AS kind, idea AS title, source_videos AS identifier,
                       '' AS reference_code,
                       notes AS summary
                FROM video_ideas_without_product_record
                WHERE idea LIKE ? OR source_videos LIKE ? OR notes LIKE ?
                ORDER BY idea
                LIMIT 80
                """,
                (like_query, like_query, like_query),
            )
        else:
            result = conn.execute(
                """
                SELECT 'idea' AS kind, idea AS title, source_videos AS identifier,
                       '' AS reference_code,
                       notes AS summary
                FROM video_ideas_without_product_record
                ORDER BY idea
                LIMIT 30
                """
            )
        rows.extend(dict_rows(result))

    if scope in {"all", "videos"}:
        add_videos()
    if scope in {"all", "products"}:
        add_products()
    if scope in {"all", "crossrefs"}:
        add_crossrefs()
    if scope in {"all", "ideas"}:
        add_ideas()
    return enrich_search_rows(conn, rows)


class ResearchHandler(BaseHTTPRequestHandler):
    db_path: Path = DEFAULT_DB_PATH

    def log_message(self, format: str, *args: object) -> None:
        print(f"{self.address_string()} - {format % args}")

    def send_json(self, payload: object, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_html(self) -> None:
        body = HTML.encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)

        if path == "/":
            self.send_html()
            return
        if not self.db_path.exists():
            self.send_json({"error": f"Database not found: {self.db_path}"}, HTTPStatus.NOT_FOUND)
            return

        try:
            with connect(self.db_path) as conn:
                if path == "/api/stats":
                    self.send_json(
                        {
                            "videos": conn.execute("SELECT count(*) FROM videos").fetchone()[0],
                            "products": conn.execute("SELECT count(*) FROM current_products").fetchone()[0],
                            "crossrefs": conn.execute("SELECT count(*) FROM product_crossrefs").fetchone()[0],
                            "ideas": conn.execute("SELECT count(*) FROM video_product_ideas").fetchone()[0],
                            "unmatched_products": conn.execute("SELECT count(*) FROM current_products_without_video_match").fetchone()[0],
                            "unmatched_ideas": conn.execute("SELECT count(*) FROM video_ideas_without_product_record").fetchone()[0],
                        }
                    )
                elif path == "/api/search":
                    q = qs.get("q", [""])[0].strip()
                    scope = qs.get("scope", ["all"])[0]
                    self.send_json({"rows": search_rows(conn, q, scope)})
                elif path == "/api/videos":
                    rows = dict_rows(conn.execute("SELECT video_no, title, woodworking_relevance, concept, products_text, url FROM videos ORDER BY video_no"))
                    links = video_product_links(conn)
                    ideas = video_idea_links(conn)
                    for row in rows:
                        linked_products = links.get(int(row["video_no"]))
                        if linked_products:
                            row.update(linked_products)
                        else:
                            row["associated_product_links"] = []
                        linked_ideas = ideas.get(int(row["video_no"]))
                        if linked_ideas:
                            row.update(linked_ideas)
                        else:
                            row["ideas_text"] = ""
                            row["associated_idea_links"] = []
                    self.send_json({"rows": rows})
                elif path == "/api/products":
                    rows = dict_rows(
                        conn.execute(
                            """
                            SELECT catalog_id, product_id, product_name, reference_code, status, primary_use_case, plans_source_ref
                            FROM current_products
                            ORDER BY product_name
                            """
                        )
                    )
                    links = product_video_links(conn)
                    for row in rows:
                        row.update(
                            links.get(
                                row["product_id"],
                                {"primary_video_url": "", "associated_videos": "", "associated_video_links": []},
                            )
                        )
                    self.send_json({"rows": rows})
                elif path == "/api/pricing":
                    rows = dict_rows(
                        conn.execute(
                            """
                            SELECT
                                catalog_id,
                                product_id,
                                product_name,
                                reference_code,
                                status,
                                verification_status,
                                build_model,
                                cost_sheet_ref,
                                build_time_estimate,
                                lead_time_estimate,
                                unit_cost_estimate,
                                materials_cost_estimate,
                                pricing_strategy_1_price_floor,
                                pricing_strategy_2_price_floor,
                                target_price,
                                margin_estimate,
                                material_cost_percent_of_price,
                                recommended_price_floor,
                                pricing_strategy_review,
                                pricing_validation
                            FROM current_products
                            ORDER BY product_name
                            """
                        )
                    )
                    for row in rows:
                        material_amount, material_info = split_money_info(row.get("materials_cost_estimate"))
                        row["materials_cost_amount"] = material_amount
                        row["materials_cost_info"] = material_info
                        row["materials_cost_status"] = estimate_status(row.get("materials_cost_estimate"))
                        row["sale_price_status"] = estimate_status(row.get("target_price"))
                    self.send_json({"rows": rows})
                elif path == "/api/crossrefs":
                    rows = dict_rows(conn.execute("SELECT section, catalog_id, product_id, product_name, reference_code, matched_videos, confidence, how_identified FROM product_crossrefs ORDER BY section, product_name"))
                    links = product_video_links(conn)
                    for row in rows:
                        row.update(
                            links.get(
                                row["product_id"],
                                {"primary_video_url": "", "associated_videos": "", "associated_video_links": []},
                            )
                        )
                    self.send_json({"rows": rows})
                elif path == "/api/unmatched-products":
                    rows = dict_rows(conn.execute("SELECT catalog_id, product_id, product_name, reference_code, status, notes FROM current_products_without_video_match ORDER BY product_name"))
                    self.send_json({"rows": rows})
                elif path == "/api/unmatched-ideas":
                    rows = dict_rows(conn.execute("SELECT idea, source_videos, current_product_record, notes FROM video_ideas_without_product_record ORDER BY idea"))
                    videos = video_index(conn)
                    for row in rows:
                        row["source_video_links"] = source_video_links(row["source_videos"], videos)
                    self.send_json({"rows": rows})
                else:
                    self.send_json({"error": "Not found"}, HTTPStatus.NOT_FOUND)
        except Exception as exc:
            self.send_json({"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the local Woodcraft research web UI.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH, help="SQLite database path.")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind.")
    parser.add_argument("--port", type=int, default=8765, help="Port to bind.")
    args = parser.parse_args()

    db_path = args.db if args.db.is_absolute() else REPO_ROOT / args.db
    ResearchHandler.db_path = db_path
    server = ThreadingHTTPServer((args.host, args.port), ResearchHandler)
    print(f"Serving Woodcraft research UI at http://{args.host}:{args.port}")
    print(f"Database: {db_path}")
    server.serve_forever()


if __name__ == "__main__":
    main()
