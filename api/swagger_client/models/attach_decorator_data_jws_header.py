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


class AttachDecoratorDataJWSHeader(object):
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
        'kid': 'str'
    }

    attribute_map = {
        'kid': 'kid'
    }

    def __init__(self, kid=None, _configuration=None):  # noqa: E501
        """AttachDecoratorDataJWSHeader - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._kid = None
        self.discriminator = None

        self.kid = kid

    @property
    def kid(self):
        """Gets the kid of this AttachDecoratorDataJWSHeader.  # noqa: E501

        Key identifier, in W3C did:key or DID URL format  # noqa: E501

        :return: The kid of this AttachDecoratorDataJWSHeader.  # noqa: E501
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this AttachDecoratorDataJWSHeader.

        Key identifier, in W3C did:key or DID URL format  # noqa: E501

        :param kid: The kid of this AttachDecoratorDataJWSHeader.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and kid is None:
            raise ValueError("Invalid value for `kid`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                kid is not None and not re.search(r'^did:(?:key:z[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]+|sov:[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}(;.*)?(\\?.*)?#.+)$', kid)):  # noqa: E501
            raise ValueError(r"Invalid value for `kid`, must be a follow pattern or equal to `/^did:(?:key:z[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]+|sov:[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}(;.*)?(\\?.*)?#.+)$/`")  # noqa: E501

        self._kid = kid

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
        if issubclass(AttachDecoratorDataJWSHeader, dict):
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
        if not isinstance(other, AttachDecoratorDataJWSHeader):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachDecoratorDataJWSHeader):
            return True

        return self.to_dict() != other.to_dict()