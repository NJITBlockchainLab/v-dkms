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


class MenuJson(object):
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
        'description': 'str',
        'errormsg': 'str',
        'options': 'list[MenuOption]',
        'title': 'str'
    }

    attribute_map = {
        'description': 'description',
        'errormsg': 'errormsg',
        'options': 'options',
        'title': 'title'
    }

    def __init__(self, description=None, errormsg=None, options=None, title=None, _configuration=None):  # noqa: E501
        """MenuJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._errormsg = None
        self._options = None
        self._title = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if errormsg is not None:
            self.errormsg = errormsg
        self.options = options
        if title is not None:
            self.title = title

    @property
    def description(self):
        """Gets the description of this MenuJson.  # noqa: E501

        Introductory text for the menu  # noqa: E501

        :return: The description of this MenuJson.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MenuJson.

        Introductory text for the menu  # noqa: E501

        :param description: The description of this MenuJson.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def errormsg(self):
        """Gets the errormsg of this MenuJson.  # noqa: E501

        Optional error message to display in menu header  # noqa: E501

        :return: The errormsg of this MenuJson.  # noqa: E501
        :rtype: str
        """
        return self._errormsg

    @errormsg.setter
    def errormsg(self, errormsg):
        """Sets the errormsg of this MenuJson.

        Optional error message to display in menu header  # noqa: E501

        :param errormsg: The errormsg of this MenuJson.  # noqa: E501
        :type: str
        """

        self._errormsg = errormsg

    @property
    def options(self):
        """Gets the options of this MenuJson.  # noqa: E501

        List of menu options  # noqa: E501

        :return: The options of this MenuJson.  # noqa: E501
        :rtype: list[MenuOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this MenuJson.

        List of menu options  # noqa: E501

        :param options: The options of this MenuJson.  # noqa: E501
        :type: list[MenuOption]
        """
        if self._configuration.client_side_validation and options is None:
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def title(self):
        """Gets the title of this MenuJson.  # noqa: E501

        Menu title  # noqa: E501

        :return: The title of this MenuJson.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MenuJson.

        Menu title  # noqa: E501

        :param title: The title of this MenuJson.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(MenuJson, dict):
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
        if not isinstance(other, MenuJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MenuJson):
            return True

        return self.to_dict() != other.to_dict()