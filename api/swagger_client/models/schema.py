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


class Schema(object):
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
        'attr_names': 'list[str]',
        'id': 'str',
        'name': 'str',
        'seq_no': 'int',
        'ver': 'str',
        'version': 'str'
    }

    attribute_map = {
        'attr_names': 'attrNames',
        'id': 'id',
        'name': 'name',
        'seq_no': 'seqNo',
        'ver': 'ver',
        'version': 'version'
    }

    def __init__(self, attr_names=None, id=None, name=None, seq_no=None, ver=None, version=None, _configuration=None):  # noqa: E501
        """Schema - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attr_names = None
        self._id = None
        self._name = None
        self._seq_no = None
        self._ver = None
        self._version = None
        self.discriminator = None

        if attr_names is not None:
            self.attr_names = attr_names
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if seq_no is not None:
            self.seq_no = seq_no
        if ver is not None:
            self.ver = ver
        if version is not None:
            self.version = version

    @property
    def attr_names(self):
        """Gets the attr_names of this Schema.  # noqa: E501

        Schema attribute names  # noqa: E501

        :return: The attr_names of this Schema.  # noqa: E501
        :rtype: list[str]
        """
        return self._attr_names

    @attr_names.setter
    def attr_names(self, attr_names):
        """Sets the attr_names of this Schema.

        Schema attribute names  # noqa: E501

        :param attr_names: The attr_names of this Schema.  # noqa: E501
        :type: list[str]
        """

        self._attr_names = attr_names

    @property
    def id(self):
        """Gets the id of this Schema.  # noqa: E501

        Schema identifier  # noqa: E501

        :return: The id of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Schema.

        Schema identifier  # noqa: E501

        :param id: The id of this Schema.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                id is not None and not re.search(r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$/`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Schema.  # noqa: E501

        Schema name  # noqa: E501

        :return: The name of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Schema.

        Schema name  # noqa: E501

        :param name: The name of this Schema.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def seq_no(self):
        """Gets the seq_no of this Schema.  # noqa: E501

        Schema sequence number  # noqa: E501

        :return: The seq_no of this Schema.  # noqa: E501
        :rtype: int
        """
        return self._seq_no

    @seq_no.setter
    def seq_no(self, seq_no):
        """Sets the seq_no of this Schema.

        Schema sequence number  # noqa: E501

        :param seq_no: The seq_no of this Schema.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                seq_no is not None and seq_no < 1):  # noqa: E501
            raise ValueError("Invalid value for `seq_no`, must be a value greater than or equal to `1`")  # noqa: E501

        self._seq_no = seq_no

    @property
    def ver(self):
        """Gets the ver of this Schema.  # noqa: E501

        Node protocol version  # noqa: E501

        :return: The ver of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._ver

    @ver.setter
    def ver(self, ver):
        """Sets the ver of this Schema.

        Node protocol version  # noqa: E501

        :param ver: The ver of this Schema.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                ver is not None and not re.search(r'^[0-9.]+$', ver)):  # noqa: E501
            raise ValueError(r"Invalid value for `ver`, must be a follow pattern or equal to `/^[0-9.]+$/`")  # noqa: E501

        self._ver = ver

    @property
    def version(self):
        """Gets the version of this Schema.  # noqa: E501

        Schema version  # noqa: E501

        :return: The version of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Schema.

        Schema version  # noqa: E501

        :param version: The version of this Schema.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                version is not None and not re.search(r'^[0-9.]+$', version)):  # noqa: E501
            raise ValueError(r"Invalid value for `version`, must be a follow pattern or equal to `/^[0-9.]+$/`")  # noqa: E501

        self._version = version

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
        if issubclass(Schema, dict):
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
        if not isinstance(other, Schema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Schema):
            return True

        return self.to_dict() != other.to_dict()