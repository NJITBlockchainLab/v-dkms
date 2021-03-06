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


class PublishRevocations(object):
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
        'rrid2crid': 'dict(str, list[str])'
    }

    attribute_map = {
        'rrid2crid': 'rrid2crid'
    }

    def __init__(self, rrid2crid=None, _configuration=None):  # noqa: E501
        """PublishRevocations - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rrid2crid = None
        self.discriminator = None

        if rrid2crid is not None:
            self.rrid2crid = rrid2crid

    @property
    def rrid2crid(self):
        """Gets the rrid2crid of this PublishRevocations.  # noqa: E501

        Credential revocation ids by revocation registry id  # noqa: E501

        :return: The rrid2crid of this PublishRevocations.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._rrid2crid

    @rrid2crid.setter
    def rrid2crid(self, rrid2crid):
        """Sets the rrid2crid of this PublishRevocations.

        Credential revocation ids by revocation registry id  # noqa: E501

        :param rrid2crid: The rrid2crid of this PublishRevocations.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._rrid2crid = rrid2crid

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
        if issubclass(PublishRevocations, dict):
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
        if not isinstance(other, PublishRevocations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublishRevocations):
            return True

        return self.to_dict() != other.to_dict()
