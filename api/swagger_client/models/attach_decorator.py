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


class AttachDecorator(object):
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
        'id': 'str',
        'byte_count': 'int',
        'data': 'AttachDecoratorData',
        'description': 'str',
        'filename': 'str',
        'lastmod_time': 'str',
        'mime_type': 'str'
    }

    attribute_map = {
        'id': '@id',
        'byte_count': 'byte_count',
        'data': 'data',
        'description': 'description',
        'filename': 'filename',
        'lastmod_time': 'lastmod_time',
        'mime_type': 'mime-type'
    }

    def __init__(self, id=None, byte_count=None, data=None, description=None, filename=None, lastmod_time=None, mime_type=None, _configuration=None):  # noqa: E501
        """AttachDecorator - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._byte_count = None
        self._data = None
        self._description = None
        self._filename = None
        self._lastmod_time = None
        self._mime_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if byte_count is not None:
            self.byte_count = byte_count
        self.data = data
        if description is not None:
            self.description = description
        if filename is not None:
            self.filename = filename
        if lastmod_time is not None:
            self.lastmod_time = lastmod_time
        if mime_type is not None:
            self.mime_type = mime_type

    @property
    def id(self):
        """Gets the id of this AttachDecorator.  # noqa: E501

        Attachment identifier  # noqa: E501

        :return: The id of this AttachDecorator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttachDecorator.

        Attachment identifier  # noqa: E501

        :param id: The id of this AttachDecorator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def byte_count(self):
        """Gets the byte_count of this AttachDecorator.  # noqa: E501

        Byte count of data included by reference  # noqa: E501

        :return: The byte_count of this AttachDecorator.  # noqa: E501
        :rtype: int
        """
        return self._byte_count

    @byte_count.setter
    def byte_count(self, byte_count):
        """Sets the byte_count of this AttachDecorator.

        Byte count of data included by reference  # noqa: E501

        :param byte_count: The byte_count of this AttachDecorator.  # noqa: E501
        :type: int
        """

        self._byte_count = byte_count

    @property
    def data(self):
        """Gets the data of this AttachDecorator.  # noqa: E501


        :return: The data of this AttachDecorator.  # noqa: E501
        :rtype: AttachDecoratorData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AttachDecorator.


        :param data: The data of this AttachDecorator.  # noqa: E501
        :type: AttachDecoratorData
        """
        if self._configuration.client_side_validation and data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def description(self):
        """Gets the description of this AttachDecorator.  # noqa: E501

        Human-readable description of content  # noqa: E501

        :return: The description of this AttachDecorator.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AttachDecorator.

        Human-readable description of content  # noqa: E501

        :param description: The description of this AttachDecorator.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def filename(self):
        """Gets the filename of this AttachDecorator.  # noqa: E501

        File name  # noqa: E501

        :return: The filename of this AttachDecorator.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this AttachDecorator.

        File name  # noqa: E501

        :param filename: The filename of this AttachDecorator.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def lastmod_time(self):
        """Gets the lastmod_time of this AttachDecorator.  # noqa: E501

        Hint regarding last modification datetime, in ISO-8601 format  # noqa: E501

        :return: The lastmod_time of this AttachDecorator.  # noqa: E501
        :rtype: str
        """
        return self._lastmod_time

    @lastmod_time.setter
    def lastmod_time(self, lastmod_time):
        """Sets the lastmod_time of this AttachDecorator.

        Hint regarding last modification datetime, in ISO-8601 format  # noqa: E501

        :param lastmod_time: The lastmod_time of this AttachDecorator.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                lastmod_time is not None and not re.search(r'^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$', lastmod_time)):  # noqa: E501
            raise ValueError(r"Invalid value for `lastmod_time`, must be a follow pattern or equal to `/^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$/`")  # noqa: E501

        self._lastmod_time = lastmod_time

    @property
    def mime_type(self):
        """Gets the mime_type of this AttachDecorator.  # noqa: E501

        MIME type  # noqa: E501

        :return: The mime_type of this AttachDecorator.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this AttachDecorator.

        MIME type  # noqa: E501

        :param mime_type: The mime_type of this AttachDecorator.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

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
        if issubclass(AttachDecorator, dict):
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
        if not isinstance(other, AttachDecorator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachDecorator):
            return True

        return self.to_dict() != other.to_dict()