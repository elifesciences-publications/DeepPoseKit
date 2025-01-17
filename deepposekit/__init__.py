# -*- coding: utf-8 -*-
# Copyright 2018-2019 Jacob M. Graving <jgraving@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
import sys
import warnings

from deepposekit.io import TrainingGenerator, DataGenerator
from deepposekit.augment.FlipAxis import FlipAxis

from deepposekit.annotate.gui.Annotator import Annotator
from deepposekit.annotate.gui.Skeleton import Skeleton
from deepposekit.annotate.KMeansSampler import KMeansSampler

from deepposekit.io.video import VideoReader, VideoWriter


__doc__ = """ """  # open('README.md').read()
__version__ = "0.3.4.dev"
