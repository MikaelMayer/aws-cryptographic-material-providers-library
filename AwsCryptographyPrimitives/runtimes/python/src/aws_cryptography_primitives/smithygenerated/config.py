# Code generated by smithy-python-codegen DO NOT EDIT.

import aws_cryptography_primitives.smithygenerated.dafny_to_smithy
import aws_cryptography_primitives.smithygenerated.smithy_to_dafny
from dataclasses import dataclass
import module_
from software_amazon_cryptography_primitives_internaldafny_types import (
    CryptoConfig_CryptoConfig as DafnyCryptoConfig,
)
from typing import Any, Callable, TypeAlias, Union

from .dafnyImplInterface import DafnyImplInterface
from smithy_python._private.retries import SimpleRetryStrategy
from smithy_python.interfaces.interceptor import Interceptor
from smithy_python.interfaces.retries import RetryStrategy

from .models import (
    AESDecryptInput,
    AESDecryptOutput,
    AESEncryptInput,
    AESEncryptOutput,
    AesKdfCtrInput,
    AesKdfCtrOutput,
    DigestInput,
    DigestOutput,
    ECDSASignInput,
    ECDSASignOutput,
    ECDSAVerifyInput,
    ECDSAVerifyOutput,
    GenerateECDSASignatureKeyInput,
    GenerateECDSASignatureKeyOutput,
    GenerateRSAKeyPairInput,
    GenerateRSAKeyPairOutput,
    GenerateRandomBytesInput,
    GenerateRandomBytesOutput,
    GetRSAKeyModulusLengthInput,
    GetRSAKeyModulusLengthOutput,
    HMacInput,
    HMacOutput,
    HkdfExpandInput,
    HkdfExpandOutput,
    HkdfExtractInput,
    HkdfExtractOutput,
    HkdfInput,
    HkdfOutput,
    KdfCtrInput,
    KdfCtrOutput,
    RSADecryptInput,
    RSADecryptOutput,
    RSAEncryptInput,
    RSAEncryptOutput,
)


_ServiceInterceptor = Union[Interceptor[AESDecryptInput, AESDecryptOutput, Any, Any], Interceptor[AESEncryptInput, AESEncryptOutput, Any, Any], Interceptor[AesKdfCtrInput, AesKdfCtrOutput, Any, Any], Interceptor[DigestInput, DigestOutput, Any, Any], Interceptor[ECDSASignInput, ECDSASignOutput, Any, Any], Interceptor[ECDSAVerifyInput, ECDSAVerifyOutput, Any, Any], Interceptor[GenerateECDSASignatureKeyInput, GenerateECDSASignatureKeyOutput, Any, Any], Interceptor[GenerateRandomBytesInput, GenerateRandomBytesOutput, Any, Any], Interceptor[GenerateRSAKeyPairInput, GenerateRSAKeyPairOutput, Any, Any], Interceptor[GetRSAKeyModulusLengthInput, GetRSAKeyModulusLengthOutput, Any, Any], Interceptor[HkdfInput, HkdfOutput, Any, Any], Interceptor[HkdfExpandInput, HkdfExpandOutput, Any, Any], Interceptor[HkdfExtractInput, HkdfExtractOutput, Any, Any], Interceptor[HMacInput, HMacOutput, Any, Any], Interceptor[KdfCtrInput, KdfCtrOutput, Any, Any], Interceptor[RSADecryptInput, RSADecryptOutput, Any, Any], Interceptor[RSAEncryptInput, RSAEncryptOutput, Any, Any]]
@dataclass(init=False)
class Config:
    """Configuration for AwsCryptographicPrimitives."""

    interceptors: list[_ServiceInterceptor]
    retry_strategy: RetryStrategy
    dafnyImplInterface: DafnyImplInterface | None

    def __init__(
        self,
        *,
        interceptors: list[_ServiceInterceptor] | None = None,
        retry_strategy: RetryStrategy | None = None,
        dafnyImplInterface: DafnyImplInterface | None = None,
    ):
        """Constructor.

        :param interceptors: The list of interceptors, which are hooks that are called
        during the execution of a request.

        :param retry_strategy: The retry strategy for issuing retry tokens and computing
        retry delays.

        :param dafnyImplInterface:
        """
        self.interceptors = interceptors or []
        self.retry_strategy = retry_strategy or SimpleRetryStrategy()
        self.dafnyImplInterface = dafnyImplInterface

# A callable that allows customizing the config object on each request.
Plugin: TypeAlias = Callable[[Config], None]

class CryptoConfig(Config):
    '''
    Smithy-modelled localService Config shape for this localService.
    '''
    # TODO-Python: Add types to Config members

    def __init__(self, ):
        super().__init__()

def dafny_config_to_smithy_config(dafny_config):
    '''
    Converts the provided Dafny shape for this localService's config
    into the corresponding Smithy-modelled shape.
    '''
    return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_CryptoConfig(dafny_config)

def smithy_config_to_dafny_config(smithy_config):
    '''
    Converts the provided Smithy-modelled shape for this localService's config
    into the corresponding Dafny shape.
    '''
    return aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_CryptoConfig(smithy_config)
