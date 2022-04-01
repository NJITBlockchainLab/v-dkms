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


class V10PresentationRequest(object):
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
        'requested_attributes': 'dict(str, IndyRequestedCredsRequestedAttr)',
        'requested_predicates': 'dict(str, IndyRequestedCredsRequestedPred)',
        'self_attested_attributes': 'dict(str, str)',
        'trace': 'bool'
    }

    attribute_map = {
        'requested_attributes': 'requested_attributes',
        'requested_predicates': 'requested_predicates',
        'self_attested_attributes': 'self_attested_attributes',
        'trace': 'trace'
    }

    def __init__(self, requested_attributes=None, requested_predicates=None, self_attested_attributes=None, trace=None, _configuration=None):  # noqa: E501
        """V10PresentationRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._requested_attributes = None
        self._requested_predicates = None
        self._self_attested_attributes = None
        self._trace = None
        self.discriminator = None

        self.requested_attributes = requested_attributes
        self.requested_predicates = requested_predicates
        self.self_attested_attributes = self_attested_attributes
        if trace is not None:
            self.trace = trace

    @property
    def requested_attributes(self):
        """Gets the requested_attributes of this V10PresentationRequest.  # noqa: E501

        Nested object mapping proof request attribute referents to requested-attribute specifiers  # noqa: E501

        :return: The requested_attributes of this V10PresentationRequest.  # noqa: E501
        :rtype: dict(str, IndyRequestedCredsRequestedAttr)
        """
        return self._requested_attributes

    @requested_attributes.setter
    def requested_attributes(self, requested_attributes):
        """Sets the requested_attributes of this V10PresentationRequest.

        Nested object mapping proof request attribute referents to requested-attribute specifiers  # noqa: E501

        :param requested_attributes: The requested_attributes of this V10PresentationRequest.  # noqa: E501
        :type: dict(str, IndyRequestedCredsRequestedAttr)
        """
        if self._configuration.client_side_validation and requested_attributes is None:
            raise ValueError("Invalid value for `requested_attributes`, must not be `None`")  # noqa: E501

        self._requested_attributes = requested_attributes

    @property
    def requested_predicates(self):
        """Gets the requested_predicates of this V10PresentationRequest.  # noqa: E501

        Nested object mapping proof request predicate referents to requested-predicate specifiers  # noqa: E501

        :return: The requested_predicates of this V10PresentationRequest.  # noqa: E501
        :rtype: dict(str, IndyRequestedCredsRequestedPred)
        """
        return self._requested_predicates

    @requested_predicates.setter
    def requested_predicates(self, requested_predicates):
        """Sets the requested_predicates of this V10PresentationRequest.

        Nested object mapping proof request predicate referents to requested-predicate specifiers  # noqa: E501

        :param requested_predicates: The requested_predicates of this V10PresentationRequest.  # noqa: E501
        :type: dict(str, IndyRequestedCredsRequestedPred)
        """
        if self._configuration.client_side_validation and requested_predicates is None:
            raise ValueError("Invalid value for `requested_predicates`, must not be `None`")  # noqa: E501

        self._requested_predicates = requested_predicates

    @property
    def self_attested_attributes(self):
        """Gets the self_attested_attributes of this V10PresentationRequest.  # noqa: E501

        Self-attested attributes to build into proof  # noqa: E501

        :return: The self_attested_attributes of this V10PresentationRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._self_attested_attributes

    @self_attested_attributes.setter
    def self_attested_attributes(self, self_attested_attributes):
        """Sets the self_attested_attributes of this V10PresentationRequest.

        Self-attested attributes to build into proof  # noqa: E501

        :param self_attested_attributes: The self_attested_attributes of this V10PresentationRequest.  # noqa: E501
        :type: dict(str, str)
        """
        if self._configuration.client_side_validation and self_attested_attributes is None:
            raise ValueError("Invalid value for `self_attested_attributes`, must not be `None`")  # noqa: E501

        self._self_attested_attributes = self_attested_attributes

    @property
    def trace(self):
        """Gets the trace of this V10PresentationRequest.  # noqa: E501

        Whether to trace event (default false)  # noqa: E501

        :return: The trace of this V10PresentationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this V10PresentationRequest.

        Whether to trace event (default false)  # noqa: E501

        :param trace: The trace of this V10PresentationRequest.  # noqa: E501
        :type: bool
        """

        self._trace = trace

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
        if issubclass(V10PresentationRequest, dict):
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
        if not isinstance(other, V10PresentationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V10PresentationRequest):
            return True

        return self.to_dict() != other.to_dict()
