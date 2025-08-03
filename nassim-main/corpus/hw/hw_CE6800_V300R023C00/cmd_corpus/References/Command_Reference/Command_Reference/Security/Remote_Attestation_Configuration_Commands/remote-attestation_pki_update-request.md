remote-attestation pki update-request
=====================================

remote-attestation pki update-request

Function
--------



The **remote-attestation pki update-request** command updates PKI certificate information.




Format
------

**remote-attestation pki update-request** { **all** | **slot** *slotID* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Updates PKI certificate information on the boards in all slots. | - |
| **slot** *slotID* | Updates PKI certificate information on a board in a specified slot. | - |



Views
-----

Trust environment management


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



When remote attestation is configured, if the LAK certificate becomes invalid (for example, the certificate is revoked due to certificate information leakage), you need to update the LAK certificate.After the **remote-attestation pki update-request** command is executed, the device immediately applies to the CA server for certificate update.



**Precautions**

Only HTM profiles support this command.


Example
-------

# Update PKI certificate information on all boards.
```
<HUAWEI> system-view
[~HUAWEI] trustem
[~HUAWEI-trustem] remote-attestation pki update-request all

```