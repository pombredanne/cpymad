#-------------------------------------------------------------------------------
# This file is part of PyMad.
#
# Copyright (c) 2011, CERN. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#-------------------------------------------------------------------------------

'''
.. module: cern.pymad

PyMad is the API which CPyMad and JPyMad should follow.

.. moduleauthor:: Kajetan Fuchsberger <Kajetan.Fuchsberger@cern.ch>

'''
from __future__ import absolute_import

from .io.tfs import tfs
from .tools.run import init

from .tools.ls import ls_models,ls_mdefs
