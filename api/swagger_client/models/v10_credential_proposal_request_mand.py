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


class V10CredentialProposalRequestMand(object):
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
        'auto_remove': 'bool',
        'comment': 'str',
        'connection_id': 'str',
        'cred_def_id': 'str',
        'credential_proposal': 'CredentialPreview',
        'issuer_did': 'str',
        'schema_id': 'str',
        'schema_issuer_did': 'str',
        'schema_name': 'str',
        'schema_version': 'str',
        'trace': 'bool'
    }

    attribute_map = {
        'auto_remove': 'auto_remove',
        'comment': 'comment',
        'connection_id': 'connection_id',
        'cred_def_id': 'cred_def_id',
        'credential_proposal': 'credential_proposal',
        'issuer_did': 'issuer_did',
        'schema_id': 'schema_id',
        'schema_issuer_did': 'schema_issuer_did',
        'schema_name': 'schema_name',
        'schema_version': 'schema_version',
        'trace': 'trace'
    }

    def __init__(self, auto_remove=None, comment=None, connection_id=None, cred_def_id=None, credential_proposal=None, issuer_did=None, schema_id=None, schema_issuer_did=None, schema_name=None, schema_version=None, trace=None, _configuration=None):  # noqa: E501
        """V10CredentialProposalRequestMand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_remove = None
        self._comment = None
        self._connection_id = None
        self._cred_def_id = None
        self._credential_proposal = None
        self._issuer_did = None
        self._schema_id = None
        self._schema_issuer_did = None
        self._schema_name = None
        self._schema_version = None
        self._trace = None
        self.discriminator = None

        if auto_remove is not None:
            self.auto_remove = auto_remove
        if comment is not None:
            self.comment = comment
        self.connection_id = connection_id
        if cred_def_id is not None:
            self.cred_def_id = cred_def_id
        self.credential_proposal = credential_proposal
        if issuer_did is not None:
            self.issuer_did = issuer_did
        if schema_id is not None:
            self.schema_id = schema_id
        if schema_issuer_did is not None:
            self.schema_issuer_did = schema_issuer_did
        if schema_name is not None:
            self.schema_name = schema_name
        if schema_version is not None:
            self.schema_version = schema_version
        if trace is not None:
            self.trace = trace

    @property
    def auto_remove(self):
        """Gets the auto_remove of this V10CredentialProposalRequestMand.  # noqa: E501

        Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting)  # noqa: E501

        :return: The auto_remove of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: bool
        """
        return self._auto_remove

    @auto_remove.setter
    def auto_remove(self, auto_remove):
        """Sets the auto_remove of this V10CredentialProposalRequestMand.

        Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting)  # noqa: E501

        :param auto_remove: The auto_remove of this V10CredentialProposalRequestMand.  # noqa: E501
        :type: bool
        """

        self._auto_remove = auto_remove

    @property
    def comment(self):
        """Gets the comment of this V10CredentialProposalRequestMand.  # noqa: E501

        Human-readable comment  # noqa: E501

        :return: The comment of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this V10CredentialProposalRequestMand.

        Human-readable comment  # noqa: E501

        :param comment: The comment of this V10CredentialProposalRequestMand.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def connection_id(self):
        """Gets the connection_id of this V10CredentialProposalRequestMand.  # noqa: E501

        Connection identifier  # noqa: E501

        :return: The connection_id of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this V10CredentialProposalRequestMand.

        Connection identifier  # noqa: E501

        :param connection_id: The connection_id of this V10CredentialProposalRequestMand.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and connection_id is None:
            raise ValueError("Invalid value for `connection_id`, must not be `None`")  # noqa: E501

        self._connection_id = connection_id

    @property
    def cred_def_id(self):
        """Gets the cred_def_id of this V10CredentialProposalRequestMand.  # noqa: E501

        Credential definition identifier  # noqa: E501

        :return: The cred_def_id of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: str
        """
        return self._cred_def_id

    @cred_def_id.setter
    def cred_def_id(self, cred_def_id):
        """Sets the cred_def_id of this V10CredentialProposalRequestMand.

        Credential definition identifier  # noqa: E501

        :param cred_def_id: The cred_def_id of this V10CredentialProposalRequestMand.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cred_def_id is not None and not re.search(r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$', cred_def_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `cred_def_id`, must be a follow pattern or equal to `/^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$/`")  # noqa: E501

        self._cred_def_id = cred_def_id

    @property
    def credential_proposal(self):
        """Gets the credential_proposal of this V10CredentialProposalRequestMand.  # noqa: E501


        :return: The credential_proposal of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: CredentialPreview
        """
        return self._credential_proposal

    @credential_proposal.setter
    def credential_proposal(self, credential_proposal):
        """Sets the credential_proposal of this V10CredentialProposalRequestMand.


        :param credential_proposal: The credential_proposal of this V10CredentialProposalRequestMand.  # noqa: E501
        :type: CredentialPreview
        """
        if self._configuration.client_side_validation and credential_proposal is None:
            raise ValueError("Invalid value for `credential_proposal`, must not be `None`")  # noqa: E501

        self._credential_proposal = credential_proposal

    @property
    def issuer_did(self):
        """Gets the issuer_did of this V10CredentialProposalRequestMand.  # noqa: E501

        Credential issuer DID  # noqa: E501

        :return: The issuer_did of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: str
        """
        return self._issuer_did

    @issuer_did.setter
    def issuer_did(self, issuer_did):
        """Sets the issuer_did of this V10CredentialProposalRequestMand.

        Credential issuer DID  # noqa: E501

        :param issuer_did: The issuer_did of this V10CredentialProposalRequestMand.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                issuer_did is not None and not re.search(r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$', issuer_did)):  # noqa: E501
            raise ValueError(r"Invalid value for `issuer_did`, must be a follow pattern or equal to `/^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/`")  # noqa: E501

        self._issuer_did = issuer_did

    @property
    def schema_id(self):
        """Gets the schema_id of this V10CredentialProposalRequestMand.  # noqa: E501

        Schema identifier  # noqa: E501

        :return: The schema_id of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this V10CredentialProposalRequestMand.

        Schema identifier  # noqa: E501

        :param schema_id: The schema_id of this V10CredentialProposalRequestMand.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                schema_id is not None and not re.search(r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$', schema_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `schema_id`, must be a follow pattern or equal to `/^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$/`")  # noqa: E501

        self._schema_id = schema_id

    @property
    def schema_issuer_did(self):
        """Gets the schema_issuer_did of this V10CredentialProposalRequestMand.  # noqa: E501

        Schema issuer DID  # noqa: E501

        :return: The schema_issuer_did of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: str
        """
        return self._schema_issuer_did

    @schema_issuer_did.setter
    def schema_issuer_did(self, schema_issuer_did):
        """Sets the schema_issuer_did of this V10CredentialProposalRequestMand.

        Schema issuer DID  # noqa: E501

        :param schema_issuer_did: The schema_issuer_did of this V10CredentialProposalRequestMand.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                schema_issuer_did is not None and not re.search(r'^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$', schema_issuer_did)):  # noqa: E501
            raise ValueError(r"Invalid value for `schema_issuer_did`, must be a follow pattern or equal to `/^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/`")  # noqa: E501

        self._schema_issuer_did = schema_issuer_did

    @property
    def schema_name(self):
        """Gets the schema_name of this V10CredentialProposalRequestMand.  # noqa: E501

        Schema name  # noqa: E501

        :return: The schema_name of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this V10CredentialProposalRequestMand.

        Schema name  # noqa: E501

        :param schema_name: The schema_name of this V10CredentialProposalRequestMand.  # noqa: E501
        :type: str
        """

        self._schema_name = schema_name

    @property
    def schema_version(self):
        """Gets the schema_version of this V10CredentialProposalRequestMand.  # noqa: E501

        Schema version  # noqa: E501

        :return: The schema_version of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this V10CredentialProposalRequestMand.

        Schema version  # noqa: E501

        :param schema_version: The schema_version of this V10CredentialProposalRequestMand.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                schema_version is not None and not re.search(r'^[0-9.]+$', schema_version)):  # noqa: E501
            raise ValueError(r"Invalid value for `schema_version`, must be a follow pattern or equal to `/^[0-9.]+$/`")  # noqa: E501

        self._schema_version = schema_version

    @property
    def trace(self):
        """Gets the trace of this V10CredentialProposalRequestMand.  # noqa: E501

        Whether to trace event (default false)  # noqa: E501

        :return: The trace of this V10CredentialProposalRequestMand.  # noqa: E501
        :rtype: bool
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this V10CredentialProposalRequestMand.

        Whether to trace event (default false)  # noqa: E501

        :param trace: The trace of this V10CredentialProposalRequestMand.  # noqa: E501
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
        if issubclass(V10CredentialProposalRequestMand, dict):
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
        if not isinstance(other, V10CredentialProposalRequestMand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V10CredentialProposalRequestMand):
            return True

        return self.to_dict() != other.to_dict()