pki validate-certificate device
===============================

pki validate-certificate device

Function
--------



The **pki validate-certificate device** command verifies the initial certificates (including the local certificate and CA certificate) loaded on the device.




Format
------

**pki validate-certificate device slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Verifies the device's initial certificate information in a specified slot. | The value is a string and depends on the device configuration. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The validity of the initial local certificate and CA certificate has been verified before device delivery. Generally, you do not need to run this command.


Example
-------

# Verify the initial local certificate and CA certificate.
```
<HUAWEI> system-view
[~HUAWEI] pki validate-certificate device slot 0
2021-02-08 11:37:12.647                                                                                                             
Info: The Device certificate is valid.

```