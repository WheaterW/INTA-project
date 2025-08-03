pki export-certificate default
==============================

pki export-certificate default

Function
--------



The **pki export-certificate default** command exports a default built-in certificate to the flash.




Format
------

**pki export-certificate default ca filename** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ca** | Specifies the CA certificate to be exported. | - |
| **filename** *file-name* | Specifies the name of an exported certificate file. | The value is a string of 1 to 64 case-insensitive characters without spaces and question marks (?). |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To copy a certificate to another device, run this command to export the certificate to the flash on the local device first, and transfer the certificate file to the other device using a protocol transfer protocol.Before using this command, run the display pki certificate (all views) command to view information about default built-in certificates on the device.




Example
-------

# Export the default built-in CA certificate.
```
<HUAWEI> system-view
[~HUAWEI] pki export-certificate default ca filename ca.der
 Info: Succeeded in exporting the certificate.

```