pki export sm2-key-pair
=======================

pki export sm2-key-pair

Function
--------



The **pki export sm2-key-pair** command exports an SM2 key pair to the device storage.




Format
------

**pki export sm2-key-pair** *keyname* **der** *filename*

**pki export sm2-key-pair** *keyname* **pem** *filename* [ **password** *password* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *keyname* | Specifies the name of the SM2 key pair on the device. | The value must be an existing SM2 key pair name. |
| **der** *filename* | Exports the SM2 key pair as a DER file and specifies the file name. | The value is a string of 1 to 64 case-insensitive characters without spaces and question marks (?). |
| **pem** *filename* | Exports the SM2 key pair as a PEM file and specifies the file name. | The value is a string of 1 to 64 case-insensitive characters without spaces and question marks (?). |
| **password** *password* | Specifies the password for the SM2 key pair file. This password is used when you import an SM2 key pair file. | The value is a string of 8 to 32 case-sensitive characters without question marks (?).  For security purposes, a password must meet the minimum strength requirements, that is, the password needs to contain at least three types of the following characters: uppercase letters, lowercase letters, numerals, and special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To transfer or back up an SM2 key pair, run this command to generate a file containing the SM2 key pair in the device memory.Before running this command, you can run the **display pki sm2 local-key-pair public** command to view information about the SM2 key pair on the device.

**Prerequisites**

The SM2 key pair has been created using the **pki sm2 local-key-pair create** command and can be exported, or the SM2 key pair has been imported to the device memory using the **pki import sm2-key-pair** command and can be exported.

**Precautions**

An SM2 key pair is sensitive information. Delete or destroy the exported SM2 key pair from your device or storage device immediately after you do not use it.


Example
-------

# Export the SM2 key pair key-1 to the file aaa.pem.
```
<HUAWEI> system-view
[~HUAWEI] pki sm2 local-key-pair create key-1 exportable
 Info: The name of the new key-pair will be: key-1
 Generating key-pairs...
[~HUAWEI] pki export sm2-key-pair key-1 pem aaa.pem password YsHsjx_202206
 Warning: Exporting the key pair impose security risks, are you sure you want to export it? [y/n]:y                                                             
 Info: Succeeded in exporting the SM2 key pair in PEM format.

```