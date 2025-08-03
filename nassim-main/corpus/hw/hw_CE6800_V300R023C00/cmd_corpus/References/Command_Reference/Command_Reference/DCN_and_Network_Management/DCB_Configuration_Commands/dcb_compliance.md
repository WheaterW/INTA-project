dcb compliance
==============

dcb compliance

Function
--------



The **dcb compliance** command configures the version of Data Center Bridging eXchange (DCBX) TLVs sent from an interface.

The **undo dcb compliance** command restores the default version of DCBX TLVs sent from an interface.



By default, an interface sends DCBX TLVs of the IEEE standard version.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcb compliance intel-oui**

**undo dcb compliance intel-oui**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **intel-oui** | Indicates Intel DCBX. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Two standards are available for the DCBX protocol: IEEE DCBX and Intel DCBX.Huawei switches support both the two standards. By default, an interface sends DCBX TLVs of the IEEE standard version.When a Huawei switch connects to a non-Huawei device, the two devices must use the same DCBX version. Otherwise, DCBX negotiation fails. You can run the **dcb compliance** command to change the local DCBX version.

**Precautions**

Executing the **dcb compliance** command results in DCBX re-negotiation.


Example
-------

# Set the DCBX version to Intel DCBX on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] dcb compliance intel-oui

```