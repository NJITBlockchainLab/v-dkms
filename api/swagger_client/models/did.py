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


class DID(object):
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
        'did': 'str',
        'posture': 'str',
        'verkey': 'str'
    }

    attribute_map = {
        'did': 'did',
        'posture': 'posture',
        'verkey': 'verkey'
    }

    def __init__(self, did=None, posture=None, verkey=None, _configuration=None):  # noqa: E501
        """DID - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._did = None
        self._posture = None
        self._verkey = None
        self.discriminator = None

        if did is not None:
            self.did = did
        if posture is not None:
            self.posture = posture
        if verkey is not None:
            self.verkey = verkey

    @property
    def did(self):
        """Gets the did of this DID.  # noqa: E501

        DID of interest  # noqa: E501

        :return: The did of this DID.  # noqa: E501
        :rtype: str
        """
        return self._did

    @did.setter
    def did(self, did):
        """Sets the did of this DID.

        DID of interest  # noqa: E501

        :param did: The did of this DID.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                did is not None and not re.search(r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$', did)):  # noqa: E501
            raise ValueError(r"Invalid value for `did`, must be a follow pattern or equal to `/^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/`")  # noqa: E501

        self._did = did

    @property
    def posture(self):
        """Gets the posture of this DID.  # noqa: E501

        Whether DID is current public DID, posted to ledger but not current public DID, or local to the wallet  # noqa: E501

        :return: The posture of this DID.  # noqa: E501
        :rtype: str
        """
        return self._posture

    @posture.setter
    def posture(self, posture):
        """Sets the posture of this DID.

        Whether DID is current public DID, posted to ledger but not current public DID, or local to the wallet  # noqa: E501

        :param posture: The posture of this DID.  # noqa: E501
        :type: str
        """
        allowed_values = ["public", "posted", "wallet_only"]  # noqa: E501
        if (self._configuration.client_side_validation and
                posture not in allowed_values):
            raise ValueError(
                "Invalid value for `posture` ({0}), must be one of {1}"  # noqa: E501
                .format(posture, allowed_values)
            )

        self._posture = posture

    @property
    def verkey(self):
        """Gets the verkey of this DID.  # noqa: E501

        Public verification key  # noqa: E501

        :return: The verkey of this DID.  # noqa: E501
        :rtype: str
        """
        return self._verkey

    @verkey.setter
    def verkey(self, verkey):
        """Sets the verkey of this DID.

        Public verification key  # noqa: E501

        :param verkey: The verkey of this DID.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                verkey is not None and not re.search(r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$', verkey)):  # noqa: E501
            raise ValueError(r"Invalid value for `verkey`, must be a follow pattern or equal to `/^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$/`")  # noqa: E501

        self._verkey = verkey

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
        if issubclass(DID, dict):
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
        if not isinstance(other, DID):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DID):
            return True

        return self.to_dict() != other.to_dict()