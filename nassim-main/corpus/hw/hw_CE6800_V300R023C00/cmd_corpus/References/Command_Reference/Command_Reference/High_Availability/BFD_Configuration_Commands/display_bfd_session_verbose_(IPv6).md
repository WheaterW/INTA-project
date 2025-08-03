display bfd session verbose (IPv6)
==================================

display bfd session verbose (IPv6)

Function
--------



The **display bfd session verbose** command displays the detailed information of the BFD session for monitoring an IPv6 link.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bfd session peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-name* ] **verbose**

**display bfd session all for-ipv6 verbose**

**display bfd session static for-ipv6 verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer-ipv6** *peer-ipv6* | Displays information about the BFD session with a specified peer IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-name* | Displays information about the BFD session bound to a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **verbose** | Displays detailed information about BFD sessions. | - |
| **all** | Displays information about all BFD sessions. | - |
| **for-ipv6** | Displays information about the BFD session for detecting faults in IPv6 links. | - |
| **static** | Displays information about all static BFD sessions. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view the detailed information of the BFD session for monitoring an IPv6 link, run the display bfd session verbose (IPv6) command.

**Prerequisites**

BFD has been globally enabled using the **bfd** command in the system view.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about all IPv6 BFD sessions.
```
<HUAWEI> display bfd session all for-ipv6 verbose
(w): State in WTR
(*): State is invalid
Total UP/DOWN Session Number : 0/1
--------------------------------------------------------------------------------
  Name : S                                                                (Multiple Hops) State : Down
--------------------------------------------------------------------------------
  Local Discriminator    : 4                Remote Discriminator   : 6
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Peer IP Address
  Bind Session Type      : Static
  Bind Peer IP Address   : 2001:db8::1
  Bind Interface         : -
  FSM Board Id           : -                TOS-EXP                : 7
  Min Tx Interval (ms)   : 1000             Min Rx Interval (ms)   : 1000
  Actual Tx Interval (ms): 2001             Actual Rx Interval (ms): 2001
  WTR Interval (ms)      : -                Detect Interval (ms)   : -
  Local Detect Multi     : 3                Active Multi           : -
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 4784             TTL                    : 255
  Proc Interface Status  : Disable          Process PST            : Disable
  Config PST             : Disable
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : No Application Bind
  Session Not Up Reason  : In negotiation
  Session Description    : -
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display bfd session verbose (IPv6)** command output
| Item | Description |
| --- | --- |
| State | Status of the BFD session:   * Up: The BFD session is in the Up state. * Down: The BFD session is in the Down state. * AdminDown: The BFD session is in the AdminDown state. After the shutdown (BFD session view) command is run, the BFD session becomes AdminDown. * Up(w): indicates that the BFD session is in the Up state and during the WTR time. * Up(\*)/Down(\*): indicates that the BFD session is in the invalid state. * Init: The BFD session is in the Init state. |
| WTR Interval (ms) | Wait-to-restore time of the BFD session. |
| Total UP/DOWN Session Number | UP BFD Session Number/DOWN BFD Session Number. |
| Session Description | Description of the BFD session. |
| Session Detect Mode | Detection mode of the BFD session:   * Asynchronous Mode Without Echo Function. * Asynchronous Mode With Echo Function. * Asynchronous One-arm-echo Mode. |
| Session Not Up Reason | Cause for a session negotiation failure, displayed when a session is in the following state:   * Board selecting failed. * In negotiation: The negotiation fails because no packet is received from the peer end. For example, BFD is configured on only one end. |
| Name | Name of the BFD session. |
| Local Discriminator | Local BFD session discriminator. |
| Local Detect Multi | Configured local detection multiplier of BFD packets. |
| Remote Discriminator | Remote discriminator of the BFD session. |
| Detect Interval (ms) | BFD session detection interval. |
| Echo Passive | Whether the BFD passive Echo function is enabled. The value can be:   * Enable: indicates that the passive Echo function is enabled. * Disable: The passive Echo function is disabled. |
| BFD Bind Type | Binding type of the BFD session:   * Peer Ip Address: The BFD session detects a multi-hop IP link. * For the single-hop IP link to be detected, the interface and the bound local interface are displayed. * Static\_Auto: A static BFD session is established through automatically negotiated discriminators. * VXLAN: indicates that the BFD session detects a VXLAN tunnel. |
| Bind Peer IP Address | Peer IP address of the BFD session. |
| Bind Interface | Outbound interface to which the BFD session is bound. |
| Bind Application | Applications to which a BFD session is bound:   * If the BFD session is not bound to an application, No Application Bind is displayed. * If the BFD session is bound to an interface or a route, specific applications are displayed. For example, if the BFD session is bound to an interface, IFNET is displayed. |
| Bind Session Type | Establishment type of the BFD session:   * Static: A BFD session is established through static configuration. * Dynamic: The establishment of a BFD session is triggered dynamically. * Static\_Auto: A static BFD session is established through automatically negotiated discriminators. |
| FSM Board Id | Slot ID of the main control board where the BFD state machine resides. |
| TOS-EXP | Priority of BFD packets. |
| Min Tx Interval (ms) | Configured minimum interval between sending BFD packets. |
| Min Rx Interval (ms) | Configured minimum interval at which BFD packets are received. |
| Actual Tx Interval (ms) | Indicates the actual minimum interval between sending BFD packets. |
| Actual Rx Interval (ms) | Actual minimum interval between receiving BFD packets. |
| Active Multi | Effective detection multiplier. |
| Destination Port | Destination port number of BFD packets. |
| TTL | TTL of BFD packets. |
| Proc Interface Status | Status of the association between the status of a BFD session and an interface. The value can be:   * Enable: The BFD session is associated with the interface. * Disable: the BFD session is not associated with the interface.   If the process-interface-status command has been configured, the field is displayed as Enable; otherwise, the field is displayed as Disable. |
| Last Local Diagnostic | Local diagnostic cause for the last BFD session in Down state. The value can be:   * Control Detection Time Expired. * No Diagnostic. * Neighbor Signaled Session Down. * Administratively Down. * Neighbor Signaled Session Down (Receive AdminDown). * Concatenated Path Down. * Reverse Concatenated Path Down. |
| Acl Number | ACL number applied to the BFD session. |
| Process PST | Flag of processing the PST:   * Enable: permits the BFD session to modify the PST. * Disable: prohibits the BFD session from modifying the PST.   If the process-pst command has been configured, the field is displayed as Enable; otherwise, the field is displayed as Disable. |
| Config PST | Indicates the ID of the configured port status table. The options are as follows:   * Enable: permits the BFD session to modify the port status table. * Disable: prohibits the BFD session from modifying the port status table.   If the process-pst command is configured, this field is displayed as Enable; otherwise, it is displayed as Disable. |