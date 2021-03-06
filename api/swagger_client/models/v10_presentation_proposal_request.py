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


class V10PresentationProposalRequest(object):
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
        'auto_present': 'bool',
        'comment': 'str',
        'connection_id': 'str',
        'presentation_proposal': 'PresentationPreview',
        'trace': 'bool'
    }

    attribute_map = {
        'auto_present': 'auto_present',
        'comment': 'comment',
        'connection_id': 'connection_id',
        'presentation_proposal': 'presentation_proposal',
        'trace': 'trace'
    }

    def __init__(self, auto_present=None, comment=None, connection_id=None, presentation_proposal=None, trace=None, _configuration=None):  # noqa: E501
        """V10PresentationProposalRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_present = None
        self._comment = None
        self._connection_id = None
        self._presentation_proposal = None
        self._trace = None
        self.discriminator = None

        if auto_present is not None:
            self.auto_present = auto_present
        if comment is not None:
            self.comment = comment
        self.connection_id = connection_id
        self.presentation_proposal = presentation_proposal
        if trace is not None:
            self.trace = trace

    @property
    def auto_present(self):
        """Gets the auto_present of this V10PresentationProposalRequest.  # noqa: E501

        Whether to respond automatically to presentation requests, building and presenting requested proof  # noqa: E501

        :return: The auto_present of this V10PresentationProposalRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_present

    @auto_present.setter
    def auto_present(self, auto_present):
        """Sets the auto_present of this V10PresentationProposalRequest.

        Whether to respond automatically to presentation requests, building and presenting requested proof  # noqa: E501

        :param auto_present: The auto_present of this V10PresentationProposalRequest.  # noqa: E501
        :type: bool
        """

        self._auto_present = auto_present

    @property
    def comment(self):
        """Gets the comment of this V10PresentationProposalRequest.  # noqa: E501

        Human-readable comment  # noqa: E501

        :return: The comment of this V10PresentationProposalRequest.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this V10PresentationProposalRequest.

        Human-readable comment  # noqa: E501

        :param comment: The comment of this V10PresentationProposalRequest.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def connection_id(self):
        """Gets the connection_id of this V10PresentationProposalRequest.  # noqa: E501

        Connection identifier  # noqa: E501

        :return: The connection_id of this V10PresentationProposalRequest.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this V10PresentationProposalRequest.

        Connection identifier  # noqa: E501

        :param connection_id: The connection_id of this V10PresentationProposalRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and connection_id is None:
            raise ValueError("Invalid value for `connection_id`, must not be `None`")  # noqa: E501

        self._connection_id = connection_id

    @property
    def presentation_proposal(self):
        """Gets the presentation_proposal of this V10PresentationProposalRequest.  # noqa: E501


        :return: The presentation_proposal of this V10PresentationProposalRequest.  # noqa: E501
        :rtype: PresentationPreview
        """
        return self._presentation_proposal

    @presentation_proposal.setter
    def presentation_proposal(self, presentation_proposal):
        """Sets the presentation_proposal of this V10PresentationProposalRequest.


        :param presentation_proposal: The presentation_proposal of this V10PresentationProposalRequest.  # noqa: E501
        :type: PresentationPreview
        """
        if self._configuration.client_side_validation and presentation_proposal is None:
            raise ValueError("Invalid value for `presentation_proposal`, must not be `None`")  # noqa: E501

        self._presentation_proposal = presentation_proposal

    @property
    def trace(self):
        """Gets the trace of this V10PresentationProposalRequest.  # noqa: E501

        Whether to trace event (default false)  # noqa: E501

        :return: The trace of this V10PresentationProposalRequest.  # noqa: E501
        :rtype: bool
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this V10PresentationProposalRequest.

        Whether to trace event (default false)  # noqa: E501

        :param trace: The trace of this V10PresentationProposalRequest.  # noqa: E501
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
        if issubclass(V10PresentationProposalRequest, dict):
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
        if not isinstance(other, V10PresentationProposalRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V10PresentationProposalRequest):
            return True

        return self.to_dict() != other.to_dict()
