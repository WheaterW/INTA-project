pki delete-crl
==============

pki delete-crl

Function
--------



The **pki delete-crl** command deletes a CRL from the memory.




Format
------

**pki delete-crl** { **realm** *realm-name* | **filename** *file-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **realm** *realm-name* | Specifies the name of the PKI realm that the certificate belongs to. | The value must be an existing PKI realm name. |
| **filename** *file-name* | Specifies the name of a CRL file. | The value must be an existing CRL file name. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a CRL expires, run this command to delete a CRL file from the memory. This command will not delete the CRL files in storage card.

**Prerequisites**



To check whether a CRL file exists, run the display pki crl (all views) command.




Example
-------

# Delete the CRL of PKI realm default from the memory.
```
<HUAWEI> system-view
[~HUAWEI] pki delete-crl realm default

```