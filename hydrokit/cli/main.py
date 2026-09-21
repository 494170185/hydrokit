"""CLI entry: `python -m hydrokit`."""
from __future__ import annotations

import argparse
import sys

from hydrokit import __version__
from hydrokit.infiltration.curve_number import runoff_depth_cn
from hydrokit.precip.design_storm import chicago_hyetograph
from hydrokit.precip.idf import IDFCurve


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="hydrokit")
    p.add_argument("--version", action="store_true")
    sub = p.add_subparsers(dest="cmd")

    p_storm = sub.add_parser("storm")
    p_storm.add_argument("--a", type=float, default=20.0)
    p_storm.add_argument("--c", type=float, default=0.4)
    p_storm.add_argument("--b", type=float, default=10.0)
    p_storm.add_argument("--n", type=float, default=0.7)
    p_storm.add_argument("--duration", type=float, default=60.0, help="min")
    p_storm.add_argument("--step", type=float, default=5.0, help="min")
    p_storm.add_argument("--T", type=float, default=20.0, help="return period years")

    p_cn = sub.add_parser("runoff")
    p_cn.add_argument("--p", type=float, required=True, help="precip depth mm")
    p_cn.add_argument("--cn", type=float, required=True)
    p_cn.add_argument("--lambda-coef", type=float, default=0.2)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.version:
        print(__version__)
        return 0
    if args.cmd == "storm":
        curve = IDFCurve(a=args.a, c=args.c, b=args.b, n=args.n)
        hs = chicago_hyetograph(curve, args.duration, args.step, args.T)
        for i, h in enumerate(hs):
            print(f"step {i + 1}: {h:.3f} mm")
        print(f"total: {sum(hs):.2f} mm")
        return 0
    if args.cmd == "runoff":
        q = runoff_depth_cn(args.p, args.cn, lambda_coef=args.lambda_coef)
        print(f"runoff depth: {q:.3f} mm (P={args.p}, CN={args.cn})")
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
