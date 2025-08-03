pki import whitelist
====================

pki import whitelist

Function
--------



The **pki import whitelist** command imports certificate whitelist files to the device memory.




Format
------

**pki import whitelist filename** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **filename** *file-name* | Specifies the name of a certificate whitelist file. | The value is a string of 1 to 64 case-sensitive characters without spaces or question marks. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In an LTE scenario, the device establishes tunnels with multiple base stations using certificate negotiation. The certificate whitelist is defined to facilitate unified management of base station certificates, determining the base stations allowed to establish tunnels with the device.A certificate whitelist contains common names (CNs) in the certificate subjects of base stations. After PKI certificate whitelist check is enabled, the local device checks whether the CN in the certificate subject of the remote device carried in the received certificate authentication packet matches that in the local certificate whitelist. If not, authentication fails and a tunnel cannot be established between the two devices.Before enabling PKI certificate whitelist check, run the **pki import whitelist** command to import the certificate whitelist file to the device memory.



**Prerequisites**

The certificate whitelist file already exists in the device's storage media.

**Precautions**

A certificate whitelist file is in XML format and uses 7-bit ASCII coding. The following is an example of adding two CNs to the certificate whitelist.<SerialnumberList><Serialnumber>CN-on-Certificate\_of-RBS-1</Serialnumber><Serialnumber>CN-on-Certificate\_of-RBS-2</Serialnumber></SerialnumberList>CN is a string of 1 to 128 case-sensitive characters.The value can contain letters, digits, apostrophes ('), equal signs (=), parentheses (), plus signs (+), minus signs (-), periods (.), slashes (/), colons (:), @, underscore (\_), and space.When importing a certificate whitelist file, ensure that the file is saved to the specified directory (the public directory in the public system). The following is an example of entering the public directory in the public system.<huawei> cd pki<huawei> cd public/After the import is successful, the source files in the public directory are deleted by default. If you do not need to delete them, select N as prompted.


Example
-------

# Import a certificate whitelist file to the device memory.
```
<HUAWEI> system-view
[~HUAWEI] pki import whitelist filename whl.xml
Info: Succeeded in importing whitelist file.
Warning: The file in the flash will be deleted. Please select 'N' if you want to keep it. Please select [Y/N]:y                     
Info: Delete Success.

```