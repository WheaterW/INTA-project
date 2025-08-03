display pim bsr-info
====================

display pim bsr-info

Function
--------



The **display pim bsr-info** command displays information about bootstrap routers (BSRs) in a PIM-SM domain.




Format
------

**display pim vpn-instance** *vpn-instance-name* **bsr-info**

**display pim** [ **all-instance** ] **bsr-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all-instance** | Displays information about BSRs in all instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays information about the BSR in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to the PIM-SM domain where a rendezvous point (RP) is dynamically elected using the BSR mechanism. You can run this command on any Router in the domain to view BSR information.

* If a candidate-bootstrap router (C-BSR) is configured on a Router, the command displays information about the elected BSR and locally configured C-BSR.
* If a candidate-bootstrap router (C-BSR) is not configured on a Router, the command displays information only about the elected BSR

**Precautions**

If neither vpn-instance nor all-instance is specified, the command displays information about the BSR in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the BSR in the public network instance. If a C-BSR is configured on a router, the command displays information about the elected BSR and configured C-BSR.
```
<HUAWEI> display pim bsr-info
 VPN-Instance: public net
 Elected AdminScope BSR Count: 0
 Elected BSR Address: 10.1.2.2
     Priority: 0
     Hash mask length: 30
     State: Elected
     Scope: Not scoped
     Uptime: 00:10:42
     Next BSR message scheduled at: 00:00:31
     C-RP Count: 1
 Candidate AdminScope BSR Count: 0
 Candidate BSR Address: 10.1.2.2
     Priority: 0
     Hash mask length: 30
     State: Elected
     Scope: Not scoped
     Wait to be BSR: 0

```

# Display information about the BSR in the public network instance. If a C-BSR is not configured on a Router, the command displays information only about the elected BSR.
```
<HUAWEI> display pim bsr-info
 VPN-Instance: public net
 Elected AdminScope BSR Count: 0
 Elected BSR Address: 10.1.2.2
     Priority: 0
     Hash mask length: 30
     State: Accept Preferred
     Scope: Not scoped
     Uptime: 00:01:46
     Expires: 00:02:02
     C-RP Count: 1

```

**Table 1** Description of the **display pim bsr-info** command output
| Item | Description |
| --- | --- |
| Elected AdminScope BSR Count | Number of elected BSRs in administrative domains. |
| Elected BSR Address | Address of the elected BSR. |
| Hash mask length | Mask length in the RP hash calculation. |
| Next BSR message scheduled at | Period after which the next BSR message is sent.  BSR messages are sent only when the timer maintained by the elected BSR times out. |
| C-RP Count | Number of RPs learned through the BSR. |
| Candidate AdminScope BSR Count | Number of C-BSRs in administrative domains. |
| Candidate BSR Address | Address of a C-BSR. |
| Wait to be BSR | Whether the current C-BSR is valid (0: valid; 1: invalid). |
| VPN-Instance | Instance in which information about BSRs is displayed. |
| Priority | Priority of the BSR. By default, the value is 0. |
| State | Status of the BSR.   * Accept Preferred: The router knows the current BSR, and is using the RP-set provided by that BSR. Only bootstrap messages from that BSR or from a C-BSR with higher weight than the current BSR will be accepted. * Accept Any: The router does not know an active BSR, and will accept the first bootstrap message it sees as giving the new BSR's identity and the RP-set. This state exists only if a BSR administrative domain has been configured. * Elected: The router is the elected BSR for the PIM-SM domain and it must perform all the BSR functions. * Candidate: The router is a candidate to be the BSR for the PIM-SM domain, but currently another router is the preferred BSR. * Pending: The router is a candidate to be the BSR for the PIM-SM domain. Currently, no other router is the preferred BSR, but this router is not yet the elected BSR. This is a temporary state that prevents rapid thrashing of the choice of BSR during BSR election. After the elected BSR fails, other C-BSRs enter the pending state. |
| Scope | Range of multicast addresses in the administrative scope when the BSR is a BSR in an administrative domain.  Not scoped: indicates that the BSR is not in an administrative domain. |
| Uptime | Period since the BSR became Up. |
| Expires | Period after which the BSR expires. |