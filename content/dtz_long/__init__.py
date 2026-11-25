# -*- coding: utf-8 -*-
"""Lengthening patches so DTZ Hören/Lesen texts reach the length of the official DTZ Übungssätze (see claude/dtz-b1-patterns.md).
LONGER[n] = dict(h1=[ins x4], h2=[ins x5], h3=[(pos,[turns]) x4], h3tf={i:(stmt,idx)}, h4=[ins x3], l2=[ins x8], l3=[ins x3], l3tf={i:(stmt,idx)}, l4=[ins...], l5=[ins...])
ins = extra string (appended) or (anchor, extra) -> extra inserted right after anchor (anchor must occur in the text)."""
import importlib, pkgutil
LONGER = {}
for _m in pkgutil.iter_modules(__path__):
    mod = importlib.import_module(__name__ + "." + _m.name)
    LONGER.update(getattr(mod, "LONGER", {}))


def _ins(text, spec, where=""):
    if spec in (None, "", ()):
        return text
    if isinstance(spec, list):
        for sp in spec:
            text = _ins(text, sp, where)
        return text
    if isinstance(spec, str):
        if spec.startswith("\n"):
            return text.rstrip() + spec
        return text.rstrip() + " " + spec
    anchor, extra = spec
    assert anchor in text, f"anchor not found ({where}): {anchor!r}"
    return text.replace(anchor, anchor + " " + extra, 1)


def apply(n, M):
    P = LONGER.get(n)
    if not P:
        return
    for k in ("h1", "h2"):
        if k in P:
            assert len(P[k]) == len(M[k]), (n, k)
            M[k] = [(_ins(t, P[k][i], f"{n}{k}{i}"), q, o, a) for i, (t, q, o, a) in enumerate(M[k])]
    if "h3" in P:
        out = []
        for i, (st, turns, qs) in enumerate(M["h3"]):
            turns = list(turns)
            pos, extra = P["h3"][i]
            if pos < 0:
                pos = len(turns) + pos
            turns[pos:pos] = [tuple(x) for x in extra]
            turns += [tuple(x) for x in P.get("h3end", {}).get(i, [])]
            qs = list(qs)
            if i in P.get("h3q", {}):
                qs = [tuple(x) for x in P["h3q"][i]]
            if i in P.get("h3tf", {}):
                for j, (q, o, a) in enumerate(qs):
                    if o.startswith("richtig"):
                        qs[j] = (P["h3tf"][i][0], o, P["h3tf"][i][1])
            out.append((st, turns, qs))
        M["h3"] = out
    if "h4" in P:
        th, sp, stm, ans = M["h4"]
        M["h4"] = (th, [_ins(t, P["h4"][i], f"{n}h4{i}") for i, t in enumerate(sp)], stm, ans)
    if "l2" in P:
        ads, sits, ans = M["l2"]
        M["l2"] = ([_ins(t, P["l2"][i], f"{n}l2{i}") for i, t in enumerate(ads)], sits, ans)
    if "l3" in P:
        new = []
        for i, item in enumerate(M["l3"]):
            tx, qs = item[0], [list(q) for q in item[1]]
            tx = _ins(tx, P["l3"][i], f"{n}l3{i}")
            if i in P.get("l3tf", {}):
                for q in qs:
                    if q[1].startswith("richtig"):
                        q[0], q[2] = P["l3tf"][i]
            new.append([tx, qs] if isinstance(item, list) else (tx, qs))
        M["l3"] = new
    for k in ("l4", "l5"):
        if k in P:
            tx, qs = M[k]
            for j, sp_ in enumerate(P[k]):
                tx = _ins(tx, sp_, f"{n}{k}{j}")
            M[k] = (tx, qs)
