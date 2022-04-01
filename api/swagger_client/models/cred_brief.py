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


class CredBrief(object):
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
        'attrs': 'dict(str, str)',
        'cred_def_id': 'str',
        'cred_rev_id': 'str',
        'referent': 'str',
        'rev_reg_id': 'str',
        'schema_id': 'str'
    }

    attribute_map = {
        'attrs': 'attrs',
        'cred_def_id': 'cred_def_id',
        'cred_rev_id': 'cred_rev_id',
        'referent': 'referent',
        'rev_reg_id': 'rev_reg_id',
        'schema_id': 'schema_id'
    }

    def __init__(self, attrs=None, cred_def_id=None, cred_rev_id=None, referent=None, rev_reg_id=None, schema_id=None, _configuration=None):  # noqa: E501
        """CredBrief - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attrs = None
        self._cred_def_id = None
        self._cred_rev_id = None
        self._referent = None
        self._rev_reg_id = None
        self._schema_id = None
        self.discriminator = None

        if attrs is not None:
            self.attrs = attrs
        if cred_def_id is not None:
            self.cred_def_id = cred_def_id
        if cred_rev_id is not None:
            self.cred_rev_id = cred_rev_id
        if referent is not None:
            self.referent = referent
        if rev_reg_id is not None:
            self.rev_reg_id = rev_reg_id
        if schema_id is not None:
            self.schema_id = schema_id

    @property
    def attrs(self):
        """Gets the attrs of this CredBrief.  # noqa: E501

        Attribute names mapped to their raw values  # noqa: E501

        :return: The attrs of this CredBrief.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attrs

    @attrs.setter
    def attrs(self, attrs):
        """Sets the attrs of this CredBrief.

        Attribute names mapped to their raw values  # noqa: E501

        :param attrs: The attrs of this CredBrief.  # noqa: E501
        :type: dict(str, str)
        """

        self._attrs = attrs

    @property
    def cred_def_id(self):
        """Gets the cred_def_id of this CredBrief.  # noqa: E501

        Credential definition identifier  # noqa: E501

        :return: The cred_def_id of this CredBrief.  # noqa: E501
        :rtype: str
        """
        return self._cred_def_id

    @cred_def_id.setter
    def cred_def_id(self, cred_def_id):
        """Sets the cred_def_id of this CredBrief.

        Credential definition identifier  # noqa: E501

        :param cred_def_id: The cred_def_id of this CredBrief.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cred_def_id is not None and not re.search(r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$', cred_def_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `cred_def_id`, must be a follow pattern or equal to `/^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$/`")  # noqa: E501

        self._cred_def_id = cred_def_id

    @property
    def cred_rev_id(self):
        """Gets the cred_rev_id of this CredBrief.  # noqa: E501

        Credential revocation identifier  # noqa: E501

        :return: The cred_rev_id of this CredBrief.  # noqa: E501
        :rtype: str
        """
        return self._cred_rev_id

    @cred_rev_id.setter
    def cred_rev_id(self, cred_rev_id):
        """Sets the cred_rev_id of this CredBrief.

        Credential revocation identifier  # noqa: E501

        :param cred_rev_id: The cred_rev_id of this CredBrief.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cred_rev_id is not None and not re.search(r'^[1-9][0-9]*$', cred_rev_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `cred_rev_id`, must be a follow pattern or equal to `/^[1-9][0-9]*$/`")  # noqa: E501

        self._cred_rev_id = cred_rev_id

    @property
    def referent(self):
        """Gets the referent of this CredBrief.  # noqa: E501

        Credential referent  # noqa: E501

        :return: The referent of this CredBrief.  # noqa: E501
        :rtype: str
        """
        return self._referent

    @referent.setter
    def referent(self, referent):
        """Sets the referent of this CredBrief.

        Credential referent  # noqa: E501

        :param referent: The referent of this CredBrief.  # noqa: E501
        :type: str
        """

        self._referent = referent

    @property
    def rev_reg_id(self):
        """Gets the rev_reg_id of this CredBrief.  # noqa: E501

        Revocation registry identifier  # noqa: E501

        :return: The rev_reg_id of this CredBrief.  # noqa: E501
        :rtype: str
        """
        return self._rev_reg_id

    @rev_reg_id.setter
    def rev_reg_id(self, rev_reg_id):
        """Sets the rev_reg_id of this CredBrief.

        Revocation registry identifier  # noqa: E501

        :param rev_reg_id: The rev_reg_id of this CredBrief.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                rev_reg_id is not None and not re.search(r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)', rev_reg_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `rev_reg_id`, must be a follow pattern or equal to `/^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)/`")  # noqa: E501

        self._rev_reg_id = rev_reg_id

    @property
    def schema_id(self):
        """Gets the schema_id of this CredBrief.  # noqa: E501

        Schema identifier  # noqa: E501

        :return: The schema_id of this CredBrief.  # noqa: E501
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this CredBrief.

        Schema identifier  # noqa: E501

        :param schema_id: The schema_id of this CredBrief.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                schema_id is not None and not re.search(r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$', schema_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `schema_id`, must be a follow pattern or equal to `/^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$/`")  # noqa: E501

        self._schema_id = schema_id

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
        if issubclass(CredBrief, dict):
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
        if not isinstance(other, CredBrief):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CredBrief):
            return True

        return self.to_dict() != other.to_dict()
