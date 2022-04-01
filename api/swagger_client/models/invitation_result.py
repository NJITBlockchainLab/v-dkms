# coding: utf-8

"""
    sp

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class InvitationResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'connection_id': 'str',
        'invitation': 'ConnectionInvitation',
        'invitation_url': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'invitation': 'invitation',
        'invitation_url': 'invitation_url'
    }

    def __init__(self, connection_id=None, invitation=None, invitation_url=None, _configuration=None):  # noqa: E501
        """InvitationResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection_id = None
        self._invitation = None
        self._invitation_url = None
        self.discriminator = None

        if connection_id is not None:
            self.connection_id = connection_id
        if invitation is not None:
            self.invitation = invitation
        if invitation_url is not None:
            self.invitation_url = invitation_url

    @property
    def connection_id(self):
        """Gets the connection_id of this InvitationResult.  # noqa: E501

        Connection identifier  # noqa: E501

        :return: The connection_id of this InvitationResult.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this InvitationResult.

        Connection identifier  # noqa: E501

        :param connection_id: The connection_id of this InvitationResult.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def invitation(self):
        """Gets the invitation of this InvitationResult.  # noqa: E501


        :return: The invitation of this InvitationResult.  # noqa: E501
        :rtype: ConnectionInvitation
        """
        return self._invitation

    @invitation.setter
    def invitation(self, invitation):
        """Sets the invitation of this InvitationResult.


        :param invitation: The invitation of this InvitationResult.  # noqa: E501
        :type: ConnectionInvitation
        """

        self._invitation = invitation

    @property
    def invitation_url(self):
        """Gets the invitation_url of this InvitationResult.  # noqa: E501

        Invitation URL  # noqa: E501

        :return: The invitation_url of this InvitationResult.  # noqa: E501
        :rtype: str
        """
        return self._invitation_url

    @invitation_url.setter
    def invitation_url(self, invitation_url):
        """Sets the invitation_url of this InvitationResult.

        Invitation URL  # noqa: E501

        :param invitation_url: The invitation_url of this InvitationResult.  # noqa: E501
        :type: str
        """

        self._invitation_url = invitation_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InvitationResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InvitationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvitationResult):
            return True

        return self.to_dict() != other.to_dict()
