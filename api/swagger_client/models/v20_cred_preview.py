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


class V20CredPreview(object):
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
        'type': 'str',
        'attributes': 'list[V20CredAttrSpec]'
    }

    attribute_map = {
        'type': '@type',
        'attributes': 'attributes'
    }

    def __init__(self, type=None, attributes=None, _configuration=None):  # noqa: E501
        """V20CredPreview - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._attributes = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.attributes = attributes

    @property
    def type(self):
        """Gets the type of this V20CredPreview.  # noqa: E501

        Message type identifier  # noqa: E501

        :return: The type of this V20CredPreview.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V20CredPreview.

        Message type identifier  # noqa: E501

        :param type: The type of this V20CredPreview.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def attributes(self):
        """Gets the attributes of this V20CredPreview.  # noqa: E501


        :return: The attributes of this V20CredPreview.  # noqa: E501
        :rtype: list[V20CredAttrSpec]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this V20CredPreview.


        :param attributes: The attributes of this V20CredPreview.  # noqa: E501
        :type: list[V20CredAttrSpec]
        """
        if self._configuration.client_side_validation and attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

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
        if issubclass(V20CredPreview, dict):
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
        if not isinstance(other, V20CredPreview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V20CredPreview):
            return True

        return self.to_dict() != other.to_dict()
