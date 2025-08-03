pki import-certificate peer
===========================

pki import-certificate peer

Function
--------



The **pki import-certificate peer** command imports a certificate of the remote device to the device memory.




Format
------

**pki import-certificate peer** *peer-name* { **der** | **pem** | **pkcs12** } **filename** *filename* [ **cert-name** *cert-name* ] [ **no-check-same-name** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **der** | Imports a certificate of the remote device in DER format. | - |
| **pem** | Imports a certificate of the remote device in PEM format. | - |
| **pkcs12** | Imports a certificate of the remote device in P12 format. | - |
| **filename** *filename* | Imports a certificate of the remote device in file mode. | The value is an existing certificate name of the remote device. |
| **cert-name** *cert-name* | Specifies the name of the peer certificate to be saved. | The value must be the name of an existing peer certificate. The value is a string of 1 to 64 characters. |
| **peer** *peer-name* | Specifies the name of peer certificate.  A certificate cannot be imported to multiple peers. | The value is a string of 1 to 32 case-insensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Where digital envelop authentication is used, configure the public key of the remote device. The public key can be obtained from the public and private key management module or certificate of the remote device.

**Prerequisites**

The certificate file of the remote device must already exist on the storage device.

**Precautions**



When a certificate in pkcs12 format is imported, the PKI system deletes the file name extension of the original certificate file, adds \_local.cer or ca.cer to generate a new file name, and saves it to the storage component. Therefore, the name of the certificate file to be imported cannot exceed 50 characters. Otherwise, the total certificate file name will exceed 64 characters, and the certificate file cannot be imported to the storage component.You can import a peer certificate generated using the RSA encryption algorithm to the device.Before importing a certificate or key pair, ensure that the certificate or key pair is stored in the specified directory (public directory on the public system). For example, the certificate or key pair is in the public directory of the system:

<huawei> cd pki<huawei> cd public/After the import succeeds, the source file in the public directory is deleted by default. If the source file does not need to be deleted, select N to keep it.




Example
-------

# Import the certificate aa.pem of the remote device in the file mode.
```
<HUAWEI> system-view
[~HUAWEI] pki import-certificate peer abcd pem filename aa.pem
 Info: Succeeded in importing the peer certificate.
Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:y                     
Info: Delete Success.

```