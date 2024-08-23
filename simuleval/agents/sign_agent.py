# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from . agent import Agent


class SignAgent(Agent):
    data_type = "sign"
    sign_segment_size = 40  # in milliseconds
