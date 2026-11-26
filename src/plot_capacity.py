import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

inp, out = sys.argv[1], sys.argv[2]
df = pd.read_csv(inp)
keep = ["B0005", "B0006", "B0007", "B0018"]

fig, ax = plt.subplots()
for b, g in df[df.battery_id.isin(keep)].groupby("battery_id"):
    ax.plot(g.cycle, g.capacity, label=b)
ax.set_xlabel("Cycle")
ax.set_ylabel("Capacity (Ah)")
ax.legend()
fig.savefig(out, dpi=150, bbox_inches="tight")
