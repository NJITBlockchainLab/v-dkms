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


class V20CredExRecord(object):
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
        'auto_issue': 'bool',
        'auto_offer': 'bool',
        'auto_remove': 'bool',
        'conn_id': 'str',
        'created_at': 'str',
        'cred_ex_id': 'str',
        'cred_id_stored': 'str',
        'cred_issue': 'object',
        'cred_offer': 'object',
        'cred_preview': 'object',
        'cred_proposal': 'object',
        'cred_request': 'object',
        'cred_request_metadata': 'object',
        'error_msg': 'str',
        'initiator': 'str',
        'parent_thread_id': 'str',
        'role': 'str',
        'state': 'str',
        'thread_id': 'str',
        'trace': 'bool',
        'updated_at': 'str'
    }

    attribute_map = {
        'auto_issue': 'auto_issue',
        'auto_offer': 'auto_offer',
        'auto_remove': 'auto_remove',
        'conn_id': 'conn_id',
        'created_at': 'created_at',
        'cred_ex_id': 'cred_ex_id',
        'cred_id_stored': 'cred_id_stored',
        'cred_issue': 'cred_issue',
        'cred_offer': 'cred_offer',
        'cred_preview': 'cred_preview',
        'cred_proposal': 'cred_proposal',
        'cred_request': 'cred_request',
        'cred_request_metadata': 'cred_request_metadata',
        'error_msg': 'error_msg',
        'initiator': 'initiator',
        'parent_thread_id': 'parent_thread_id',
        'role': 'role',
        'state': 'state',
        'thread_id': 'thread_id',
        'trace': 'trace',
        'updated_at': 'updated_at'
    }

    def __init__(self, auto_issue=None, auto_offer=None, auto_remove=None, conn_id=None, created_at=None, cred_ex_id=None, cred_id_stored=None, cred_issue=None, cred_offer=None, cred_preview=None, cred_proposal=None, cred_request=None, cred_request_metadata=None, error_msg=None, initiator=None, parent_thread_id=None, role=None, state=None, thread_id=None, trace=None, updated_at=None, _configuration=None):  # noqa: E501
        """V20CredExRecord - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_issue = None
        self._auto_offer = None
        self._auto_remove = None
        self._conn_id = None
        self._created_at = None
        self._cred_ex_id = None
        self._cred_id_stored = None
        self._cred_issue = None
        self._cred_offer = None
        self._cred_preview = None
        self._cred_proposal = None
        self._cred_request = None
        self._cred_request_metadata = None
        self._error_msg = None
        self._initiator = None
        self._parent_thread_id = None
        self._role = None
        self._state = None
        self._thread_id = None
        self._trace = None
        self._updated_at = None
        self.discriminator = None

        if auto_issue is not None:
            self.auto_issue = auto_issue
        if auto_offer is not None:
            self.auto_offer = auto_offer
        if auto_remove is not None:
            self.auto_remove = auto_remove
        if conn_id is not None:
            self.conn_id = conn_id
        if created_at is not None:
            self.created_at = created_at
        if cred_ex_id is not None:
            self.cred_ex_id = cred_ex_id
        if cred_id_stored is not None:
            self.cred_id_stored = cred_id_stored
        if cred_issue is not None:
            self.cred_issue = cred_issue
        if cred_offer is not None:
            self.cred_offer = cred_offer
        if cred_preview is not None:
            self.cred_preview = cred_preview
        if cred_proposal is not None:
            self.cred_proposal = cred_proposal
        if cred_request is not None:
            self.cred_request = cred_request
        if cred_request_metadata is not None:
            self.cred_request_metadata = cred_request_metadata
        if error_msg is not None:
            self.error_msg = error_msg
        if initiator is not None:
            self.initiator = initiator
        if parent_thread_id is not None:
            self.parent_thread_id = parent_thread_id
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

    @property
    def auto_issue(self):
        """Gets the auto_issue of this V20CredExRecord.  # noqa: E501

        Issuer choice to issue to request in this credential exchange  # noqa: E501

        :return: The auto_issue of this V20CredExRecord.  # noqa: E501
        :rtype: bool
        """
        return self._auto_issue

    @auto_issue.setter
    def auto_issue(self, auto_issue):
        """Sets the auto_issue of this V20CredExRecord.

        Issuer choice to issue to request in this credential exchange  # noqa: E501

        :param auto_issue: The auto_issue of this V20CredExRecord.  # noqa: E501
        :type: bool
        """

        self._auto_issue = auto_issue

    @property
    def auto_offer(self):
        """Gets the auto_offer of this V20CredExRecord.  # noqa: E501

        Holder choice to accept offer in this credential exchange  # noqa: E501

        :return: The auto_offer of this V20CredExRecord.  # noqa: E501
        :rtype: bool
        """
        return self._auto_offer

    @auto_offer.setter
    def auto_offer(self, auto_offer):
        """Sets the auto_offer of this V20CredExRecord.

        Holder choice to accept offer in this credential exchange  # noqa: E501

        :param auto_offer: The auto_offer of this V20CredExRecord.  # noqa: E501
        :type: bool
        """

        self._auto_offer = auto_offer

    @property
    def auto_remove(self):
        """Gets the auto_remove of this V20CredExRecord.  # noqa: E501

        Issuer choice to remove this credential exchange record when complete  # noqa: E501

        :return: The auto_remove of this V20CredExRecord.  # noqa: E501
        :rtype: bool
        """
        return self._auto_remove

    @auto_remove.setter
    def auto_remove(self, auto_remove):
        """Sets the auto_remove of this V20CredExRecord.

        Issuer choice to remove this credential exchange record when complete  # noqa: E501

        :param auto_remove: The auto_remove of this V20CredExRecord.  # noqa: E501
        :type: bool
        """

        self._auto_remove = auto_remove

    @property
    def conn_id(self):
        """Gets the conn_id of this V20CredExRecord.  # noqa: E501

        Connection identifier  # noqa: E501

        :return: The conn_id of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._conn_id

    @conn_id.setter
    def conn_id(self, conn_id):
        """Sets the conn_id of this V20CredExRecord.

        Connection identifier  # noqa: E501

        :param conn_id: The conn_id of this V20CredExRecord.  # noqa: E501
        :type: str
        """

        self._conn_id = conn_id

    @property
    def created_at(self):
        """Gets the created_at of this V20CredExRecord.  # noqa: E501

        Time of record creation  # noqa: E501

        :return: The created_at of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V20CredExRecord.

        Time of record creation  # noqa: E501

        :param created_at: The created_at of this V20CredExRecord.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                created_at is not None and not re.search(r'^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$', created_at)):  # noqa: E501
            raise ValueError(r"Invalid value for `created_at`, must be a follow pattern or equal to `/^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$/`")  # noqa: E501

        self._created_at = created_at

    @property
    def cred_ex_id(self):
        """Gets the cred_ex_id of this V20CredExRecord.  # noqa: E501

        Credential exchange identifier  # noqa: E501

        :return: The cred_ex_id of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._cred_ex_id

    @cred_ex_id.setter
    def cred_ex_id(self, cred_ex_id):
        """Sets the cred_ex_id of this V20CredExRecord.

        Credential exchange identifier  # noqa: E501

        :param cred_ex_id: The cred_ex_id of this V20CredExRecord.  # noqa: E501
        :type: str
        """

        self._cred_ex_id = cred_ex_id

    @property
    def cred_id_stored(self):
        """Gets the cred_id_stored of this V20CredExRecord.  # noqa: E501

        Credential identifier stored in wallet  # noqa: E501

        :return: The cred_id_stored of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._cred_id_stored

    @cred_id_stored.setter
    def cred_id_stored(self, cred_id_stored):
        """Sets the cred_id_stored of this V20CredExRecord.

        Credential identifier stored in wallet  # noqa: E501

        :param cred_id_stored: The cred_id_stored of this V20CredExRecord.  # noqa: E501
        :type: str
        """

        self._cred_id_stored = cred_id_stored

    @property
    def cred_issue(self):
        """Gets the cred_issue of this V20CredExRecord.  # noqa: E501

        Serialized credential issue message  # noqa: E501

        :return: The cred_issue of this V20CredExRecord.  # noqa: E501
        :rtype: object
        """
        return self._cred_issue

    @cred_issue.setter
    def cred_issue(self, cred_issue):
        """Sets the cred_issue of this V20CredExRecord.

        Serialized credential issue message  # noqa: E501

        :param cred_issue: The cred_issue of this V20CredExRecord.  # noqa: E501
        :type: object
        """

        self._cred_issue = cred_issue

    @property
    def cred_offer(self):
        """Gets the cred_offer of this V20CredExRecord.  # noqa: E501

        Serialized credential offer message  # noqa: E501

        :return: The cred_offer of this V20CredExRecord.  # noqa: E501
        :rtype: object
        """
        return self._cred_offer

    @cred_offer.setter
    def cred_offer(self, cred_offer):
        """Sets the cred_offer of this V20CredExRecord.

        Serialized credential offer message  # noqa: E501

        :param cred_offer: The cred_offer of this V20CredExRecord.  # noqa: E501
        :type: object
        """

        self._cred_offer = cred_offer

    @property
    def cred_preview(self):
        """Gets the cred_preview of this V20CredExRecord.  # noqa: E501

        Serialized credential preview from credential proposal  # noqa: E501

        :return: The cred_preview of this V20CredExRecord.  # noqa: E501
        :rtype: object
        """
        return self._cred_preview

    @cred_preview.setter
    def cred_preview(self, cred_preview):
        """Sets the cred_preview of this V20CredExRecord.

        Serialized credential preview from credential proposal  # noqa: E501

        :param cred_preview: The cred_preview of this V20CredExRecord.  # noqa: E501
        :type: object
        """

        self._cred_preview = cred_preview

    @property
    def cred_proposal(self):
        """Gets the cred_proposal of this V20CredExRecord.  # noqa: E501

        Serialized credential proposal message  # noqa: E501

        :return: The cred_proposal of this V20CredExRecord.  # noqa: E501
        :rtype: object
        """
        return self._cred_proposal

    @cred_proposal.setter
    def cred_proposal(self, cred_proposal):
        """Sets the cred_proposal of this V20CredExRecord.

        Serialized credential proposal message  # noqa: E501

        :param cred_proposal: The cred_proposal of this V20CredExRecord.  # noqa: E501
        :type: object
        """

        self._cred_proposal = cred_proposal

    @property
    def cred_request(self):
        """Gets the cred_request of this V20CredExRecord.  # noqa: E501

        Serialized credential request message  # noqa: E501

        :return: The cred_request of this V20CredExRecord.  # noqa: E501
        :rtype: object
        """
        return self._cred_request

    @cred_request.setter
    def cred_request(self, cred_request):
        """Sets the cred_request of this V20CredExRecord.

        Serialized credential request message  # noqa: E501

        :param cred_request: The cred_request of this V20CredExRecord.  # noqa: E501
        :type: object
        """

        self._cred_request = cred_request

    @property
    def cred_request_metadata(self):
        """Gets the cred_request_metadata of this V20CredExRecord.  # noqa: E501

        (Indy) credential request metadata  # noqa: E501

        :return: The cred_request_metadata of this V20CredExRecord.  # noqa: E501
        :rtype: object
        """
        return self._cred_request_metadata

    @cred_request_metadata.setter
    def cred_request_metadata(self, cred_request_metadata):
        """Sets the cred_request_metadata of this V20CredExRecord.

        (Indy) credential request metadata  # noqa: E501

        :param cred_request_metadata: The cred_request_metadata of this V20CredExRecord.  # noqa: E501
        :type: object
        """

        self._cred_request_metadata = cred_request_metadata

    @property
    def error_msg(self):
        """Gets the error_msg of this V20CredExRecord.  # noqa: E501

        Error message  # noqa: E501

        :return: The error_msg of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this V20CredExRecord.

        Error message  # noqa: E501

        :param error_msg: The error_msg of this V20CredExRecord.  # noqa: E501
        :type: str
        """

        self._error_msg = error_msg

    @property
    def initiator(self):
        """Gets the initiator of this V20CredExRecord.  # noqa: E501

        Issue-credential exchange initiator: self or external  # noqa: E501

        :return: The initiator of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this V20CredExRecord.

        Issue-credential exchange initiator: self or external  # noqa: E501

        :param initiator: The initiator of this V20CredExRecord.  # noqa: E501
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
    def parent_thread_id(self):
        """Gets the parent_thread_id of this V20CredExRecord.  # noqa: E501

        Parent thread identifier  # noqa: E501

        :return: The parent_thread_id of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._parent_thread_id

    @parent_thread_id.setter
    def parent_thread_id(self, parent_thread_id):
        """Sets the parent_thread_id of this V20CredExRecord.

        Parent thread identifier  # noqa: E501

        :param parent_thread_id: The parent_thread_id of this V20CredExRecord.  # noqa: E501
        :type: str
        """

        self._parent_thread_id = parent_thread_id

    @property
    def role(self):
        """Gets the role of this V20CredExRecord.  # noqa: E501

        Issue-credential exchange role: holder or issuer  # noqa: E501

        :return: The role of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this V20CredExRecord.

        Issue-credential exchange role: holder or issuer  # noqa: E501

        :param role: The role of this V20CredExRecord.  # noqa: E501
        :type: str
        """
        allowed_values = ["issuer", "holder"]  # noqa: E501
        if (self._configuration.client_side_validation and
                role not in allowed_values):
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def state(self):
        """Gets the state of this V20CredExRecord.  # noqa: E501

        Issue-credential exchange state  # noqa: E501

        :return: The state of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V20CredExRecord.

        Issue-credential exchange state  # noqa: E501

        :param state: The state of this V20CredExRecord.  # noqa: E501
        :type: str
        """
        allowed_values = ["proposal-sent", "proposal-received", "offer-sent", "offer-received", "request-sent", "request-received", "credential-issued", "credential-received", "done"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def thread_id(self):
        """Gets the thread_id of this V20CredExRecord.  # noqa: E501

        Thread identifier  # noqa: E501

        :return: The thread_id of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        """Sets the thread_id of this V20CredExRecord.

        Thread identifier  # noqa: E501

        :param thread_id: The thread_id of this V20CredExRecord.  # noqa: E501
        :type: str
        """

        self._thread_id = thread_id

    @property
    def trace(self):
        """Gets the trace of this V20CredExRecord.  # noqa: E501

        Record trace information, based on agent configuration  # noqa: E501

        :return: The trace of this V20CredExRecord.  # noqa: E501
        :rtype: bool
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this V20CredExRecord.

        Record trace information, based on agent configuration  # noqa: E501

        :param trace: The trace of this V20CredExRecord.  # noqa: E501
        :type: bool
        """

        self._trace = trace

    @property
    def updated_at(self):
        """Gets the updated_at of this V20CredExRecord.  # noqa: E501

        Time of last record update  # noqa: E501

        :return: The updated_at of this V20CredExRecord.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this V20CredExRecord.

        Time of last record update  # noqa: E501

        :param updated_at: The updated_at of this V20CredExRecord.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                updated_at is not None and not re.search(r'^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$', updated_at)):  # noqa: E501
            raise ValueError(r"Invalid value for `updated_at`, must be a follow pattern or equal to `/^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$/`")  # noqa: E501

        self._updated_at = updated_at

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
        if issubclass(V20CredExRecord, dict):
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
        if not isinstance(other, V20CredExRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V20CredExRecord):
            return True

        return self.to_dict() != other.to_dict()
