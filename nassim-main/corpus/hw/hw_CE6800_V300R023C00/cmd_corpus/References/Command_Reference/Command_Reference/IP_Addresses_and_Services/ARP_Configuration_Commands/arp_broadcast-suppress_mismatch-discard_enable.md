arp broadcast-suppress mismatch-discard enable
==============================================

arp broadcast-suppress mismatch-discard enable

Function
--------



The **arp broadcast-suppress mismatch-discard enable** command enables ARP broadcast suppression in a BD. This function allows a gateway to unicast the ARP broadcast packets received in a BD, preventing network congestion.

The **undo arp broadcast-suppress mismatch-discard enable** command disables ARP broadcast suppression in a BD.



By default, ARP broadcast suppression is disabled in a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp broadcast-suppress mismatch-discard enable**

**undo arp broadcast-suppress mismatch-discard enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mismatch-discard** | Indicates that the device drops packets that do not match any entries in the ARP broadcast suppression table.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a gateway receives a large number of ARP requests within a short period and broadcasts the ARP requests in a BD, excessive ARP requests are forwarded. As a result, excessive network resources are used, and traffic congestion may occur. ARP broadcast suppression can effectively ease the pressure on gateways in handling ARP packets.ARP broadcast suppression can effectively ease the pressure on gateways in handling ARP packets. After receiving an ARP request, a gateway searches the broadcast suppression table that contains the mapping between the IP and MAC addresses of each destination device.

* If a matching entry is found, the gateway replaces the broadcast MAC address in the received ARP request with the MAC address of the destination device, and then sends the request out through the interface matching the destination MAC address.
* If a matching entry is not found:The gateway broadcasts the ARP request in the BD if the mismatch-discard parameter is not set in the **arp broadcast-suppress enable** command.The gateway drops the ARP request if the mismatch-discard parameter is set in the **arp broadcast-suppress enable** command.

**Precautions**



The implementation of ARP broadcast suppression depends on the ARP broadcast suppression table stored on the gateway. If the gateway does not have an ARP broadcast suppression table and this command is configured, all received ARP request packets are processed according to the preceding process when no entry is matched. If both the arp broadcast-suppress enable and **arp broadcast-suppress mismatch-discard enable** commands are run, the latest configuration overrides the previous one.




Example
-------

# Enable ARP broadcast suppression in BD 20.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 20
[*HUAWEI-bd20] arp broadcast-suppress mismatch-discard enable

```