pki export-certificate
======================

pki export-certificate

Function
--------



The **pki export-certificate** command exports a certificate to the flash.




Format
------

**pki export-certificate** { **ca** | **local** | **ocsp** } **realm** *realm-name* { **pkcs12** | **pem** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ca** | Exports a CA certificate. | - |
| **local** | Exports a local certificate. | - |
| **ocsp** | Exports the Online Certificate Status Protocol (OCSP) certificate. | - |
| **realm** *realm-name* | Specifies the PKI realm name of a certificate. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain tildes, backslashes (\), spaces, double quotation marks ("), single quotation marks ('), asterisks (\*), colons (:), less-than signs (<), question marks (?), slashes (/), or vertical bars (|). |
| **pkcs12** | Exports a certificate in P12 format. | - |
| **pem** | Exports a certificate in PEM format. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To copy a certificate to another device, run the pki export-certificate command to export a certificate to the flash of the local device first, and then transfer the certificate to another device using a file transfer protocol.Before using this command, run the display pki certificate (all views) command to view information about certificates on the device.

**Prerequisites**

A PKI realm has been created using the pki realm (system view) command.

**Precautions**

* When the exported certificate file does not contain a private key, the device does not encrypt this file.
* When you export the private key, the system asks you to enter the private key file name. If the private key file name and the certificate file name are the same, the private key and certificate are stored in the same file. If they are different, they are stored in different files.
* When you export the private key, the system asks you to enter the private key file format and set the password. The password will be used when you run the **pki import-certificate** command to import this private key.
* Using a simple password may introduce security risks. The password must consist of at least two types of the following: uppercase letters, lowercase letters, numerals, and special characters.

Example
-------

# Export the local certificate in the PKI realm abc.
```
<HUAWEI> system-view
[~HUAWEI] pki realm abc
[*HUAWEI-pki-realm-abc] quit
[~HUAWEI] pki export-certificate local realm abc pem
 Please enter the name of certificate file <length 1-127>: aa  
 If you only export the certificate, do not export the private key.   
 You can directly enter empty of private key file.
 Please enter the name of private key file <length 1-127>:     
 Info: Succeeded in exporting the certificate.

```