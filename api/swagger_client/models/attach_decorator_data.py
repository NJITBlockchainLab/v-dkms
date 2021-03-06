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


class AttachDecoratorData(object):
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
        'base64': 'str',
        'json': 'object',
        'jws': 'object',
        'links': 'list[str]',
        'sha256': 'str'
    }

    attribute_map = {
        'base64': 'base64',
        'json': 'json',
        'jws': 'jws',
        'links': 'links',
        'sha256': 'sha256'
    }

    def __init__(self, base64=None, json=None, jws=None, links=None, sha256=None, _configuration=None):  # noqa: E501
        """AttachDecoratorData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base64 = None
        self._json = None
        self._jws = None
        self._links = None
        self._sha256 = None
        self.discriminator = None

        if base64 is not None:
            self.base64 = base64
        if json is not None:
            self.json = json
        if jws is not None:
            self.jws = jws
        if links is not None:
            self.links = links
        if sha256 is not None:
            self.sha256 = sha256

    @property
    def base64(self):
        """Gets the base64 of this AttachDecoratorData.  # noqa: E501

        Base64-encoded data  # noqa: E501

        :return: The base64 of this AttachDecoratorData.  # noqa: E501
        :rtype: str
        """
        return self._base64

    @base64.setter
    def base64(self, base64):
        """Sets the base64 of this AttachDecoratorData.

        Base64-encoded data  # noqa: E501

        :param base64: The base64 of this AttachDecoratorData.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                base64 is not None and not re.search(r'^[a-zA-Z0-9+\/]*={0,2}$', base64)):  # noqa: E501
            raise ValueError(r"Invalid value for `base64`, must be a follow pattern or equal to `/^[a-zA-Z0-9+\/]*={0,2}$/`")  # noqa: E501

        self._base64 = base64

    @property
    def json(self):
        """Gets the json of this AttachDecoratorData.  # noqa: E501

        JSON-serialized data  # noqa: E501

        :return: The json of this AttachDecoratorData.  # noqa: E501
        :rtype: object
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this AttachDecoratorData.

        JSON-serialized data  # noqa: E501

        :param json: The json of this AttachDecoratorData.  # noqa: E501
        :type: object
        """

        self._json = json

    @property
    def jws(self):
        """Gets the jws of this AttachDecoratorData.  # noqa: E501

        Detached Java Web Signature  # noqa: E501

        :return: The jws of this AttachDecoratorData.  # noqa: E501
        :rtype: object
        """
        return self._jws

    @jws.setter
    def jws(self, jws):
        """Sets the jws of this AttachDecoratorData.

        Detached Java Web Signature  # noqa: E501

        :param jws: The jws of this AttachDecoratorData.  # noqa: E501
        :type: object
        """

        self._jws = jws

    @property
    def links(self):
        """Gets the links of this AttachDecoratorData.  # noqa: E501

        List of hypertext links to data  # noqa: E501

        :return: The links of this AttachDecoratorData.  # noqa: E501
        :rtype: list[str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AttachDecoratorData.

        List of hypertext links to data  # noqa: E501

        :param links: The links of this AttachDecoratorData.  # noqa: E501
        :type: list[str]
        """

        self._links = links

    @property
    def sha256(self):
        """Gets the sha256 of this AttachDecoratorData.  # noqa: E501

        SHA256 hash (binhex encoded) of content  # noqa: E501

        :return: The sha256 of this AttachDecoratorData.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this AttachDecoratorData.

        SHA256 hash (binhex encoded) of content  # noqa: E501

        :param sha256: The sha256 of this AttachDecoratorData.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                sha256 is not None and not re.search(r'^[a-fA-F0-9+\/]{64}$', sha256)):  # noqa: E501
            raise ValueError(r"Invalid value for `sha256`, must be a follow pattern or equal to `/^[a-fA-F0-9+\/]{64}$/`")  # noqa: E501

        self._sha256 = sha256

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
        if issubclass(AttachDecoratorData, dict):
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
        if not isinstance(other, AttachDecoratorData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachDecoratorData):
            return True

        return self.to_dict() != other.to_dict()
