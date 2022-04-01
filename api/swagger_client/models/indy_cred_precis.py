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


class IndyCredPrecis(object):
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
        'cred_def_id': 'str',
        'cred_info': 'object',
        'cred_rev': 'str',
        'interval': 'object',
        'presentation_referents': 'list[str]',
        'rev_reg_id': 'str',
        'schema_id': 'str'
    }

    attribute_map = {
        'cred_def_id': 'cred_def_id',
        'cred_info': 'cred_info',
        'cred_rev': 'cred_rev',
        'interval': 'interval',
        'presentation_referents': 'presentation_referents',
        'rev_reg_id': 'rev_reg_id',
        'schema_id': 'schema_id'
    }

    def __init__(self, cred_def_id=None, cred_info=None, cred_rev=None, interval=None, presentation_referents=None, rev_reg_id=None, schema_id=None, _configuration=None):  # noqa: E501
        """IndyCredPrecis - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cred_def_id = None
        self._cred_info = None
        self._cred_rev = None
        self._interval = None
        self._presentation_referents = None
        self._rev_reg_id = None
        self._schema_id = None
        self.discriminator = None

        if cred_def_id is not None:
            self.cred_def_id = cred_def_id
        if cred_info is not None:
            self.cred_info = cred_info
        if cred_rev is not None:
            self.cred_rev = cred_rev
        if interval is not None:
            self.interval = interval
        if presentation_referents is not None:
            self.presentation_referents = presentation_referents
        if rev_reg_id is not None:
            self.rev_reg_id = rev_reg_id
        if schema_id is not None:
            self.schema_id = schema_id

    @property
    def cred_def_id(self):
        """Gets the cred_def_id of this IndyCredPrecis.  # noqa: E501

        Credential definition identifier  # noqa: E501

        :return: The cred_def_id of this IndyCredPrecis.  # noqa: E501
        :rtype: str
        """
        return self._cred_def_id

    @cred_def_id.setter
    def cred_def_id(self, cred_def_id):
        """Sets the cred_def_id of this IndyCredPrecis.

        Credential definition identifier  # noqa: E501

        :param cred_def_id: The cred_def_id of this IndyCredPrecis.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cred_def_id is not None and not re.search(r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$', cred_def_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `cred_def_id`, must be a follow pattern or equal to `/^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$/`")  # noqa: E501

        self._cred_def_id = cred_def_id

    @property
    def cred_info(self):
        """Gets the cred_info of this IndyCredPrecis.  # noqa: E501

        Credential info  # noqa: E501

        :return: The cred_info of this IndyCredPrecis.  # noqa: E501
        :rtype: object
        """
        return self._cred_info

    @cred_info.setter
    def cred_info(self, cred_info):
        """Sets the cred_info of this IndyCredPrecis.

        Credential info  # noqa: E501

        :param cred_info: The cred_info of this IndyCredPrecis.  # noqa: E501
        :type: object
        """

        self._cred_info = cred_info

    @property
    def cred_rev(self):
        """Gets the cred_rev of this IndyCredPrecis.  # noqa: E501

        Credential revocation identifier  # noqa: E501

        :return: The cred_rev of this IndyCredPrecis.  # noqa: E501
        :rtype: str
        """
        return self._cred_rev

    @cred_rev.setter
    def cred_rev(self, cred_rev):
        """Sets the cred_rev of this IndyCredPrecis.

        Credential revocation identifier  # noqa: E501

        :param cred_rev: The cred_rev of this IndyCredPrecis.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cred_rev is not None and not re.search(r'^[1-9][0-9]*$', cred_rev)):  # noqa: E501
            raise ValueError(r"Invalid value for `cred_rev`, must be a follow pattern or equal to `/^[1-9][0-9]*$/`")  # noqa: E501

        self._cred_rev = cred_rev

    @property
    def interval(self):
        """Gets the interval of this IndyCredPrecis.  # noqa: E501

        Non-revocation interval from presentation request  # noqa: E501

        :return: The interval of this IndyCredPrecis.  # noqa: E501
        :rtype: object
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this IndyCredPrecis.

        Non-revocation interval from presentation request  # noqa: E501

        :param interval: The interval of this IndyCredPrecis.  # noqa: E501
        :type: object
        """

        self._interval = interval

    @property
    def presentation_referents(self):
        """Gets the presentation_referents of this IndyCredPrecis.  # noqa: E501


        :return: The presentation_referents of this IndyCredPrecis.  # noqa: E501
        :rtype: list[str]
        """
        return self._presentation_referents

    @presentation_referents.setter
    def presentation_referents(self, presentation_referents):
        """Sets the presentation_referents of this IndyCredPrecis.


        :param presentation_referents: The presentation_referents of this IndyCredPrecis.  # noqa: E501
        :type: list[str]
        """

        self._presentation_referents = presentation_referents

    @property
    def rev_reg_id(self):
        """Gets the rev_reg_id of this IndyCredPrecis.  # noqa: E501

        Revocation registry identifier  # noqa: E501

        :return: The rev_reg_id of this IndyCredPrecis.  # noqa: E501
        :rtype: str
        """
        return self._rev_reg_id

    @rev_reg_id.setter
    def rev_reg_id(self, rev_reg_id):
        """Sets the rev_reg_id of this IndyCredPrecis.

        Revocation registry identifier  # noqa: E501

        :param rev_reg_id: The rev_reg_id of this IndyCredPrecis.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                rev_reg_id is not None and not re.search(r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)', rev_reg_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `rev_reg_id`, must be a follow pattern or equal to `/^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)/`")  # noqa: E501

        self._rev_reg_id = rev_reg_id

    @property
    def schema_id(self):
        """Gets the schema_id of this IndyCredPrecis.  # noqa: E501

        Schema identifier  # noqa: E501

        :return: The schema_id of this IndyCredPrecis.  # noqa: E501
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this IndyCredPrecis.

        Schema identifier  # noqa: E501

        :param schema_id: The schema_id of this IndyCredPrecis.  # noqa: E501
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
        if issubclass(IndyCredPrecis, dict):
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
        if not isinstance(other, IndyCredPrecis):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IndyCredPrecis):
            return True

        return self.to_dict() != other.to_dict()
