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


class ConnectionStaticResult(object):
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
        'mv_verkey': 'str',
        'my_did': 'str',
        'my_endpoint': 'str',
        'record': 'ConnRecord',
        'their_did': 'str',
        'their_verkey': 'str'
    }

    attribute_map = {
        'mv_verkey': 'mv_verkey',
        'my_did': 'my_did',
        'my_endpoint': 'my_endpoint',
        'record': 'record',
        'their_did': 'their_did',
        'their_verkey': 'their_verkey'
    }

    def __init__(self, mv_verkey=None, my_did=None, my_endpoint=None, record=None, their_did=None, their_verkey=None, _configuration=None):  # noqa: E501
        """ConnectionStaticResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mv_verkey = None
        self._my_did = None
        self._my_endpoint = None
        self._record = None
        self._their_did = None
        self._their_verkey = None
        self.discriminator = None

        self.mv_verkey = mv_verkey
        self.my_did = my_did
        self.my_endpoint = my_endpoint
        self.record = record
        self.their_did = their_did
        self.their_verkey = their_verkey

    @property
    def mv_verkey(self):
        """Gets the mv_verkey of this ConnectionStaticResult.  # noqa: E501

        My verification key  # noqa: E501

        :return: The mv_verkey of this ConnectionStaticResult.  # noqa: E501
        :rtype: str
        """
        return self._mv_verkey

    @mv_verkey.setter
    def mv_verkey(self, mv_verkey):
        """Sets the mv_verkey of this ConnectionStaticResult.

        My verification key  # noqa: E501

        :param mv_verkey: The mv_verkey of this ConnectionStaticResult.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and mv_verkey is None:
            raise ValueError("Invalid value for `mv_verkey`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                mv_verkey is not None and not re.search(r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$', mv_verkey)):  # noqa: E501
            raise ValueError(r"Invalid value for `mv_verkey`, must be a follow pattern or equal to `/^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$/`")  # noqa: E501

        self._mv_verkey = mv_verkey

    @property
    def my_did(self):
        """Gets the my_did of this ConnectionStaticResult.  # noqa: E501

        Local DID  # noqa: E501

        :return: The my_did of this ConnectionStaticResult.  # noqa: E501
        :rtype: str
        """
        return self._my_did

    @my_did.setter
    def my_did(self, my_did):
        """Sets the my_did of this ConnectionStaticResult.

        Local DID  # noqa: E501

        :param my_did: The my_did of this ConnectionStaticResult.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and my_did is None:
            raise ValueError("Invalid value for `my_did`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                my_did is not None and not re.search(r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$', my_did)):  # noqa: E501
            raise ValueError(r"Invalid value for `my_did`, must be a follow pattern or equal to `/^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/`")  # noqa: E501

        self._my_did = my_did

    @property
    def my_endpoint(self):
        """Gets the my_endpoint of this ConnectionStaticResult.  # noqa: E501

        My URL endpoint  # noqa: E501

        :return: The my_endpoint of this ConnectionStaticResult.  # noqa: E501
        :rtype: str
        """
        return self._my_endpoint

    @my_endpoint.setter
    def my_endpoint(self, my_endpoint):
        """Sets the my_endpoint of this ConnectionStaticResult.

        My URL endpoint  # noqa: E501

        :param my_endpoint: The my_endpoint of this ConnectionStaticResult.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and my_endpoint is None:
            raise ValueError("Invalid value for `my_endpoint`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                my_endpoint is not None and not re.search(r'^[A-Za-z0-9\\.\\-\\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$', my_endpoint)):  # noqa: E501
            raise ValueError(r"Invalid value for `my_endpoint`, must be a follow pattern or equal to `/^[A-Za-z0-9\\.\\-\\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$/`")  # noqa: E501

        self._my_endpoint = my_endpoint

    @property
    def record(self):
        """Gets the record of this ConnectionStaticResult.  # noqa: E501


        :return: The record of this ConnectionStaticResult.  # noqa: E501
        :rtype: ConnRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this ConnectionStaticResult.


        :param record: The record of this ConnectionStaticResult.  # noqa: E501
        :type: ConnRecord
        """
        if self._configuration.client_side_validation and record is None:
            raise ValueError("Invalid value for `record`, must not be `None`")  # noqa: E501

        self._record = record

    @property
    def their_did(self):
        """Gets the their_did of this ConnectionStaticResult.  # noqa: E501

        Remote DID  # noqa: E501

        :return: The their_did of this ConnectionStaticResult.  # noqa: E501
        :rtype: str
        """
        return self._their_did

    @their_did.setter
    def their_did(self, their_did):
        """Sets the their_did of this ConnectionStaticResult.

        Remote DID  # noqa: E501

        :param their_did: The their_did of this ConnectionStaticResult.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and their_did is None:
            raise ValueError("Invalid value for `their_did`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                their_did is not None and not re.search(r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$', their_did)):  # noqa: E501
            raise ValueError(r"Invalid value for `their_did`, must be a follow pattern or equal to `/^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/`")  # noqa: E501

        self._their_did = their_did

    @property
    def their_verkey(self):
        """Gets the their_verkey of this ConnectionStaticResult.  # noqa: E501

        Remote verification key  # noqa: E501

        :return: The their_verkey of this ConnectionStaticResult.  # noqa: E501
        :rtype: str
        """
        return self._their_verkey

    @their_verkey.setter
    def their_verkey(self, their_verkey):
        """Sets the their_verkey of this ConnectionStaticResult.

        Remote verification key  # noqa: E501

        :param their_verkey: The their_verkey of this ConnectionStaticResult.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and their_verkey is None:
            raise ValueError("Invalid value for `their_verkey`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                their_verkey is not None and not re.search(r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$', their_verkey)):  # noqa: E501
            raise ValueError(r"Invalid value for `their_verkey`, must be a follow pattern or equal to `/^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$/`")  # noqa: E501

        self._their_verkey = their_verkey

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
        if issubclass(ConnectionStaticResult, dict):
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
        if not isinstance(other, ConnectionStaticResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectionStaticResult):
            return True

        return self.to_dict() != other.to_dict()
