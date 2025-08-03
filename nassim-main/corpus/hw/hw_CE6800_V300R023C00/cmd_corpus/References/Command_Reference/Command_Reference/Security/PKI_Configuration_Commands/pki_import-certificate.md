pki import-certificate
======================

pki import-certificate

Function
--------



The **pki import-certificate** command imports a certificate to the device memory. You can import a key pair when importing a certificate.




Format
------

**pki import-certificate ocsp** [ **realm** *realm-name* ] { **der** | **pkcs12** | **pem** } **filename** *file-name* [ **cert-name** *cert-name* ] [ **no-check-same-name** ]

**pki import-certificate** { **ca** | **local** } [ [ **realm** *realm-name* ] { **pkcs12** | **pem** } ] **filename** *file-name* [ **cert-name** *cert-name* ] [ **no-check-same-name** ] { **include-rsa-key** | **include-sm2-key** } [ **exportable** ] [ **password** *password* ]

**pki import-certificate** { **local** | **ca** } **realm** *realm-name* { **der** | **pkcs12** | **pem** } **filename** *file-name* [ **cert-name** *cert-name* ] [ **replace** ]

**pki import-certificate** { **local** | **ca** } [ [ **realm** *realm-name* ] { **der** | **pkcs12** | **pem** } ] **filename** *file-name* [ **cert-name** *cert-name* ] [ **no-check-hash-alg** ] [ **no-check-same-name** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **realm** *realm-name* | Specifies the PKI realm name of the imported certificate. | The PKI realm name must already exist.  The realm name cannot contain spaces. Otherwise, the certificate cannot be imported. |
| **der** | Imports a certificate in DER format. | - |
| **pkcs12** | Imports a certificate in PKCS12 format. | - |
| **pem** | Imports a certificate in PEM format. | - |
| **filename** *file-name* | Specifies the name of the imported certificate. | The file name must already exist. |
| **cert-name** *cert-name* | Specifies the name of the peer certificate to be saved. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain spaces. |
| **no-check-same-name** | Indicates whether to check the Issuer and Subject fields in the imported certificate. | - |
| **ca** | Imports a CA certificate.  For example, when the device works as an SSL proxy, import the SSL proxy CA certificate and use the private key in the certificate to sign the SSL client certificate again. | - |
| **local** | Imports a local certificate. | - |
| **include-rsa-key** | Imports an RSA key pair. | - |
| **include-sm2-key** | Imports an SM2 key pair. | - |
| **exportable** | The key pair can be exported. | - |
| **password** *password* | Specifies the decryption password of an RSA or SM2 key pair file. The value must be the same as the password set during the export. | The value is a string of 1 to 32 characters. |
| **replace** | Deletes the original certificate and the corresponding key pair, and imports the new certificate. The issuer and user information of the certificate before and after the replacement must be the same.  If the key pair of the original certificate is not referenced by other realms, the certificate and key pair are deleted. If the key pair of the original certificate is referenced by other realms or a CMP session, only the original certificate is deleted but the key pair is not deleted. | - |
| **no-check-hash-alg** | Specifies whether a check is performed on the hash algorithm used for the signature of the imported certificate. | - |
| **ocsp** | Imports the Online Certificate Status Protocol (OCSP) server's certificate. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a certificate is saved to the storage, run this command to import the certificate to the memory for it to take effect.Multiple certificates can be imported to the device, and the key pair can be imported when a certificate is imported. The imported certificate can be a CA certificate or a local certificate. You can use the keyword cert-name to rename the certificate and use the keyword no-check-same-name to import certificates with the same subject and issuer repeatedly.If you do not know the format of the certificate you want to import, configure each format in turn and check whether the certificate is successfully imported. If you do not specify the format of the CA certificate or local certificate to be imported, the system automatically identifies and imports the certificate.

**Prerequisites**



The certificate file already exists on the storage device.



**Precautions**

* default\_ca.cer and default\_local.cer are the names of the initial CA certificate and local certificate reserved in the system. A newly imported certificate cannot be named default\_ca.cer or default\_local.cer.
* A local certificate cannot be imported to the default PKI realm default.
* If the certificate file contains a key pair file, you can run the **pki import-certificate** command to import the certificate separately or import the key pair together with the certificate. If a certificate with the same name has been imported, you can use the keyword cert-name to rename the certificate and then import it.
* Do not import multiple local certificates to the same PKI realm. Otherwise, certificate-related services may use certificates that do not match services in the PKI realm. As a result, services are unavailable.
* When a certificate in PKCS12 format is imported, the PKI system deletes the file name extension of the original certificate, adds \_local.cer or \_ca.cer to generate a new file name, and saves it to the device storage. Therefore, it is recommended that the name of the certificate file to be imported contain fewer than 50 characters. If the certificate file name contains more than 64 characters, a new certificate file name cannot be generated correctly.
* The device supports the import of the peer certificates generated using the RSA encryption algorithm.
* Before importing a certificate or key pair, ensure that the certificate or key pair is stored in the specified directory (public directory in the system). Perform the following steps:<huawei> cd pki<huawei> cd public/After the import succeeds, the source files in the public directory are deleted by default. If you do not need to delete them, select N as prompted to keep them.


Example
-------

# When certificates with the same name are imported into the PKI realm in the file mode, use cert-name to rename the certificates and import them.
```
<HUAWEI> system-view
[~HUAWEI] pki import-certificate ca realm default pem filename ca.cer cert-name ca1.cer include-rsa-key exportable password YsHsjx_202206
Info: Succeeded in importing the certificate.                                                                                       
Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:n                     
Info: The file will keep in the flash.

```

# Import the key pair when importing a CA certificate to the PKI realm in file mode.
```
<HUAWEI> system-view
[~HUAWEI] pki import-certificate ca realm default pem filename ca.cer include-rsa-key exportable password YsHsjx_202206
Info: Succeeded in importing the certificate.                                                                                       
Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:n                     
Info: The file will keep in the flash.

```

# Import the key pair when importing the local certificate to the PKI realm in file mode.
```
<HUAWEI> system-view
[~HUAWEI] pki import-certificate local realm default pem filename local.cer include-rsa-key exportable password YsHsjx_202206
Info: Succeeded in importing the certificate.                                                                                       
Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:n                     
Info: The file will keep in the flash.

```

# Import a CA certificate to a PKI realm in file mode.
```
<HUAWEI> system-view
[~HUAWEI] pki import-certificate ca realm default  pem filename ca.cer
 The CA's Subject is /C=CN/ST=Zhejiang/L=Hangzhou/O=Huawei/OU=FW/CN=bzh1_sha256                                                     
 The CA's fingerprint is:                                                                                                           
   SHA1   fingerprint:C4:4C:0D:F8:BF:D8:44:2C:30:50:51:44:B9:0B:64:31:C0:0B:3C:A7                                                   
   SHA256 fingerprint:05:F0:F9:E4:8B:F7:63:41:9B:A4:2B:59:59:E9:82:6D:74:9D:A4:06:37:9F:FA:E5:E0:3E:C6:4C:DA:34:98:04               
 Is the fingerprint correct? [Y/N]:y
Info: Succeeded in importing the certificate.                                                                                       
Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:n                     
Info: The file will keep in the flash.

```

# Import a local certificate to a PKI realm in file mode.
```
<HUAWEI> system-view
[~HUAWEI] pki import-certificate local realm default der filename local.cer
Info: Succeeded in importing the certificate.                                                                                       
Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:n                     
Info: The file will keep in the flash.

```