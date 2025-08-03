if-match l2-protocol
====================

if-match l2-protocol

Function
--------



The **if-match l2-protocol** command configures a matching rule based on the Layer 2 protocol type in a traffic classifier.

The **undo if-match l2-protocol** command deletes a matching rule based on the Layer 2 protocol type in a traffic classifier.



By default, a matching rule based on the Layer 2 protocol type is not configured in a traffic classifier.


Format
------

**if-match l2-protocol** { **arp** | **ip** | **rarp** | *protocol-value* }

**undo if-match l2-protocol**

**undo if-match l2-protocol** { **arp** | **ip** | **rarp** | *protocol-value* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **arp** | Indicates that ARP packets are classified. | The value of arp corresponds to 0x0806. |
| **ip** | Indicates that IP packets are classified. | The value of ip corresponds to 0x0800. |
| **rarp** | Indicates that RARP packets are classified. | The value of rarp corresponds to 0x8035. |
| *protocol-value* | Specifies the value of a protocol type. | The value ranges from 0x0 to 0xFFFF in hexadecimal notation and must start with 0x. If the value of protocol-value is smaller than 0x0600, the Destination Service Access Point (DSAP) and Source Service Access Point (SSAP) fields in the Logical Line Control (LLC) protocol packets are matched. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match l2-protocol** command to classify packets based on the Layer 2 protocol type so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

* The device supports Layer 2 protocols including ARP, IP, and RARP.
* If you run the **if-match l2-protocol** command in the same traffic classifier view multiple times, only the latest configuration takes effect.


Example
-------

# Define a matching rule based on the protocol type of ARP in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match l2-protocol arp

```