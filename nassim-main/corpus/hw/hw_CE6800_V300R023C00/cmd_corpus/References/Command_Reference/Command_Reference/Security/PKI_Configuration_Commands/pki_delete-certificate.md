pki delete-certificate
======================

pki delete-certificate

Function
--------



The **pki delete-certificate** command deletes a certificate from the memory.




Format
------

**pki delete-certificate ocsp** { **realm** *realm-name* | **filename** *file-name* }

**pki delete-certificate** { **ca** | **local** } { **realm** *realm-name* | **filename** *file-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **realm** *realm-name* | Specifies the name of the PKI realm to which a certificate belongs. | The value must be an existing PKI realm name. |
| **filename** *file-name* | Specifies the name of a certificate file. | The value must be an existing certificate file name. |
| **ca** | Deletes a CA certificate. | - |
| **local** | Deletes a local certificate. | - |
| **ocsp** | Deletes an Online Certificate Status Protocol (OCSP) server's certificate. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When the certificate expires or you want to apply for a new certificate, run this command to delete the CA certificate or local certificate from the memory.



**Prerequisites**



A certificate has been imported to the memory using the **pki import-certificate** command.




Example
-------

# Delete the local certificate from the memory.
```
<HUAWEI> system-view
[~HUAWEI] pki delete-certificate local realm default

```

# Delete the ca certificate from the memory.
```
<HUAWEI> system-view
[~HUAWEI] pki delete-certificate ca realm default

```