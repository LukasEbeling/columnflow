# coding: utf-8

"""
Scinentific constants.
"""

from scinum import Number, Correlation, REL

from ap.util import DotDict


# misc
n_leps = Number(3)

# masses
m_z = Number(91.1876, {"z_mass": 0.0021})

# branching ratios
br_w = DotDict()
br_w["had"] = Number(0.6741, {"br_w": 0.0027})
br_w["lep"] = 1 - br_w.had

br_ww = DotDict(
    fh=br_w.had ** 2,
    dl=br_w.lep ** 2,
    sl=2 * br_w.had * Correlation(br_w=-1) * br_w.lep,
)

br_z = DotDict(
    clep=Number(0.033658, {"br_z_clep": 0.000023}) * n_leps,
)

br_h = DotDict(
    ww=Number(0.2152, (REL, 0.0153, 0.0152)),
    zz=Number(0.02641, (REL, 0.0153, 0.0152)),
    gg=Number(0.002270, (REL, 0.0205, 0.0209)),
    bb=Number(0.5809, (REL, 0.0124, 0.0126)),
    tt=Number(0.06256, (REL, 0.0165, 0.0163)),
)

br_hh = DotDict(
    bbbb=br_h.bb ** 2.0,
    bbvv=2.0 * br_h.bb * (br_h.ww + br_h.zz),
    bbww=2.0 * br_h.bb * br_h.ww,
    bbzz=2.0 * br_h.bb * br_h.zz,
    bbtt=2.0 * br_h.bb * br_h.tt,
    bbgg=2.0 * br_h.bb * br_h.gg,
    ttww=2.0 * br_h.tt * br_h.ww,
    ttzz=2.0 * br_h.tt * br_h.zz,
    tttt=br_h.tt ** 2.0,
    wwww=br_h.ww ** 2.0,
    zzzz=br_h.zz ** 2.0,
    wwzz=2.0 * br_h.ww * br_h.zz,
    wwgg=2.0 * br_h.ww * br_h.gg,
)
