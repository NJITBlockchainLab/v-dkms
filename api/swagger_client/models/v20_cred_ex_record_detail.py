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


class V20CredExRecordDetail(object):
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
        'cred_ex_record': 'object',
        'dif': 'V20CredExRecordDIF',
        'indy': 'V20CredExRecordIndy'
    }

    attribute_map = {
        'cred_ex_record': 'cred_ex_record',
        'dif': 'dif',
        'indy': 'indy'
    }

    def __init__(self, cred_ex_record=None, dif=None, indy=None, _configuration=None):  # noqa: E501
        """V20CredExRecordDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cred_ex_record = None
        self._dif = None
        self._indy = None
        self.discriminator = None

        if cred_ex_record is not None:
            self.cred_ex_record = cred_ex_record
        if dif is not None:
            self.dif = dif
        if indy is not None:
            self.indy = indy

    @property
    def cred_ex_record(self):
        """Gets the cred_ex_record of this V20CredExRecordDetail.  # noqa: E501

        Credential exchange record  # noqa: E501

        :return: The cred_ex_record of this V20CredExRecordDetail.  # noqa: E501
        :rtype: object
        """
        return self._cred_ex_record

    @cred_ex_record.setter
    def cred_ex_record(self, cred_ex_record):
        """Sets the cred_ex_record of this V20CredExRecordDetail.

        Credential exchange record  # noqa: E501

        :param cred_ex_record: The cred_ex_record of this V20CredExRecordDetail.  # noqa: E501
        :type: object
        """

        self._cred_ex_record = cred_ex_record

    @property
    def dif(self):
        """Gets the dif of this V20CredExRecordDetail.  # noqa: E501


        :return: The dif of this V20CredExRecordDetail.  # noqa: E501
        :rtype: V20CredExRecordDIF
        """
        return self._dif

    @dif.setter
    def dif(self, dif):
        """Sets the dif of this V20CredExRecordDetail.


        :param dif: The dif of this V20CredExRecordDetail.  # noqa: E501
        :type: V20CredExRecordDIF
        """

        self._dif = dif

    @property
    def indy(self):
        """Gets the indy of this V20CredExRecordDetail.  # noqa: E501


        :return: The indy of this V20CredExRecordDetail.  # noqa: E501
        :rtype: V20CredExRecordIndy
        """
        return self._indy

    @indy.setter
    def indy(self, indy):
        """Sets the indy of this V20CredExRecordDetail.


        :param indy: The indy of this V20CredExRecordDetail.  # noqa: E501
        :type: V20CredExRecordIndy
        """

        self._indy = indy

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
        if issubclass(V20CredExRecordDetail, dict):
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
        if not isinstance(other, V20CredExRecordDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V20CredExRecordDetail):
            return True

        return self.to_dict() != other.to_dict()