import sympy
from sympy.abc import n

import rooted_trees as rt
import runge_kutta_method as rk

def test_elementary_weight_MatrixExpr():
    ex = rk.extrap(6, 'midpoint')
    results = map(rk.elementary_weight, rt.list_trees(4))
    # Verification by hand
    # for a, b in zip(map(rk.elementary_weight_str, rt.list_trees(4)), results):
    #     print a, b

    assert len(results) == 4
    assert all(isinstance(r, sympy.MatrixExpr) for r in results)
    assert all(r.shape == (n, 1) for r in results)
