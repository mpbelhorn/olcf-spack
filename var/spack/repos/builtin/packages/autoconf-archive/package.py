# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class AutoconfArchive(AutotoolsPackage, GNUMirrorPackage):
    """
    The GNU Autoconf Archive is a collection of more than 500 macros for GNU
    Autoconf that have been contributed as free software by friendly supporters
    of the cause from all over the Internet. Every single one of those macros
    can be re-used without imposing any restrictions whatsoever on the licensing
    of the generated configure script.
    """

    homepage = "https://www.gnu.org/software/autoconf-archive/"
    gnu_mirror_path = "mpfr/mpfr-4.0.2.tar.bz2"
    gnu_mirror_path = "autoconf-archive/autoconf-archive-2019.01.06.tar.xz"

    maintainers = ['mpbelhorn']

    version('2019.01.06', sha256='17195c833098da79de5778ee90948f4c5d90ed1a0cf8391b4ab348e2ec511e3f')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    def setup_dependent_build_environment(self, env, dependent_spec):
        """Adds the ACLOCAL path for autotools."""
        env.append_path('ACLOCAL_PATH', self.prefix.share.aclocal)
