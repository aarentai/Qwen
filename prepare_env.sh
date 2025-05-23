cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ~/Miniconda3-latest-Linux-x86_64.sh
conda create -n qwen python=3.12.6
conda activate qwen
pip install --file requirements.txt
git clone https://github.com/Dao-AILab/flash-attention
cd flash-attention && pip install .