rule all:
    input: "results/capacity_vs_cycle.png"

rule plot_capacity:
    input: "data/raw/battery_cycle_level_dataset_CLEAN_FINAL.csv"
    output: "results/capacity_vs_cycle.png"
    shell: "python src/plot_capacity.py {input} {output}"
