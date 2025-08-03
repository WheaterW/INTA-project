display bfd session verbose
===========================

display bfd session verbose

Function
--------



The **display bfd session verbose** command displays detailed information about BFD sessions.




Format
------

**display bfd session all** [ **for-ip** | **for-srv6-segment-list** ] **verbose**

**display bfd session passive-dynamic** [ **peer-ip** *peer-ip* **remote-discriminator** *discr-value* ] **verbose**

**display bfd session dynamic verbose**

**display bfd session discriminator** *discr-value* **verbose**

**display bfd session peer-ip** { *peer-ip* [ **vpn-instance** *vpn-name* ] | **default-ip** } **verbose**

**display bfd session static-auto verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **for-ip** | Displays detailed information about the BFD session for detecting faults in IP links. | - |
| **all** | Displays detailed information about all BFD sessions. | - |
| **static** | Displays detailed information about all static BFD sessions. | - |
| **passive-dynamic** | Displays detailed information about the BFD sessions that are passively created. | - |
| **peer-ip** *peer-ip* | Displays detailed information about the BFD session with a specified peer IP address. | The value is in dotted decimal notation. |
| **remote-discriminator** *discr-value* | Displays detailed information about a BFD session with a specified remote discriminator. | The value is an integer ranging from 1 to 4294967295. |
| **dynamic** | Displays detailed information about dynamic and statically self-negotiated BFD sessions. | - |
| **discriminator** *discr-value* | Displays detailed information about a BFD session with a specified local discriminator. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-name* | Displays detailed information about the BFD session bound to a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **default-ip** | Displays statistics about BFD sessions with the default multicast address. | - |
| **static-auto** | Displays detailed information about static BFD sessions with automatically negotiated discriminators. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view detailed information about BFD sessions, run the **display bfd session verbose** command with one or more parameters.

**Prerequisites**



BFD has been globally enabled using the **bfd** command in the system view.



**Precautions**

* When the BFD session changes from Down to Up, and the WTR time is not zero, the notification that the BFD session goes Up can be received only after the WTR time expires.
* If a static BFD session with automatically negotiated discriminators and a dynamic BFD session have the same configurations, you can view that the shared BFD session belongs to both the static session with automatically negotiated discriminators and the dynamic session in terms of the BFD session type.
* The **display bfd session dynamic** command displays information about both dynamic and static sessions. The statically self-negotiated sessions are treated as dynamic sessions.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about all BFD sessions.
```
<HUAWEI> display bfd session all verbose
(w): State in WTR
(*): State is invalid
Total UP/DOWN Session Number : 0/1
--------------------------------------------------------------------------------
  Name : a                                                                (Multiple Hops) State : Down
--------------------------------------------------------------------------------
  Local Discriminator    : 1                Remote Discriminator   : 2
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Peer IP Address
  Bind Session Type      : Static
  Bind Peer IP Address   : 10.0.0.2
  Bind Interface         : -
  Bind Source IP Address : 10.0.0.1
  FSM Board ID           : -                ToS-EXP                : 7
  Min Tx Interval (ms)   : 1000             Min Rx Interval (ms)   : 1000
  Actual Tx Interval (ms): 2000             Actual Rx Interval (ms): 2000
  WTR Interval (ms)      : -                Detect Interval (ms)   : -
  Local Detect Multi     : 3                Active Multi           : -
  Echo Passive           : Disable          Acl Number             : -
  Destination Port       : 4784             TTL                    : 254
  Proc Interface Status  : Disable          Process PST            : Disable
  Config PST             : Disable
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : No Application Bind
  Session Not Up Reason  : In negotiation
  Session Description    : -
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display bfd session verbose** command output
| Item | Description |
| --- | --- |
| State | Current status of the BFD session. The value can be:   * Up: The BFD session is in the Up state. * Down: The BFD session is in the Down state. * AdminDown: The BFD session is in the AdminDown state. After the shutdown (BFD session view) command is run, the BFD session becomes AdminDown. * Up(w): The BFD session is Up but is in the WTR state. * Up(\*)/Down(\*): The BFD session status is invalid. * Init: The BFD session is in the Init state. |
| WTR Interval (ms) | WTR time of a BFD session. |
| Total UP/DOWN Session Number | Number of BFD sessions in the Up or Down state. |
| Session Description | Description of the BFD session. |
| Session Detect Mode | Detection mode of the BFD session. The value can be:   * Asynchronous Mode Without Echo Function. * Asynchronous Mode With Echo Function. * Asynchronous One-arm-echo Mode. |
| Session Not Up Reason | Reason why the session does not go up through negotiation. This field is displayed when the session is in the Down or Init state. The possible causes and solutions are as follows:   * Board selecting failed: Board selection fails. * In negotiation: The session is being negotiated and does not go Up because no packet is received from the peer end. For example, BFD is configured only on one end. |
| Name | BFD session name. |
| Local | Local discriminator of a BFD session. |
| Local Discriminator | Local discriminator of a BFD session. |
| Local Detect Multi | Configured local detection multiplier of BFD packets. |
| Remote | Remote discriminator of a BFD session. |
| Remote Discriminator | Remote discriminator of a BFD session. |
| Detect Interval (ms) | Indicates the detection time of the BFD session.  If the BFD session detection time is shorter than the link delay, run the detect-multiplier, min-rx-interval, and min-tx-interval commands to increase the BFD session detection time to be longer than the link delay. |
| Echo Passive | Whether the BFD passive Echo function is enabled. The value can be:   * Enable: The passive echo function is enabled. * Disable: The passive echo function is disabled. |
| BFD Bind Type | BFD session binding type. The value can be:   * Peer Ip Address: indicates the BFD session that detects the multi-hop IP link. * For single-hop IP link detection, this field displays interface and the bound local interface. * Static\_Auto: indicates a static BFD session with automatically negotiated discriminators. * VXLAN: indicates a BFD session for detecting VXLAN tunnels. |
| Bind Peer IP Address | Peer IP address tracked by BFD. |
| Bind Interface | Outbound interface bound to the BFD session. |
| Bind Source IP Address | Source IP address of the local interface bound to the BFD session. The Bind Source Ip Address field is displayed only if the source IP address is specified in creating a BFD session by running the bfd bind peer-ip command. |
| Bind Application | Application to which the BFD session is bound:   * If the BFD session is not bound to an application, No Application Bind is displayed. * If the BFD session is bound to an interface or a route, the specific application is displayed. For example, if an interface is bound to the BFD session, IFNET is displayed. |
| Bind Session Type | BFD session type:   * Static: statically configured BFD session. * Dynamic: dynamically triggered BFD session. * Static\_Auto: static BFD session with automatically negotiated discriminators. |
| FSM Board Id | Slot ID of the main control board where the BFD state machine resides. |
| Min Tx Interval (ms) | Configured minimum interval for sending BFD packets. |
| Min Tx Interval (ms) | Configured minimum interval for sending BFD packets. |
| Min Rx Interval (ms) | Configured minimum interval at which BFD packets are received. |
| Actual Tx Interval (ms) | Actual minimum interval between sending BFD packets. |
| Actual Rx Interval (ms) | Actual minimum interval at which BFD packets are received. |
| Active Multi | Active detection multiplier of the BFD session. |
| Destination Port | Destination port number of BFD packets. |
| TTL | TTL of BFD packets. |
| Proc Interface Status | Status of the association between the status of a BFD session and an interface. The value can be:   * Enable: The BFD session is associated with the interface. * Disable: the BFD session is not associated with the interface.   If the process-interface-status command has been configured, the field is displayed as Enable; otherwise, the field is displayed as Disable. |
| Last Local Diagnostic | Local diagnostic cause for the last BFD session in Down state. The value can be:   * Control Detection Time Expired. * No Diagnostic. * Neighbor Signaled Session Down. * Administratively Down. * Neighbor Signaled Session Down (Receive AdminDown). * Concatenated Path Down. * Reverse Concatenated Path Down. |
| Acl Number | ACL number applied to the BFD session. |
| Process PST | Flag for processing the Port Status Table (PST). The value can be:   * Enable: The BFD session is allowed to modify the PST. * Disable: The BFD session is disabled from modifying the PST.   If the process-pst command is configured and takes effect, this field is displayed as Enable. Otherwise, this field is displayed as Disable. |
| Config PST | PST status. The value can be:   * Enable: The BFD session is allowed to modify the PST. * Disable: The BFD session is disabled from modifying the PST.   If the process-pst command is configured, this field is displayed as Enable. Otherwise, this field is displayed as Disable. |
| TOS-EXP | Priority of BFD packets. |