# -*- coding: utf-8 -*- #
# Copyright 2017 Google Inc. All Rights Reserved.
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

"""Cloud Pub/Sub topics get-iam-policy command."""

from __future__ import absolute_import
from __future__ import unicode_literals

from googlecloudsdk.api_lib.pubsub import topics
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.pubsub import resource_args


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class GetIamPolicy(base.ListCommand):
  """Get the IAM policy for a Cloud Pub/Sub Topic."""

  detailed_help = {
      'DESCRIPTION':
          '{description}',
      'EXAMPLES':
          """\
          To print the IAM policy for a given topic, run:

            $ {command} my-topic
          """,
  }

  @staticmethod
  def Args(parser):
    resource_args.AddTopicResourceArg(parser, 'to get the IAM policy of.')
    base.URI_FLAG.RemoveFromParser(parser)

  def Run(self, args):
    client = topics.TopicsClient()
    topic_ref = args.CONCEPTS.topic.Parse()

    return client.GetIamPolicy(topic_ref)
