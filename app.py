import numpy as np
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(page_title="Gradient Descent Visualizer", layout="wide")
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');
:root {
    --ink: #0f172a;
    --muted: #475569;
    --accent: #0ea5a4;
    --accent-2: #f97316;
    --card: rgba(255, 255, 255, 0.78);
    --border: rgba(15, 23, 42, 0.13);
}
.stApp {
    background:
        radial-gradient(1200px 440px at 0% -12%, rgba(14, 165, 164, 0.2), transparent 56%),
        radial-gradient(1100px 480px at 100% -14%, rgba(249, 115, 22, 0.16), transparent 54%),
        linear-gradient(180deg, #f4f8f6 0%, #eef3ff 100%);
    color: var(--ink);
    font-family: "Space Grotesk", "Avenir Next", "Segoe UI", sans-serif;
}
html, body, .stApp {
    color: var(--ink) !important;
}
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] *,
[data-testid="stSidebar"],
[data-testid="stSidebar"] * {
    color: var(--ink) !important;
}
[data-testid="stMarkdownContainer"] *,
[data-testid="stCaptionContainer"] *,
[data-testid="stText"] *,
[data-testid="stWidgetLabel"] * {
    color: var(--ink) !important;
}
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li {
    color: var(--ink) !important;
}
.stButton button,
.stButton button span,
.stButton button p,
button,
button span,
button p {
    color: var(--ink) !important;
}
[data-baseweb="input"] *,
[data-baseweb="select"] *,
input,
textarea,
label {
    color: var(--ink) !important;
}
[data-testid="stHeader"] {
    background: transparent;
}
.block-container {
    max-width: 96rem;
    padding-top: 1rem;
}
.app-hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 1rem 1.1rem;
    border: 1px solid var(--border);
    border-radius: 16px;
    background: linear-gradient(125deg, rgba(255,255,255,0.88), rgba(255,255,255,0.63));
    box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08);
    margin-bottom: 0.8rem;
}
.app-hero h1 {
    margin: 0.1rem 0 0.3rem;
    font-size: clamp(1.35rem, 2.4vw, 2.15rem);
    line-height: 1.1;
    color: var(--ink);
    letter-spacing: -0.015em;
}
.hero-kicker {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #0f766e;
}
.app-hero p {
    margin: 0;
    font-size: 0.93rem;
    color: #334155;
}
.hero-chip {
    min-width: 220px;
    padding: 0.72rem 0.8rem;
    border-radius: 12px;
    border: 1px solid rgba(14, 165, 164, 0.2);
    background: linear-gradient(135deg, rgba(14,165,164,0.13), rgba(249,115,22,0.14));
    color: #0f172a;
    font-size: 0.8rem;
    line-height: 1.45;
    font-weight: 600;
}
[data-testid="stMetric"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 0.52rem 0.62rem;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
}
[data-testid="stMetricValue"] {
    font-size: 1.02rem;
}
[data-testid="stMetricDelta"],
[data-testid="stMetricLabel"] {
    font-size: 0.76rem;
}
[data-testid="stMetricLabel"] p {
    color: var(--muted);
    font-weight: 600;
}
[data-testid="stInfo"] {
    border-radius: 12px;
    border: 1px solid var(--border);
    background: linear-gradient(135deg, rgba(14,165,164,0.13), rgba(56,189,248,0.08));
}
[data-testid="stSidebar"] > div:first-child {
    background: rgba(255, 255, 255, 0.66);
    border-right: 1px solid var(--border);
    backdrop-filter: blur(8px);
}
[data-testid="stSidebar"] .stSlider > div[data-baseweb="slider"] > div {
    background: rgba(15, 23, 42, 0.16) !important;
}
[data-testid="stSidebar"] .stSlider > div[data-baseweb="slider"] > div > div {
    background: linear-gradient(90deg, #0891b2, #0ea5a4) !important;
}
[data-testid="stSidebar"] .stSlider [role="slider"] {
    border: 2px solid #0f766e !important;
    background: #ffffff !important;
    box-shadow: 0 0 0 3px rgba(14, 165, 164, 0.24) !important;
}
[data-testid="stSidebar"] .stSlider [data-testid="stTickBar"] * {
    color: #0f172a !important;
}
[data-testid="stSidebar"] .stSlider [data-baseweb="input"] input {
    color: #0f172a !important;
    font-weight: 700 !important;
}
div[data-testid="stPlotlyChart"] {
    background: rgba(255, 255, 255, 0.53);
    border: 1px solid rgba(15, 23, 42, 0.1);
    border-radius: 14px;
    padding: 0.25rem 0.2rem 0.1rem;
    box-shadow: 0 7px 18px rgba(15, 23, 42, 0.07);
}
[data-testid="stCaptionContainer"] p {
    color: #334155;
}
code {
    font-family: "IBM Plex Mono", "Menlo", "Consolas", monospace;
}
pre, pre code {
    color: #0f172a !important;
    background: rgba(255, 255, 255, 0.86) !important;
}
.equation-strip {
    margin-top: 0.35rem;
    margin-bottom: 0.35rem;
    padding: 0.62rem 0.8rem;
    border-radius: 12px;
    border: 1px solid var(--border);
    background: linear-gradient(135deg, rgba(255,255,255,0.82), rgba(236,253,245,0.72));
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.8rem;
}
.equation-strip .label {
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #0f766e;
}
.equation-strip .eq {
    font-size: 0.96rem;
    font-weight: 700;
    color: #0f172a;
    font-family: "IBM Plex Mono", "Menlo", "Consolas", monospace;
}
.diagram-label {
    margin-top: 0.3rem;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: #0f766e !important;
}
.diagram-note {
    margin-top: 0.12rem;
    font-size: 0.8rem;
    color: #334155 !important;
}
.st-key-floating_controls {
    position: fixed;
    left: 22rem;
    bottom: 1rem;
    width: 290px;
    padding: 0.55rem 0.6rem;
    border: 1px solid var(--border);
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.94);
    box-shadow: 0 8px 24px rgba(17, 24, 39, 0.2);
    backdrop-filter: blur(4px);
    z-index: 1200;
}
.floating-label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #0f766e;
    margin-bottom: 0.25rem;
}
.st-key-floating_controls .stButton > button {
    height: 2.6rem;
    font-weight: 700;
    border-radius: 10px;
}
.st-key-next_step_floating button {
    background: linear-gradient(135deg, #0891b2, #0ea5a4) !important;
    color: white !important;
    border: none !important;
}
.st-key-reset_floating button {
    border: 1px solid rgba(15, 23, 42, 0.18) !important;
    background: rgba(255, 255, 255, 0.92) !important;
    color: #0f172a !important;
}
body:has(section[data-testid="stSidebar"][aria-expanded="false"]) .st-key-floating_controls {
    left: 1.25rem;
}
@media (max-width: 900px) {
    .app-hero {
        flex-direction: column;
        align-items: flex-start;
    }
    .hero-chip {
        width: 100%;
    }
    .st-key-floating_controls {
        left: 0.6rem;
        right: 0.6rem;
        width: auto;
        bottom: 0.6rem;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


def generate_data(n: int = 10, seed: int = 7) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    x = np.linspace(0.0, 10.0, n)
    noise = rng.normal(0.0, 0.8, size=n)
    y = 0.5 * x + 2.0 + noise
    return x, y


def ssr(x: np.ndarray, y: np.ndarray, m: float, b: float) -> float:
    residuals = y - (m * x + b)
    return float(np.sum(residuals ** 2))


def gradients(x: np.ndarray, y: np.ndarray, m: float, b: float) -> tuple[float, float, np.ndarray]:
    residuals = y - (m * x + b)
    grad_m = -2.0 * float(np.sum(x * residuals))
    grad_b = -2.0 * float(np.sum(residuals))
    return grad_m, grad_b, residuals


def initialize_state() -> None:
    x, y = generate_data()
    m0, b0 = 0.0, 0.0

    st.session_state.initialized = True
    st.session_state.x = x
    st.session_state.y = y
    st.session_state.m = m0
    st.session_state.b = b0
    st.session_state.step = 0
    st.session_state.last_grad_m = 0.0
    st.session_state.last_grad_b = 0.0
    st.session_state.last_grad_norm = 0.0
    st.session_state.last_delta_m = 0.0
    st.session_state.last_delta_b = 0.0
    st.session_state.m_history = [m0]
    st.session_state.b_history = [b0]
    st.session_state.ssr_history = [ssr(x, y, m0, b0)]


def run_step(learning_rate: float) -> None:
    x = st.session_state.x
    y = st.session_state.y
    m = st.session_state.m
    b = st.session_state.b

    grad_m, grad_b, _ = gradients(x, y, m, b)
    m_new = m - learning_rate * grad_m
    b_new = b - learning_rate * grad_b
    delta_m = m_new - m
    delta_b = b_new - b

    st.session_state.m = m_new
    st.session_state.b = b_new
    st.session_state.step += 1
    st.session_state.last_grad_m = grad_m
    st.session_state.last_grad_b = grad_b
    st.session_state.last_grad_norm = float(np.sqrt(grad_m ** 2 + grad_b ** 2))
    st.session_state.last_delta_m = delta_m
    st.session_state.last_delta_b = delta_b
    st.session_state.m_history.append(m_new)
    st.session_state.b_history.append(b_new)
    st.session_state.ssr_history.append(ssr(x, y, m_new, b_new))


def apply_2d_theme(fig: go.Figure) -> go.Figure:
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.48)",
        font=dict(family="Space Grotesk, Avenir Next, sans-serif", color="#0f172a", size=12),
        legend=dict(
            bgcolor="rgba(255,255,255,0.58)",
            bordercolor="rgba(15,23,42,0.08)",
            borderwidth=1,
            font=dict(color="#0f172a", size=11),
            title_font=dict(color="#0f172a", size=11),
        ),
    )
    fig.update_xaxes(
        gridcolor="rgba(100,116,139,0.24)",
        zeroline=False,
        title_standoff=8,
        tickfont=dict(color="#0f172a", size=11),
        title_font=dict(color="#0f172a", size=12),
        color="#0f172a",
    )
    fig.update_yaxes(
        gridcolor="rgba(100,116,139,0.24)",
        zeroline=False,
        title_standoff=8,
        tickfont=dict(color="#0f172a", size=11),
        title_font=dict(color="#0f172a", size=12),
        color="#0f172a",
    )
    return fig


def apply_3d_theme(fig: go.Figure) -> go.Figure:
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Space Grotesk, Avenir Next, sans-serif", color="#0f172a", size=12),
        legend=dict(
            bgcolor="rgba(255,255,255,0.58)",
            bordercolor="rgba(15,23,42,0.08)",
            borderwidth=1,
            font=dict(color="#0f172a", size=11),
            title_font=dict(color="#0f172a", size=11),
        ),
    )
    fig.update_scenes(
        bgcolor="rgba(255,255,255,0.3)",
        xaxis=dict(
            gridcolor="rgba(100,116,139,0.26)",
            zerolinecolor="rgba(100,116,139,0.33)",
            tickfont=dict(color="#0f172a", size=11),
            title_font=dict(color="#0f172a", size=12),
            color="#0f172a",
        ),
        yaxis=dict(
            gridcolor="rgba(100,116,139,0.26)",
            zerolinecolor="rgba(100,116,139,0.33)",
            tickfont=dict(color="#0f172a", size=11),
            title_font=dict(color="#0f172a", size=12),
            color="#0f172a",
        ),
        zaxis=dict(
            gridcolor="rgba(100,116,139,0.26)",
            zerolinecolor="rgba(100,116,139,0.33)",
            tickfont=dict(color="#0f172a", size=11),
            title_font=dict(color="#0f172a", size=12),
            color="#0f172a",
        ),
    )
    return fig


def build_data_space_fig(x: np.ndarray, y: np.ndarray, m: float, b: float) -> go.Figure:
    y_hat = m * x + b
    x_line = np.linspace(float(np.min(x)) - 0.5, float(np.max(x)) + 0.5, 150)
    y_line = m * x_line + b
    x_current = float(np.mean(x))
    y_current = m * x_current + b

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            name="Data",
            marker=dict(size=10, color="#1f77b4", line=dict(color="white", width=1)),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x_line,
            y=y_line,
            mode="lines",
            name="Prediction y = mx + b",
            line=dict(color="#ef4444", width=3),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[x_current],
            y=[y_current],
            mode="markers+text",
            name="Current model",
            marker=dict(size=10, color="#111827", symbol="diamond"),
            text=["Current"],
            textposition="top center",
            textfont=dict(color="#0f172a", size=11),
            hovertemplate="x=%{x:.3f}<br>y=%{y:.3f}<br>m="
            + f"{m:.3f}"
            + "<br>b="
            + f"{b:.3f}"
            + "<extra>Current model</extra>",
        )
    )

    for i, (x_i, y_i, y_hat_i) in enumerate(zip(x, y, y_hat)):
        fig.add_trace(
            go.Scatter(
                x=[x_i, x_i],
                y=[y_hat_i, y_i],
                mode="lines",
                line=dict(color="#6b7280", dash="dash", width=1.5),
                name="Residual" if i == 0 else None,
                showlegend=i == 0,
            )
        )

    fig.update_layout(
        xaxis_title="x",
        yaxis_title="y",
        margin=dict(l=10, r=10, t=10, b=10),
        height=470,
        showlegend=False,
    )
    return apply_2d_theme(fig)


def build_intercept_fig(x: np.ndarray, y: np.ndarray, m: float, b_current: float) -> go.Figure:
    b_opt_fixed_m = float(np.mean(y - m * x))
    spread = max(2.5, abs(b_current - b_opt_fixed_m) * 2.0 + 0.8)
    b_min = min(b_current, b_opt_fixed_m) - spread
    b_max = max(b_current, b_opt_fixed_m) + spread
    b_values = np.linspace(b_min, b_max, 280)
    ssr_values = np.array([ssr(x, y, m, b_val) for b_val in b_values])
    current_ssr = ssr(x, y, m, b_current)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=b_values,
            y=ssr_values,
            mode="lines",
            name="SSR(b) at fixed m",
            line=dict(color="#10b981", width=3),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[b_current],
            y=[current_ssr],
            mode="markers+text",
            name="Current (b, SSR)",
            marker=dict(size=11, color="#ef4444", symbol="diamond"),
            text=["Current"],
            textposition="bottom center",
            textfont=dict(color="#0f172a", size=10),
            hovertemplate="b=%{x:.3f}<br>SSR=%{y:.3f}<extra>Current point</extra>",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[b_current, b_current],
            y=[float(np.min(ssr_values)), current_ssr],
            mode="lines",
            name="Current b guide",
            line=dict(color="#111827", width=2, dash="dot"),
            hoverinfo="skip",
            showlegend=False,
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[b_values[0], b_current],
            y=[current_ssr, current_ssr],
            mode="lines",
            name="Current SSR guide",
            line=dict(color="#111827", width=2, dash="dot"),
            hoverinfo="skip",
            showlegend=False,
        )
    )

    fig.update_layout(
        xaxis_title="Intercept b",
        yaxis_title="SSR",
        margin=dict(l=10, r=10, t=10, b=10),
        height=470,
        showlegend=False,
    )
    return apply_2d_theme(fig)


def build_ssr_progress_fig(ssr_history: list[float]) -> go.Figure:
    steps = list(range(len(ssr_history)))
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=steps,
            y=ssr_history,
            mode="lines+markers",
            name="SSR over steps",
            line=dict(color="#0ea5e9", width=2.5),
            marker=dict(size=6),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[steps[-1]],
            y=[ssr_history[-1]],
            mode="markers",
            name="Current SSR",
            marker=dict(size=10, color="#ef4444", symbol="diamond"),
        )
    )
    fig.update_layout(
        title="SSR Progress by Step",
        xaxis_title="Step",
        yaxis_title="SSR",
        margin=dict(l=10, r=10, t=35, b=10),
        height=260,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0),
    )
    return apply_2d_theme(fig)


def compute_cost_grid(
    x: np.ndarray, y: np.ndarray, m_values: np.ndarray, b_values: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    m_grid, b_grid = np.meshgrid(m_values, b_values)
    y_pred = m_grid[..., None] * x + b_grid[..., None]
    residuals = y - y_pred
    z = np.sum(residuals ** 2, axis=2)
    return m_grid, b_grid, z


def build_cost_fig(
    x: np.ndarray,
    y: np.ndarray,
    m_history: list[float],
    b_history: list[float],
    grad_m: float,
    grad_b: float,
    use_surface: bool,
) -> go.Figure:
    m_ls, b_ls = np.polyfit(x, y, 1)
    m_candidates = np.array(m_history + [float(m_ls)])
    b_candidates = np.array(b_history + [float(b_ls)])

    m_pad = max(1.0, (float(np.max(m_candidates)) - float(np.min(m_candidates))) * 0.6 + 0.6)
    b_pad = max(1.5, (float(np.max(b_candidates)) - float(np.min(b_candidates))) * 0.6 + 1.0)

    m_values = np.linspace(float(np.min(m_candidates)) - m_pad, float(np.max(m_candidates)) + m_pad, 80)
    b_values = np.linspace(float(np.min(b_candidates)) - b_pad, float(np.max(b_candidates)) + b_pad, 80)
    m_grid, b_grid, z = compute_cost_grid(x, y, m_values, b_values)

    m_current = m_history[-1]
    b_current = b_history[-1]
    path_z = [ssr(x, y, m, b) for m, b in zip(m_history, b_history)]
    z_current = path_z[-1]
    z_min = float(np.min(z))
    z_max = float(np.max(z))
    z_range = max(1e-9, z_max - z_min)

    # Two slices through the current point make the m/b directions explicit.
    m_slice = np.linspace(float(m_values[0]), float(m_values[-1]), 120)
    z_slice_m = np.array([ssr(x, y, m_val, b_current) for m_val in m_slice])
    b_slice = np.linspace(float(b_values[0]), float(b_values[-1]), 120)
    z_slice_b = np.array([ssr(x, y, m_current, b_val) for b_val in b_slice])
    z_opt = ssr(x, y, float(m_ls), float(b_ls))

    neg_grad = np.array([-grad_m, -grad_b], dtype=float)
    grad_norm = float(np.linalg.norm(neg_grad))
    m_span = float(m_values[-1] - m_values[0])
    b_span = float(b_values[-1] - b_values[0])
    arrow_len = 0.12 * float(np.sqrt(m_span ** 2 + b_span ** 2))
    show_grad_arrow = grad_norm > 1e-12

    if show_grad_arrow:
        neg_grad = neg_grad / grad_norm
        m_arrow_end = m_current + arrow_len * float(neg_grad[0])
        b_arrow_end = b_current + arrow_len * float(neg_grad[1])
    else:
        m_arrow_end = m_current
        b_arrow_end = b_current

    if use_surface:
        fig = go.Figure()
        fig.add_trace(
            go.Surface(
                x=m_grid,
                y=b_grid,
                z=z,
                colorscale="Viridis",
                opacity=0.9,
                showscale=False,
                name="SSR Surface",
                contours=dict(
                    z=dict(show=True, usecolormap=True, highlightwidth=1, project_z=True),
                ),
                hovertemplate="m=%{x:.3f}<br>b=%{y:.3f}<br>SSR=%{z:.3f}<extra>SSR Surface</extra>",
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=m_history,
                y=b_history,
                z=path_z,
                mode="lines+markers",
                name="Descent path",
                line=dict(color="#ef4444", width=6),
                marker=dict(size=4, color="#ef4444"),
                customdata=np.arange(len(m_history)),
                hovertemplate="step=%{customdata}<br>m=%{x:.3f}<br>b=%{y:.3f}<br>SSR=%{z:.3f}<extra>Descent path</extra>",
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=m_history,
                y=b_history,
                z=[z_min] * len(m_history),
                mode="lines",
                name="Path projection",
                line=dict(color="#ef4444", width=3, dash="dot"),
                hoverinfo="skip",
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=m_slice,
                y=[b_current] * len(m_slice),
                z=z_slice_m,
                mode="lines",
                name="Slice: vary m (b fixed)",
                line=dict(color="#f59e0b", width=5),
                hovertemplate="m=%{x:.3f}<br>b=%{y:.3f} (fixed)<br>SSR=%{z:.3f}<extra>m-slice</extra>",
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=[m_current] * len(b_slice),
                y=b_slice,
                z=z_slice_b,
                mode="lines",
                name="Slice: vary b (m fixed)",
                line=dict(color="#06b6d4", width=5),
                hovertemplate="m=%{x:.3f} (fixed)<br>b=%{y:.3f}<br>SSR=%{z:.3f}<extra>b-slice</extra>",
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=[m_current, m_current],
                y=[b_current, b_current],
                z=[z_min, z_current],
                mode="lines",
                name="Current SSR height",
                line=dict(color="#111827", width=4, dash="dot"),
                hoverinfo="skip",
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=[m_current],
                y=[b_current],
                z=[z_current],
                mode="markers+text",
                name="Current",
                marker=dict(size=7, color="#111827"),
                text=["Current"],
                textposition="top center",
                textfont=dict(color="#0f172a", size=11),
                hovertemplate="m=%{x:.3f}<br>b=%{y:.3f}<br>SSR=%{z:.3f}<extra>Current</extra>",
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=[float(m_ls)],
                y=[float(b_ls)],
                z=[z_opt],
                mode="markers+text",
                name="Least-squares optimum",
                marker=dict(size=8, color="#fde047", symbol="diamond"),
                text=["Optimum"],
                textposition="top center",
                textfont=dict(color="#0f172a", size=11),
                hovertemplate="m*=%{x:.3f}<br>b*=%{y:.3f}<br>SSR*=%{z:.3f}<extra>Least-squares</extra>",
            )
        )
        if show_grad_arrow:
            arrow_z = z_current + 0.03 * z_range
            fig.add_trace(
                go.Scatter3d(
                    x=[m_current, m_arrow_end],
                    y=[b_current, b_arrow_end],
                    z=[arrow_z, arrow_z],
                    mode="lines",
                    name="-Gradient direction",
                    line=dict(color="#111827", width=5, dash="dash"),
                )
            )
            fig.add_trace(
                go.Cone(
                    x=[m_arrow_end],
                    y=[b_arrow_end],
                    z=[arrow_z],
                    u=[m_arrow_end - m_current],
                    v=[b_arrow_end - b_current],
                    w=[0.0],
                    anchor="tip",
                    sizemode="absolute",
                    sizeref=arrow_len * 0.18,
                    colorscale=[[0, "#111827"], [1, "#111827"]],
                    showscale=False,
                    name="-Gradient direction",
                )
            )
        fig.update_layout(
            scene=dict(
                xaxis_title="Slope m",
                yaxis_title="Intercept b",
                zaxis_title="SSR",
                xaxis=dict(range=[float(m_values[0]), float(m_values[-1])]),
                yaxis=dict(range=[float(b_values[0]), float(b_values[-1])]),
                camera=dict(eye=dict(x=1.6, y=1.4, z=0.9)),
                aspectmode="cube",
            ),
            margin=dict(l=10, r=10, t=10, b=10),
            height=620,
            showlegend=False,
        )
        return apply_3d_theme(fig)

    fig = go.Figure()
    fig.add_trace(
        go.Contour(
            x=m_values,
            y=b_values,
            z=z,
            colorscale="Viridis",
            contours=dict(showlabels=False),
            name="SSR contours",
            showscale=False,
        )
    )
    fig.add_trace(
        go.Scatter(
            x=m_history,
            y=b_history,
            mode="lines+markers",
            name="Descent path",
            line=dict(color="#ef4444", width=3),
            marker=dict(size=6, color="#ef4444"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[m_history[-1]],
            y=[b_history[-1]],
            mode="markers",
            name="Current",
            marker=dict(size=11, color="#111827", symbol="diamond"),
        )
    )
    if show_grad_arrow:
        fig.add_annotation(
            x=m_arrow_end,
            y=b_arrow_end,
            ax=m_current,
            ay=b_current,
            xref="x",
            yref="y",
            axref="x",
            ayref="y",
            showarrow=True,
            arrowhead=3,
            arrowsize=1.2,
            arrowwidth=2.5,
            arrowcolor="#111827",
        )
        fig.add_trace(
            go.Scatter(
                x=[m_current, m_arrow_end],
                y=[b_current, b_arrow_end],
                mode="lines",
                name="-Gradient direction",
                line=dict(color="#111827", width=2.5, dash="dash"),
            )
        )

    fig.update_layout(
        xaxis_title="Slope m",
        yaxis_title="Intercept b",
        margin=dict(l=10, r=10, t=10, b=10),
        height=620,
        showlegend=False,
    )
    return apply_2d_theme(fig)


if "initialized" not in st.session_state:
    initialize_state()

st.markdown(
    """
<section class="app-hero">
  <div>
    <div class="hero-kicker">Interactive Optimization Studio</div>
    <h1>Gradient Descent Visualization</h1>
    <p>Track how updates in parameter space move the line fit in data space and reduce SSR.</p>
  </div>
  <div class="hero-chip">
    Batch Gradient Descent<br>
    Loss: Sum of Squared Residuals (SSR)<br>
    Model: y = mx + b
  </div>
</section>
""",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Controls")
    learning_rate = st.slider(
        "Learning rate",
        min_value=0.0001,
        max_value=0.01,
        value=0.0010,
        step=0.0001,
        format="%.4f",
    )
    steps_per_click = st.slider("Steps per click", 1, 25, 1)
    use_3d_surface = st.checkbox("Diagram 3 as 3D surface", value=True)

floating_controls = st.container(key="floating_controls")
with floating_controls:
    st.markdown("<div class='floating-label'>Quick Actions</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        next_step = st.button(
            "Next Step",
            key="next_step_floating",
            use_container_width=True,
            type="primary",
        )
    with c2:
        reset = st.button("Reset", key="reset_floating", use_container_width=True)

if reset:
    initialize_state()
elif next_step:
    for _ in range(steps_per_click):
        run_step(learning_rate)

x = st.session_state.x
y = st.session_state.y
m = st.session_state.m
b = st.session_state.b
current_ssr = st.session_state.ssr_history[-1]
prev_ssr = st.session_state.ssr_history[-2] if len(st.session_state.ssr_history) > 1 else current_ssr
ssr_delta = current_ssr - prev_ssr

metrics = st.columns(7)
metrics[0].metric("Step", st.session_state.step)
metrics[1].metric("Slope (m)", f"{m:.4f}")
metrics[2].metric("Intercept (b)", f"{b:.4f}")
metrics[3].metric("SSR", f"{current_ssr:.4f}", delta=f"{ssr_delta:+.4f}")
metrics[4].metric("Delta m", f"{st.session_state.last_delta_m:+.4f}")
metrics[5].metric("Delta b", f"{st.session_state.last_delta_b:+.4f}")
metrics[6].metric("Gradient norm ||g||", f"{st.session_state.last_grad_norm:.4f}")
st.caption(
    f"Current gradients: dm = {st.session_state.last_grad_m:.4f}, db = {st.session_state.last_grad_b:.4f}"
)

st.markdown(
    f"""
<div class="equation-strip">
  <div class="label">Current Equation</div>
  <div class="eq">y = {m:.4f}x + {b:.4f}</div>
</div>
""",
    unsafe_allow_html=True,
)

fig_progress = build_ssr_progress_fig(st.session_state.ssr_history)
st.plotly_chart(fig_progress, use_container_width=True)

st.markdown("#### Synchronized Views")
col1, col2, col3 = st.columns([1.0, 1.0, 1.6])

with col1:
    fig1 = build_data_space_fig(x, y, m, b)
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("**Diagram 1: Data Space**")
    st.caption(f"Scatter + prediction line + residuals. Current m={m:.3f}, b={b:.3f}")

with col2:
    fig2 = build_intercept_fig(x, y, m, b)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("**Diagram 2: Intercept Space**")
    st.caption(f"SSR vs intercept b at fixed m. Current b={b:.3f}, SSR={current_ssr:.3f}")

with col3:
    fig3 = build_cost_fig(
        x=x,
        y=y,
        m_history=st.session_state.m_history,
        b_history=st.session_state.b_history,
        grad_m=st.session_state.last_grad_m,
        grad_b=st.session_state.last_grad_b,
        use_surface=use_3d_surface,
    )
    st.plotly_chart(fig3, use_container_width=True)
    title3 = "Diagram 3 · Full Cost Surface" if use_3d_surface else "Diagram 3 · Cost Contour"
    st.markdown(f"**{title3.replace('·', ':')}**")
    note3 = (
        "Error landscape over (m,b). Red path shows descent; orange/cyan are local m/b slices."
        if use_3d_surface
        else "Top-down error bowl in (m,b) with descent path and gradient direction."
    )
    st.caption(note3)

st.markdown("### Update Rule Used For Each Step")
st.code(
    "grad_m = -2 * sum(x_i * (y_i - y_pred_i))\n"
    "grad_b = -2 * sum(y_i - y_pred_i)\n"
    "m <- m - learning_rate * grad_m\n"
    "b <- b - learning_rate * grad_b",
    language="text",
)
st.markdown("<div style='height: 90px;'></div>", unsafe_allow_html=True)
