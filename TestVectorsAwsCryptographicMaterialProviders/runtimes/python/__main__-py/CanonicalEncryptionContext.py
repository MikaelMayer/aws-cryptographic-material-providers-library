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

# Module: CanonicalEncryptionContext

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextToAAD(encryptionContext):
        d_310_valueOrError0_ = Wrappers.default__.Need((len(encryptionContext)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context is too large")))
        if (d_310_valueOrError0_).IsFailure():
            return (d_310_valueOrError0_).PropagateFailure()
        elif True:
            d_311_keys_ = StandardLibrary.default__.SetToOrderedSequence((encryptionContext).keys, StandardLibrary_UInt.default__.UInt8Less)
            if (len(d_311_keys_)) == (0):
                return Wrappers.Result_Success(_dafny.Seq([]))
            elif True:
                def lambda20_(d_313_encryptionContext_):
                    def lambda21_(d_314_k_):
                        def iife7_(_pat_let2_0):
                            def iife8_(d_315_v_):
                                def iife9_(_pat_let3_0):
                                    def iife10_(d_316_valueOrError1_):
                                        return ((d_316_valueOrError1_).PropagateFailure() if (d_316_valueOrError1_).IsFailure() else Wrappers.Result_Success((((StandardLibrary_UInt.default__.UInt16ToSeq(len(d_314_k_))) + (d_314_k_)) + (StandardLibrary_UInt.default__.UInt16ToSeq(len(d_315_v_)))) + (d_315_v_)))
                                    return iife10_(_pat_let3_0)
                                return iife9_(Wrappers.default__.Need((StandardLibrary_UInt.default__.HasUint16Len(d_314_k_)) and (StandardLibrary_UInt.default__.HasUint16Len(d_315_v_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to serialize encryption context"))))
                            return iife8_(_pat_let2_0)
                        return iife7_((d_313_encryptionContext_)[d_314_k_])

                    return lambda21_

                d_312_KeyIntoPairBytes_ = lambda20_(encryptionContext)
                d_317_valueOrError2_ = Seq.default__.MapWithResult(d_312_KeyIntoPairBytes_, d_311_keys_)
                if (d_317_valueOrError2_).IsFailure():
                    return (d_317_valueOrError2_).PropagateFailure()
                elif True:
                    d_318_pairsBytes_ = (d_317_valueOrError2_).Extract()
                    d_319_allBytes_ = (StandardLibrary_UInt.default__.UInt16ToSeq(len(d_311_keys_))) + (Seq.default__.Flatten(d_318_pairsBytes_))
                    return Wrappers.Result_Success(d_319_allBytes_)

