from pyrepro.pyrepro import Artifact

@Artifact(keyword='outpath', allow_dirty=True)
def save_thing(outpath):
    with open(outpath) as outf:
        outf.write('good job')
