display pim ipv6 bfd session
============================

display pim ipv6 bfd session

Function
--------



The **display pim ipv6 bfd session** command displays information about PIM IPv6 BFD sessions.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display pim ipv6 bfd session** [ **neighbor** *ipv6-link-local-address* | **interface** { *interface-name* | *interface-type* *interface-number* } ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **neighbor** *ipv6-link-local-address* | Displays information about PIM IPv6 BFD sessions on a specified neighbor. | The value ranges from FE80:: to FE80:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF, in hexadecimal notation. |
| **interface** *interface-type* *interface-number* | Displays information about PIM IPv6 BFD sessions on a specified interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After BFD for IPv6 PIM is configured to detect the status of PIM neighbors, a PIM IPv6 BFD session needs to be established. The **display pim ipv6 bfd session** command can be used to view statistics about and configurations of PIM IPv6 BFD sessions.The following commands are commonly used to view statistics and configurations of PIM IPv6 BFD sessions:

* The **display pim ipv6 bfd session statistics** command is used to display statistics about PIM IPv6 BFD sessions in the public network instance.
* The **display pim ipv6 bfd session** command is used to view information about PIM IPv6 BFD sessions on all interfaces of a device.
* The display pim ipv6 bfd session interface interface-type interface-number neighbor neighbor-address command is used to view information about the PIM IPv6 BFD session on a specified interface or a specified neighbor.On an IPv6 network, information about PIM-SM/SSM IPv6 BFD sessions on the public network instance can be viewed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about PIM IPv6 BFD sessions on all interfaces of the public network instance.
```
<HUAWEI> display pim ipv6 bfd session
 VPN-Instance: public net
 Total 1 BFD session Created

 100GE1/0/1 (FE80::7): Total 1 BFD session Created

 Neighbor        ActTx(ms) ActRx(ms) ActMulti Local/Remote State
 FE80::6         200       300       4         8211/8214   Up

```

# Display information about PIM IPv6 BFD sessions on 100GE1/0/1 in the public network instance.
```
<HUAWEI> display pim ipv6 bfd session interface 100GE 1/0/1
 VPN-Instance: public net

 100GE1/0/1 (FE80::7): Total 1 BFD session Created

 Neighbor        ActTx(ms) ActRx(ms) ActMulti Local/Remote State
 FE80::6         100       100       4         8211/8214   Up

```

**Table 1** Description of the **display pim ipv6 bfd session** command output
| Item | Description |
| --- | --- |
| Total 1 BFD session Created | Total number of established PIM IPv6 BFD sessions. |
| Neighbor | IPv6 address of a PIM neighbor. |
| ActTx(ms) | Actual interval for sending PIM IPv6 BFD packets. |
| ActRx(ms) | Actual interval for receiving PIM IPv6 BFD packets. |
| ActMulti | Actual detection time multiplier of PIM IPv6 BFD packets. |
| Local/Remote | Local/remote discriminator of a PIM IPv6 BFD session. |
| State | Status of a PIM IPv6 BFD session:   * Up: The BFD session is set up and detection packets are exchanged periodically. * Init: The local system can communicate with the peer system and the local system expects the session to go Up. * Admin down: The BFD session is in the AdminDown state (the shutdown command is run in the BFD session view). * Down: The BFD session is in the Down state. |
| VPN-Instance | VPN instance to which PIM IPv6 BFD session information belongs. |