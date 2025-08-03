arp broadcast-detect times
==========================

arp broadcast-detect times

Function
--------



The **arp broadcast-detect times** command sets the maximum allowable number of ARP broadcast probes implemented when a VXLAN tunnel or Layer 2 sub-interface goes Down.

The **undo arp broadcast-detect times** command restores the default configuration.



By default, a maximum of three ARP broadcast probes can be implemented when a VXLAN tunnel or Layer 2 sub-interface goes Down.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp broadcast-detect times** *detect-times*

**undo arp broadcast-detect times** [ *detect-times* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *detect-times* | Specifies the maximum allowable number of ARP broadcast probes. | The value is an integer ranging from 1 to 10. |



Views
-----

VBDIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the NFVI distributed gateway scenario, if the local VXLAN tunnel or Layer 2 sub-interface functioning as the gateway to receive ARP request packets goes Down, ARP entries cannot be generated, and packets are discarded. In this case, run the arp broadcast-detect enable command to enable ARP broadcast probe in the VBDIF interface view. Because ARP request packets are broadcast, they can be broadcast in a BD. When the local VXLAN tunnel or Layer 2 sub-interface is Down, ARP request packets cannot be sent locally. However, if the remote VXLAN tunnel or Layer 2 sub-interface is Up, ARP requests can be sent, and dynamic ARP entries can be learned upon receipt of ARP response packets. The remote device can then synchronize learned ARP entries to the local device through EVPN routes, and redirected ARP entries are generated on the local device.To set the maximum allowable number of ARP broadcast probes implemented when a VXLAN tunnel or Layer 2 sub-interface goes Down, run the **arp broadcast-detect times** command.

**Configuration Impact**

After a VXLAN tunnel or Layer 2 sub-interface goes from Up to Down, if the device fails to relearn dynamic ARP entries from the remote VXLAN tunnel or sub-interface within the period specified by arp broadcast-detect interval detect-interval and arp broadcast-detect times detect-times, dynamic ARP entries learned on the local VXLAN tunnel or Layer 2 sub-interface will be deleted.


Example
-------

# On VBDIF 10, set the maximum allowable number of ARP broadcast probes implemented when a VXLAN tunnel or Layer 2 sub-interface goes Down to 5.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] quit
[*HUAWEI] interface vbdif 10
[*HUAWEI-Vbdif10] arp broadcast-detect times 5

```