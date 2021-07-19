# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class VotcaCsg(CMakePackage):
    """Versatile Object-oriented Toolkit for Coarse-graining
       Applications (VOTCA) is a package intended to reduce the amount of
       routine work when doing systematic coarse-graining of various
       systems. The core is written in C++.

       This package contains the VOTCA coarse-graining engine.
    """
    homepage = "http://www.votca.org"
    url      = "https://github.com/votca/csg/tarball/v1.4"
    git      = "https://github.com/votca/csg.git"
    maintainers = ['junghans']

    version('master', branch='master')
    version('stable', branch='stable')
    version('2021.1',
            sha256='e87791c7534996909a403f61ca1f2725e91f1ca7185aa6655188b814ca04f278',
            url='https://github.com/votca/csg/archive/77b8a0bb7b1272cb65d2b02c7db8b14cb5c2a6c5.tar.gz')
    version('1.6.2', sha256='96b244b282005259832ed6ec0dc22dafe132dcfc3d73dcd8e53b62f40befb545')
    version('1.6.1', sha256='ed12bcb1ccdf71f54e21cdcc9803add4b8ebdc6b8263cb5b0034f5db01e31dbb')
    version('1.6', sha256='8cf6a4ac3ef7347c720a44d8a676f8cbd1462e162f6113de39f27b89354465ea')
    version('1.5.1', sha256='7fca1261bd267bf38d2edd26259730fed3126c0c3fd91fb81940dbe17bb568fd')
    version('1.5', sha256='160387cdc51f87dd20ff2e2eed97086beee415d48f3c92f4199f6109068c8ff4')
    version('1.4.1', sha256='41dccaecadd0165c011bec36a113629e27745a5a133d1a042efe4356acdb5450')
    version('1.4', sha256='c13e7febd792de8c3d426203f089bd4d33b8067f9db5e8840e4579c88b61146e')

    depends_on("cmake@2.8:", type='build')
    for v in ["1.4", "1.4.1", "1.5", "1.5.1", "1.6", "1.6.1", "1.6.2",
              "master", "stable"]:
        depends_on('votca-tools@%s' % v, when="@%s:%s.0" % (v, v))
    depends_on('votca-tools@2021', when="@2021:2021.1")
    depends_on("boost")
    depends_on("gromacs~mpi@5.1:2019.9999")
    depends_on("hdf5~mpi")
