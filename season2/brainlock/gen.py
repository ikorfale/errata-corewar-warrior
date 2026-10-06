#!/usr/bin/env python3
"""gen.py — Trapdoor-family renderer for #170: trap list before/after, silk constants. Usage from other scripts."""
I3 = '((3-CORESIZE%3)*CORESIZE+1)/3'
def render(pre, post, d1=6368, d2=4980, j=-3135, name='t', nsplit=5):
    L = [';redcode-94', f';name {name}', ';author fable-terminal', f'I3      EQU     {I3}']
    L += [f'        STP.AB  #{v}, #{c}' for v, c in pre]
    L += ['paper   SPL     1'] + ['        SPL     1'] * (nsplit - 1)
    L += [f'silk    SPL     @0, {d1}', '        MOV.I   }-1, >-1', f'        SPL     @0, {d2}', '        MOV.I   }-1, >-1',
          '        MOV.I   pbomb, >-2', '        MOV.I   {-3, <1', f'        JMP     @0, {j}', 'pbomb   DAT.F   <I3, <2*I3']
    L += [f'        STP.AB  #{v}, #{c}' for v, c in post]
    L += ['        END     paper']
    return '\n'.join(L) + '\n'
TD = [(1, 113), (9, 115), (1, 101), (1000, 9)] * 3
