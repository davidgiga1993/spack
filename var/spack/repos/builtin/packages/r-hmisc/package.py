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


class RHmisc(RPackage):
    """Contains many functions useful for data analysis, high-level
    graphics, utility operations, functions for computing sample size
    and power, importing and annotating datasets, imputing missing
    values, advanced table making, variable clustering, character
    string manipulation, conversion of R objects to LaTeX and html
    code, and recoding variables."""

    homepage = "http://biostat.mc.vanderbilt.edu/Hmisc"
    url      = "https://cran.rstudio.com/src/contrib/Hmisc_4.0-3.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/Hmisc"

    version('4.0-3', '7091924db1e473419d8116c3335f82da')

    depends_on('r-lattice', type=('build', 'run'))
    depends_on('r-survival', type=('build', 'run'))
    depends_on('r-formula', type=('build', 'run'))
    depends_on('r-ggplot2', type=('build', 'run'))
    depends_on('r-latticeextra', type=('build', 'run'))
    depends_on('r-acepack', type=('build', 'run'))
    depends_on('r-gridextra', type=('build', 'run'))
    depends_on('r-data-table', type=('build', 'run'))
    depends_on('r-htmltools', type=('build', 'run'))
    depends_on('r-base64enc', type=('build', 'run'))
    depends_on('r-htmltable', type=('build', 'run'))
    depends_on('r-viridis', type=('build', 'run'))
