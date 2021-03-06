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


class MenuFormParam(object):
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
        'default': 'str',
        'description': 'str',
        'name': 'str',
        'required': 'bool',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'default': 'default',
        'description': 'description',
        'name': 'name',
        'required': 'required',
        'title': 'title',
        'type': 'type'
    }

    def __init__(self, default=None, description=None, name=None, required=None, title=None, type=None, _configuration=None):  # noqa: E501
        """MenuFormParam - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._default = None
        self._description = None
        self._name = None
        self._required = None
        self._title = None
        self._type = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        self.name = name
        if required is not None:
            self.required = required
        self.title = title
        if type is not None:
            self.type = type

    @property
    def default(self):
        """Gets the default of this MenuFormParam.  # noqa: E501

        Default parameter value  # noqa: E501

        :return: The default of this MenuFormParam.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this MenuFormParam.

        Default parameter value  # noqa: E501

        :param default: The default of this MenuFormParam.  # noqa: E501
        :type: str
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this MenuFormParam.  # noqa: E501

        Additional descriptive text for menu form parameter  # noqa: E501

        :return: The description of this MenuFormParam.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MenuFormParam.

        Additional descriptive text for menu form parameter  # noqa: E501

        :param description: The description of this MenuFormParam.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this MenuFormParam.  # noqa: E501

        Menu parameter name  # noqa: E501

        :return: The name of this MenuFormParam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MenuFormParam.

        Menu parameter name  # noqa: E501

        :param name: The name of this MenuFormParam.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def required(self):
        """Gets the required of this MenuFormParam.  # noqa: E501

        Whether parameter is required  # noqa: E501

        :return: The required of this MenuFormParam.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this MenuFormParam.

        Whether parameter is required  # noqa: E501

        :param required: The required of this MenuFormParam.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def title(self):
        """Gets the title of this MenuFormParam.  # noqa: E501

        Menu parameter title  # noqa: E501

        :return: The title of this MenuFormParam.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MenuFormParam.

        Menu parameter title  # noqa: E501

        :param title: The title of this MenuFormParam.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def type(self):
        """Gets the type of this MenuFormParam.  # noqa: E501

        Menu form parameter input type  # noqa: E501

        :return: The type of this MenuFormParam.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MenuFormParam.

        Menu form parameter input type  # noqa: E501

        :param type: The type of this MenuFormParam.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(MenuFormParam, dict):
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
        if not isinstance(other, MenuFormParam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MenuFormParam):
            return True

        return self.to_dict() != other.to_dict()
