# -*- coding: utf-8 -*- #
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Genomics pipelines sub-group."""
from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.api_lib import genomics as lib
from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.calliope import base


class Pipelines(base.Group):
  """Commands for Genomics pipelines.

  Command to run a pipeline.
  """

  def Filter(self, context, args):
    """Setup the API client within the context for this group's commands.

    Args:
      context: {str:object}, A set of key-value pairs that can be used for
          common initialization among commands.
      args: argparse.Namespace: The same namespace given to the corresponding
          .Run() invocation.

    Returns:
      The updated context.
    """

    context[lib.STORAGE_V1_CLIENT_KEY] = apis.GetClientInstance(
        'storage', 'v1')
    return context
