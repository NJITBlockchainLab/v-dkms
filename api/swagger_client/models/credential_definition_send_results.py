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


class CredentialDefinitionSendResults(object):
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
        'credential_definition_id': 'str'
    }

    attribute_map = {
        'credential_definition_id': 'credential_definition_id'
    }

    def __init__(self, credential_definition_id=None, _configuration=None):  # noqa: E501
        """CredentialDefinitionSendResults - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._credential_definition_id = None
        self.discriminator = None

        if credential_definition_id is not None:
            self.credential_definition_id = credential_definition_id

    @property
    def credential_definition_id(self):
        """Gets the credential_definition_id of this CredentialDefinitionSendResults.  # noqa: E501

        Credential definition identifier  # noqa: E501

        :return: The credential_definition_id of this CredentialDefinitionSendResults.  # noqa: E501
        :rtype: str
        """
        return self._credential_definition_id

    @credential_definition_id.setter
    def credential_definition_id(self, credential_definition_id):
        """Sets the credential_definition_id of this CredentialDefinitionSendResults.

        Credential definition identifier  # noqa: E501

        :param credential_definition_id: The credential_definition_id of this CredentialDefinitionSendResults.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                credential_definition_id is not None and not re.search(r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$', credential_definition_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `credential_definition_id`, must be a follow pattern or equal to `/^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$/`")  # noqa: E501

        self._credential_definition_id = credential_definition_id

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
        if issubclass(CredentialDefinitionSendResults, dict):
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
        if not isinstance(other, CredentialDefinitionSendResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CredentialDefinitionSendResults):
            return True

        return self.to_dict() != other.to_dict()
