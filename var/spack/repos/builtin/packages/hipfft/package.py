# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Hipfft(CMakePackage):
    """hipFFT is an FFT marshalling library. Currently, hipFFT supports either
       rocFFT or cuFFT as backends."""

    homepage = "https://github.com/ROCmSoftwarePlatform/hipFFT"
    git      = "https://github.com/ROCmSoftwarePlatform/hipFFT.git"
    url      = "https://github.com/ROCmSoftwarePlatform/hipFFT/archive/rocm-4.1.0.tar.gz"

    version('4.1.0', sha256='885ffd4813f2c271150f1b8b386f0af775b38fc82b96ce6fd94eb4ba0c0180be')

    maintainers = ['belhornmp']

    for ver in ['4.1.0']:
        depends_on('hip@' + ver, when='@' + ver)
        depends_on('hsa-rocr-dev@' + ver, when='@' + ver)
        depends_on('comgr@' + ver, when='@' + ver)
        depends_on('hsakmt-roct@' + ver, when='@' + ver)
        depends_on('rocfft@' + ver, type='link', when='@' + ver)
        depends_on('rocm-device-libs@' + ver, type='build', when='@' + ver)

    def cmake_args(self):
        tgt = self.spec['rocfft'].variants['amdgpu_target'].value

        args = [
            '-DBUILD_CLIENTS_SAMPLES=OFF',
            '-DBUILD_CLIENTS_TESTS=OFF'
        ]

        if tgt[0] != 'none':
            args.append(self.define('AMDGPU_TARGETS', ";".join(tgt)))

        return args

    def setup_build_environment(self, env):
        env.set('CXX', self.spec['hip'].hipcc)
