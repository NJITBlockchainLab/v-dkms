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


class V10PresentationExchange(object):
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
        'connection_id': 'str',
        'created_at': 'str',
        'error_msg': 'str',
        'initiator': 'str',
        'presentation': 'object',
        'presentation_exchange_id': 'str',
        'presentation_proposal_dict': 'object',
        'presentation_request': 'object',
        'presentation_request_dict': 'object',
        'role': 'str',
        'state': 'str',
        'thread_id': 'str',
        'trace': 'bool',
        'updated_at': 'str',
        'verified': 'str'
    }

    attribute_map = {
        'auto_present': 'auto_present',
        'connection_id': 'connection_id',
        'created_at': 'created_at',
        'error_msg': 'error_msg',
        'initiator': 'initiator',
        'presentation': 'presentation',
        'presentation_exchange_id': 'presentation_exchange_id',
        'presentation_proposal_dict': 'presentation_proposal_dict',
        'presentation_request': 'presentation_request',
        'presentation_request_dict': 'presentation_request_dict',
        'role': 'role',
        'state': 'state',
        'thread_id': 'thread_id',
        'trace': 'trace',
        'updated_at': 'updated_at',
        'verified': 'verified'
    }

    def __init__(self, auto_present=None, connection_id=None, created_at=None, error_msg=None, initiator=None, presentation=None, presentation_exchange_id=None, presentation_proposal_dict=None, presentation_request=None, presentation_request_dict=None, role=None, state=None, thread_id=None, trace=None, updated_at=None, verified=None, _configuration=None):  # noqa: E501
        """V10PresentationExchange - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_present = None
        self._connection_id = None
        self._created_at = None
        self._error_msg = None
        self._initiator = None
        self._presentation = None
        self._presentation_exchange_id = None
        self._presentation_proposal_dict = None
        self._presentation_request = None
        self._presentation_request_dict = None
        self._role = None
        self._state = None
        self._thread_id = None
        self._trace = None
        self._updated_at = None
        self._verified = None
        self.discriminator = None

        if auto_present is not None:
            self.auto_present = auto_present
        if connection_id is not None:
            self.connection_id = connection_id
        if created_at is not None:
            self.created_at = created_at
        if error_msg is not None:
            self.error_msg = error_msg
        if initiator is not None:
            self.initiator = initiator
        if presentation is not None:
            self.presentation = presentation
        if presentation_exchange_id is not None:
            self.presentation_exchange_id = presentation_exchange_id
        if presentation_proposal_dict is not None:
            self.presentation_proposal_dict = presentation_proposal_dict
        if presentation_request is not None:
            self.presentation_request = presentation_request
        if presentation_request_dict is not None:
            self.presentation_request_dict = presentation_request_dict
        if role is not None:
            self.role = role
        if state is not None:
            self.state = state
        if thread_id is not None:
            self.thread_id = thread_id
        if trace is not None:
            self.trace = trace
        if updated_at is not None:
            self.updated_at = updated_at
        if verified is not None:
            self.verified = verified

    @property
    def auto_present(self):
        """Gets the auto_present of this V10PresentationExchange.  # noqa: E501

        Prover choice to auto-present proof as verifier requests  # noqa: E501

        :return: The auto_present of this V10PresentationExchange.  # noqa: E501
        :rtype: bool
        """
        return self._auto_present

    @auto_present.setter
    def auto_present(self, auto_present):
        """Sets the auto_present of this V10PresentationExchange.

        Prover choice to auto-present proof as verifier requests  # noqa: E501

        :param auto_present: The auto_present of this V10PresentationExchange.  # noqa: E501
        :type: bool
        """

        self._auto_present = auto_present

    @property
    def connection_id(self):
        """Gets the connection_id of this V10PresentationExchange.  # noqa: E501

        Connection identifier  # noqa: E501

        :return: The connection_id of this V10PresentationExchange.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this V10PresentationExchange.

        Connection identifier  # noqa: E501

        :param connection_id: The connection_id of this V10PresentationExchange.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def created_at(self):
        """Gets the created_at of this V10PresentationExchange.  # noqa: E501

        Time of record creation  # noqa: E501

        :return: The created_at of this V10PresentationExchange.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V10PresentationExchange.

        Time of record creation  # noqa: E501

        :param created_at: The created_at of this V10PresentationExchange.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                created_at is not None and not re.search(r'^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$', created_at)):  # noqa: E501
            raise ValueError(r"Invalid value for `created_at`, must be a follow pattern or equal to `/^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$/`")  # noqa: E501

        self._created_at = created_at

    @property
    def error_msg(self):
        """Gets the error_msg of this V10PresentationExchange.  # noqa: E501

        Error message  # noqa: E501

        :return: The error_msg of this V10PresentationExchange.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this V10PresentationExchange.

        Error message  # noqa: E501

        :param error_msg: The error_msg of this V10PresentationExchange.  # noqa: E501
        :type: str
        """

        self._error_msg = error_msg

    @property
    def initiator(self):
        """Gets the initiator of this V10PresentationExchange.  # noqa: E501

        Present-proof exchange initiator: self or external  # noqa: E501

        :return: The initiator of this V10PresentationExchange.  # noqa: E501
        :rtype: str
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this V10PresentationExchange.

        Present-proof exchange initiator: self or external  # noqa: E501

        :param initiator: The initiator of this V10PresentationExchange.  # noqa: E501
        :type: str
        """
        allowed_values = ["self", "external"]  # noqa: E501
        if (self._configuration.client_side_validation and
                initiator not in allowed_values):
            raise ValueError(
                "Invalid value for `initiator` ({0}), must be one of {1}"  # noqa: E501
                .format(initiator, allowed_values)
            )

        self._initiator = initiator

    @property
    def presentation(self):
        """Gets the presentation of this V10PresentationExchange.  # noqa: E501

        (Indy) presentation (also known as proof)  # noqa: E501

        :return: The presentation of this V10PresentationExchange.  # noqa: E501
        :rtype: object
        """
        return self._presentation

    @presentation.setter
    def presentation(self, presentation):
        """Sets the presentation of this V10PresentationExchange.

        (Indy) presentation (also known as proof)  # noqa: E501

        :param presentation: The presentation of this V10PresentationExchange.  # noqa: E501
        :type: object
        """

        self._presentation = presentation

    @property
    def presentation_exchange_id(self):
        """Gets the presentation_exchange_id of this V10PresentationExchange.  # noqa: E501

        Presentation exchange identifier  # noqa: E501

        :return: The presentation_exchange_id of this V10PresentationExchange.  # noqa: E501
        :rtype: str
        """
        return self._presentation_exchange_id

    @presentation_exchange_id.setter
    def presentation_exchange_id(self, presentation_exchange_id):
        """Sets the presentation_exchange_id of this V10PresentationExchange.

        Presentation exchange identifier  # noqa: E501

        :param presentation_exchange_id: The presentation_exchange_id of this V10PresentationExchange.  # noqa: E501
        :type: str
        """

        self._presentation_exchange_id = presentation_exchange_id

    @property
    def presentation_proposal_dict(self):
        """Gets the presentation_proposal_dict of this V10PresentationExchange.  # noqa: E501

        Serialized presentation proposal message  # noqa: E501

        :return: The presentation_proposal_dict of this V10PresentationExchange.  # noqa: E501
        :rtype: object
        """
        return self._presentation_proposal_dict

    @presentation_proposal_dict.setter
    def presentation_proposal_dict(self, presentation_proposal_dict):
        """Sets the presentation_proposal_dict of this V10PresentationExchange.

        Serialized presentation proposal message  # noqa: E501

        :param presentation_proposal_dict: The presentation_proposal_dict of this V10PresentationExchange.  # noqa: E501
        :type: object
        """

        self._presentation_proposal_dict = presentation_proposal_dict

    @property
    def presentation_request(self):
        """Gets the presentation_request of this V10PresentationExchange.  # noqa: E501

        (Indy) presentation request (also known as proof request)  # noqa: E501

        :return: The presentation_request of this V10PresentationExchange.  # noqa: E501
        :rtype: object
        """
        return self._presentation_request

    @presentation_request.setter
    def presentation_request(self, presentation_request):
        """Sets the presentation_request of this V10PresentationExchange.

        (Indy) presentation request (also known as proof request)  # noqa: E501

        :param presentation_request: The presentation_request of this V10PresentationExchange.  # noqa: E501
        :type: object
        """

        self._presentation_request = presentation_request

    @property
    def presentation_request_dict(self):
        """Gets the presentation_request_dict of this V10PresentationExchange.  # noqa: E501

        Serialized presentation request message  # noqa: E501

        :return: The presentation_request_dict of this V10PresentationExchange.  # noqa: E501
        :rtype: object
        """
        return self._presentation_request_dict

    @presentation_request_dict.setter
    def presentation_request_dict(self, presentation_request_dict):
        """Sets the presentation_request_dict of this V10PresentationExchange.

        Serialized presentation request message  # noqa: E501

        :param presentation_request_dict: The presentation_request_dict of this V10PresentationExchange.  # noqa: E501
        :type: object
        """

        self._presentation_request_dict = presentation_request_dict

    @property
    def role(self):
        """Gets the role of this V10PresentationExchange.  # noqa: E501

        Present-proof exchange role: prover or verifier  # noqa: E501

        :return: The role of this V10PresentationExchange.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this V10PresentationExchange.

        Present-proof exchange role: prover or verifier  # noqa: E501

        :param role: The role of this V10PresentationExchange.  # noqa: E501
        :type: str
        """
        allowed_values = ["prover", "verifier"]  # noqa: E501
        if (self._configuration.client_side_validation and
                role not in allowed_values):
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def state(self):
        """Gets the state of this V10PresentationExchange.  # noqa: E501

        Present-proof exchange state  # noqa: E501

        :return: The state of this V10PresentationExchange.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V10PresentationExchange.

        Present-proof exchange state  # noqa: E501

        :param state: The state of this V10PresentationExchange.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def thread_id(self):
        """Gets the thread_id of this V10PresentationExchange.  # noqa: E501

        Thread identifier  # noqa: E501

        :return: The thread_id of this V10PresentationExchange.  # noqa: E501
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        """Sets the thread_id of this V10PresentationExchange.

        Thread identifier  # noqa: E501

        :param thread_id: The thread_id of this V10PresentationExchange.  # noqa: E501
        :type: str
        """

        self._thread_id = thread_id

    @property
    def trace(self):
        """Gets the trace of this V10PresentationExchange.  # noqa: E501

        Record trace information, based on agent configuration  # noqa: E501

        :return: The trace of this V10PresentationExchange.  # noqa: E501
        :rtype: bool
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this V10PresentationExchange.

        Record trace information, based on agent configuration  # noqa: E501

        :param trace: The trace of this V10PresentationExchange.  # noqa: E501
        :type: bool
        """

        self._trace = trace

    @property
    def updated_at(self):
        """Gets the updated_at of this V10PresentationExchange.  # noqa: E501

        Time of last record update  # noqa: E501

        :return: The updated_at of this V10PresentationExchange.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this V10PresentationExchange.

        Time of last record update  # noqa: E501

        :param updated_at: The updated_at of this V10PresentationExchange.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                updated_at is not None and not re.search(r'^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$', updated_at)):  # noqa: E501
            raise ValueError(r"Invalid value for `updated_at`, must be a follow pattern or equal to `/^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$/`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def verified(self):
        """Gets the verified of this V10PresentationExchange.  # noqa: E501

        Whether presentation is verified: true or false  # noqa: E501

        :return: The verified of this V10PresentationExchange.  # noqa: E501
        :rtype: str
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this V10PresentationExchange.

        Whether presentation is verified: true or false  # noqa: E501

        :param verified: The verified of this V10PresentationExchange.  # noqa: E501
        :type: str
        """
        allowed_values = ["true", "false"]  # noqa: E501
        if (self._configuration.client_side_validation and
                verified not in allowed_values):
            raise ValueError(
                "Invalid value for `verified` ({0}), must be one of {1}"  # noqa: E501
                .format(verified, allowed_values)
            )

        self._verified = verified

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
        if issubclass(V10PresentationExchange, dict):
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
        if not isinstance(other, V10PresentationExchange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V10PresentationExchange):
            return True

        return self.to_dict() != other.to_dict()
