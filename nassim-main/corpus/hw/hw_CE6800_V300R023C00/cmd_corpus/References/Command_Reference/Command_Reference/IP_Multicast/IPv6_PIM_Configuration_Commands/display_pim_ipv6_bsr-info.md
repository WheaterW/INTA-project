display pim ipv6 bsr-info
=========================

display pim ipv6 bsr-info

Function
--------



The **display pim ipv6 bsr-info** command displays information about a BootStrap router (BSR) in a PIM-SM domain.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 bsr-info**

**display pim ipv6** { **vpn-instance** *instance-name* | **all-instance** } **bsr-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command is applicable to Rendezvous Point (RP) election in a PIM-SM domain. This command can be used to view BSR information on each Router in a PIM-SM domain.

* If the current Router is configured with a Candidate-BootStrap Router (C-BSR), information about the elected BSR and locally configured C-BSR is displayed.
* If the current Router is not configured with any C-BSR, only information about the elected BSR is displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about a BSR. If the Router is configured with a C-BSR, information about the elected BSR and the C-BSR is displayed.
```
<HUAWEI> display pim ipv6 bsr-info
VPN-Instance: public net
Elected AdminScope BSR Count: 0
Elected BSR Address: 2001:DB8:1::1
Priority: 0
Hash mask length: 64
State: Elected
Uptime: 00:00:07
Next BSR message scheduled at: 00:00:53
C-RP Count: 0
Candidate AdminScope BSR Count: 0
Candidate BSR Address: 2001:DB8:1::1
Priority: 0
Hash mask length: 64
State: Elected
Wait to be BSR: 0

```

**Table 1** Description of the **display pim ipv6 bsr-info** command output
| Item | Description |
| --- | --- |
| Elected AdminScope BSR Count | Indicates the number of elected AdminScope BSRs. |
| Elected BSR Address | Indicates the IPv6 address of the elected BSR. |
| Hash mask length | Indicates the hash mask length for the RP calculation. |
| Next BSR message scheduled at | Indicates the period for waiting to receive the next BSR message. BSR messages are sent only when the timer maintained by the elected BSR times out. |
| C-RP Count | Indicates the number of C-RPs. |
| Candidate AdminScope BSR Count | Indicates the number of candidate AdminScope BSRs. |
| Candidate BSR Address | Indicates the IPv6 address of a C-BSR. |
| Wait to be BSR | Indicates whether the CBSR is valid. |
| VPN-Instance | Indicates the VPN instance to which BSR information belongs. |
| Priority | Indicates the BSR priority. |
| State | Indicates the BSR status.   * Accept Preferred: The router knows the identity of the current BSR, and is using the RP-Set provided by that BSR. Only Bootstrap messages from that BSR or from a C-BSR with higher weight than the current BSR will be accepted. * Accept Any: The router does not know an active BSR, and will accept the first Bootstrap message it sees as giving the new BSR's identity and the RP-Set. This state exists only if a BSR administrative domain has been configured. * Elected: The router is the elected BSR for the PIM-SM domain and it must perform all the BSR functions. * Candidate: The router is a candidate to be the BSR for the PIM-SM domain, but currently another router is the preferred BSR. * Pending: The router is a candidate to be the BSR for the PIM-SM domain. Currently, no other router is the preferred BSR, but this router is not yet the elected BSR. This is a temporary state that prevents rapid thrashing of the choice of BSR during BSR election. After the elected BSR fails, other C-BSRs enter the Pending state. |
| Uptime | Indicates the running time of the BSR. |