import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types

assert "software_amazon_cryptography_materialproviders_internaldafny_types" == __name__
software_amazon_cryptography_materialproviders_internaldafny_types = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsValid__CountingNumber(x):
        return (1) <= (x)

    @staticmethod
    def IsValid__PositiveInteger(x):
        return (0) <= (x)

    @staticmethod
    def IsValid__PositiveLong(x):
        return (0) <= (x)


class DafnyCallEvent:
    @classmethod
    def default(cls, default_I, default_O):
        return lambda: DafnyCallEvent_DafnyCallEvent(default_I(), default_O())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DafnyCallEvent(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DafnyCallEvent_DafnyCallEvent)

class DafnyCallEvent_DafnyCallEvent(DafnyCallEvent, NamedTuple('DafnyCallEvent', [('input', Any), ('output', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DafnyCallEvent.DafnyCallEvent({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DafnyCallEvent_DafnyCallEvent) and self.input == __o.input and self.output == __o.output
    def __hash__(self) -> int:
        return super().__hash__()


class AesWrappingAlg:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16(), AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16(), AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16()]
    @classmethod
    def default(cls, ):
        return lambda: AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ALG__AES128__GCM__IV12__TAG16(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16)
    @property
    def is_ALG__AES192__GCM__IV12__TAG16(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16)
    @property
    def is_ALG__AES256__GCM__IV12__TAG16(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16)

class AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16(AesWrappingAlg, NamedTuple('ALG__AES128__GCM__IV12__TAG16', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.ALG_AES128_GCM_IV12_TAG16'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16)
    def __hash__(self) -> int:
        return super().__hash__()

class AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16(AesWrappingAlg, NamedTuple('ALG__AES192__GCM__IV12__TAG16', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.ALG_AES192_GCM_IV12_TAG16'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16)
    def __hash__(self) -> int:
        return super().__hash__()

class AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16(AesWrappingAlg, NamedTuple('ALG__AES256__GCM__IV12__TAG16', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16)
    def __hash__(self) -> int:
        return super().__hash__()


class AlgorithmSuiteId:
    @classmethod
    def default(cls, ):
        return lambda: AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ESDK(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK)
    @property
    def is_DBE(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE)

class AlgorithmSuiteId_ESDK(AlgorithmSuiteId, NamedTuple('ESDK', [('ESDK', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId.ESDK({_dafny.string_of(self.ESDK)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK) and self.ESDK == __o.ESDK
    def __hash__(self) -> int:
        return super().__hash__()

class AlgorithmSuiteId_DBE(AlgorithmSuiteId, NamedTuple('DBE', [('DBE', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId.DBE({_dafny.string_of(self.DBE)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE) and self.DBE == __o.DBE
    def __hash__(self) -> int:
        return super().__hash__()


class AlgorithmSuiteInfo:
    @classmethod
    def default(cls, ):
        return lambda: AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK.default()(), _dafny.Seq({}), int(0), software_amazon_cryptography_materialproviders_internaldafny_types.Encrypt_AES__GCM.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_HKDF.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_HKDF.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_HMAC.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AlgorithmSuiteInfo(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo)

class AlgorithmSuiteInfo_AlgorithmSuiteInfo(AlgorithmSuiteInfo, NamedTuple('AlgorithmSuiteInfo', [('id', Any), ('binaryId', Any), ('messageVersion', Any), ('encrypt', Any), ('kdf', Any), ('commitment', Any), ('signature', Any), ('symmetricSignature', Any), ('edkWrapping', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo.AlgorithmSuiteInfo({_dafny.string_of(self.id)}, {_dafny.string_of(self.binaryId)}, {_dafny.string_of(self.messageVersion)}, {_dafny.string_of(self.encrypt)}, {_dafny.string_of(self.kdf)}, {_dafny.string_of(self.commitment)}, {_dafny.string_of(self.signature)}, {_dafny.string_of(self.symmetricSignature)}, {_dafny.string_of(self.edkWrapping)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo) and self.id == __o.id and self.binaryId == __o.binaryId and self.messageVersion == __o.messageVersion and self.encrypt == __o.encrypt and self.kdf == __o.kdf and self.commitment == __o.commitment and self.signature == __o.signature and self.symmetricSignature == __o.symmetricSignature and self.edkWrapping == __o.edkWrapping
    def __hash__(self) -> int:
        return super().__hash__()


class IAwsCryptographicMaterialProvidersClientCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClientCallHistory"

class IAwsCryptographicMaterialProvidersClient:
    pass
    def CreateAwsKmsKeyring(self, input):
        pass

    def CreateAwsKmsDiscoveryKeyring(self, input):
        pass

    def CreateAwsKmsMultiKeyring(self, input):
        pass

    def CreateAwsKmsDiscoveryMultiKeyring(self, input):
        pass

    def CreateAwsKmsMrkKeyring(self, input):
        pass

    def CreateAwsKmsMrkMultiKeyring(self, input):
        pass

    def CreateAwsKmsMrkDiscoveryKeyring(self, input):
        pass

    def CreateAwsKmsMrkDiscoveryMultiKeyring(self, input):
        pass

    def CreateAwsKmsHierarchicalKeyring(self, input):
        pass

    def CreateMultiKeyring(self, input):
        pass

    def CreateRawAesKeyring(self, input):
        pass

    def CreateRawRsaKeyring(self, input):
        pass

    def CreateAwsKmsRsaKeyring(self, input):
        pass

    def CreateDefaultCryptographicMaterialsManager(self, input):
        pass

    def CreateRequiredEncryptionContextCMM(self, input):
        pass

    def CreateCryptographicMaterialsCache(self, input):
        pass

    def CreateDefaultClientSupplier(self, input):
        pass


class IBranchKeyIdSupplierCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.IBranchKeyIdSupplierCallHistory"

class IBranchKeyIdSupplier:
    pass
    @staticmethod
    def GetBranchKeyId(self, input):
        pass

    @staticmethod
    def GetBranchKeyId(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput.default())()
        out0_: Wrappers.Result
        out0_ = (self).GetBranchKeyId_k(input)
        output = out0_
        return output

    def GetBranchKeyId_k(self, input):
        pass


class CacheType:
    @classmethod
    def default(cls, ):
        return lambda: CacheType_Default(software_amazon_cryptography_materialproviders_internaldafny_types.DefaultCache_DefaultCache.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Default(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_Default)
    @property
    def is_No(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_No)
    @property
    def is_SingleThreaded(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_SingleThreaded)
    @property
    def is_MultiThreaded(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_MultiThreaded)
    @property
    def is_StormTracking(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_StormTracking)

class CacheType_Default(CacheType, NamedTuple('Default', [('Default', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.Default({_dafny.string_of(self.Default)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_Default) and self.Default == __o.Default
    def __hash__(self) -> int:
        return super().__hash__()

class CacheType_No(CacheType, NamedTuple('No', [('No', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.No({_dafny.string_of(self.No)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_No) and self.No == __o.No
    def __hash__(self) -> int:
        return super().__hash__()

class CacheType_SingleThreaded(CacheType, NamedTuple('SingleThreaded', [('SingleThreaded', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.SingleThreaded({_dafny.string_of(self.SingleThreaded)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_SingleThreaded) and self.SingleThreaded == __o.SingleThreaded
    def __hash__(self) -> int:
        return super().__hash__()

class CacheType_MultiThreaded(CacheType, NamedTuple('MultiThreaded', [('MultiThreaded', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.MultiThreaded({_dafny.string_of(self.MultiThreaded)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_MultiThreaded) and self.MultiThreaded == __o.MultiThreaded
    def __hash__(self) -> int:
        return super().__hash__()

class CacheType_StormTracking(CacheType, NamedTuple('StormTracking', [('StormTracking', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CacheType.StormTracking({_dafny.string_of(self.StormTracking)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_StormTracking) and self.StormTracking == __o.StormTracking
    def __hash__(self) -> int:
        return super().__hash__()


class IClientSupplierCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.IClientSupplierCallHistory"

class IClientSupplier:
    pass
    @staticmethod
    def GetClient(self, input):
        pass

    @staticmethod
    def GetClient(self, input):
        output: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = (self).GetClient_k(input)
        output = out1_
        return output

    def GetClient_k(self, input):
        pass


class CommitmentPolicy:
    @classmethod
    def default(cls, ):
        return lambda: CommitmentPolicy_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ESDK(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK)
    @property
    def is_DBE(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_DBE)

class CommitmentPolicy_ESDK(CommitmentPolicy, NamedTuple('ESDK', [('ESDK', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CommitmentPolicy.ESDK({_dafny.string_of(self.ESDK)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK) and self.ESDK == __o.ESDK
    def __hash__(self) -> int:
        return super().__hash__()

class CommitmentPolicy_DBE(CommitmentPolicy, NamedTuple('DBE', [('DBE', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CommitmentPolicy.DBE({_dafny.string_of(self.DBE)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_DBE) and self.DBE == __o.DBE
    def __hash__(self) -> int:
        return super().__hash__()


class CountingNumber:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class CreateAwsKmsDiscoveryKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput(None, Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsDiscoveryKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput)

class CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput(CreateAwsKmsDiscoveryKeyringInput, NamedTuple('CreateAwsKmsDiscoveryKeyringInput', [('kmsClient', Any), ('discoveryFilter', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsDiscoveryKeyringInput.CreateAwsKmsDiscoveryKeyringInput({_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.discoveryFilter)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput) and self.kmsClient == __o.kmsClient and self.discoveryFilter == __o.discoveryFilter and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsDiscoveryMultiKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput(_dafny.Seq({}), Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsDiscoveryMultiKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput)

class CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput(CreateAwsKmsDiscoveryMultiKeyringInput, NamedTuple('CreateAwsKmsDiscoveryMultiKeyringInput', [('regions', Any), ('discoveryFilter', Any), ('clientSupplier', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsDiscoveryMultiKeyringInput.CreateAwsKmsDiscoveryMultiKeyringInput({_dafny.string_of(self.regions)}, {_dafny.string_of(self.discoveryFilter)}, {_dafny.string_of(self.clientSupplier)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput) and self.regions == __o.regions and self.discoveryFilter == __o.discoveryFilter and self.clientSupplier == __o.clientSupplier and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsHierarchicalKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), None, int(0), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsHierarchicalKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput)

class CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(CreateAwsKmsHierarchicalKeyringInput, NamedTuple('CreateAwsKmsHierarchicalKeyringInput', [('branchKeyId', Any), ('branchKeyIdSupplier', Any), ('keyStore', Any), ('ttlSeconds', Any), ('cache', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput.CreateAwsKmsHierarchicalKeyringInput({_dafny.string_of(self.branchKeyId)}, {_dafny.string_of(self.branchKeyIdSupplier)}, {_dafny.string_of(self.keyStore)}, {_dafny.string_of(self.ttlSeconds)}, {_dafny.string_of(self.cache)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput) and self.branchKeyId == __o.branchKeyId and self.branchKeyIdSupplier == __o.branchKeyIdSupplier and self.keyStore == __o.keyStore and self.ttlSeconds == __o.ttlSeconds and self.cache == __o.cache
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(_dafny.Seq({}), None, Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput)

class CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(CreateAwsKmsKeyringInput, NamedTuple('CreateAwsKmsKeyringInput', [('kmsKeyId', Any), ('kmsClient', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput.CreateAwsKmsKeyringInput({_dafny.string_of(self.kmsKeyId)}, {_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput) and self.kmsKeyId == __o.kmsKeyId and self.kmsClient == __o.kmsClient and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsMrkDiscoveryKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput(None, Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsMrkDiscoveryKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput)

class CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput(CreateAwsKmsMrkDiscoveryKeyringInput, NamedTuple('CreateAwsKmsMrkDiscoveryKeyringInput', [('kmsClient', Any), ('discoveryFilter', Any), ('grantTokens', Any), ('region', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryKeyringInput.CreateAwsKmsMrkDiscoveryKeyringInput({_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.discoveryFilter)}, {_dafny.string_of(self.grantTokens)}, {_dafny.string_of(self.region)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput) and self.kmsClient == __o.kmsClient and self.discoveryFilter == __o.discoveryFilter and self.grantTokens == __o.grantTokens and self.region == __o.region
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsMrkDiscoveryMultiKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(_dafny.Seq({}), Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsMrkDiscoveryMultiKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput)

class CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(CreateAwsKmsMrkDiscoveryMultiKeyringInput, NamedTuple('CreateAwsKmsMrkDiscoveryMultiKeyringInput', [('regions', Any), ('discoveryFilter', Any), ('clientSupplier', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput.CreateAwsKmsMrkDiscoveryMultiKeyringInput({_dafny.string_of(self.regions)}, {_dafny.string_of(self.discoveryFilter)}, {_dafny.string_of(self.clientSupplier)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput) and self.regions == __o.regions and self.discoveryFilter == __o.discoveryFilter and self.clientSupplier == __o.clientSupplier and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsMrkKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(_dafny.Seq({}), None, Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsMrkKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput)

class CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(CreateAwsKmsMrkKeyringInput, NamedTuple('CreateAwsKmsMrkKeyringInput', [('kmsKeyId', Any), ('kmsClient', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput.CreateAwsKmsMrkKeyringInput({_dafny.string_of(self.kmsKeyId)}, {_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput) and self.kmsKeyId == __o.kmsKeyId and self.kmsClient == __o.kmsClient and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsMrkMultiKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput(Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsMrkMultiKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput)

class CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput(CreateAwsKmsMrkMultiKeyringInput, NamedTuple('CreateAwsKmsMrkMultiKeyringInput', [('generator', Any), ('kmsKeyIds', Any), ('clientSupplier', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkMultiKeyringInput.CreateAwsKmsMrkMultiKeyringInput({_dafny.string_of(self.generator)}, {_dafny.string_of(self.kmsKeyIds)}, {_dafny.string_of(self.clientSupplier)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput) and self.generator == __o.generator and self.kmsKeyIds == __o.kmsKeyIds and self.clientSupplier == __o.clientSupplier and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsMultiKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput(Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsMultiKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput)

class CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput(CreateAwsKmsMultiKeyringInput, NamedTuple('CreateAwsKmsMultiKeyringInput', [('generator', Any), ('kmsKeyIds', Any), ('clientSupplier', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMultiKeyringInput.CreateAwsKmsMultiKeyringInput({_dafny.string_of(self.generator)}, {_dafny.string_of(self.kmsKeyIds)}, {_dafny.string_of(self.clientSupplier)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput) and self.generator == __o.generator and self.kmsKeyIds == __o.kmsKeyIds and self.clientSupplier == __o.clientSupplier and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateAwsKmsRsaKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_None.default()(), _dafny.Seq({}), software_amazon_cryptography_services_kms_internaldafny_types.EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateAwsKmsRsaKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput)

class CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(CreateAwsKmsRsaKeyringInput, NamedTuple('CreateAwsKmsRsaKeyringInput', [('publicKey', Any), ('kmsKeyId', Any), ('encryptionAlgorithm', Any), ('kmsClient', Any), ('grantTokens', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput.CreateAwsKmsRsaKeyringInput({_dafny.string_of(self.publicKey)}, {_dafny.string_of(self.kmsKeyId)}, {_dafny.string_of(self.encryptionAlgorithm)}, {_dafny.string_of(self.kmsClient)}, {_dafny.string_of(self.grantTokens)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput) and self.publicKey == __o.publicKey and self.kmsKeyId == __o.kmsKeyId and self.encryptionAlgorithm == __o.encryptionAlgorithm and self.kmsClient == __o.kmsClient and self.grantTokens == __o.grantTokens
    def __hash__(self) -> int:
        return super().__hash__()


class CreateCryptographicMaterialsCacheInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(software_amazon_cryptography_materialproviders_internaldafny_types.CacheType_Default.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateCryptographicMaterialsCacheInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput)

class CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput(CreateCryptographicMaterialsCacheInput, NamedTuple('CreateCryptographicMaterialsCacheInput', [('cache', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateCryptographicMaterialsCacheInput.CreateCryptographicMaterialsCacheInput({_dafny.string_of(self.cache)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput) and self.cache == __o.cache
    def __hash__(self) -> int:
        return super().__hash__()


class CreateDefaultClientSupplierInput:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput()]
    @classmethod
    def default(cls, ):
        return lambda: CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateDefaultClientSupplierInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput)

class CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput(CreateDefaultClientSupplierInput, NamedTuple('CreateDefaultClientSupplierInput', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput.CreateDefaultClientSupplierInput'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput)
    def __hash__(self) -> int:
        return super().__hash__()


class CreateDefaultCryptographicMaterialsManagerInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(None)
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateDefaultCryptographicMaterialsManagerInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput)

class CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput(CreateDefaultCryptographicMaterialsManagerInput, NamedTuple('CreateDefaultCryptographicMaterialsManagerInput', [('keyring', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateDefaultCryptographicMaterialsManagerInput.CreateDefaultCryptographicMaterialsManagerInput({_dafny.string_of(self.keyring)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput) and self.keyring == __o.keyring
    def __hash__(self) -> int:
        return super().__hash__()


class CreateMultiKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateMultiKeyringInput_CreateMultiKeyringInput(Wrappers.Option_None.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateMultiKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput)

class CreateMultiKeyringInput_CreateMultiKeyringInput(CreateMultiKeyringInput, NamedTuple('CreateMultiKeyringInput', [('generator', Any), ('childKeyrings', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput.CreateMultiKeyringInput({_dafny.string_of(self.generator)}, {_dafny.string_of(self.childKeyrings)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateMultiKeyringInput_CreateMultiKeyringInput) and self.generator == __o.generator and self.childKeyrings == __o.childKeyrings
    def __hash__(self) -> int:
        return super().__hash__()


class CreateRawAesKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateRawAesKeyringInput_CreateRawAesKeyringInput(_dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateRawAesKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput)

class CreateRawAesKeyringInput_CreateRawAesKeyringInput(CreateRawAesKeyringInput, NamedTuple('CreateRawAesKeyringInput', [('keyNamespace', Any), ('keyName', Any), ('wrappingKey', Any), ('wrappingAlg', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput.CreateRawAesKeyringInput({_dafny.string_of(self.keyNamespace)}, {_dafny.string_of(self.keyName)}, {_dafny.string_of(self.wrappingKey)}, {_dafny.string_of(self.wrappingAlg)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawAesKeyringInput_CreateRawAesKeyringInput) and self.keyNamespace == __o.keyNamespace and self.keyName == __o.keyName and self.wrappingKey == __o.wrappingKey and self.wrappingAlg == __o.wrappingAlg
    def __hash__(self) -> int:
        return super().__hash__()


class CreateRawRsaKeyringInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(_dafny.Seq({}), _dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_PKCS1.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateRawRsaKeyringInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput)

class CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(CreateRawRsaKeyringInput, NamedTuple('CreateRawRsaKeyringInput', [('keyNamespace', Any), ('keyName', Any), ('paddingScheme', Any), ('publicKey', Any), ('privateKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput.CreateRawRsaKeyringInput({_dafny.string_of(self.keyNamespace)}, {_dafny.string_of(self.keyName)}, {_dafny.string_of(self.paddingScheme)}, {_dafny.string_of(self.publicKey)}, {_dafny.string_of(self.privateKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput) and self.keyNamespace == __o.keyNamespace and self.keyName == __o.keyName and self.paddingScheme == __o.paddingScheme and self.publicKey == __o.publicKey and self.privateKey == __o.privateKey
    def __hash__(self) -> int:
        return super().__hash__()


class CreateRequiredEncryptionContextCMMInput:
    @classmethod
    def default(cls, ):
        return lambda: CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput(Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CreateRequiredEncryptionContextCMMInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput)

class CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput(CreateRequiredEncryptionContextCMMInput, NamedTuple('CreateRequiredEncryptionContextCMMInput', [('underlyingCMM', Any), ('keyring', Any), ('requiredEncryptionContextKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.CreateRequiredEncryptionContextCMMInput.CreateRequiredEncryptionContextCMMInput({_dafny.string_of(self.underlyingCMM)}, {_dafny.string_of(self.keyring)}, {_dafny.string_of(self.requiredEncryptionContextKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput) and self.underlyingCMM == __o.underlyingCMM and self.keyring == __o.keyring and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys
    def __hash__(self) -> int:
        return super().__hash__()


class ICryptographicMaterialsCacheCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCacheCallHistory"

class ICryptographicMaterialsCache:
    pass
    @staticmethod
    def PutCacheEntry(self, input):
        pass

    @staticmethod
    def PutCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out2_: Wrappers.Result
        out2_ = (self).PutCacheEntry_k(input)
        output = out2_
        return output

    def PutCacheEntry_k(self, input):
        pass

    @staticmethod
    def UpdateUsageMetadata(self, input):
        pass

    @staticmethod
    def UpdateUsageMetadata(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out3_: Wrappers.Result
        out3_ = (self).UpdateUsageMetadata_k(input)
        output = out3_
        return output

    def UpdateUsageMetadata_k(self, input):
        pass

    @staticmethod
    def GetCacheEntry(self, input):
        pass

    @staticmethod
    def GetCacheEntry(self, input):
        output: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = (self).GetCacheEntry_k(input)
        output = out4_
        return output

    def GetCacheEntry_k(self, input):
        pass

    @staticmethod
    def DeleteCacheEntry(self, input):
        pass

    @staticmethod
    def DeleteCacheEntry(self, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out5_: Wrappers.Result
        out5_ = (self).DeleteCacheEntry_k(input)
        output = out5_
        return output

    def DeleteCacheEntry_k(self, input):
        pass


class ICryptographicMaterialsManagerCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManagerCallHistory"

class ICryptographicMaterialsManager:
    pass
    @staticmethod
    def GetEncryptionMaterials(self, input):
        pass

    @staticmethod
    def GetEncryptionMaterials(self, input):
        output: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = (self).GetEncryptionMaterials_k(input)
        output = out6_
        return output

    def GetEncryptionMaterials_k(self, input):
        pass

    @staticmethod
    def DecryptMaterials(self, input):
        pass

    @staticmethod
    def DecryptMaterials(self, input):
        output: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = (self).DecryptMaterials_k(input)
        output = out7_
        return output

    def DecryptMaterials_k(self, input):
        pass


class DBEAlgorithmSuiteId:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(), DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()]
    @classmethod
    def default(cls, ):
        return lambda: DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384)
    @property
    def is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384)

class DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(DBEAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384)
    def __hash__(self) -> int:
        return super().__hash__()

class DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(DBEAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384_SYMSIG_HMAC_SHA384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384)
    def __hash__(self) -> int:
        return super().__hash__()


class DBECommitmentPolicy:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()]
    @classmethod
    def default(cls, ):
        return lambda: DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_REQUIRE__ENCRYPT__REQUIRE__DECRYPT(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT)

class DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT(DBECommitmentPolicy, NamedTuple('REQUIRE__ENCRYPT__REQUIRE__DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DBECommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DBECommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptionMaterials:
    @classmethod
    def default(cls, ):
        return lambda: DecryptionMaterials_DecryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo.default()(), _dafny.Map({}), _dafny.Seq({}), Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptionMaterials(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials)

class DecryptionMaterials_DecryptionMaterials(DecryptionMaterials, NamedTuple('DecryptionMaterials', [('algorithmSuite', Any), ('encryptionContext', Any), ('requiredEncryptionContextKeys', Any), ('plaintextDataKey', Any), ('verificationKey', Any), ('symmetricSigningKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DecryptionMaterials.DecryptionMaterials({_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.verificationKey)}, {_dafny.string_of(self.symmetricSigningKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials) and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.plaintextDataKey == __o.plaintextDataKey and self.verificationKey == __o.verificationKey and self.symmetricSigningKey == __o.symmetricSigningKey
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptMaterialsInput:
    @classmethod
    def default(cls, ):
        return lambda: DecryptMaterialsInput_DecryptMaterialsInput(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK.default()(), _dafny.Seq({}), _dafny.Map({}), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptMaterialsInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsInput_DecryptMaterialsInput)

class DecryptMaterialsInput_DecryptMaterialsInput(DecryptMaterialsInput, NamedTuple('DecryptMaterialsInput', [('algorithmSuiteId', Any), ('commitmentPolicy', Any), ('encryptedDataKeys', Any), ('encryptionContext', Any), ('reproducedEncryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DecryptMaterialsInput.DecryptMaterialsInput({_dafny.string_of(self.algorithmSuiteId)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.encryptedDataKeys)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.reproducedEncryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsInput_DecryptMaterialsInput) and self.algorithmSuiteId == __o.algorithmSuiteId and self.commitmentPolicy == __o.commitmentPolicy and self.encryptedDataKeys == __o.encryptedDataKeys and self.encryptionContext == __o.encryptionContext and self.reproducedEncryptionContext == __o.reproducedEncryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class DecryptMaterialsOutput:
    @classmethod
    def default(cls, ):
        return lambda: DecryptMaterialsOutput_DecryptMaterialsOutput(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DecryptMaterialsOutput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsOutput_DecryptMaterialsOutput)

class DecryptMaterialsOutput_DecryptMaterialsOutput(DecryptMaterialsOutput, NamedTuple('DecryptMaterialsOutput', [('decryptionMaterials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DecryptMaterialsOutput.DecryptMaterialsOutput({_dafny.string_of(self.decryptionMaterials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DecryptMaterialsOutput_DecryptMaterialsOutput) and self.decryptionMaterials == __o.decryptionMaterials
    def __hash__(self) -> int:
        return super().__hash__()


class DefaultCache:
    @classmethod
    def default(cls, ):
        return lambda: DefaultCache_DefaultCache(int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DefaultCache(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DefaultCache_DefaultCache)

class DefaultCache_DefaultCache(DefaultCache, NamedTuple('DefaultCache', [('entryCapacity', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DefaultCache.DefaultCache({_dafny.string_of(self.entryCapacity)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DefaultCache_DefaultCache) and self.entryCapacity == __o.entryCapacity
    def __hash__(self) -> int:
        return super().__hash__()


class DeleteCacheEntryInput:
    @classmethod
    def default(cls, ):
        return lambda: DeleteCacheEntryInput_DeleteCacheEntryInput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DeleteCacheEntryInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput)

class DeleteCacheEntryInput_DeleteCacheEntryInput(DeleteCacheEntryInput, NamedTuple('DeleteCacheEntryInput', [('identifier', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DeleteCacheEntryInput.DeleteCacheEntryInput({_dafny.string_of(self.identifier)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DeleteCacheEntryInput_DeleteCacheEntryInput) and self.identifier == __o.identifier
    def __hash__(self) -> int:
        return super().__hash__()


class DerivationAlgorithm:
    @classmethod
    def default(cls, ):
        return lambda: DerivationAlgorithm_HKDF(software_amazon_cryptography_materialproviders_internaldafny_types.HKDF_HKDF.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HKDF(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_HKDF)
    @property
    def is_IDENTITY(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY)
    @property
    def is_None(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None)

class DerivationAlgorithm_HKDF(DerivationAlgorithm, NamedTuple('HKDF', [('HKDF', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm.HKDF({_dafny.string_of(self.HKDF)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_HKDF) and self.HKDF == __o.HKDF
    def __hash__(self) -> int:
        return super().__hash__()

class DerivationAlgorithm_IDENTITY(DerivationAlgorithm, NamedTuple('IDENTITY', [('IDENTITY', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm.IDENTITY({_dafny.string_of(self.IDENTITY)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY) and self.IDENTITY == __o.IDENTITY
    def __hash__(self) -> int:
        return super().__hash__()

class DerivationAlgorithm_None(DerivationAlgorithm, NamedTuple('None_', [('None_', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm.None({_dafny.string_of(self.None_)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None) and self.None_ == __o.None_
    def __hash__(self) -> int:
        return super().__hash__()


class DIRECT__KEY__WRAPPING:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()]
    @classmethod
    def default(cls, ):
        return lambda: DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DIRECT__KEY__WRAPPING(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING)

class DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING(DIRECT__KEY__WRAPPING, NamedTuple('DIRECT__KEY__WRAPPING', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DIRECT_KEY_WRAPPING.DIRECT_KEY_WRAPPING'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING)
    def __hash__(self) -> int:
        return super().__hash__()


class DiscoveryFilter:
    @classmethod
    def default(cls, ):
        return lambda: DiscoveryFilter_DiscoveryFilter(_dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DiscoveryFilter(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter)

class DiscoveryFilter_DiscoveryFilter(DiscoveryFilter, NamedTuple('DiscoveryFilter', [('accountIds', Any), ('partition', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.DiscoveryFilter.DiscoveryFilter({_dafny.string_of(self.accountIds)}, {_dafny.string_of(self.partition)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter) and self.accountIds == __o.accountIds and self.partition == __o.partition
    def __hash__(self) -> int:
        return super().__hash__()


class ECDSA:
    @classmethod
    def default(cls, ):
        return lambda: ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECDSA(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA)

class ECDSA_ECDSA(ECDSA, NamedTuple('ECDSA', [('curve', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ECDSA.ECDSA({_dafny.string_of(self.curve)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA) and self.curve == __o.curve
    def __hash__(self) -> int:
        return super().__hash__()


class EdkWrappingAlgorithm:
    @classmethod
    def default(cls, ):
        return lambda: EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_DIRECT__KEY__WRAPPING(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING)
    @property
    def is_IntermediateKeyWrapping(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_IntermediateKeyWrapping)

class EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(EdkWrappingAlgorithm, NamedTuple('DIRECT__KEY__WRAPPING', [('DIRECT__KEY__WRAPPING', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm.DIRECT_KEY_WRAPPING({_dafny.string_of(self.DIRECT__KEY__WRAPPING)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING) and self.DIRECT__KEY__WRAPPING == __o.DIRECT__KEY__WRAPPING
    def __hash__(self) -> int:
        return super().__hash__()

class EdkWrappingAlgorithm_IntermediateKeyWrapping(EdkWrappingAlgorithm, NamedTuple('IntermediateKeyWrapping', [('IntermediateKeyWrapping', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm.IntermediateKeyWrapping({_dafny.string_of(self.IntermediateKeyWrapping)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_IntermediateKeyWrapping) and self.IntermediateKeyWrapping == __o.IntermediateKeyWrapping
    def __hash__(self) -> int:
        return super().__hash__()


class Encrypt:
    @classmethod
    def default(cls, ):
        return lambda: Encrypt_AES__GCM(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AES__GCM(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Encrypt_AES__GCM)

class Encrypt_AES__GCM(Encrypt, NamedTuple('AES__GCM', [('AES__GCM', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Encrypt.AES_GCM({_dafny.string_of(self.AES__GCM)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Encrypt_AES__GCM) and self.AES__GCM == __o.AES__GCM
    def __hash__(self) -> int:
        return super().__hash__()


class EncryptedDataKey:
    @classmethod
    def default(cls, ):
        return lambda: EncryptedDataKey_EncryptedDataKey(UTF8.ValidUTF8Bytes.default(), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EncryptedDataKey(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey)

class EncryptedDataKey_EncryptedDataKey(EncryptedDataKey, NamedTuple('EncryptedDataKey', [('keyProviderId', Any), ('keyProviderInfo', Any), ('ciphertext', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.EncryptedDataKey.EncryptedDataKey({_dafny.string_of(self.keyProviderId)}, {_dafny.string_of(self.keyProviderInfo)}, {_dafny.string_of(self.ciphertext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey) and self.keyProviderId == __o.keyProviderId and self.keyProviderInfo == __o.keyProviderInfo and self.ciphertext == __o.ciphertext
    def __hash__(self) -> int:
        return super().__hash__()


class EncryptionMaterials:
    @classmethod
    def default(cls, ):
        return lambda: EncryptionMaterials_EncryptionMaterials(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo.default()(), _dafny.Map({}), _dafny.Seq({}), _dafny.Seq({}), Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EncryptionMaterials(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials)

class EncryptionMaterials_EncryptionMaterials(EncryptionMaterials, NamedTuple('EncryptionMaterials', [('algorithmSuite', Any), ('encryptionContext', Any), ('encryptedDataKeys', Any), ('requiredEncryptionContextKeys', Any), ('plaintextDataKey', Any), ('signingKey', Any), ('symmetricSigningKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.EncryptionMaterials.EncryptionMaterials({_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.encryptedDataKeys)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.plaintextDataKey)}, {_dafny.string_of(self.signingKey)}, {_dafny.string_of(self.symmetricSigningKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials) and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext and self.encryptedDataKeys == __o.encryptedDataKeys and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.plaintextDataKey == __o.plaintextDataKey and self.signingKey == __o.signingKey and self.symmetricSigningKeys == __o.symmetricSigningKeys
    def __hash__(self) -> int:
        return super().__hash__()


class ESDKAlgorithmSuiteId:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(), ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(), ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(), ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(), ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(), ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(), ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(), ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(), ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(), ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(), ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()]
    @classmethod
    def default(cls, ):
        return lambda: ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF)
    @property
    def is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF)
    @property
    def is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF)
    @property
    def is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256)
    @property
    def is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256)
    @property
    def is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256)
    @property
    def is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256)
    @property
    def is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384)
    @property
    def is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384)
    @property
    def is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY)
    @property
    def is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384)

class ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__128__GCM__IV12__TAG16__NO__KDF', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_NO_KDF'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__192__GCM__IV12__TAG16__NO__KDF', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_NO_KDF'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__IV12__TAG16__NO__KDF', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_NO_KDF'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256_ECDSA_P256'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(ESDKAlgorithmSuiteId, NamedTuple('ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384)
    def __hash__(self) -> int:
        return super().__hash__()


class ESDKCommitmentPolicy:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT(), ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT(), ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT()]
    @classmethod
    def default(cls, ):
        return lambda: ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_FORBID__ENCRYPT__ALLOW__DECRYPT(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT)
    @property
    def is_REQUIRE__ENCRYPT__ALLOW__DECRYPT(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT)
    @property
    def is_REQUIRE__ENCRYPT__REQUIRE__DECRYPT(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT)

class ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT(ESDKCommitmentPolicy, NamedTuple('FORBID__ENCRYPT__ALLOW__DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKCommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_FORBID__ENCRYPT__ALLOW__DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT(ESDKCommitmentPolicy, NamedTuple('REQUIRE__ENCRYPT__ALLOW__DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKCommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_REQUIRE__ENCRYPT__ALLOW__DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()

class ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT(ESDKCommitmentPolicy, NamedTuple('REQUIRE__ENCRYPT__REQUIRE__DECRYPT', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ESDKCommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKCommitmentPolicy_REQUIRE__ENCRYPT__REQUIRE__DECRYPT)
    def __hash__(self) -> int:
        return super().__hash__()


class GetBranchKeyIdInput:
    @classmethod
    def default(cls, ):
        return lambda: GetBranchKeyIdInput_GetBranchKeyIdInput(_dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetBranchKeyIdInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdInput_GetBranchKeyIdInput)

class GetBranchKeyIdInput_GetBranchKeyIdInput(GetBranchKeyIdInput, NamedTuple('GetBranchKeyIdInput', [('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput.GetBranchKeyIdInput({_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdInput_GetBranchKeyIdInput) and self.encryptionContext == __o.encryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class GetBranchKeyIdOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetBranchKeyIdOutput_GetBranchKeyIdOutput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetBranchKeyIdOutput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput_GetBranchKeyIdOutput)

class GetBranchKeyIdOutput_GetBranchKeyIdOutput(GetBranchKeyIdOutput, NamedTuple('GetBranchKeyIdOutput', [('branchKeyId', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.GetBranchKeyIdOutput({_dafny.string_of(self.branchKeyId)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput_GetBranchKeyIdOutput) and self.branchKeyId == __o.branchKeyId
    def __hash__(self) -> int:
        return super().__hash__()


class GetCacheEntryInput:
    @classmethod
    def default(cls, ):
        return lambda: GetCacheEntryInput_GetCacheEntryInput(_dafny.Seq({}), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetCacheEntryInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput)

class GetCacheEntryInput_GetCacheEntryInput(GetCacheEntryInput, NamedTuple('GetCacheEntryInput', [('identifier', Any), ('bytesUsed', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput.GetCacheEntryInput({_dafny.string_of(self.identifier)}, {_dafny.string_of(self.bytesUsed)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput) and self.identifier == __o.identifier and self.bytesUsed == __o.bytesUsed
    def __hash__(self) -> int:
        return super().__hash__()


class GetCacheEntryOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetCacheEntryOutput_GetCacheEntryOutput(software_amazon_cryptography_materialproviders_internaldafny_types.Materials_Encryption.default()(), int(0), int(0), int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetCacheEntryOutput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryOutput_GetCacheEntryOutput)

class GetCacheEntryOutput_GetCacheEntryOutput(GetCacheEntryOutput, NamedTuple('GetCacheEntryOutput', [('materials', Any), ('creationTime', Any), ('expiryTime', Any), ('messagesUsed', Any), ('bytesUsed', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetCacheEntryOutput.GetCacheEntryOutput({_dafny.string_of(self.materials)}, {_dafny.string_of(self.creationTime)}, {_dafny.string_of(self.expiryTime)}, {_dafny.string_of(self.messagesUsed)}, {_dafny.string_of(self.bytesUsed)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryOutput_GetCacheEntryOutput) and self.materials == __o.materials and self.creationTime == __o.creationTime and self.expiryTime == __o.expiryTime and self.messagesUsed == __o.messagesUsed and self.bytesUsed == __o.bytesUsed
    def __hash__(self) -> int:
        return super().__hash__()


class GetClientInput:
    @classmethod
    def default(cls, ):
        return lambda: GetClientInput_GetClientInput(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetClientInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput)

class GetClientInput_GetClientInput(GetClientInput, NamedTuple('GetClientInput', [('region', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetClientInput.GetClientInput({_dafny.string_of(self.region)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput) and self.region == __o.region
    def __hash__(self) -> int:
        return super().__hash__()


class GetEncryptionMaterialsInput:
    @classmethod
    def default(cls, ):
        return lambda: GetEncryptionMaterialsInput_GetEncryptionMaterialsInput(_dafny.Map({}), software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetEncryptionMaterialsInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput)

class GetEncryptionMaterialsInput_GetEncryptionMaterialsInput(GetEncryptionMaterialsInput, NamedTuple('GetEncryptionMaterialsInput', [('encryptionContext', Any), ('commitmentPolicy', Any), ('algorithmSuiteId', Any), ('maxPlaintextLength', Any), ('requiredEncryptionContextKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsInput.GetEncryptionMaterialsInput({_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.commitmentPolicy)}, {_dafny.string_of(self.algorithmSuiteId)}, {_dafny.string_of(self.maxPlaintextLength)}, {_dafny.string_of(self.requiredEncryptionContextKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsInput_GetEncryptionMaterialsInput) and self.encryptionContext == __o.encryptionContext and self.commitmentPolicy == __o.commitmentPolicy and self.algorithmSuiteId == __o.algorithmSuiteId and self.maxPlaintextLength == __o.maxPlaintextLength and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys
    def __hash__(self) -> int:
        return super().__hash__()


class GetEncryptionMaterialsOutput:
    @classmethod
    def default(cls, ):
        return lambda: GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GetEncryptionMaterialsOutput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput)

class GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput(GetEncryptionMaterialsOutput, NamedTuple('GetEncryptionMaterialsOutput', [('encryptionMaterials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.GetEncryptionMaterialsOutput.GetEncryptionMaterialsOutput({_dafny.string_of(self.encryptionMaterials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput) and self.encryptionMaterials == __o.encryptionMaterials
    def __hash__(self) -> int:
        return super().__hash__()


class HKDF:
    @classmethod
    def default(cls, ):
        return lambda: HKDF_HKDF(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512.default()(), int(0), int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HKDF(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.HKDF_HKDF)

class HKDF_HKDF(HKDF, NamedTuple('HKDF', [('hmac', Any), ('saltLength', Any), ('inputKeyLength', Any), ('outputKeyLength', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.HKDF.HKDF({_dafny.string_of(self.hmac)}, {_dafny.string_of(self.saltLength)}, {_dafny.string_of(self.inputKeyLength)}, {_dafny.string_of(self.outputKeyLength)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.HKDF_HKDF) and self.hmac == __o.hmac and self.saltLength == __o.saltLength and self.inputKeyLength == __o.inputKeyLength and self.outputKeyLength == __o.outputKeyLength
    def __hash__(self) -> int:
        return super().__hash__()


class IDENTITY:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [IDENTITY_IDENTITY()]
    @classmethod
    def default(cls, ):
        return lambda: IDENTITY_IDENTITY()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_IDENTITY(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY)

class IDENTITY_IDENTITY(IDENTITY, NamedTuple('IDENTITY', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.IDENTITY.IDENTITY'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY)
    def __hash__(self) -> int:
        return super().__hash__()


class InitializeDecryptionMaterialsInput:
    @classmethod
    def default(cls, ):
        return lambda: InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK.default()(), _dafny.Map({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_InitializeDecryptionMaterialsInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput)

class InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput(InitializeDecryptionMaterialsInput, NamedTuple('InitializeDecryptionMaterialsInput', [('algorithmSuiteId', Any), ('encryptionContext', Any), ('requiredEncryptionContextKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.InitializeDecryptionMaterialsInput.InitializeDecryptionMaterialsInput({_dafny.string_of(self.algorithmSuiteId)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.requiredEncryptionContextKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput) and self.algorithmSuiteId == __o.algorithmSuiteId and self.encryptionContext == __o.encryptionContext and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys
    def __hash__(self) -> int:
        return super().__hash__()


class InitializeEncryptionMaterialsInput:
    @classmethod
    def default(cls, ):
        return lambda: InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK.default()(), _dafny.Map({}), _dafny.Seq({}), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_InitializeEncryptionMaterialsInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput)

class InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput(InitializeEncryptionMaterialsInput, NamedTuple('InitializeEncryptionMaterialsInput', [('algorithmSuiteId', Any), ('encryptionContext', Any), ('requiredEncryptionContextKeys', Any), ('signingKey', Any), ('verificationKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.InitializeEncryptionMaterialsInput.InitializeEncryptionMaterialsInput({_dafny.string_of(self.algorithmSuiteId)}, {_dafny.string_of(self.encryptionContext)}, {_dafny.string_of(self.requiredEncryptionContextKeys)}, {_dafny.string_of(self.signingKey)}, {_dafny.string_of(self.verificationKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput) and self.algorithmSuiteId == __o.algorithmSuiteId and self.encryptionContext == __o.encryptionContext and self.requiredEncryptionContextKeys == __o.requiredEncryptionContextKeys and self.signingKey == __o.signingKey and self.verificationKey == __o.verificationKey
    def __hash__(self) -> int:
        return super().__hash__()


class IntermediateKeyWrapping:
    @classmethod
    def default(cls, ):
        return lambda: IntermediateKeyWrapping_IntermediateKeyWrapping(software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_HKDF.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_HKDF.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.Encrypt_AES__GCM.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_IntermediateKeyWrapping(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.IntermediateKeyWrapping_IntermediateKeyWrapping)

class IntermediateKeyWrapping_IntermediateKeyWrapping(IntermediateKeyWrapping, NamedTuple('IntermediateKeyWrapping', [('keyEncryptionKeyKdf', Any), ('macKeyKdf', Any), ('pdkEncryptAlgorithm', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.IntermediateKeyWrapping.IntermediateKeyWrapping({_dafny.string_of(self.keyEncryptionKeyKdf)}, {_dafny.string_of(self.macKeyKdf)}, {_dafny.string_of(self.pdkEncryptAlgorithm)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.IntermediateKeyWrapping_IntermediateKeyWrapping) and self.keyEncryptionKeyKdf == __o.keyEncryptionKeyKdf and self.macKeyKdf == __o.macKeyKdf and self.pdkEncryptAlgorithm == __o.pdkEncryptAlgorithm
    def __hash__(self) -> int:
        return super().__hash__()


class IKeyringCallHistory:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsCryptographyMaterialProvidersTypes.IKeyringCallHistory"

class IKeyring:
    pass
    @staticmethod
    def OnEncrypt(self, input):
        pass

    @staticmethod
    def OnEncrypt(self, input):
        output: Wrappers.Result = None
        out8_: Wrappers.Result
        out8_ = (self).OnEncrypt_k(input)
        output = out8_
        return output

    def OnEncrypt_k(self, input):
        pass

    @staticmethod
    def OnDecrypt(self, input):
        pass

    @staticmethod
    def OnDecrypt(self, input):
        output: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = (self).OnDecrypt_k(input)
        output = out9_
        return output

    def OnDecrypt_k(self, input):
        pass


class MaterialProvidersConfig:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [MaterialProvidersConfig_MaterialProvidersConfig()]
    @classmethod
    def default(cls, ):
        return lambda: MaterialProvidersConfig_MaterialProvidersConfig()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_MaterialProvidersConfig(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.MaterialProvidersConfig_MaterialProvidersConfig)

class MaterialProvidersConfig_MaterialProvidersConfig(MaterialProvidersConfig, NamedTuple('MaterialProvidersConfig', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.MaterialProvidersConfig.MaterialProvidersConfig'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.MaterialProvidersConfig_MaterialProvidersConfig)
    def __hash__(self) -> int:
        return super().__hash__()


class Materials:
    @classmethod
    def default(cls, ):
        return lambda: Materials_Encryption(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Encryption(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_Encryption)
    @property
    def is_Decryption(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_Decryption)
    @property
    def is_BranchKey(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey)
    @property
    def is_BeaconKey(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BeaconKey)

class Materials_Encryption(Materials, NamedTuple('Encryption', [('Encryption', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Materials.Encryption({_dafny.string_of(self.Encryption)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_Encryption) and self.Encryption == __o.Encryption
    def __hash__(self) -> int:
        return super().__hash__()

class Materials_Decryption(Materials, NamedTuple('Decryption', [('Decryption', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Materials.Decryption({_dafny.string_of(self.Decryption)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_Decryption) and self.Decryption == __o.Decryption
    def __hash__(self) -> int:
        return super().__hash__()

class Materials_BranchKey(Materials, NamedTuple('BranchKey', [('BranchKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Materials.BranchKey({_dafny.string_of(self.BranchKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey) and self.BranchKey == __o.BranchKey
    def __hash__(self) -> int:
        return super().__hash__()

class Materials_BeaconKey(Materials, NamedTuple('BeaconKey', [('BeaconKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Materials.BeaconKey({_dafny.string_of(self.BeaconKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BeaconKey) and self.BeaconKey == __o.BeaconKey
    def __hash__(self) -> int:
        return super().__hash__()


class MultiThreadedCache:
    @classmethod
    def default(cls, ):
        return lambda: MultiThreadedCache_MultiThreadedCache(int(0), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_MultiThreadedCache(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.MultiThreadedCache_MultiThreadedCache)

class MultiThreadedCache_MultiThreadedCache(MultiThreadedCache, NamedTuple('MultiThreadedCache', [('entryCapacity', Any), ('entryPruningTailSize', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.MultiThreadedCache.MultiThreadedCache({_dafny.string_of(self.entryCapacity)}, {_dafny.string_of(self.entryPruningTailSize)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.MultiThreadedCache_MultiThreadedCache) and self.entryCapacity == __o.entryCapacity and self.entryPruningTailSize == __o.entryPruningTailSize
    def __hash__(self) -> int:
        return super().__hash__()


class NoCache:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [NoCache_NoCache()]
    @classmethod
    def default(cls, ):
        return lambda: NoCache_NoCache()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_NoCache(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.NoCache_NoCache)

class NoCache_NoCache(NoCache, NamedTuple('NoCache', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.NoCache.NoCache'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.NoCache_NoCache)
    def __hash__(self) -> int:
        return super().__hash__()


class None_:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [None_None()]
    @classmethod
    def default(cls, ):
        return lambda: None_None()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_None(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.None_None)

class None_None(None_, NamedTuple('None_', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.None.None'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.None_None)
    def __hash__(self) -> int:
        return super().__hash__()


class OnDecryptInput:
    @classmethod
    def default(cls, ):
        return lambda: OnDecryptInput_OnDecryptInput(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials.default()(), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OnDecryptInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput)

class OnDecryptInput_OnDecryptInput(OnDecryptInput, NamedTuple('OnDecryptInput', [('materials', Any), ('encryptedDataKeys', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.OnDecryptInput.OnDecryptInput({_dafny.string_of(self.materials)}, {_dafny.string_of(self.encryptedDataKeys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptInput_OnDecryptInput) and self.materials == __o.materials and self.encryptedDataKeys == __o.encryptedDataKeys
    def __hash__(self) -> int:
        return super().__hash__()


class OnDecryptOutput:
    @classmethod
    def default(cls, ):
        return lambda: OnDecryptOutput_OnDecryptOutput(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OnDecryptOutput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput)

class OnDecryptOutput_OnDecryptOutput(OnDecryptOutput, NamedTuple('OnDecryptOutput', [('materials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.OnDecryptOutput.OnDecryptOutput({_dafny.string_of(self.materials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput) and self.materials == __o.materials
    def __hash__(self) -> int:
        return super().__hash__()


class OnEncryptInput:
    @classmethod
    def default(cls, ):
        return lambda: OnEncryptInput_OnEncryptInput(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OnEncryptInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput)

class OnEncryptInput_OnEncryptInput(OnEncryptInput, NamedTuple('OnEncryptInput', [('materials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.OnEncryptInput.OnEncryptInput({_dafny.string_of(self.materials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptInput_OnEncryptInput) and self.materials == __o.materials
    def __hash__(self) -> int:
        return super().__hash__()


class OnEncryptOutput:
    @classmethod
    def default(cls, ):
        return lambda: OnEncryptOutput_OnEncryptOutput(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OnEncryptOutput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput)

class OnEncryptOutput_OnEncryptOutput(OnEncryptOutput, NamedTuple('OnEncryptOutput', [('materials', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.OnEncryptOutput.OnEncryptOutput({_dafny.string_of(self.materials)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput) and self.materials == __o.materials
    def __hash__(self) -> int:
        return super().__hash__()


class PaddingScheme:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [PaddingScheme_PKCS1(), PaddingScheme_OAEP__SHA1__MGF1(), PaddingScheme_OAEP__SHA256__MGF1(), PaddingScheme_OAEP__SHA384__MGF1(), PaddingScheme_OAEP__SHA512__MGF1()]
    @classmethod
    def default(cls, ):
        return lambda: PaddingScheme_PKCS1()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PKCS1(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_PKCS1)
    @property
    def is_OAEP__SHA1__MGF1(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1)
    @property
    def is_OAEP__SHA256__MGF1(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA256__MGF1)
    @property
    def is_OAEP__SHA384__MGF1(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA384__MGF1)
    @property
    def is_OAEP__SHA512__MGF1(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA512__MGF1)

class PaddingScheme_PKCS1(PaddingScheme, NamedTuple('PKCS1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PaddingScheme.PKCS1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_PKCS1)
    def __hash__(self) -> int:
        return super().__hash__()

class PaddingScheme_OAEP__SHA1__MGF1(PaddingScheme, NamedTuple('OAEP__SHA1__MGF1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PaddingScheme.OAEP_SHA1_MGF1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA1__MGF1)
    def __hash__(self) -> int:
        return super().__hash__()

class PaddingScheme_OAEP__SHA256__MGF1(PaddingScheme, NamedTuple('OAEP__SHA256__MGF1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PaddingScheme.OAEP_SHA256_MGF1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA256__MGF1)
    def __hash__(self) -> int:
        return super().__hash__()

class PaddingScheme_OAEP__SHA384__MGF1(PaddingScheme, NamedTuple('OAEP__SHA384__MGF1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PaddingScheme.OAEP_SHA384_MGF1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA384__MGF1)
    def __hash__(self) -> int:
        return super().__hash__()

class PaddingScheme_OAEP__SHA512__MGF1(PaddingScheme, NamedTuple('OAEP__SHA512__MGF1', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PaddingScheme.OAEP_SHA512_MGF1'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.PaddingScheme_OAEP__SHA512__MGF1)
    def __hash__(self) -> int:
        return super().__hash__()


class PositiveInteger:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class PositiveLong:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class PutCacheEntryInput:
    @classmethod
    def default(cls, ):
        return lambda: PutCacheEntryInput_PutCacheEntryInput(_dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.Materials_Encryption.default()(), int(0), int(0), Wrappers.Option_None.default()(), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_PutCacheEntryInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput)

class PutCacheEntryInput_PutCacheEntryInput(PutCacheEntryInput, NamedTuple('PutCacheEntryInput', [('identifier', Any), ('materials', Any), ('creationTime', Any), ('expiryTime', Any), ('messagesUsed', Any), ('bytesUsed', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput.PutCacheEntryInput({_dafny.string_of(self.identifier)}, {_dafny.string_of(self.materials)}, {_dafny.string_of(self.creationTime)}, {_dafny.string_of(self.expiryTime)}, {_dafny.string_of(self.messagesUsed)}, {_dafny.string_of(self.bytesUsed)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput) and self.identifier == __o.identifier and self.materials == __o.materials and self.creationTime == __o.creationTime and self.expiryTime == __o.expiryTime and self.messagesUsed == __o.messagesUsed and self.bytesUsed == __o.bytesUsed
    def __hash__(self) -> int:
        return super().__hash__()


class SignatureAlgorithm:
    @classmethod
    def default(cls, ):
        return lambda: SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ECDSA(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA)
    @property
    def is_None(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None)

class SignatureAlgorithm_ECDSA(SignatureAlgorithm, NamedTuple('ECDSA', [('ECDSA', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm.ECDSA({_dafny.string_of(self.ECDSA)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA) and self.ECDSA == __o.ECDSA
    def __hash__(self) -> int:
        return super().__hash__()

class SignatureAlgorithm_None(SignatureAlgorithm, NamedTuple('None_', [('None_', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm.None({_dafny.string_of(self.None_)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None) and self.None_ == __o.None_
    def __hash__(self) -> int:
        return super().__hash__()


class SingleThreadedCache:
    @classmethod
    def default(cls, ):
        return lambda: SingleThreadedCache_SingleThreadedCache(int(0), Wrappers.Option_None.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SingleThreadedCache(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.SingleThreadedCache_SingleThreadedCache)

class SingleThreadedCache_SingleThreadedCache(SingleThreadedCache, NamedTuple('SingleThreadedCache', [('entryCapacity', Any), ('entryPruningTailSize', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.SingleThreadedCache.SingleThreadedCache({_dafny.string_of(self.entryCapacity)}, {_dafny.string_of(self.entryPruningTailSize)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.SingleThreadedCache_SingleThreadedCache) and self.entryCapacity == __o.entryCapacity and self.entryPruningTailSize == __o.entryPruningTailSize
    def __hash__(self) -> int:
        return super().__hash__()


class StormTrackingCache:
    @classmethod
    def default(cls, ):
        return lambda: StormTrackingCache_StormTrackingCache(int(0), Wrappers.Option_None.default()(), int(0), int(0), int(0), int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_StormTrackingCache(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache)

class StormTrackingCache_StormTrackingCache(StormTrackingCache, NamedTuple('StormTrackingCache', [('entryCapacity', Any), ('entryPruningTailSize', Any), ('gracePeriod', Any), ('graceInterval', Any), ('fanOut', Any), ('inFlightTTL', Any), ('sleepMilli', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.StormTrackingCache.StormTrackingCache({_dafny.string_of(self.entryCapacity)}, {_dafny.string_of(self.entryPruningTailSize)}, {_dafny.string_of(self.gracePeriod)}, {_dafny.string_of(self.graceInterval)}, {_dafny.string_of(self.fanOut)}, {_dafny.string_of(self.inFlightTTL)}, {_dafny.string_of(self.sleepMilli)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.StormTrackingCache_StormTrackingCache) and self.entryCapacity == __o.entryCapacity and self.entryPruningTailSize == __o.entryPruningTailSize and self.gracePeriod == __o.gracePeriod and self.graceInterval == __o.graceInterval and self.fanOut == __o.fanOut and self.inFlightTTL == __o.inFlightTTL and self.sleepMilli == __o.sleepMilli
    def __hash__(self) -> int:
        return super().__hash__()


class SymmetricSignatureAlgorithm:
    @classmethod
    def default(cls, ):
        return lambda: SymmetricSignatureAlgorithm_HMAC(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HMAC(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_HMAC)
    @property
    def is_None(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None)

class SymmetricSignatureAlgorithm_HMAC(SymmetricSignatureAlgorithm, NamedTuple('HMAC', [('HMAC', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm.HMAC({_dafny.string_of(self.HMAC)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_HMAC) and self.HMAC == __o.HMAC
    def __hash__(self) -> int:
        return super().__hash__()

class SymmetricSignatureAlgorithm_None(SymmetricSignatureAlgorithm, NamedTuple('None_', [('None_', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm.None({_dafny.string_of(self.None_)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None) and self.None_ == __o.None_
    def __hash__(self) -> int:
        return super().__hash__()


class UpdateUsageMetadataInput:
    @classmethod
    def default(cls, ):
        return lambda: UpdateUsageMetadataInput_UpdateUsageMetadataInput(_dafny.Seq({}), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UpdateUsageMetadataInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.UpdateUsageMetadataInput_UpdateUsageMetadataInput)

class UpdateUsageMetadataInput_UpdateUsageMetadataInput(UpdateUsageMetadataInput, NamedTuple('UpdateUsageMetadataInput', [('identifier', Any), ('bytesUsed', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.UpdateUsageMetadataInput.UpdateUsageMetadataInput({_dafny.string_of(self.identifier)}, {_dafny.string_of(self.bytesUsed)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.UpdateUsageMetadataInput_UpdateUsageMetadataInput) and self.identifier == __o.identifier and self.bytesUsed == __o.bytesUsed
    def __hash__(self) -> int:
        return super().__hash__()


class ValidateCommitmentPolicyOnDecryptInput:
    @classmethod
    def default(cls, ):
        return lambda: ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ValidateCommitmentPolicyOnDecryptInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput)

class ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput(ValidateCommitmentPolicyOnDecryptInput, NamedTuple('ValidateCommitmentPolicyOnDecryptInput', [('algorithm', Any), ('commitmentPolicy', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ValidateCommitmentPolicyOnDecryptInput.ValidateCommitmentPolicyOnDecryptInput({_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.commitmentPolicy)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput) and self.algorithm == __o.algorithm and self.commitmentPolicy == __o.commitmentPolicy
    def __hash__(self) -> int:
        return super().__hash__()


class ValidateCommitmentPolicyOnEncryptInput:
    @classmethod
    def default(cls, ):
        return lambda: ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.CommitmentPolicy_ESDK.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ValidateCommitmentPolicyOnEncryptInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput)

class ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput(ValidateCommitmentPolicyOnEncryptInput, NamedTuple('ValidateCommitmentPolicyOnEncryptInput', [('algorithm', Any), ('commitmentPolicy', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ValidateCommitmentPolicyOnEncryptInput.ValidateCommitmentPolicyOnEncryptInput({_dafny.string_of(self.algorithm)}, {_dafny.string_of(self.commitmentPolicy)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput) and self.algorithm == __o.algorithm and self.commitmentPolicy == __o.commitmentPolicy
    def __hash__(self) -> int:
        return super().__hash__()


class ValidDecryptionMaterialsTransitionInput:
    @classmethod
    def default(cls, ):
        return lambda: ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ValidDecryptionMaterialsTransitionInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput)

class ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput(ValidDecryptionMaterialsTransitionInput, NamedTuple('ValidDecryptionMaterialsTransitionInput', [('start', Any), ('stop', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ValidDecryptionMaterialsTransitionInput.ValidDecryptionMaterialsTransitionInput({_dafny.string_of(self.start)}, {_dafny.string_of(self.stop)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput) and self.start == __o.start and self.stop == __o.stop
    def __hash__(self) -> int:
        return super().__hash__()


class ValidEncryptionMaterialsTransitionInput:
    @classmethod
    def default(cls, ):
        return lambda: ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials.default()(), software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ValidEncryptionMaterialsTransitionInput(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput)

class ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput(ValidEncryptionMaterialsTransitionInput, NamedTuple('ValidEncryptionMaterialsTransitionInput', [('start', Any), ('stop', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.ValidEncryptionMaterialsTransitionInput.ValidEncryptionMaterialsTransitionInput({_dafny.string_of(self.start)}, {_dafny.string_of(self.stop)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput) and self.start == __o.start and self.stop == __o.stop
    def __hash__(self) -> int:
        return super().__hash__()


class Error:
    @classmethod
    def default(cls, ):
        return lambda: Error_AwsCryptographicMaterialProvidersException(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsCryptographicMaterialProvidersException(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException)
    @property
    def is_EntryAlreadyExists(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryAlreadyExists)
    @property
    def is_EntryDoesNotExist(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryDoesNotExist)
    @property
    def is_InvalidAlgorithmSuiteInfo(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfo)
    @property
    def is_InvalidAlgorithmSuiteInfoOnDecrypt(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfoOnDecrypt)
    @property
    def is_InvalidAlgorithmSuiteInfoOnEncrypt(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfoOnEncrypt)
    @property
    def is_InvalidDecryptionMaterials(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials)
    @property
    def is_InvalidDecryptionMaterialsTransition(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition)
    @property
    def is_InvalidEncryptionMaterials(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterials)
    @property
    def is_InvalidEncryptionMaterialsTransition(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition)
    @property
    def is_AwsCryptographyKeyStore(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore)
    @property
    def is_AwsCryptographyPrimitives(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives)
    @property
    def is_ComAmazonawsDynamodb(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsDynamodb)
    @property
    def is_ComAmazonawsKms(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms)
    @property
    def is_CollectionOfErrors(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors)
    @property
    def is_Opaque(self) -> bool:
        return isinstance(self, software_amazon_cryptography_materialproviders_internaldafny_types.Error_Opaque)

class Error_AwsCryptographicMaterialProvidersException(Error, NamedTuple('AwsCryptographicMaterialProvidersException', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.AwsCryptographicMaterialProvidersException({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_EntryAlreadyExists(Error, NamedTuple('EntryAlreadyExists', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.EntryAlreadyExists({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryAlreadyExists) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_EntryDoesNotExist(Error, NamedTuple('EntryDoesNotExist', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.EntryDoesNotExist({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryDoesNotExist) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidAlgorithmSuiteInfo(Error, NamedTuple('InvalidAlgorithmSuiteInfo', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidAlgorithmSuiteInfo({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfo) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidAlgorithmSuiteInfoOnDecrypt(Error, NamedTuple('InvalidAlgorithmSuiteInfoOnDecrypt', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidAlgorithmSuiteInfoOnDecrypt({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfoOnDecrypt) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidAlgorithmSuiteInfoOnEncrypt(Error, NamedTuple('InvalidAlgorithmSuiteInfoOnEncrypt', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidAlgorithmSuiteInfoOnEncrypt({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfoOnEncrypt) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidDecryptionMaterials(Error, NamedTuple('InvalidDecryptionMaterials', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidDecryptionMaterials({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidDecryptionMaterialsTransition(Error, NamedTuple('InvalidDecryptionMaterialsTransition', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidDecryptionMaterialsTransition({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidEncryptionMaterials(Error, NamedTuple('InvalidEncryptionMaterials', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidEncryptionMaterials({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterials) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_InvalidEncryptionMaterialsTransition(Error, NamedTuple('InvalidEncryptionMaterialsTransition', [('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.InvalidEncryptionMaterialsTransition({_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition) and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_AwsCryptographyKeyStore(Error, NamedTuple('AwsCryptographyKeyStore', [('AwsCryptographyKeyStore', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.AwsCryptographyKeyStore({_dafny.string_of(self.AwsCryptographyKeyStore)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore) and self.AwsCryptographyKeyStore == __o.AwsCryptographyKeyStore
    def __hash__(self) -> int:
        return super().__hash__()

class Error_AwsCryptographyPrimitives(Error, NamedTuple('AwsCryptographyPrimitives', [('AwsCryptographyPrimitives', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.AwsCryptographyPrimitives({_dafny.string_of(self.AwsCryptographyPrimitives)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives) and self.AwsCryptographyPrimitives == __o.AwsCryptographyPrimitives
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ComAmazonawsDynamodb(Error, NamedTuple('ComAmazonawsDynamodb', [('ComAmazonawsDynamodb', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.ComAmazonawsDynamodb({_dafny.string_of(self.ComAmazonawsDynamodb)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsDynamodb) and self.ComAmazonawsDynamodb == __o.ComAmazonawsDynamodb
    def __hash__(self) -> int:
        return super().__hash__()

class Error_ComAmazonawsKms(Error, NamedTuple('ComAmazonawsKms', [('ComAmazonawsKms', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.ComAmazonawsKms({_dafny.string_of(self.ComAmazonawsKms)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms) and self.ComAmazonawsKms == __o.ComAmazonawsKms
    def __hash__(self) -> int:
        return super().__hash__()

class Error_CollectionOfErrors(Error, NamedTuple('CollectionOfErrors', [('list', Any), ('message', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.CollectionOfErrors({_dafny.string_of(self.list)}, {_dafny.string_of(self.message)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors) and self.list == __o.list and self.message == __o.message
    def __hash__(self) -> int:
        return super().__hash__()

class Error_Opaque(Error, NamedTuple('Opaque', [('obj', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyMaterialProvidersTypes.Error.Opaque({_dafny.string_of(self.obj)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, software_amazon_cryptography_materialproviders_internaldafny_types.Error_Opaque) and self.obj == __o.obj
    def __hash__(self) -> int:
        return super().__hash__()


class OpaqueError:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException.default()()
