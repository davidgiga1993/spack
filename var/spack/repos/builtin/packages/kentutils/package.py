##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Kentutils(MakefilePackage):
    """Jim Kent command line bioinformatic utilities"""

    homepage = "https://github.com/ENCODE-DCC/kentUtils"
    url      = "https://github.com/ENCODE-DCC/kentUtils"

    version('302.1', git='https://github.com/ENCODE-DCC/kentUtils.git', commit='d8376c5d52a161f2267346ed3dc94b5dce74c2f9')

    depends_on('libpng')
    depends_on('openssl')

    # Actually depends on mysql, but mariadb works for now until mysql is
    # available
    depends_on('mariadb')

    conflicts('%cce')
    conflicts('%clang')
    conflicts('%intel')
    conflicts('%nag')
    conflicts('%pgi')
    conflicts('%xl')
    conflicts('%xl_r')

    def install(self, spec, prefix):
        install_tree('bin', prefix.bin)
