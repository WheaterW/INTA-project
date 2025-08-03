pki rsa local-key-pair create
=============================

pki rsa local-key-pair create

Function
--------



The **pki rsa local-key-pair create** command creates the specified RSA key pair.




Format
------

**pki rsa local-key-pair create** *key-name* [ **modulus** *modulus-size* ] [ **exportable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-name* | Specifies the name of the RSA key pair to be created. | The value is a string of 1 to 64 case-sensitive characters, and spaces and question marks (?) are not supported. If the string is enclosed in double quotation marks ("), spaces are allowed in the string. |
| **modulus** *modulus-size* | Specifies the size of the RSK key pair. | The value is an even number ranging from 2048 to 4096 bits. The default value is 3072 bits. If you enter an odd number, the value of the generated key pair is the odd number minus 1. |
| **exportable** | Indicates that the new RSA key pair can be exported from the device. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a PKI entity requests a certificate from the CA, the certificate enrollment request that it sends contains information such as the public key. Run this command to create the RSA key pair for the certificate request.Windows Server 2003 has a low processing performance. For the device to connect to a Windows Server 2003, the device cannot have too many entities configured or use a large-sized key pair.

**Precautions**

* When you create a key pair, the system prompts you to enter the number of bits in the RSA key pair. The larger the number of bits in a key pair, the more difficult it is to crack the key pair, the more secure the algorithm, but the slower the calculation speed. It is recommended that the RSA key pair contain more than 3072 bits. Otherwise, security risks exist.
* The name of an RSA key pair cannot exceed 50 characters. When an RSA key pair is imported, if the file contains a certificate, PKI adds \_localx.cer to the end of the RSA key pair name to generate a new certificate file name and saves the new certificate file name to the storage device. If the name of the RSA key pair exceeds 50 characters, the name of the imported certificate exceeds 64 characters and cannot be saved to the storage device.
* The RSA key pair referenced by a PKI realm cannot be overwritten. The RSA key pair can be overwritten only after the reference relationship is canceled.
* If the name of the new RSA key pair is the same as that of an existing RSA key pair on the device, the system prompts you whether to overwrite the existing RSA key pair.

Example
-------

# Create RSA key pair abc with 3072 bits.
```
<HUAWEI> system-view
[HUAWEI] pki rsa local-key-pair create abc
Info: The name of the new key-pair will be: abc
The size of the public key ranges from 2048 to 4096 and is an even number.
If the input value is an odd number, the size of the public key is the input value minus one.
Input the bits in the modules:3072
Generating key-pairs...
Generating key-pairs finished

```