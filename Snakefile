# Snakefile for Food Health Analysis

# 1. TARGET RULE
rule all:
    input:
        "is477_final_analysis_executed.ipynb"

# 2. ACQUISITION RULE
rule acquire_data:
    output:
        "fastfood.csv",
        "food.csv",
        "FOOD-DATA-GROUP1.csv"
    shell:
        "python scripts/acquire_data.py"

# 3. ANALYSIS RULE
rule run_analysis:
    input:
        notebook = "is477_final_analysis.ipynb",
        # We list the data as inputs so Snakemake knows to run acquire_data first
        data1 = "fastfood.csv",
        data2 = "food.csv",
        data3 = "FOOD-DATA-GROUP1.csv"
    output:
        "is477_final_analysis_executed.ipynb"
    shell:
        # Removed --inplace so it creates the new output file required by Snakemake
        "jupyter nbconvert --to notebook --execute {input.notebook} --output {output}"