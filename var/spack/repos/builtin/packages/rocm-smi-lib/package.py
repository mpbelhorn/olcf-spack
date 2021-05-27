# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import shutil
import os


class RocmSmiLib(CMakePackage):
    """It is a C library for Linux that provides a user space interface
       for applications to monitor and control GPU applications."""

    homepage = "https://github.com/RadeonOpenCompute/rocm_smi_lib"
    git      = "https://github.com/RadeonOpenCompute/rocm_smi_lib.git"
    url      = "https://github.com/RadeonOpenCompute/rocm_smi_lib/archive/rocm-4.2.0.tar.gz"

    maintainers = ['srekolam', 'arjun-raj-kuppala']

    version('master', branch='master')
    version('4.2.0', sha256='c31bf91c492f00d0c5ab21e45afbd7baa990e4a8d7ce9b01e3b988e5fdd53f50')
    version('4.1.0', sha256='0c1d2152e40e14bb385071ae16e7573290fb9f74afa5ab887c54f4dd75849a6b')
    version('4.0.0', sha256='93d19229b5a511021bf836ddc2a9922e744bf8ee52ee0e2829645064301320f4')
    version('3.10.0', sha256='8bb2142640d1c6bf141f19accf809e61377a6e0c0222e47ac4daa5da2c85ddac')
    version('3.9.0', sha256='b2934b112542af56de2dc1d5bffff59957e21050db6e3e5abd4c99e46d4a0ffe')
    version('3.8.0', sha256='86250c9ae9dfb18d4f7259a5f2f09b21574d4996fe5034a739ce63a27acd0082')
    version('3.7.0', sha256='72d2a3deda0b55a2d92833cd648f50c7cb64f8341b254a0badac0152b26f1391')
    version('3.5.0', sha256='a5d2ec3570d018b60524f0e589c4917f03d26578443f94bde27a170c7bb21e6e')

    variant('build_type', default='Release', values=("Release", "Debug"), description='CMake build type')
    variant('shared', default=True, description='Build shared or static library')

    depends_on('cmake@3:', type='build')

    def cmake_args(self):
        return [
            self.define_from_variant('BUILD_SHARED_LIBS', 'shared')
        ]

    @run_after('install')
    def post_install(self):
        shutil.rmtree(self.prefix.lib)
        install_tree(self.prefix.rocm_smi,  self.prefix)
        shutil.rmtree(self.prefix.rocm_smi)
        self.fix_bindings_link()

    def fix_bindings_link(self):
        '''Corrects broken symlink at "$PREFIX/bin/rsmiBindings.py"'''
        fname = 'rsmiBindings.py'
        link = join_path(self.prefix.bin, fname)
        if not os.path.islink(link):
            return
        original_target = os.readlink(link)
        if not original_target.startswith('.'):
            # Only proceed if link is to a relative path.
            return
        if os.path.exists(join_path(self.prefix.bin, original_target)):
            # No action necessary if symlink is valid
            return
        rel_target = join_path('..', 'bindings', fname)
        abs_target = join_path(self.prefix.bin, rel_target)
        if os.path.exists(abs_target):
            # If the correct target exists, replace the link
            os.unlink(link)
            os.symlink(rel_target, link)
