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


class V20CredExRecordIndy(object):
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
        'created_at': 'str',
        'cred_ex_id': 'str',
        'cred_ex_indy_id': 'str',
        'cred_request_metadata': 'object',
        'cred_rev_id': 'str',
        'rev_reg_id': 'str',
        'state': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'cred_ex_id': 'cred_ex_id',
        'cred_ex_indy_id': 'cred_ex_indy_id',
        'cred_request_metadata': 'cred_request_metadata',
        'cred_rev_id': 'cred_rev_id',
        'rev_reg_id': 'rev_reg_id',
        'state': 'state',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, cred_ex_id=None, cred_ex_indy_id=None, cred_request_metadata=None, cred_rev_id=None, rev_reg_id=None, state=None, updated_at=None, _configuration=None):  # noqa: E501
        """V20CredExRecordIndy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._cred_ex_id = None
        self._cred_ex_indy_id = None
        self._cred_request_metadata = None
        self._cred_rev_id = None
        self._rev_reg_id = None
        self._state = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if cred_ex_id is not None:
            self.cred_ex_id = cred_ex_id
        if cred_ex_indy_id is not None:
            self.cred_ex_indy_id = cred_ex_indy_id
        if cred_request_metadata is not None:
            self.cred_request_metadata = cred_request_metadata
        if cred_rev_id is not None:
            self.cred_rev_id = cred_rev_id
        if rev_reg_id is not None:
            self.rev_reg_id = rev_reg_id
        if state is not None:
            self.state = state
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this V20CredExRecordIndy.  # noqa: E501

        Time of record creation  # noqa: E501

        :return: The created_at of this V20CredExRecordIndy.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V20CredExRecordIndy.

        Time of record creation  # noqa: E501

        :param created_at: The created_at of this V20CredExRecordIndy.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                created_at is not None and not re.search(r'^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$', created_at)):  # noqa: E501
            raise ValueError(r"Invalid value for `created_at`, must be a follow pattern or equal to `/^\\d{4}-\\d\\d-\\d\\d[T ]\\d\\d:\\d\\d(?:\\:(?:\\d\\d(?:\\.\\d{1,6})?))?(?:[+-]\\d\\d:?\\d\\d|Z|)$/`")  # noqa: E501

        self._created_at = created_at

    @property
    def cred_ex_id(self):
        """Gets the cred_ex_id of this V20CredExRecordIndy.  # noqa: E501

        Corresponding v2.0 credential exchange record identifier  # noqa: E501

        :return: The cred_ex_id of this V20CredExRecordIndy.  # noqa: E501
        :rtype: str
        """
        return self._cred_ex_id

    @cred_ex_id.setter
    def cred_ex_id(self, cred_ex_id):
        """Sets the cred_ex_id of this V20CredExRecordIndy.

        Corresponding v2.0 credential exchange record identifier  # noqa: E501

        :param cred_ex_id: The cred_ex_id of this V20CredExRecordIndy.  # noqa: E501
        :type: str
        """

        self._cred_ex_id = cred_ex_id

    @property
    def cred_ex_indy_id(self):
        """Gets the cred_ex_indy_id of this V20CredExRecordIndy.  # noqa: E501

        Record identifier  # noqa: E501

        :return: The cred_ex_indy_id of this V20CredExRecordIndy.  # noqa: E501
        :rtype: str
        """
        return self._cred_ex_indy_id

    @cred_ex_indy_id.setter
    def cred_ex_indy_id(self, cred_ex_indy_id):
        """Sets the cred_ex_indy_id of this V20CredExRecordIndy.

        Record identifier  # noqa: E501

        :param cred_ex_indy_id: The cred_ex_indy_id of this V20CredExRecordIndy.  # noqa: E501
        :type: str
        """

        self._cred_ex_indy_id = cred_ex_indy_id

    @property
    def cred_request_metadata(self):
        """Gets the cred_request_metadata of this V20CredExRecordIndy.  # noqa: E501

        Credential request metadata for indy holder  # noqa: E501

        :return: The cred_request_metadata of this V20CredExRecordIndy.  # noqa: E501
        :rtype: object
        """
        return self._cred_request_metadata

    @cred_request_metadata.setter
    def cred_request_metadata(self, cred_request_metadata):
        """Sets the cred_request_metadata of this V20CredExRecordIndy.

        Credential request metadata for indy holder  # noqa: E501

        :param cred_request_metadata: The cred_request_metadata of this V20CredExRecordIndy.  # noqa: E501
        :type: object
        """

        self._cred_request_metadata = cred_request_metadata

    @property
    def cred_rev_id(self):
        """Gets the cred_rev_id of this V20CredExRecordIndy.  # noqa: E501

        Credential revocation identifier within revocation registry  # noqa: E501

        :return: The cred_rev_id of this V20CredExRecordIndy.  # noqa: E501
        :rtype: str
        """
        return self._cred_rev_id

    @cred_rev_id.setter
    def cred_rev_id(self, cred_rev_id):
        """Sets the cred_rev_id of this V20CredExRecordIndy.

        Credential revocation identifier within revocation registry  # noqa: E501

        :param cred_rev_id: The cred_rev_id of this V20CredExRecordIndy.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cred_rev_id is not None and not re.search(r'^[1-9][0-9]*$', cred_rev_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `cred_rev_id`, must be a follow pattern or equal to `/^[1-9][0-9]*$/`")  # noqa: E501

        self._cred_rev_id = cred_rev_id

    @property
    def rev_reg_id(self):
        """Gets the rev_reg_id of this V20CredExRecordIndy.  # noqa: E501

        Revocation registry identifier  # noqa: E501

        :return: The rev_reg_id of this V20CredExRecordIndy.  # noqa: E501
        :rtype: str
        """
        return self._rev_reg_id

    @rev_reg_id.setter
    def rev_reg_id(self, rev_reg_id):
        """Sets the rev_reg_id of this V20CredExRecordIndy.

        Revocation registry identifier  # noqa: E501

        :param rev_reg_id: The rev_reg_id of this V20CredExRecordIndy.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                rev_reg_id is not None and not re.search(r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)', rev_reg_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `rev_reg_id`, must be a follow pattern or equal to `/^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)/`")  # noqa: E501

        self._rev_reg_id = rev_reg_id

    @property
    def state(self):
        """Gets the state of this V20CredExRecordIndy.  # noqa: E501

        Current record state  # noqa: E501

        :return: The state of this V20CredExRecordIndy.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V20CredExRecordIndy.

        Current record state  # noqa: E501

        :param state: The state of this V20CredExRecordIndy.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def updated_at(self):
        """Gets the updated_at of this V20CredExRecordIndy.  # noqa: E501

        Time of last record update  # noqa: E501

        :return: The updated_at of this V20CredExRecordIndy.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this V20CredExRecordIndy.

        Time of last record update  # noqa: E501

        :param updated_at: The updated_at of this V20CredExRecordIndy.  # noqa: E501
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
        if issubclass(V20CredExRecordIndy, dict):
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
        if not isinstance(other, V20CredExRecordIndy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V20CredExRecordIndy):
            return True

        return self.to_dict() != other.to_dict()
