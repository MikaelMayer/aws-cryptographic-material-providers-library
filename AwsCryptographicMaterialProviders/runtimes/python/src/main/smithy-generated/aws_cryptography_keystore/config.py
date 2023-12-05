# Code generated by smithy-python-codegen DO NOT EDIT.

import aws_cryptography_keystore.smithygenerated.aws_cryptography_keystore.dafny_to_smithy
import aws_cryptography_keystore.smithygenerated.aws_cryptography_keystore.smithy_to_dafny
from dataclasses import dataclass
import module_
from software_amazon_cryptography_keystore_internaldafny_types import (
    KeyStoreConfig_KeyStoreConfig as DafnyKeyStoreConfig,
)
from typing import Any, Callable, TypeAlias, Union

from .dafnyImplInterface import DafnyImplInterface
from aws_cryptography_materialproviders.smithygenerated.models import (
    DecryptMaterialsInput,
    DecryptMaterialsOutput,
    DeleteCacheEntryInput,
    GetBranchKeyIdInput,
    GetBranchKeyIdOutput,
    GetCacheEntryInput,
    GetCacheEntryOutput,
    GetClientInput,
    GetClientOutput,
    GetEncryptionMaterialsInput,
    GetEncryptionMaterialsOutput,
    OnDecryptInput,
    OnDecryptOutput,
    OnEncryptInput,
    OnEncryptOutput,
    PutCacheEntryInput,
    UpdateUsageMetadataInput,
)
from smithy_python._private.retries import SimpleRetryStrategy
from smithy_python.interfaces.interceptor import Interceptor
from smithy_python.interfaces.retries import RetryStrategy

from .models import (
    CreateKeyInput,
    CreateKeyOutput,
    CreateKeyStoreInput,
    CreateKeyStoreOutput,
    GetActiveBranchKeyInput,
    GetActiveBranchKeyOutput,
    GetBeaconKeyInput,
    GetBeaconKeyOutput,
    GetBranchKeyVersionInput,
    GetBranchKeyVersionOutput,
    GetKeyStoreInfoOutput,
    Unit,
    VersionKeyInput,
    VersionKeyOutput,
)


_ServiceInterceptor = Union[Interceptor[CreateKeyInput, CreateKeyOutput, Any, Any], Interceptor[CreateKeyStoreInput, CreateKeyStoreOutput, Any, Any], Interceptor[GetActiveBranchKeyInput, GetActiveBranchKeyOutput, Any, Any], Interceptor[GetBeaconKeyInput, GetBeaconKeyOutput, Any, Any], Interceptor[GetBranchKeyVersionInput, GetBranchKeyVersionOutput, Any, Any], Interceptor[Unit, GetKeyStoreInfoOutput, Any, Any], Interceptor[VersionKeyInput, VersionKeyOutput, Any, Any], Interceptor[DecryptMaterialsInput, DecryptMaterialsOutput, Any, Any], Interceptor[DeleteCacheEntryInput, Unit, Any, Any], Interceptor[GetBranchKeyIdInput, GetBranchKeyIdOutput, Any, Any], Interceptor[GetCacheEntryInput, GetCacheEntryOutput, Any, Any], Interceptor[GetClientInput, GetClientOutput, Any, Any], Interceptor[GetEncryptionMaterialsInput, GetEncryptionMaterialsOutput, Any, Any], Interceptor[OnDecryptInput, OnDecryptOutput, Any, Any], Interceptor[OnEncryptInput, OnEncryptOutput, Any, Any], Interceptor[PutCacheEntryInput, Unit, Any, Any], Interceptor[UpdateUsageMetadataInput, Unit, Any, Any]]
@dataclass(init=False)
class Config:
    """Configuration for KeyStore."""

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

class KeyStoreConfig(Config):
    '''
    Smithy-modelled localService Config shape for this localService.
    '''
    # TODO-Python: Add types to Config members
    ddb_table_name: Any
    kms_configuration: Any
    logical_key_store_name: Any
    id: Any
    grant_tokens: Any
    ddb_client: Any
    kms_client: Any

    def __init__(self, ddb_table_name, kms_configuration, logical_key_store_name, id, grant_tokens, ddb_client, kms_client, ):
        super().__init__()
        self.ddb_table_name = ddb_table_name
        self.kms_configuration = kms_configuration
        self.logical_key_store_name = logical_key_store_name
        self.id = id
        self.grant_tokens = grant_tokens
        self.ddb_client = ddb_client
        self.kms_client = kms_client

def dafny_config_to_smithy_config(dafny_config) -> KeyStoreConfig:
    '''
    Converts the provided Dafny shape for this localService's config
    into the corresponding Smithy-modelled shape.
    '''
    return aws_cryptography_keystore.smithygenerated.aws_cryptography_keystore.dafny_to_smithy.DafnyToSmithy_aws_cryptography_keystore_KeyStoreConfig(dafny_config)

def smithy_config_to_dafny_config(smithy_config) -> DafnyKeyStoreConfig:
    '''
    Converts the provided Smithy-modelled shape for this localService's config
    into the corresponding Dafny shape.
    '''
    return aws_cryptography_keystore.smithygenerated.aws_cryptography_keystore.smithy_to_dafny.SmithyToDafny_aws_cryptography_keystore_KeyStoreConfig(smithy_config)
