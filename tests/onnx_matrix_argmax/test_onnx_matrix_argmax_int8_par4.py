from __future__ import absolute_import
from __future__ import print_function

import os
import sys

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

import nngen as ng
import veriloggen

import onnx_matrix_argmax


act_shape = (15, 31)
act_dtype = ng.int8
par = 4
chunk_size = 64
axi_datawidth = 32


def test(request, silent=True):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    rslt = onnx_matrix_argmax.run(act_shape,
                                  act_dtype,
                                  par,
                                  chunk_size,
                                  axi_datawidth, silent,
                                  filename=None, simtype=simtype,
                                  outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')

    verify_rslt = rslt.splitlines()[-1]
    assert(verify_rslt == '# verify: PASSED')


if __name__ == '__main__':
    rslt = onnx_matrix_argmax.run(act_shape,
                                  act_dtype,
                                  par,
                                  chunk_size,
                                  axi_datawidth, silent=False,
                                  filename='tmp.v',
                                  outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')
    print(rslt)
