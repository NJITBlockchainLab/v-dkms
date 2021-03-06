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


class MenuForm(object):
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
        'params': 'list[MenuFormParam]',
        'submit_label': 'str',
        'title': 'str'
    }

    attribute_map = {
        'description': 'description',
        'params': 'params',
        'submit_label': 'submit-label',
        'title': 'title'
    }

    def __init__(self, description=None, params=None, submit_label=None, title=None, _configuration=None):  # noqa: E501
        """MenuForm - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._params = None
        self._submit_label = None
        self._title = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if params is not None:
            self.params = params
        if submit_label is not None:
            self.submit_label = submit_label
        if title is not None:
            self.title = title

    @property
    def description(self):
        """Gets the description of this MenuForm.  # noqa: E501

        Additional descriptive text for menu form  # noqa: E501

        :return: The description of this MenuForm.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MenuForm.

        Additional descriptive text for menu form  # noqa: E501

        :param description: The description of this MenuForm.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def params(self):
        """Gets the params of this MenuForm.  # noqa: E501

        List of form parameters  # noqa: E501

        :return: The params of this MenuForm.  # noqa: E501
        :rtype: list[MenuFormParam]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this MenuForm.

        List of form parameters  # noqa: E501

        :param params: The params of this MenuForm.  # noqa: E501
        :type: list[MenuFormParam]
        """

        self._params = params

    @property
    def submit_label(self):
        """Gets the submit_label of this MenuForm.  # noqa: E501

        Alternative label for form submit button  # noqa: E501

        :return: The submit_label of this MenuForm.  # noqa: E501
        :rtype: str
        """
        return self._submit_label

    @submit_label.setter
    def submit_label(self, submit_label):
        """Sets the submit_label of this MenuForm.

        Alternative label for form submit button  # noqa: E501

        :param submit_label: The submit_label of this MenuForm.  # noqa: E501
        :type: str
        """

        self._submit_label = submit_label

    @property
    def title(self):
        """Gets the title of this MenuForm.  # noqa: E501

        Menu form title  # noqa: E501

        :return: The title of this MenuForm.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MenuForm.

        Menu form title  # noqa: E501

        :param title: The title of this MenuForm.  # noqa: E501
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
        if issubclass(MenuForm, dict):
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
        if not isinstance(other, MenuForm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MenuForm):
            return True

        return self.to_dict() != other.to_dict()
