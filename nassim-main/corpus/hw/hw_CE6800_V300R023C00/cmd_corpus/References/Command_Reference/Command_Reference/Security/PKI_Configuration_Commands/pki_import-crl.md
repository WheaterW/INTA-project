pki import-crl
==============

pki import-crl

Function
--------



The **pki import-crl** command imports the CRL to the memory.




Format
------

**pki import-crl realm** *realm-name* **filename** *file-name*

**pki import-crl filename** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **filename** *file-name* | Specifies the name of an imported certificate file. Only the PEM and DER formats are supported. | The value must be an existing certificate file name. |
| **realm** *realm-name* | Specifies the PKI realm name of the imported certificate. | The value must be an existing PKI realm name. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable the CRL that is obtained in out-of-band mode or is updated manually, run this command to import the CRL to the memory.

**Prerequisites**



The CRL file exists in the device.



**Precautions**



Before importing a certificate or key pair, ensure that the certificate or key pair is stored in the specified directory (public directory on the system). For example, the certificate or key pair is in the public directory of the system:<huawei> cd pki<huawei> cd public/After the import succeeds, the source file in the public directory is deleted by default. If the source file does not need to be deleted, select N to keep it as prompted.




Example
-------

# Create PKI realm abc and import CRL to PKI realm abc.
```
<HUAWEI> system-view
[~HUAWEI] pki realm abc
[*HUAWEI-pki-realm-abc] quit
[*HUAWEI] pki import-crl realm abc filename abc.crl
Info: Succeeded in importing CRL.
Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:y                     
Info: Delete Success.

```

# Import the CRL to the PKI realm default.
```
<HUAWEI> system-view
[~HUAWEI] pki import-crl realm default filename abc.crl
Info: Succeeded in importing CRL.
Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:y                     
Info: Delete Success.

```