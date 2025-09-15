FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2022.9.5 
RUN pip install dgl==0.4.3.post2
RUN pip install dgllife==0.2.3
RUN pip install torch==1.9.0
RUN dir=$([ -w /root ] && echo /root || echo ${HOME:-/tmp}) && mkdir -p "$dir/.dgl" && [ ! -f "$dir/.dgl/config.json" ] && echo '{"backend": "pytorch"}' > "$dir/.dgl/config.json" || true

WORKDIR /repo
COPY . /repo
