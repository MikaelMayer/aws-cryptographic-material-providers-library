# Code generated by smithy-python-codegen DO NOT EDIT.

from typing import Any, Dict, Generic, List, Literal, TypeVar


class ServiceError(Exception):
    """Base error for all errors in the service.
    """
    pass

T = TypeVar('T')
class ApiError(ServiceError, Generic[T]):
    """Base error for all api errors in the service.
    """
    code: T
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class UnknownApiError(ApiError[Literal['Unknown']]):
    """Error representing any unknown api errors
    """
    code: Literal['Unknown'] = 'Unknown'

class AwsCryptographicMaterialProvidersException(ApiError[Literal["AwsCryptographicMaterialProvidersException"]]):
    code: Literal["AwsCryptographicMaterialProvidersException"] = "AwsCryptographicMaterialProvidersException"
    message: str
    def __init__(
        self,
        *,
        message: str,
    ):
        """////////////////
        :param message: A message associated with the specific error.

        """
        super().__init__(message)

    def as_dict(self):
        """Converts the AwsCryptographicMaterialProvidersException to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            'message': self.message,
            'code': self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates a AwsCryptographicMaterialProvidersException from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            'message': d['message'],
        }

        return AwsCryptographicMaterialProvidersException(**kwargs)

    def __repr__(self):
        result = "AwsCryptographicMaterialProvidersException("
        result += f'message={self.message},'
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any):
        if not isinstance(other, AwsCryptographicMaterialProvidersException):
            return False
        attributes: list[str] = ['message','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class InvalidDecryptionMaterials(ApiError[Literal["InvalidDecryptionMaterials"]]):
    code: Literal["InvalidDecryptionMaterials"] = "InvalidDecryptionMaterials"
    message: str
    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self):
        """Converts the InvalidDecryptionMaterials to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            'message': self.message,
            'code': self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates a InvalidDecryptionMaterials from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            'message': d['message'],
        }

        return InvalidDecryptionMaterials(**kwargs)

    def __repr__(self):
        result = "InvalidDecryptionMaterials("
        result += f'message={self.message},'
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any):
        if not isinstance(other, InvalidDecryptionMaterials):
            return False
        attributes: list[str] = ['message','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class InvalidEncryptionMaterials(ApiError[Literal["InvalidEncryptionMaterials"]]):
    code: Literal["InvalidEncryptionMaterials"] = "InvalidEncryptionMaterials"
    message: str
    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self):
        """Converts the InvalidEncryptionMaterials to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            'message': self.message,
            'code': self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates a InvalidEncryptionMaterials from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            'message': d['message'],
        }

        return InvalidEncryptionMaterials(**kwargs)

    def __repr__(self):
        result = "InvalidEncryptionMaterials("
        result += f'message={self.message},'
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any):
        if not isinstance(other, InvalidEncryptionMaterials):
            return False
        attributes: list[str] = ['message','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class InvalidAlgorithmSuiteInfo(ApiError[Literal["InvalidAlgorithmSuiteInfo"]]):
    code: Literal["InvalidAlgorithmSuiteInfo"] = "InvalidAlgorithmSuiteInfo"
    message: str
    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self):
        """Converts the InvalidAlgorithmSuiteInfo to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            'message': self.message,
            'code': self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates a InvalidAlgorithmSuiteInfo from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            'message': d['message'],
        }

        return InvalidAlgorithmSuiteInfo(**kwargs)

    def __repr__(self):
        result = "InvalidAlgorithmSuiteInfo("
        result += f'message={self.message},'
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any):
        if not isinstance(other, InvalidAlgorithmSuiteInfo):
            return False
        attributes: list[str] = ['message','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class InvalidAlgorithmSuiteInfoOnDecrypt(ApiError[Literal["InvalidAlgorithmSuiteInfoOnDecrypt"]]):
    code: Literal["InvalidAlgorithmSuiteInfoOnDecrypt"] = "InvalidAlgorithmSuiteInfoOnDecrypt"
    message: str
    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self):
        """Converts the InvalidAlgorithmSuiteInfoOnDecrypt to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            'message': self.message,
            'code': self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates a InvalidAlgorithmSuiteInfoOnDecrypt from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            'message': d['message'],
        }

        return InvalidAlgorithmSuiteInfoOnDecrypt(**kwargs)

    def __repr__(self):
        result = "InvalidAlgorithmSuiteInfoOnDecrypt("
        result += f'message={self.message},'
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any):
        if not isinstance(other, InvalidAlgorithmSuiteInfoOnDecrypt):
            return False
        attributes: list[str] = ['message','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class InvalidAlgorithmSuiteInfoOnEncrypt(ApiError[Literal["InvalidAlgorithmSuiteInfoOnEncrypt"]]):
    code: Literal["InvalidAlgorithmSuiteInfoOnEncrypt"] = "InvalidAlgorithmSuiteInfoOnEncrypt"
    message: str
    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self):
        """Converts the InvalidAlgorithmSuiteInfoOnEncrypt to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            'message': self.message,
            'code': self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates a InvalidAlgorithmSuiteInfoOnEncrypt from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            'message': d['message'],
        }

        return InvalidAlgorithmSuiteInfoOnEncrypt(**kwargs)

    def __repr__(self):
        result = "InvalidAlgorithmSuiteInfoOnEncrypt("
        result += f'message={self.message},'
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any):
        if not isinstance(other, InvalidAlgorithmSuiteInfoOnEncrypt):
            return False
        attributes: list[str] = ['message','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class InvalidDecryptionMaterialsTransition(ApiError[Literal["InvalidDecryptionMaterialsTransition"]]):
    code: Literal["InvalidDecryptionMaterialsTransition"] = "InvalidDecryptionMaterialsTransition"
    message: str
    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self):
        """Converts the InvalidDecryptionMaterialsTransition to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            'message': self.message,
            'code': self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates a InvalidDecryptionMaterialsTransition from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            'message': d['message'],
        }

        return InvalidDecryptionMaterialsTransition(**kwargs)

    def __repr__(self):
        result = "InvalidDecryptionMaterialsTransition("
        result += f'message={self.message},'
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any):
        if not isinstance(other, InvalidDecryptionMaterialsTransition):
            return False
        attributes: list[str] = ['message','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class InvalidEncryptionMaterialsTransition(ApiError[Literal["InvalidEncryptionMaterialsTransition"]]):
    code: Literal["InvalidEncryptionMaterialsTransition"] = "InvalidEncryptionMaterialsTransition"
    message: str
    def __init__(
        self,
        *,
        message: str,
    ):
        super().__init__(message)

    def as_dict(self):
        """Converts the InvalidEncryptionMaterialsTransition to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            'message': self.message,
            'code': self.code,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates a InvalidEncryptionMaterialsTransition from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            'message': d['message'],
        }

        return InvalidEncryptionMaterialsTransition(**kwargs)

    def __repr__(self):
        result = "InvalidEncryptionMaterialsTransition("
        result += f'message={self.message},'
        if self.message is not None:
            result += f"message={repr(self.message)}"

        return result + ")"

    def __eq__(self, other: Any):
        if not isinstance(other, InvalidEncryptionMaterialsTransition):
            return False
        attributes: list[str] = ['message','message',]
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class AwsCryptographicMaterialProvidersException(ApiError[Literal["AwsCryptographicMaterialProvidersException"]]):
    code: Literal["AwsCryptographicMaterialProvidersException"] = "AwsCryptographicMaterialProvidersException"
    message: str

class EntryAlreadyExists(ApiError[Literal["EntryAlreadyExists"]]):
    code: Literal["EntryAlreadyExists"] = "EntryAlreadyExists"
    message: str

class EntryDoesNotExist(ApiError[Literal["EntryDoesNotExist"]]):
    code: Literal["EntryDoesNotExist"] = "EntryDoesNotExist"
    message: str

class InvalidAlgorithmSuiteInfo(ApiError[Literal["InvalidAlgorithmSuiteInfo"]]):
    code: Literal["InvalidAlgorithmSuiteInfo"] = "InvalidAlgorithmSuiteInfo"
    message: str

class InvalidAlgorithmSuiteInfoOnDecrypt(ApiError[Literal["InvalidAlgorithmSuiteInfoOnDecrypt"]]):
    code: Literal["InvalidAlgorithmSuiteInfoOnDecrypt"] = "InvalidAlgorithmSuiteInfoOnDecrypt"
    message: str

class InvalidAlgorithmSuiteInfoOnEncrypt(ApiError[Literal["InvalidAlgorithmSuiteInfoOnEncrypt"]]):
    code: Literal["InvalidAlgorithmSuiteInfoOnEncrypt"] = "InvalidAlgorithmSuiteInfoOnEncrypt"
    message: str

class InvalidDecryptionMaterials(ApiError[Literal["InvalidDecryptionMaterials"]]):
    code: Literal["InvalidDecryptionMaterials"] = "InvalidDecryptionMaterials"
    message: str

class InvalidDecryptionMaterialsTransition(ApiError[Literal["InvalidDecryptionMaterialsTransition"]]):
    code: Literal["InvalidDecryptionMaterialsTransition"] = "InvalidDecryptionMaterialsTransition"
    message: str

class InvalidEncryptionMaterials(ApiError[Literal["InvalidEncryptionMaterials"]]):
    code: Literal["InvalidEncryptionMaterials"] = "InvalidEncryptionMaterials"
    message: str

class InvalidEncryptionMaterialsTransition(ApiError[Literal["InvalidEncryptionMaterialsTransition"]]):
    code: Literal["InvalidEncryptionMaterialsTransition"] = "InvalidEncryptionMaterialsTransition"
    message: str

class AwsCryptographicPrimitives(ApiError[Literal["AwsCryptographicPrimitives"]]):
    AwsCryptographicPrimitives: Any

class DynamoDB_20120810(ApiError[Literal["DynamoDB_20120810"]]):
    DynamoDB_20120810: Any

class TrentService(ApiError[Literal["TrentService"]]):
    TrentService: Any

class KeyStore(ApiError[Literal["KeyStore"]]):
    KeyStore: Any

class CollectionOfErrors(ApiError[Literal["CollectionOfErrors"]]):
    code: Literal["CollectionOfErrors"] = "CollectionOfErrors"
    message: str
    list: List[ServiceError]

    def __init__(
        self,
        *,
        message: str,
        list
    ):
        super().__init__(message)
        self.list = list

    def as_dict(self):
        """Converts the CollectionOfErrors to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            'message': self.message,
            'code': self.code,
            'list': self.list,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates a CollectionOfErrors from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            'message': d['message'],
            'list': d['list']
        }

        return CollectionOfErrors(**kwargs)

    def __repr__(self):
        result = "CollectionOfErrors("
        result += f'message={self.message},'
        if self.message is not None:
            result += f"message={repr(self.message)}"
        result += f'list={self.list}'
        result += ")"
        return result

    def __eq__(self, other: Any):
        if not isinstance(other, CollectionOfErrors):
            return False
        if not (self.list == other.list):
            return False
        attributes: list[str] = ['message','message']
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )

class OpaqueError(ApiError[Literal["OpaqueError"]]):
    code: Literal["OpaqueError"] = "OpaqueError"
    obj: Any  # As an OpaqueError, type of obj is unknown

    def __init__(
        self,
        *,
        obj
    ):
        super().__init__("")
        self.obj = obj

    def as_dict(self):
        """Converts the OpaqueError to a dictionary.

        The dictionary uses the modeled shape names rather than the parameter names as
        keys to be mostly compatible with boto3.
        """
        return {
            'message': self.message,
            'code': self.code,
            'obj': self.obj,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates a OpaqueError from a dictionary.

        The dictionary is expected to use the modeled shape names rather than the
        parameter names as keys to be mostly compatible with boto3.
        """
        kwargs: Dict[str, Any] = {
            'message': d['message'],
            'obj': d['obj']
        }

        return OpaqueError(**kwargs)

    def __repr__(self):
        result = "OpaqueError("
        result += f'message={self.message},'
        if self.message is not None:
            result += f"message={repr(self.message)}"
        result += f'obj={self.obj}'
        result += ")"
        return result

    def __eq__(self, other: Any):
        if not isinstance(other, OpaqueError):
            return False
        if not (self.obj == other.obj):
            return False
        attributes: list[str] = ['message','message']
        return all(
            getattr(self, a) == getattr(other, a)
            for a in attributes
        )
