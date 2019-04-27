=======
pyrepro
=======


.. image:: https://img.shields.io/pypi/v/pyrepro.svg
        :target: https://pypi.python.org/pypi/pyrepro

.. image:: https://img.shields.io/travis/jisantuc/pyrepro.svg
        :target: https://travis-ci.org/jisantuc/pyrepro

.. image:: https://readthedocs.org/projects/pyrepro/badge/?version=latest
        :target: https://pyrepro.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/jisantuc/pyrepro/shield.svg
     :target: https://pyup.io/repos/github/jisantuc/pyrepro/
     :alt: Updates



Simple artifact versioning and caching for scientific workflows


* Free software: MIT license
* Documentation: https://pyrepro.readthedocs.io.


Features
--------

`pyrepro` exists to provide a simple interface for versioning functions that produce artifacts.
An "artifact" could be anything -- maybe you have some sort of ETL pipeline that writes intermediate files,
or you have a plotting function that writes a bunch of plots to disk, or you have a machine learning
workflow that produces a bunch of model files somewhere. The purpose of `pyrepro` is to allow you
to write normally -- give your output its regular name, like `plot.png` -- and automatically attach
git commit and configuration information as part of the path.

Example
-------

The following example shows how to use `pyrepro` to tag an output file with commit and config info:

.. codeblock:: python

    from pyrepro import Artifact
    @Artifact(keyword='outpath', config={}, allow_dirty=True)
    def save_thing(outpath):
        with open(outpath, 'w') as outf:
            outf.write('good job')
    

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
