from pyrepro.pyrepro import Artifact

@Artifact(keyword='outpath', config={}, allow_dirty=True)
def save_thing(outpath):
    with open(outpath, 'w') as outf:
        outf.write('good job')

if __name__ == '__main__':
    save_thing(outpath='lol.txt')
