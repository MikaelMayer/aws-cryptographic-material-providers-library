// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyMaterialProvidersTestVectorKeysTypes.dfy"
  // Yes, this is reaching across.
  // ideally all these functions would exist in the STD Library.
include "../../TestVectorsAwsCryptographicMaterialProviders/src/JSONHelpers.dfy"

module {:options "-functionSyntax:4"} KeyDescription {
  import opened Wrappers
  import opened JSON.Values
  import AwsCryptographyMaterialProvidersTypes
  import opened Types = AwsCryptographyMaterialProvidersTestVectorKeysTypes
  import opened JSONHelpers
  import ComAmazonawsKmsTypes
  import Seq
  import Base64

  function printErr(e: string) : (){()} by method {print e, "\n", "\n"; return ();}
  function printJSON(e: seq<(string, JSON)>) : (){()} by method {print e, "\n", "\n"; return ();}

  function  ToKeyDescription(json: JSON)
    : Result<KeyDescription, string>
    decreases Size(json)
  {
    :- Need(json.Object?, "KeyDescription not an object");
    var obj := json.obj;
    var typString := "type";
    var typ :- GetString(typString, obj);

    :- Need(KeyDescriptionString?(typ), "Unsupported KeyDescription type:" + typ);

    match typ
    case "aws-kms-mrk-aware-discovery" => ToAwsKmsMrkAwareDiscovery(obj)
    case "caching-cmm" =>
      var u :- Get("underlying", obj);
      GetWillDecreaseSize("underlying", u, json);
      var underlying :- ToKeyDescription(u);
      var cacheLimitTtlSeconds :- GetPositiveInteger("cacheLimitTtlSeconds", obj);
      var limitBytes := GetPositiveLong("limitBytes", obj).ToOption();
      var limitMessages := GetPositiveInteger("limitMessages", obj).ToOption();

      var getEntryIdentifierEncoded :- GetOptionalString("getEntryIdentifier", obj);
      var getEntryIdentifier
        :- if getEntryIdentifierEncoded.Some? then
             var result := Base64.Decode(getEntryIdentifierEncoded.value);
             if result.Success? then Success(Some(result.value)) else Failure(result.error)
           else Success(None);

      var putEntryIdentifierEncoded :- GetOptionalString("putEntryIdentifier", obj);
      var putEntryIdentifier
        :- if putEntryIdentifierEncoded.Some? then
             var result := Base64.Decode(putEntryIdentifierEncoded.value);
             if result.Success? then Success(Some(result.value)) else Failure(result.error)
           else Success(None);

      Success(Caching(
                CachingCMM(
                  underlying := underlying,
                  cacheLimitTtlSeconds := cacheLimitTtlSeconds,
                  limitBytes := limitBytes,
                  limitMessages := limitMessages,
                  getEntryIdentifier := getEntryIdentifier,
                  putEntryIdentifier := putEntryIdentifier
                )))
    case "required-encryption-context-cmm" =>
      var u :- Get("underlying", obj);
      GetWillDecreaseSize("underlying", u, json);
      var underlying :- ToKeyDescription(u);
      var requiredEncryptionContextStrings
        := GetArrayString("requiredEncryptionContextKeys", obj)
           .ToOption()
           .UnwrapOr([]);
      var requiredEncryptionContextKeys :- utf8EncodeSeq(requiredEncryptionContextStrings);

      Success(RequiredEncryptionContext(
                RequiredEncryptionContextCMM(
                  underlying := underlying,
                  requiredEncryptionContextKeys := requiredEncryptionContextKeys
                )))
    case _ =>
      var key :- GetString("key", obj);
      match typ
      case "static-material-keyring" =>
        Success(Static(StaticKeyring( keyId := key )))
      case "aws-kms" =>
        Success(Kms(KMSInfo( keyId := key )))
      case "aws-kms-mrk-aware" =>
        Success(KmsMrk(KmsMrkAware( keyId := key )))
      case "aws-kms-rsa" => ToAwsKmsRsa(key, obj)
      case "aws-kms-hierarchy" =>
        Success(Hierarchy(HierarchyKeyring( keyId := key )))
      case "raw" =>
        var algorithm :- GetString("encryption-algorithm", obj);
        :- Need(RawAlgorithmString?(algorithm), "Unsupported algorithm:" + algorithm);
        match algorithm
        case "aes" => ToRawAes(key, obj)
        case "rsa" => ToRawRsa(key, obj)
  }

  function ToDiscoveryFilter(obj: seq<(string, JSON)>)
    : Option<AwsCryptographyMaterialProvidersTypes.DiscoveryFilter>
  {
    var filter :- GetObject("aws-kms-discovery-filter", obj).ToOption();
    var partition :- GetString("partition", filter).ToOption();
    var accountIds :- GetArrayString("account-ids", filter).ToOption();
    Some(AwsCryptographyMaterialProvidersTypes.DiscoveryFilter(
           partition := partition,
           accountIds := accountIds
         ))
  }

  function ToAwsKmsMrkAwareDiscovery(obj: seq<(string, JSON)>)
    : Result<KeyDescription, string>
  {
    var defaultMrkRegion :- GetString("default-mrk-region", obj);
    var filter := GetObject("aws-kms-discovery-filter", obj);
    var awsKmsDiscoveryFilter := ToDiscoveryFilter(obj);
    Success(KmsMrkDiscovery(
              KmsMrkAwareDiscovery(
                keyId := "aws-kms-mrk-aware-discovery",
                defaultMrkRegion := defaultMrkRegion,
                awsKmsDiscoveryFilter := awsKmsDiscoveryFilter
              )))
  }

  function ToAwsKmsRsa(key: string, obj: seq<(string, JSON)>)
    : Result<KeyDescription, string>
  {
    var encryptionAlgorithmString :- GetString("encryption-algorithm", obj);
    :- Need(EncryptionAlgorithmSpec?(encryptionAlgorithmString), "Unsupported EncryptionAlgorithmSpec:" + encryptionAlgorithmString);
    var encryptionAlgorithm := match encryptionAlgorithmString
      case "RSAES_OAEP_SHA_1" => ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_1
      case "RSAES_OAEP_SHA_256" => ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.RSAES_OAEP_SHA_256;
    Success(KmsRsa(KmsRsaKeyring( keyId := key, encryptionAlgorithm := encryptionAlgorithm )))
  }

  function ToRawAes(key: string, obj: seq<(string, JSON)>)
    : Result<KeyDescription, string>
  {
    var providerId :- GetString("provider-id", obj);
    Success(AES(RawAES( keyId := key, providerId := providerId )))
  }

  function ToRawRsa(key: string, obj: seq<(string, JSON)>)
    : Result<KeyDescription, string>
  {
    var providerId :- GetString("provider-id", obj);
    var paddingAlgorithm :- GetString("padding-algorithm", obj);
    var paddingHash :- GetString("padding-hash", obj);
    :- Need(PaddingAlgorithmString?(paddingAlgorithm), "Unsupported paddingAlgorithm:" + paddingAlgorithm);
    :- Need(PaddingHashString?(paddingHash), "Unsupported paddingHash:" + paddingHash);

    match paddingAlgorithm
    case "pkcs1" =>
      :- Need(paddingHash == "sha1", "Unsupported padding with pkcs1:" + paddingHash);
      Success(RSA(RawRSA( keyId := key, providerId := providerId, padding := AwsCryptographyMaterialProvidersTypes.PKCS1 )))
    case "oaep-mgf1" => match paddingHash
      case "sha1" => Success(RSA(RawRSA( keyId := key, providerId := providerId, padding := AwsCryptographyMaterialProvidersTypes.OAEP_SHA1_MGF1 )))
      case "sha256" => Success(RSA(RawRSA( keyId := key, providerId := providerId, padding := AwsCryptographyMaterialProvidersTypes.OAEP_SHA256_MGF1 )))
      case "sha384" => Success(RSA(RawRSA( keyId := key, providerId := providerId, padding := AwsCryptographyMaterialProvidersTypes.OAEP_SHA384_MGF1 )))
      case "sha512" => Success(RSA(RawRSA( keyId := key, providerId := providerId, padding := AwsCryptographyMaterialProvidersTypes.OAEP_SHA512_MGF1 )))
  }

  predicate KeyDescriptionString?(s: string)
  {
    || s == "static-material-keyring"
    || s == "aws-kms"
    || s == "aws-kms-mrk-aware"
    || s == "aws-kms-mrk-aware-discovery"
    || s == "raw"
    || s == "aws-kms-hierarchy"
    || s == "aws-kms-rsa"
    || s == "caching-cmm"
    || s == "required-encryption-context-cmm"
  }

  predicate RawAlgorithmString?(s: string)
  {
    || s == "aes"
    || s == "rsa"
  }

  predicate PaddingAlgorithmString?(s: string)
  {
    || s == "pkcs1"
    || s == "oaep-mgf1"
  }

  predicate PaddingHashString?(s: string)
  {
    || s == "sha1"
    || s == "sha1"
    || s == "sha256"
    || s == "sha384"
    || s == "sha512"
  }

  predicate EncryptionAlgorithmSpec?(s: string)
  {
    // This is missing SYMMETRIC_DEFAULT because this is asymmetric only
    || s == "RSAES_OAEP_SHA_1"
    || s == "RSAES_OAEP_SHA_256"
  }

}
