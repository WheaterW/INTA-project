bridge-domain
=============

bridge-domain

Function
--------



The **bridge-domain** command creates a bridge domain (BD) and displays the BD view.

The **undo bridge-domain** command deletes a BD.



By default, no bridge domain is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bridge-domain** *bd-id*

**undo bridge-domain** *bd-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bridge-domain** *bd-id* | Specifies the ID of a bridge domain. | The value is an integer  ranging from 1 to 16777215. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a VXLAN network, a BD is created as a Layer 2 broadcast domain used to forward VXLAN data packets.



**Precautions**



Multiple bridge domains can be created on a device. Bridge domains are irrelevant to VLAN tags carried in packets.




Example
-------

# Create a bridge domain with ID 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10

```