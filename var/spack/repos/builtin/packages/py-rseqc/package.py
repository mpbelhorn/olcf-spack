# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyRseqc(PythonPackage):
    """RSeQC package provides a number of useful modules that can
    comprehensively evaluate high throughput sequence data especially RNA-seq
    data."""

    homepage = "http://rseqc.sourceforge.net"
    url      = "https://pypi.io/packages/source/R/RSeQC/RSeQC-2.6.4.tar.gz"

    version('2.6.4', sha256='e11df661bda1c24fc950f0bce06f586a68ab5f4a2c356f43e4a0dfdc1e184315')

    depends_on('py-setuptools', type='build')
    depends_on('py-bx-python',  type=('build', 'run'))
    depends_on('py-numpy',      type=('build', 'run'))
    depends_on('py-pysam',      type=('build', 'run'))
    depends_on('r',             type=('build', 'run'))
