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


class V10PresentationCreateRequestRequest(object):
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
        'comment': 'str',
        'proof_request': 'IndyProofRequest',
        'trace': 'bool'
    }

    attribute_map = {
        'comment': 'comment',
        'proof_request': 'proof_request',
        'trace': 'trace'
    }

    def __init__(self, comment=None, proof_request=None, trace=None, _configuration=None):  # noqa: E501
        """V10PresentationCreateRequestRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._comment = None
        self._proof_request = None
        self._trace = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        self.proof_request = proof_request
        if trace is not None:
            self.trace = trace

    @property
    def comment(self):
        """Gets the comment of this V10PresentationCreateRequestRequest.  # noqa: E501


        :return: The comment of this V10PresentationCreateRequestRequest.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this V10PresentationCreateRequestRequest.


        :param comment: The comment of this V10PresentationCreateRequestRequest.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def proof_request(self):
        """Gets the proof_request of this V10PresentationCreateRequestRequest.  # noqa: E501


        :return: The proof_request of this V10PresentationCreateRequestRequest.  # noqa: E501
        :rtype: IndyProofRequest
        """
        return self._proof_request

    @proof_request.setter
    def proof_request(self, proof_request):
        """Sets the proof_request of this V10PresentationCreateRequestRequest.


        :param proof_request: The proof_request of this V10PresentationCreateRequestRequest.  # noqa: E501
        :type: IndyProofRequest
        """
        if self._configuration.client_side_validation and proof_request is None:
            raise ValueError("Invalid value for `proof_request`, must not be `None`")  # noqa: E501

        self._proof_request = proof_request

    @property
    def trace(self):
        """Gets the trace of this V10PresentationCreateRequestRequest.  # noqa: E501

        Whether to trace event (default false)  # noqa: E501

        :return: The trace of this V10PresentationCreateRequestRequest.  # noqa: E501
        :rtype: bool
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this V10PresentationCreateRequestRequest.

        Whether to trace event (default false)  # noqa: E501

        :param trace: The trace of this V10PresentationCreateRequestRequest.  # noqa: E501
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
        if issubclass(V10PresentationCreateRequestRequest, dict):
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
        if not isinstance(other, V10PresentationCreateRequestRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V10PresentationCreateRequestRequest):
            return True

        return self.to_dict() != other.to_dict()
