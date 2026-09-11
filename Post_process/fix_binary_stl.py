import struct
import os


cwd = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(cwd, "..", "MRF_quad_rotor_with_body", "mesh", "constant", "triSurface", "droneBody.stl")
dst = os.path.join(cwd, "..", "MRF_quad_rotor_with_body", "mesh", "constant", "triSurface", "droneBody_clean.stl")

with open(src, "rb") as f:
    header = f.read(80)
    (n,) = struct.unpack("<I", f.read(4))
    facets = [f.read(50) for _ in range(n)]

with open(dst, "wb") as f:
    f.write(b"blade_M1".ljust(80, b"\0"))
    f.write(struct.pack("<I", n))
    for tri in facets:
        f.write(tri[:48] + b"\x00\x00")

print(f"wrote {n} triangles")