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


class AttachDecoratorDataJWS(object):
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
        'header': 'AttachDecoratorDataJWSHeader',
        'protected': 'str',
        'signature': 'str',
        'signatures': 'list[AttachDecoratorData1JWS]'
    }

    attribute_map = {
        'header': 'header',
        'protected': 'protected',
        'signature': 'signature',
        'signatures': 'signatures'
    }

    def __init__(self, header=None, protected=None, signature=None, signatures=None, _configuration=None):  # noqa: E501
        """AttachDecoratorDataJWS - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._header = None
        self._protected = None
        self._signature = None
        self._signatures = None
        self.discriminator = None

        if header is not None:
            self.header = header
        if protected is not None:
            self.protected = protected
        if signature is not None:
            self.signature = signature
        if signatures is not None:
            self.signatures = signatures

    @property
    def header(self):
        """Gets the header of this AttachDecoratorDataJWS.  # noqa: E501


        :return: The header of this AttachDecoratorDataJWS.  # noqa: E501
        :rtype: AttachDecoratorDataJWSHeader
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this AttachDecoratorDataJWS.


        :param header: The header of this AttachDecoratorDataJWS.  # noqa: E501
        :type: AttachDecoratorDataJWSHeader
        """

        self._header = header

    @property
    def protected(self):
        """Gets the protected of this AttachDecoratorDataJWS.  # noqa: E501

        protected JWS header  # noqa: E501

        :return: The protected of this AttachDecoratorDataJWS.  # noqa: E501
        :rtype: str
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this AttachDecoratorDataJWS.

        protected JWS header  # noqa: E501

        :param protected: The protected of this AttachDecoratorDataJWS.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                protected is not None and not re.search(r'^[-_a-zA-Z0-9]*$', protected)):  # noqa: E501
            raise ValueError(r"Invalid value for `protected`, must be a follow pattern or equal to `/^[-_a-zA-Z0-9]*$/`")  # noqa: E501

        self._protected = protected

    @property
    def signature(self):
        """Gets the signature of this AttachDecoratorDataJWS.  # noqa: E501

        signature  # noqa: E501

        :return: The signature of this AttachDecoratorDataJWS.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this AttachDecoratorDataJWS.

        signature  # noqa: E501

        :param signature: The signature of this AttachDecoratorDataJWS.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                signature is not None and not re.search(r'^[-_a-zA-Z0-9]*$', signature)):  # noqa: E501
            raise ValueError(r"Invalid value for `signature`, must be a follow pattern or equal to `/^[-_a-zA-Z0-9]*$/`")  # noqa: E501

        self._signature = signature

    @property
    def signatures(self):
        """Gets the signatures of this AttachDecoratorDataJWS.  # noqa: E501

        List of signatures  # noqa: E501

        :return: The signatures of this AttachDecoratorDataJWS.  # noqa: E501
        :rtype: list[AttachDecoratorData1JWS]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this AttachDecoratorDataJWS.

        List of signatures  # noqa: E501

        :param signatures: The signatures of this AttachDecoratorDataJWS.  # noqa: E501
        :type: list[AttachDecoratorData1JWS]
        """

        self._signatures = signatures

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
        if issubclass(AttachDecoratorDataJWS, dict):
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
        if not isinstance(other, AttachDecoratorDataJWS):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachDecoratorDataJWS):
            return True

        return self.to_dict() != other.to_dict()
