import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibrary_UInt
import StandardLibrary_String
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
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny

# Module: DiscoveryMultiKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DiscoveryMultiKeyring(regions, discoveryFilter, clientSupplier, grantTokens):
        output: Wrappers.Result = None
        d_560_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_560_valueOrError0_ = Wrappers.default__.Need((len(regions)) > (0), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("No regions passed.")))
        if (d_560_valueOrError0_).IsFailure():
            output = (d_560_valueOrError0_).PropagateFailure()
            return output
        d_561_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_561_valueOrError1_ = Wrappers.default__.Need((Seq.default__.IndexOfOption(regions, _dafny.Seq(""))).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Empty string is not a valid region.")))
        if (d_561_valueOrError1_).IsFailure():
            output = (d_561_valueOrError1_).PropagateFailure()
            return output
        d_562_children_: _dafny.Seq
        d_562_children_ = _dafny.Seq([])
        hi4_ = len(regions)
        for d_563_i_ in range(0, hi4_):
            d_564_region_: _dafny.Seq
            d_564_region_ = (regions)[d_563_i_]
            d_565_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
            d_566_valueOrError2_: Wrappers.Result = None
            out105_: Wrappers.Result
            out105_ = (clientSupplier).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(d_564_region_))
            d_566_valueOrError2_ = out105_
            if (d_566_valueOrError2_).IsFailure():
                output = (d_566_valueOrError2_).PropagateFailure()
                return output
            d_565_client_ = (d_566_valueOrError2_).Extract()
            d_567_keyring_: AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring
            nw13_ = AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring()
            nw13_.ctor__(d_565_client_, discoveryFilter, (grantTokens).UnwrapOr(_dafny.Seq([])))
            d_567_keyring_ = nw13_
            d_562_children_ = (d_562_children_) + (_dafny.Seq([d_567_keyring_]))
        d_568_keyring_: MultiKeyring.MultiKeyring
        nw14_ = MultiKeyring.MultiKeyring()
        nw14_.ctor__(Wrappers.Option_None(), d_562_children_)
        d_568_keyring_ = nw14_
        output = Wrappers.Result_Success(d_568_keyring_)
        return output
        return output

