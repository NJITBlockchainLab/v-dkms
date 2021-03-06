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


class PresPredSpec(object):
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
        'cred_def_id': 'str',
        'name': 'str',
        'predicate': 'str',
        'threshold': 'int'
    }

    attribute_map = {
        'cred_def_id': 'cred_def_id',
        'name': 'name',
        'predicate': 'predicate',
        'threshold': 'threshold'
    }

    def __init__(self, cred_def_id=None, name=None, predicate=None, threshold=None, _configuration=None):  # noqa: E501
        """PresPredSpec - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cred_def_id = None
        self._name = None
        self._predicate = None
        self._threshold = None
        self.discriminator = None

        if cred_def_id is not None:
            self.cred_def_id = cred_def_id
        self.name = name
        self.predicate = predicate
        self.threshold = threshold

    @property
    def cred_def_id(self):
        """Gets the cred_def_id of this PresPredSpec.  # noqa: E501

        Credential definition identifier  # noqa: E501

        :return: The cred_def_id of this PresPredSpec.  # noqa: E501
        :rtype: str
        """
        return self._cred_def_id

    @cred_def_id.setter
    def cred_def_id(self, cred_def_id):
        """Sets the cred_def_id of this PresPredSpec.

        Credential definition identifier  # noqa: E501

        :param cred_def_id: The cred_def_id of this PresPredSpec.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cred_def_id is not None and not re.search(r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$', cred_def_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `cred_def_id`, must be a follow pattern or equal to `/^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$/`")  # noqa: E501

        self._cred_def_id = cred_def_id

    @property
    def name(self):
        """Gets the name of this PresPredSpec.  # noqa: E501

        Attribute name  # noqa: E501

        :return: The name of this PresPredSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PresPredSpec.

        Attribute name  # noqa: E501

        :param name: The name of this PresPredSpec.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def predicate(self):
        """Gets the predicate of this PresPredSpec.  # noqa: E501

        Predicate type ('<', '<=', '>=', or '>')  # noqa: E501

        :return: The predicate of this PresPredSpec.  # noqa: E501
        :rtype: str
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this PresPredSpec.

        Predicate type ('<', '<=', '>=', or '>')  # noqa: E501

        :param predicate: The predicate of this PresPredSpec.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and predicate is None:
            raise ValueError("Invalid value for `predicate`, must not be `None`")  # noqa: E501
        allowed_values = ["<", "<=", ">=", ">"]  # noqa: E501
        if (self._configuration.client_side_validation and
                predicate not in allowed_values):
            raise ValueError(
                "Invalid value for `predicate` ({0}), must be one of {1}"  # noqa: E501
                .format(predicate, allowed_values)
            )

        self._predicate = predicate

    @property
    def threshold(self):
        """Gets the threshold of this PresPredSpec.  # noqa: E501

        Threshold value  # noqa: E501

        :return: The threshold of this PresPredSpec.  # noqa: E501
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this PresPredSpec.

        Threshold value  # noqa: E501

        :param threshold: The threshold of this PresPredSpec.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and threshold is None:
            raise ValueError("Invalid value for `threshold`, must not be `None`")  # noqa: E501

        self._threshold = threshold

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
        if issubclass(PresPredSpec, dict):
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
        if not isinstance(other, PresPredSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PresPredSpec):
            return True

        return self.to_dict() != other.to_dict()
