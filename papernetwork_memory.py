# in ipython
#cd lib
import sys
import os
import time
import operator
import histeq
from numpy import mat
from numpy import zeros
from numpy import fill_diagonal
from numpy import sqrt, ones, multiply, array
import numpy
import networkx as nx
import community
import math
from networkx.readwrite import json_graph
from collections import defaultdict 
import tf_idf
#cd ..
from views import PaperNetwork
from app import create_app
#cd lib
app = create_app
r=app.test_client().get("/paper-network?q=star")
d = rson.loads(r.data)
with app.app_context():
    %mprun -f get_papernetwork get_papernetwork(d, 10)
