# a unit test driver -- these should ru w/o error

all = (
    'WallisPi.py',
    'weave_callback.py',
    'weave_cplx.py',
    'weave_examples.py',
    'marching_cubes.py',
    )

for fname in all:
    print 'running %s'%fname
    os.system('python %s'%fname)

print "That's all folks"
