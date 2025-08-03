display bfd statistics session
==============================

display bfd statistics session

Function
--------



The **display bfd statistics session** command displays statistics about BFD sessions.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bfd statistics session all** [ **for-ip** ]

**display bfd statistics session static** [ **for-ip** ]

**display bfd statistics session dynamic**

**display bfd statistics session discriminator** *discr-value*

**display bfd statistics session peer-ip** { *peer-ip* [ **vpn-instance** *vpn-instance-name* ] | **default-ip** }

**display bfd statistics session static-auto**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bfd statistics session peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-instance-name* ]

**display bfd statistics session all for-ipv6**

**display bfd statistics session static for-ipv6**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **for-ip** | Displays statistics on BFD sessions for detecting IP links. | - |
| **all** | Displays statistics about all BFD sessions. | - |
| **static** | Displays statistics about static BFD sessions. | - |
| **default-ip** | Displays statistics about multicast BFD sessions. | - |
| **peer-ipv6** *peer-ipv6* | Displays statistics about the BFD sessions bound to a specified peer IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **dynamic** | Displays statistics about all dynamic BFD sessions and static BFD sessions with automatically negotiated discriminators. | - |
| **discriminator** *discr-value* | Displays statistics about the BFD sessions with a specified local discriminator. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Displays statistics about the BFD sessions bound to a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **static-auto** | Displays statistics about the static BFD sessions with automatically negotiated discriminators. | - |
| **for-ipv6** | Displays statistics about the BFD sessions for detecting IPv6 links.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view statistics about BFD sessions, run the **display bfd statistics session** command.

**Precautions**

* If a static BFD session with automatically negotiated discriminators and a dynamic BFD session have the same configurations, you can view that the shared BFD session belongs to both the static session and the dynamic session in terms of the BFD session type.
* Run the **reset bfd statistics** command to clear statistics about received and sent BFD packets before collecting statistics about BFD sessions by running the **display bfd statistics session** command.
* The **display bfd statistics session dynamic** command displays statistics about both dynamic and static sessions. The statically self-negotiated sessions are treated as dynamic sessions.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about all BFD sessions.
```
<HUAWEI> display bfd statistics session all
(w): State in WTR 
(*): State is invalid
Total Session Number :  1
--------------------------------------------------------------------------------
  Name : aaa                                                              (Multiple Hops) State : Up
--------------------------------------------------------------------------------
  Session Type                        : Static
  Bind Type                           : IP  
  Local/Remote Discriminator          : 1/2
  Received Packets                    : 5
  Send Packets                        : 18808
  Received Bad Packets                : 0
  Send Bad Packets                    : 0
  Down Count                          : 0
  Create Time                         : 2012-11-17 21:14:47
  Total Time From Create              : 000:10:58:18 (DDD:HH:MM:SS) 
  Last Down Time                      : --
  Total Time From Last DOWN           : --
  Last Up Time                        : 2012-11-17 21:14:50 
  Last Up Lasting Time                : 000:00:00:07 (DDD:HH:MM:SS)
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display bfd statistics session** command output
| Item | Description |
| --- | --- |
| State | Current status of the BFD session. The values are as follows:   * Up: The BFD session is in the Up state. * Down: The BFD session is in the Down state. * AdminDown: The BFD session is in the AdminDown state. After the shutdown (BFD session view) command is run, the BFD session is in the AdminDown state. * Init: The BFD session is in the Init state. * Up(w): The BFD session is Up but is in the WTR state. * Up(\*)/Down(\*): The BFD session status is invalid. |
| Name | Name of the BFD session. |
| Session Type | Ways of establishing BFD sessions. The values are as follows:   * Static: The BFD session is set up through static configuration. * Dynamic: The establishment of a BFD session is triggered dynamically. * Static\_Auto: The BFD session is established using automatically negotiated discriminators. |
| Bind Type | BFD session binding types. The values are as follows:   * IP: The BFD session detects a link. * VXLAN: The BFD session detects a VXLAN tunnel. |
| Local/Remote Discriminator | Local discriminator and remote discriminator of the BFD session. |
| Received Packets | Number of BFD packets received by the local end. This field can be cleared using the reset bfd statistics command. |
| Received Bad Packets | Number of received error packets. |
| Send Packets | Number of BFD packets sent by the local end. This field can be cleared using the reset bfd statistics command. |
| Send Bad Packets | Number of packets that fail to be sent. |
| Down Count | Number of times that the BFD session goes down. |
| Create Time | Time when the BFD session was created. |
| Total Time From Create | Time elapsed since the BFD session was created. |
| Total Session Number | Number of BFD sessions. |
| Total Time From Last DOWN | Time elapsed since the last BFD session went Down. |
| Last Down Time | Time when the BFD session was last Down. |
| Last Up Time | Date and time when the BFD session was last up. |
| Last Up Lasting Time | Duration of the last up BFD session. |