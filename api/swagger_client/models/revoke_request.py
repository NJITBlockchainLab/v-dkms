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


class RevokeRequest(object):
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
        'cred_ex_id': 'str',
        'cred_rev_id': 'str',
        'publish': 'bool',
        'rev_reg_id': 'str'
    }

    attribute_map = {
        'cred_ex_id': 'cred_ex_id',
        'cred_rev_id': 'cred_rev_id',
        'publish': 'publish',
        'rev_reg_id': 'rev_reg_id'
    }

    def __init__(self, cred_ex_id=None, cred_rev_id=None, publish=None, rev_reg_id=None, _configuration=None):  # noqa: E501
        """RevokeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cred_ex_id = None
        self._cred_rev_id = None
        self._publish = None
        self._rev_reg_id = None
        self.discriminator = None

        if cred_ex_id is not None:
            self.cred_ex_id = cred_ex_id
        if cred_rev_id is not None:
            self.cred_rev_id = cred_rev_id
        if publish is not None:
            self.publish = publish
        if rev_reg_id is not None:
            self.rev_reg_id = rev_reg_id

    @property
    def cred_ex_id(self):
        """Gets the cred_ex_id of this RevokeRequest.  # noqa: E501

        Credential exchange identifier  # noqa: E501

        :return: The cred_ex_id of this RevokeRequest.  # noqa: E501
        :rtype: str
        """
        return self._cred_ex_id

    @cred_ex_id.setter
    def cred_ex_id(self, cred_ex_id):
        """Sets the cred_ex_id of this RevokeRequest.

        Credential exchange identifier  # noqa: E501

        :param cred_ex_id: The cred_ex_id of this RevokeRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cred_ex_id is not None and not re.search(r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}', cred_ex_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `cred_ex_id`, must be a follow pattern or equal to `/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}/`")  # noqa: E501

        self._cred_ex_id = cred_ex_id

    @property
    def cred_rev_id(self):
        """Gets the cred_rev_id of this RevokeRequest.  # noqa: E501

        Credential revocation identifier  # noqa: E501

        :return: The cred_rev_id of this RevokeRequest.  # noqa: E501
        :rtype: str
        """
        return self._cred_rev_id

    @cred_rev_id.setter
    def cred_rev_id(self, cred_rev_id):
        """Sets the cred_rev_id of this RevokeRequest.

        Credential revocation identifier  # noqa: E501

        :param cred_rev_id: The cred_rev_id of this RevokeRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cred_rev_id is not None and not re.search(r'^[1-9][0-9]*$', cred_rev_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `cred_rev_id`, must be a follow pattern or equal to `/^[1-9][0-9]*$/`")  # noqa: E501

        self._cred_rev_id = cred_rev_id

    @property
    def publish(self):
        """Gets the publish of this RevokeRequest.  # noqa: E501

        (True) publish revocation to ledger immediately, or (default, False) mark it pending  # noqa: E501

        :return: The publish of this RevokeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._publish

    @publish.setter
    def publish(self, publish):
        """Sets the publish of this RevokeRequest.

        (True) publish revocation to ledger immediately, or (default, False) mark it pending  # noqa: E501

        :param publish: The publish of this RevokeRequest.  # noqa: E501
        :type: bool
        """

        self._publish = publish

    @property
    def rev_reg_id(self):
        """Gets the rev_reg_id of this RevokeRequest.  # noqa: E501

        Revocation registry identifier  # noqa: E501

        :return: The rev_reg_id of this RevokeRequest.  # noqa: E501
        :rtype: str
        """
        return self._rev_reg_id

    @rev_reg_id.setter
    def rev_reg_id(self, rev_reg_id):
        """Sets the rev_reg_id of this RevokeRequest.

        Revocation registry identifier  # noqa: E501

        :param rev_reg_id: The rev_reg_id of this RevokeRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                rev_reg_id is not None and not re.search(r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)', rev_reg_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `rev_reg_id`, must be a follow pattern or equal to `/^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)/`")  # noqa: E501

        self._rev_reg_id = rev_reg_id

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
        if issubclass(RevokeRequest, dict):
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
        if not isinstance(other, RevokeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RevokeRequest):
            return True

        return self.to_dict() != other.to_dict()
