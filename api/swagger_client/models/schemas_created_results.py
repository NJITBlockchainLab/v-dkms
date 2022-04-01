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


class SchemasCreatedResults(object):
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
        'schema_ids': 'list[str]'
    }

    attribute_map = {
        'schema_ids': 'schema_ids'
    }

    def __init__(self, schema_ids=None, _configuration=None):  # noqa: E501
        """SchemasCreatedResults - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._schema_ids = None
        self.discriminator = None

        if schema_ids is not None:
            self.schema_ids = schema_ids

    @property
    def schema_ids(self):
        """Gets the schema_ids of this SchemasCreatedResults.  # noqa: E501


        :return: The schema_ids of this SchemasCreatedResults.  # noqa: E501
        :rtype: list[str]
        """
        return self._schema_ids

    @schema_ids.setter
    def schema_ids(self, schema_ids):
        """Sets the schema_ids of this SchemasCreatedResults.


        :param schema_ids: The schema_ids of this SchemasCreatedResults.  # noqa: E501
        :type: list[str]
        """

        self._schema_ids = schema_ids

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
        if issubclass(SchemasCreatedResults, dict):
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
        if not isinstance(other, SchemasCreatedResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SchemasCreatedResults):
            return True

        return self.to_dict() != other.to_dict()
