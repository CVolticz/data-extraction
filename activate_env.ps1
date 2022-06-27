if (conda env list | Select-String -Pattern "ToolsDevelopmentData") {
    conda activate ToolsDevelopmentData
} else {
    conda env create -n ToolsDevelopmentData python=3.8
    conda activate ToolsDevelopmentData
    pip install -r requirements.txt
}