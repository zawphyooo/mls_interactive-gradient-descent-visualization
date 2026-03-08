# Interactive Gradient Descent Visualization App

A Streamlit app that demonstrates batch gradient descent for simple linear regression (`y = mx + b`) with three synchronized diagrams:

1. **Data space (`x` vs `y`)** with residual lines.
2. **Intercept parameter space** showing `SSR` as a function of `b` with current point marker.
3. **Full cost landscape (`m`, `b`, `SSR`)** as a 3D surface (or contour alternative) with descent history trail and negative-gradient direction indicator.

Extra clarity elements:
- **SSR progress chart** (`SSR` vs optimization step).
- **Current equation panel** showing `y = m*x + b` with live values.
- **Update diagnostics** with `Delta m`, `Delta b`, and gradient norm `||g||`.
- **3D reading guides**: path projection on floor, local `m`/`b` slice curves through the current point, and a vertical SSR height line.

## Setup

```bash
cd /Users/zawphyooo/Documents/New\ project/interactive-gradient-descent-visualization
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Controls

- `Learning rate` slider
- `Steps per click` slider
- `Next Step` button (applies gradient updates)
- `Reset` button (restarts from initial parameters)
- Toggle for `Diagram 3 as 3D surface`

## Gradient Descent Equations

- `SSR(m, b) = sum((y_i - (m*x_i + b))^2)`
- `grad_m = -2 * sum(x_i * (y_i - y_pred_i))`
- `grad_b = -2 * sum(y_i - y_pred_i)`
- `m <- m - lr * grad_m`
- `b <- b - lr * grad_b`
