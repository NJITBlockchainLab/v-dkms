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


class SchemaSendResults(object):
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
        'schema': 'object',
        'schema_id': 'str'
    }

    attribute_map = {
        'schema': 'schema',
        'schema_id': 'schema_id'
    }

    def __init__(self, schema=None, schema_id=None, _configuration=None):  # noqa: E501
        """SchemaSendResults - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._schema = None
        self._schema_id = None
        self.discriminator = None

        self.schema = schema
        self.schema_id = schema_id

    @property
    def schema(self):
        """Gets the schema of this SchemaSendResults.  # noqa: E501

        Schema result  # noqa: E501

        :return: The schema of this SchemaSendResults.  # noqa: E501
        :rtype: object
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this SchemaSendResults.

        Schema result  # noqa: E501

        :param schema: The schema of this SchemaSendResults.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and schema is None:
            raise ValueError("Invalid value for `schema`, must not be `None`")  # noqa: E501

        self._schema = schema

    @property
    def schema_id(self):
        """Gets the schema_id of this SchemaSendResults.  # noqa: E501

        Schema identifier  # noqa: E501

        :return: The schema_id of this SchemaSendResults.  # noqa: E501
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this SchemaSendResults.

        Schema identifier  # noqa: E501

        :param schema_id: The schema_id of this SchemaSendResults.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and schema_id is None:
            raise ValueError("Invalid value for `schema_id`, must not be `None`")  # noqa: E501
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
        if issubclass(SchemaSendResults, dict):
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
        if not isinstance(other, SchemaSendResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SchemaSendResults):
            return True

        return self.to_dict() != other.to_dict()
