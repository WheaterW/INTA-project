pki release-certificate peer
============================

pki release-certificate peer

Function
--------



The **pki release-certificate peer** command releases a certificate of the remote device.




Format
------

**pki release-certificate peer** { **name** *peer-name* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *peer-name* | Specifies the name of peer certificate to be released. | The value must be an existing peer certificate file name. |
| **all** | Releases all certificates of the remote device. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the specified certificate of the remote device is not required, run the pki release-certificate peer command to release the certificate of the remote device.Before using this command, run the display pki peer-certificate (All views) command to view the certificate information of the remote device.

**Prerequisites**

The **pki import-certificate peer** command has been used to import the certificate of the remote device.


Example
-------

# Release the certificate huawei of the remote device.
```
<HUAWEI> system-view
[~HUAWEI] pki release-certificate peer name huawei
 Info: Succeeded in releasing the peer certificate.

```