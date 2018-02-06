# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EditionCapability(Model):
    """The edition capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The database edition name.
    :vartype name: str
    :ivar supported_service_level_objectives: The list of supported service
     objectives for the edition.
    :vartype supported_service_level_objectives:
     list[~azure.mgmt.sql.models.ServiceLevelObjectiveCapability]
    :ivar zone_redundant: Whether or not zone redundancy is supported for the
     edition.
    :vartype zone_redundant: bool
    :ivar status: The status of the capability. Possible values include:
     'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :param reason: The reason for the capability not being available.
    :type reason: str
    """

    _validation = {
        'name': {'readonly': True},
        'supported_service_level_objectives': {'readonly': True},
        'zone_redundant': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'supported_service_level_objectives': {'key': 'supportedServiceLevelObjectives', 'type': '[ServiceLevelObjectiveCapability]'},
        'zone_redundant': {'key': 'zoneRedundant', 'type': 'bool'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(self, reason=None):
        super(EditionCapability, self).__init__()
        self.name = None
        self.supported_service_level_objectives = None
        self.zone_redundant = None
        self.status = None
        self.reason = reason
