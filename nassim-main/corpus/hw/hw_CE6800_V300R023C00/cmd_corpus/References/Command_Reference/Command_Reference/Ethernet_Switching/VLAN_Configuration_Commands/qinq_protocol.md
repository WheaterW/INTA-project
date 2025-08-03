qinq protocol
=============

qinq protocol

Function
--------



The **qinq protocol** command configures the EtherType value in the outer tag of tagged packets.

The **undo qinq protocol** command restores the default EtherType value in the outer tag of tagged packets.



By default, the EtherType value in the outer tag of tagged packets received by an Ethernet interface is 0x8100.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qinq protocol** *ethertype-value*

**undo qinq protocol**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **protocol** *ethertype-value* | Specifies the EtherType value in the outer tag of tagged packets on an Ethernet interface. If this parameter is set to a well-known Ethernet encapsulation type, packet identification will be affected on inbound interfaces, which will result in packet forwarding errors. Therefore, setting this parameter to a well-known Ethernet encapsulation type is not recommended. | The value ranges from 0x0600 to 0xFFFF, in hexadecimal format. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a Huawei device connects to a non-Huawei device and QinQ is configured, these devices all use 0x8100 as the EtherType value in the inner tag protocol identifier (TPID) but may use different EtherType values in the outer TPID. For example, the non-Huawei device uses the EtherType value 0x88a8 defined in IEEE 802.1ad in the outer TPID while the Huawei device uses the EtherType value 0x8100. To implement interoperation between these devices, run the qinq protocol command to configure an EtherType value in the outer tag.

**Precautions**

The qinq protocol command takes effect both on double-tagged and single-tagged packets.This command can only be used on Layer 2 Ethernet interfaces.


Example
-------

# Configure the EtherType value in the outer tag to be 0x9100 on an Ethernet interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] qinq protocol 9100

```