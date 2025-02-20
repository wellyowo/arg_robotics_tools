FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
###################################### user #####################################

ENV SHELL=/bin/bash \
    USER=arg \
    UID=1000 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

ENV HOME=/home/${USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${UID} \
    ${USER} 

RUN echo "root:root" | chpasswd
RUN echo "${USER}:111111" | chpasswd

###################################### basic tools #####################################

RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -yq dist-upgrade \
    && apt-get -o Acquire::ForceIPv4=true install -yq --no-install-recommends \
    locales \
    cmake\
    make \
    git \
    vim \
    gedit \
    wget \
    sudo \
    lsb-release \
    build-essential \
    net-tools \
    dirmngr \
    gnupg2 \
    mercurial \
    libopencv-dev \
    libcanberra-gtk-module \
    libcanberra-gtk3-module \
    libpcap-dev \
    python3-pip \
    python3-setuptools \
    python3-opencv \
    python3-numpy \
    python3-empy  \
    python3-lxml \
    python3-pymodbus \
    terminator \
    screen \
    nginx \
    openssh-server \
    libglfw3-dev \
    iputils-ping \
    libncurses5-dev \
    libgtk2.0-dev \
    libatk1.0-dev \
    libcairo2-dev \
    libx11-dev \
    libxpm-dev \
    libxt-dev \
    python3-dev \
    pybind11-dev \
    ctags \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

##################################### PIP3 ######################################

RUN pip3 install --upgrade pip setuptools

RUN pip3 install \
    gdown \
    nbdev \
    apriltag \
    pytransform3d \
    virtualenv \
    pytest \
    flask \
    jupyter \
    jupyter_http_over_ws \
    flask-socketio \
    urdfpy \
    twine \
    roslibpy \
    python_tsp \ 
    pypozyx \
    pyyaml \
    arg_robotics_tools

RUN jupyter serverextension enable --py jupyter_http_over_ws

##################################### vim-python-ide ######################################

RUN git clone https://github.com/ARG-NCTU/vim-python-ide.git && \
    cd vim-python-ide && ./install.sh

##################################### setting #####################################

RUN chown -R ${USER}:${USER} ${HOME}/
RUN echo "${USER} ALL=(ALL)  ALL" > /etc/sudoers
RUN usermod -a -G dialout ${USER}

COPY ./colab_jupyter.sh /home/arg/
USER ${USER}

WORKDIR ${HOME}
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
