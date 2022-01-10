MMTF PySpark
============

|Build Status| |GitHub license| |Version| |Download MMTF| |Download MMTF
Reduced| |Twitter URL|

mmtfPyspark is a python package that provides APIs and sample
applications for distributed analysis and scalable mining of 3D
biomacromolecular structures, such as the Protein Data Bank (PDB)
archive. mmtfPyspark uses Big Data technologies to enable
high-performance parallel processing of macromolecular structures.
mmtfPyspark use the following technology stack:

- `Apache Spark <https://spark.apache.org/>`__ a fast and general engine for large-scale distributed data processing.
- `MMTF <https://mmtf.rcsb.org/>`__ the Macromolecular Transmission Format for compact data storage, transmission and high-performance parsing
- `Hadoop Sequence File <https://wiki.apache.org/hadoop/SequenceFile>`__ a Big Data file format for parallel I/O
- `Apache Parquet <https://parquet.apache.org/>`__ a columnar data format to store dataframes

This project is under development.

Run mmtf-pyspark in your Web Browser
------------------------------------

The Jupyter Notebooks in this repository can be run in your web browser using two freely available servers: Binder and CyVerse/VICE. Click on the buttons below to launch Jupyter Lab. **It may take several minutes for Jupyter Lab to launch.**

Navigate to the `demos directory <demos>`_ to run any of the example notebooks.

Binder
~~~~~~

`Binder <https://mybinder.org/>`_ is an experimental platform for reproducible research developed by `Project Jupyter <https://jupyter.org/>`_. Learn more about `Binder <https://blog.jupyter.org/mybinder-org-serves-two-million-launches-7543ae498a2a>`_. There are specific links for each notebook below, however, once Jupyter Lab is launched, navigate to any of the other notebooks using the Jupyter Lab file panel.

**NOTE:** Authentication is now required to launch binder! Sign into GitHub from your browser, then click on the `launch binder` badge below to launch Jupyter Lab.

.. image:: https://aws-uswest2-binder.pangeo.io/badge_logo.svg 
   :target: https://aws-uswest2-binder.pangeo.io/v2/gh/sbl-sdsc/mmtf-pyspark/master?urlpath=lab 

CyVerse (experimental version)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The new VICE (Visual Interactive Computing Environment) in the `CyVerse Discovery Environment <https://www.cyverse.org/discovery-environment>`_ enables users to run Jupyter Lab in a production environment. To use VICE, sign up for a free `CyVerse account <https://www.cyverse.org/create-account>`_.

The VICE environment supports large-scale analyses. Users can upload and download files, and save and share results of their analyses in their user accounts (up to 100GB of data). The environment is preloaded with a local copy of the entire Protein Data Bank (~148,000 structures).

.. image:: docs/vice_badge.png
   :target: https://de.cyverse.org/de/?type=apps&app-id=0c25cbcc-4a74-11e9-b417-008cfa5ae621&system-id=de 

`Follow these step to run Jupyter Lab on VICE <docs/vice_instructions.rst>`_


Documentation
-------------

`Documentation <http://mmtf-pyspark.readthedocs.io/en/latest/>`_

`In Depth Tutorial <https://github.com/sbl-sdsc/mmtf-workshop-2018/>`_

Installation
------------

Python
~~~~~~

We strongly recommend that you have
`anaconda <https://docs.continuum.io/anaconda/install/>`__ and we
require at least python 3.6 installed. To check your python version:

::

    python --version

If **Anaconda** is installed, and if you have python 3.6, the above
command should return:

::

    Python 3.6.4 :: Anaconda, Inc.

mmtfPyspark and dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since mmtfPyspark uses parallel computing to ensure high-performance, it
requires additional dependencies such as Apache Spark. Therefore, please
read follow the installation instructions for your OS carefully:

`MacOS and LINUX <http://mmtf-pyspark.readthedocs.io/en/latest/MacLinuxInstallation.html>`_

`Windows <http://mmtf-pyspark.readthedocs.io/en/latest/WindowsInstallation.html>`_

Hadoop Sequence Files
---------------------

This project uses the PDB archive in the form of MMTF Hadoop Sequence File. The files can be downloaded
by:

::

    curl -O https://mmtf.rcsb.org/v1.0/hadoopfiles/full.tar
    tar -xvf full.tar

    curl -O https://mmtf.rcsb.org/v1.0/hadoopfiles/reduced.tar
    tar -xvf reduced.tar

For Mac and Linux, the Hadoop sequence files can be downloaded and saved
as environmental variables by running the following command:

::

    curl https://raw.githubusercontent.com/sbl-sdsc/mmtf-pyspark/master/bin/download_mmtf_files.sh -o download_mmtf_files.sh
    . ./download_mmtf_files.sh

.. |Build Status| image:: https://travis-ci.org/sbl-sdsc/mmtf-pyspark.svg?branch=master
   :target: https://travis-ci.org/sbl-sdsc/mmtf-pyspark
.. |GitHub license| image:: https://img.shields.io/github/license/sbl-sdsc/mmtf-pyspark.svg
   :target: https://github.com/sbl-sdsc/mmtf-pyspark/blob/master/LICENSE
.. |Version| image:: http://img.shields.io/badge/version-0.3.6-yellowgreen.svg?style=flat
   :target: https://github.com/sbl-sdsc/mmtf-pyspark
.. |Download MMTF| image:: http://img.shields.io/badge/download-MMTF_full-yellow.svg?style=flat
   :target: https://mmtf.rcsb.org/v1.0/hadoopfiles/full.tar
.. |Download MMTF Reduced| image:: http://img.shields.io/badge/download-MMTF_reduced-orange.svg?style=flat
   :target: https://mmtf.rcsb.org/v1.0/hadoopfiles/reduced.tar
.. |Binder| image:: https://aws-uswest2-binder.pangeo.io/badge_logo.svg 
   :target: https://aws-uswest2-binder.pangeo.io/v2/gh/sbl-sdsc/mmtf-pyspark/master?urlpath=lab
.. |Twitter URL| image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social
   :target: https://twitter.com/mmtf_spec

How to Cite this Work
---------------------

Bradley AR, Rose AS, Pavelka A, Valasatava Y, Duarte JM, Prlić A, Rose PW (2017) MMTF - an efficient file format for the transmission, visualization, and analysis of macromolecular structures. PLOS Computational Biology 13(6): e1005575. doi: `10.1371/journal.pcbi.1005575 <https://doi.org/10.1371/journal.pcbi.1005575>`_

Valasatava Y, Bradley AR, Rose AS, Duarte JM, Prlić A, Rose PW (2017) Towards an efficient compression of 3D coordinates of macromolecular structures. PLOS ONE 12(3): e0174846. doi: `10.1371/journal.pone.01748464 <https://doi.org/10.1371/journal.pone.0174846>`_

Rose AS, Bradley AR, Valasatava Y, Duarte JM, Prlić A, Rose PW (2018) NGL viewer: web-based molecular graphics for large complexes, Bioinformatics, bty419. doi: `10.1093/bioinformatics/bty419 <https://doi.org/10.1093/bioinformatics/bty419>`_

Rose AS, Bradley AR, Valasatava Y, Duarte JM, Prlić A, Rose PW (2016) Web-based molecular graphics for large complexes. In Proceedings of the 21st International Conference on Web3D Technology (Web3D '16). ACM, New York, NY, USA, 185-186. doi: `10.1145/2945292.2945324 <https://doi.org/10.1145/2945292.2945324>`_

Binder
~~~~~~

Project Jupyter, et al. (2018) Binder 2.0 - Reproducible, Interactive, Sharable Environments for Science at Scale. Proceedings of the 17th Python in Science Conference. 2018. doi: `10.25080/Majora-4af1f417-011 <https://doi.org/10.25080/Majora-4af1f417-011>`_


CyVerse
~~~~~~~

Merchant N, Lyons E, Goff S, Vaughn M, Ware D, Micklos D, et al. (2016) The iPlant Collaborative: Cyberinfrastructure for Enabling Data to Discovery for the Life Sciences. PLoS Biol 14(1): e1002342. doi: `10.1371/journal.pbio.1002342 <https://doi.org/10.1371/journal.pbio.1002342>`_
 

Py3Dmol
~~~~~~~
Rego N, Koes, D (2015) 3Dmol.js: molecular visualization with WebGL, Bioinformatics 31, 1322–1324. doi: `10.1093/bioinformatics/btu829 <https://doi.org/10.1093/bioinformatics/btu829>`_

Funding
-------

The MMTF project (Compressive Structural BioInformatics: High Efficiency 3D Structure Compression) is supported by the National Cancer Institute of the National Institutes of Health under Award Number U01CA198942. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.

The CyVerse project is supported by the National Science Foundation under Award Numbers DBI-0735191,  DBI-1265383, and DBI-1743442. URL: www.cyverse.org
