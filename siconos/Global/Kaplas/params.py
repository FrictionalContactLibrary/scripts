import siconos.numerics as Numerics

t0 = 0
T = 10
h = 0.0005
g = 9.81
theta = 0.50001
mu = 0.3
dump_itermax = 80
dump_probability = .02
itermax = 1000
NewtonMaxIter = 1
tolerance = 1e-8
solver = Numerics.SICONOS_GLOBAL_FRICTION_3D_ADMM

# fileName = "KaplasTower"
# title = "KaplasTower"
# description = """
# A Kapla Tower with Bullet collision detection
# Moreau TimeStepping: h={0}, theta = {1}
# One Step non smooth problem: {2}, maxiter={3}, tol={4}
# """.format(h, theta, Numerics.idToName(solver),
#            itermax,
#            tolerance)

# mathInfo = ""
