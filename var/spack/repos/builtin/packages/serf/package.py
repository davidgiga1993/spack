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


class Serf(SConsPackage):
    """Apache Serf - a high performance C-based HTTP client library
    built upon the Apache Portable Runtime (APR) library"""

    homepage  = 'https://serf.apache.org/'
    url       = 'https://archive.apache.org/dist/serf/serf-1.3.9.tar.bz2'

    version('1.3.9', '26015c63e3bbb108c1689bf2090e4c26351db674')
    version('1.3.8', '1d45425ca324336ce2f4ae7d7b4cfbc5567c5446')

    variant('debug', default=False,
            description='Enable debugging info and strict compile warnings')

    depends_on('scons@2.3.0:', type='build')

    depends_on('apr')
    depends_on('apr-util')
    depends_on('openssl')
    depends_on('zlib')

    def build_args(self, spec, prefix):
        args = [
            'PREFIX={0}'.format(prefix),
            'APR={0}'.format(spec['apr'].prefix),
            'APU={0}'.format(spec['apr-util'].prefix),
            'OPENSSL={0}'.format(spec['openssl'].prefix),
            'ZLIB={0}'.format(spec['zlib'].prefix),
        ]

        if '+debug' in spec:
            args.append('DEBUG=yes')
        else:
            args.append('DEBUG=no')

        # SCons doesn't pass Spack environment variables to the
        # execution environment. Therefore, we can't use Spack's compiler
        # wrappers. Use the actual compilers. SCons seems to RPATH things
        # on its own anyway.
        args.append('CC={0}'.format(self.compiler.cc))

        return args

    def test(self):
        # FIXME: Several test failures:
        #
        # There were 14 failures:
        # 1) test_ssl_trust_rootca
        # 2) test_ssl_certificate_chain_with_anchor
        # 3) test_ssl_certificate_chain_all_from_server
        # 4) test_ssl_no_servercert_callback_allok
        # 5) test_ssl_large_response
        # 6) test_ssl_large_request
        # 7) test_ssl_client_certificate
        # 8) test_ssl_future_server_cert
        # 9) test_setup_ssltunnel
        # 10) test_ssltunnel_basic_auth
        # 11) test_ssltunnel_basic_auth_server_has_keepalive_off
        # 12) test_ssltunnel_basic_auth_proxy_has_keepalive_off
        # 13) test_ssltunnel_basic_auth_proxy_close_conn_on_200resp
        # 14) test_ssltunnel_digest_auth
        #
        # These seem to be related to:
        # https://groups.google.com/forum/#!topic/serf-dev/YEFTTdF1Qwc
        scons('check')
