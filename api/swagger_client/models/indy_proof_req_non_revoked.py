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


class IndyProofReqNonRevoked(object):
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
        'to': 'int'
    }

    attribute_map = {
        'to': 'to'
    }

    def __init__(self, to=None, _configuration=None):  # noqa: E501
        """IndyProofReqNonRevoked - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._to = None
        self.discriminator = None

        self.to = to

    @property
    def to(self):
        """Gets the to of this IndyProofReqNonRevoked.  # noqa: E501

        Timestamp of interest for non-revocation proof  # noqa: E501

        :return: The to of this IndyProofReqNonRevoked.  # noqa: E501
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this IndyProofReqNonRevoked.

        Timestamp of interest for non-revocation proof  # noqa: E501

        :param to: The to of this IndyProofReqNonRevoked.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                to is not None and to > 384):  # noqa: E501
            raise ValueError("Invalid value for `to`, must be a value less than or equal to `384`")  # noqa: E501
        if (self._configuration.client_side_validation and
                to is not None and to < 0):  # noqa: E501
            raise ValueError("Invalid value for `to`, must be a value greater than or equal to `0`")  # noqa: E501

        self._to = to

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
        if issubclass(IndyProofReqNonRevoked, dict):
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
        if not isinstance(other, IndyProofReqNonRevoked):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IndyProofReqNonRevoked):
            return True

        return self.to_dict() != other.to_dict()
