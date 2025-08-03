pki export rsa-key-pair
=======================

pki export rsa-key-pair

Function
--------



The **pki export rsa-key-pair** command exports the RSA key pair to the flash and allows the export of the associated certificate and certificate chain.




Format
------

**pki export rsa-key-pair** *keyname* [ **and-certificate** *certificate-name* ] { **pem** *filename* [ **aes** ] | **pkcs12** *filename* } **password** *password*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *keyname* | Specifies the name of the RSA key pair on the device. | The value must be an existing RSA key pair name. |
| **and-certificate** *certificate-name* | Indicates that the certificate and certificate chain related to the RSA key pair are exported. | The value must be an existing certificate file name. |
| **pem** *filename* | Indicates that the RSA key pair to be exported is in the PEM format and specifies the name of the file to be exported. | The value is a string of 1 to 64 case-insensitive characters without spaces and question marks (?). |
| **aes** | Sets the encryption algorithm to AES if a file is exported in the PEM format. The default value is AES. | - |
| **pkcs12** *filename* | Indicates that the RSA key pair to be exported is in the PKCS12 format and specifies the file name to be exported. | The value is a string of 1 to 64 case-insensitive characters without spaces and question marks (?). |
| **password** *password* | Specifies the encryption password for the RSA key pair file. This password is used when you import an RSA key pair file. | The value is a string of 6 to 32 case-sensitive characters without question marks (?).  To enhance security, a password must contain at least two types of the following characters: uppercase letters, lowercase letters, numerals, and special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent (%). |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To transfer or back up the RSA key pair, run this command to generate a PEM or PKCS12 file that contains the RSA key pair (including the certificate and certificate chain) in the flash memory.Before running this command, you can run the **display pki rsa local-key-pair** command to view information about the RSA key pair on the device.

**Prerequisites**

The RSA key pair has been created using the **pki rsa local-key-pair create** command and can be exported, or the RSA key pair has been imported to the device memory using the **pki import rsa-key-pair** command and can be exported.

**Precautions**

The RSA key pair is sensitive information. Delete and destroy the exported RSA key pair on the device or storage device immediately after you do not need it.


Example
-------

# Export the RSA key pair key1 to the file aaa.pem and set the encryption method to AES.
```
<HUAWEI> system-view
[HUAWEI] pki rsa local-key-pair create key1 exportable
Info: The name of the new key-pair will be: key1
The size of the public key ranges from 2048 to 4096 and is an even number.
If the input value is an odd number, the size of the public key is the input value minus one.
Input the bits in the modules:3072
Generating key-pairs...
Generating key-pairs finished
[HUAWEI] pki export rsa-key-pair key1 pem aaa.pem aes password YsHsjx_202206
Warning: Exporting the key pair impose security risks, are you sure you want to export it? [Y/N]:y
Info: It will take a few seconds or more. Please wait a moment.
Info: Succeeded in exporting the RSA key pair in PEM format.

```