import math
def predire_corners(dom, ext, moy_dom, moy_ext):
    total = moy_dom + moy_ext
    p_pair = (1 + math.exp(-2 * total)) / 2
    print(f"{dom} vs {ext}")
    print(f"Total Corners attendu : {total:.1f}")
    if p_pair > 0.5:
        print(f"CORNERS Total Pair : OUI - {p_pair*100:.0f}%")
    else:
        print(f"CORNERS Total Pair : NON - {(1-p_pair)*100:.0f}%")
predire_corners("Argentine", "Costa Rica", 6.2, 4.1)
