#!/bin/bash

/etc/init.d/ssh restart
# /bin/bash -c "cd /home/jovyan/dev/projects/master && jupyter notebook --port 8888 --no-browser --NotebookApp.password='root' --NotebookApp.token='' --NotebookApp.disable_check_xsrf=False --ip 0.0.0.0 --allow-root"
/bin/bash -c "cd /home/jovyan/dev/projects/master && jupyter notebook --port 8888 --no-browser --ip 0.0.0.0 --allow-root"
source ~/.bashrc
