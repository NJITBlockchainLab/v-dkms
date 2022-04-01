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


class IndyRequestedCredsRequestedPred(object):
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
        'cred_id': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'cred_id': 'cred_id',
        'timestamp': 'timestamp'
    }

    def __init__(self, cred_id=None, timestamp=None, _configuration=None):  # noqa: E501
        """IndyRequestedCredsRequestedPred - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cred_id = None
        self._timestamp = None
        self.discriminator = None

        self.cred_id = cred_id
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def cred_id(self):
        """Gets the cred_id of this IndyRequestedCredsRequestedPred.  # noqa: E501

        Wallet credential identifier (typically but not necessarily a UUID)  # noqa: E501

        :return: The cred_id of this IndyRequestedCredsRequestedPred.  # noqa: E501
        :rtype: str
        """
        return self._cred_id

    @cred_id.setter
    def cred_id(self, cred_id):
        """Sets the cred_id of this IndyRequestedCredsRequestedPred.

        Wallet credential identifier (typically but not necessarily a UUID)  # noqa: E501

        :param cred_id: The cred_id of this IndyRequestedCredsRequestedPred.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cred_id is None:
            raise ValueError("Invalid value for `cred_id`, must not be `None`")  # noqa: E501

        self._cred_id = cred_id

    @property
    def timestamp(self):
        """Gets the timestamp of this IndyRequestedCredsRequestedPred.  # noqa: E501

        Epoch timestamp of interest for non-revocation proof  # noqa: E501

        :return: The timestamp of this IndyRequestedCredsRequestedPred.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this IndyRequestedCredsRequestedPred.

        Epoch timestamp of interest for non-revocation proof  # noqa: E501

        :param timestamp: The timestamp of this IndyRequestedCredsRequestedPred.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                timestamp is not None and timestamp > 384):  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must be a value less than or equal to `384`")  # noqa: E501
        if (self._configuration.client_side_validation and
                timestamp is not None and timestamp < 0):  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must be a value greater than or equal to `0`")  # noqa: E501

        self._timestamp = timestamp

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
        if issubclass(IndyRequestedCredsRequestedPred, dict):
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
        if not isinstance(other, IndyRequestedCredsRequestedPred):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IndyRequestedCredsRequestedPred):
            return True

        return self.to_dict() != other.to_dict()