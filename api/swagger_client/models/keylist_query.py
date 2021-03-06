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


class KeylistQuery(object):
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
        'type': 'str',
        'filter': 'object',
        'paginate': 'object'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'filter': 'filter',
        'paginate': 'paginate'
    }

    def __init__(self, id=None, type=None, filter=None, paginate=None, _configuration=None):  # noqa: E501
        """KeylistQuery - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._type = None
        self._filter = None
        self._paginate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if filter is not None:
            self.filter = filter
        if paginate is not None:
            self.paginate = paginate

    @property
    def id(self):
        """Gets the id of this KeylistQuery.  # noqa: E501

        Message identifier  # noqa: E501

        :return: The id of this KeylistQuery.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KeylistQuery.

        Message identifier  # noqa: E501

        :param id: The id of this KeylistQuery.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this KeylistQuery.  # noqa: E501

        Message type  # noqa: E501

        :return: The type of this KeylistQuery.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this KeylistQuery.

        Message type  # noqa: E501

        :param type: The type of this KeylistQuery.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def filter(self):
        """Gets the filter of this KeylistQuery.  # noqa: E501

        Query dictionary object  # noqa: E501

        :return: The filter of this KeylistQuery.  # noqa: E501
        :rtype: object
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this KeylistQuery.

        Query dictionary object  # noqa: E501

        :param filter: The filter of this KeylistQuery.  # noqa: E501
        :type: object
        """

        self._filter = filter

    @property
    def paginate(self):
        """Gets the paginate of this KeylistQuery.  # noqa: E501

        Pagination info  # noqa: E501

        :return: The paginate of this KeylistQuery.  # noqa: E501
        :rtype: object
        """
        return self._paginate

    @paginate.setter
    def paginate(self, paginate):
        """Sets the paginate of this KeylistQuery.

        Pagination info  # noqa: E501

        :param paginate: The paginate of this KeylistQuery.  # noqa: E501
        :type: object
        """

        self._paginate = paginate

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
        if issubclass(KeylistQuery, dict):
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
        if not isinstance(other, KeylistQuery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeylistQuery):
            return True

        return self.to_dict() != other.to_dict()
