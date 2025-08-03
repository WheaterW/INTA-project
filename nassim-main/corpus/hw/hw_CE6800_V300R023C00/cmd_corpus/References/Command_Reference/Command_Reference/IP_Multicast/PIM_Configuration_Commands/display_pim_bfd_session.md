display pim bfd session
=======================

display pim bfd session

Function
--------



The **display pim bfd session** command displays information about PIM BFD sessions.




Format
------

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **bfd** **session** [ **interface** { *interface-name* | *interface-type* *interface-number* } | **neighbor** *neighbor-address* ] \*

**display pim bfd session** [ **interface** { *interface-name* | *interface-type* *interface-number* } | **neighbor** *neighbor-address* ] \*

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **bfd** **session** **statistics**

**display pim bfd session statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays information about PIM BFD sessions in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of case-sensitive characters. |
| **all-instance** | Displays information about PIM BFD sessions in all instances. | - |
| **interface** *interface-type* | Displays information about PIM BFD sessions on a specified interface type. | - |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-number* | Displays information about PIM BFD sessions on a specified interface number. | - |
| **neighbor** *neighbor-address* | Displays information about PIM BFD sessions established with a specified neighbor.  Specifies the IP address of a PIM neighbor. | The value is in dotted decimal notation. |
| **statistics** | Displays statistics about PIM BFD sessions. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When using the **display pim bfd session** command, note the following:

* If neither vpn-instance nor all-instance is specified, the command displays information about PIM BFD sessions in the public network instance.
* If neither interface nor neighbor is specified, the command displays information about PIM BFD sessions on all interfaces in a specified instance.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about PIM BFD sessions established with the PIM neighbor 10.1.2.3 in the public network instance.
```
<HUAWEI> display pim bfd session neighbor 10.1.2.3
 VPN-Instance: public net
100GE1/0/1 (10.1.2.2): Total 1 BFD session Created
 Neighbor     ActTx(ms)     ActRx(ms)     ActMulti     Local/Remote     State
 10.1.2.3     20             20              5         8756/8652          Up

```

# Display statistics about PIM BFD sessions.
```
<HUAWEI> display pim bfd session statistics
 VPN-Instance: public net
  Total 1 PIM BFD session in this instance.

   Total 0 PIM BFD session up.
   Total 1 PIM BFD session down.

```

# Display information about PIM BFD sessions on all interfaces in all instances.
```
<HUAWEI> display pim all-instance bfd session
 All-instance: Total 4 BFD sessions Created
 VPN-Instance: public net
 Total 4 BFD sessions Created
 100GE1/0/1 (10.1.2.2): Total 2 BFD sessions Created
 Neighbor     ActTx(ms)     ActRx(ms)     ActMulti     Local/Remote     State
 10.1.2.3     20            20            5            8756/8652          Up
 10.1.2.4     30            30            3            8754/8423          Up
 100GE1/0/2 (10.20.1.20): Total 2 BFD sessions Created
 Neighbor     ActTx(ms)     ActRx(ms)     ActMulti     Local/Remote     State
 10.20.1.30   30            30            5            8327/8891          Up
 10.20.1.40   50            50            3            8358/8942          Up

```

# Display information about PIM BFD sessions on GE 1/0/1 in the public network instance.
```
<HUAWEI> display pim bfd session interface 100GE 1/0/1
 VPN-Instance: public net
 100GE1/0/1 (10.1.2.2): Total 2 BFD sessions Created
 Neighbor     ActTx(ms)     ActRx(ms)     ActMulti     Local/Remote     State
 10.1.2.3     20             20              5         8756/8652          Up
 10.1.2.4     30             30              3         8754/8423          Up

```

**Table 1** Description of the **display pim bfd session** command output
| Item | Description |
| --- | --- |
| Total 1 PIM BFD session in this instance | Total number of PIM BFD sessions in an instance. |
| Total 0 PIM BFD session up | Number of PIM BFD sessions in the Up state in an instance. |
| Total 1 PIM BFD session down | Number of PIM BFD sessions in the down state in a public network instance or a VPN instance, that is, all PIM BFD sessions except the PIM BFD sessions in the up state. |
| Neighbor | IP address of a PIM neighbor. |
| ActTx(ms) | Actual minimum BFD packet transmit interval, in milliseconds. |
| ActRx(ms) | Actual minimum BFD packet receive interval, in milliseconds. |
| ActMulti | Actual local detection multiple. |
| Local/Remote | Local and remote discriminators. |
| State | Status of a PIM BFD session.   * Up: indicates that the BFD session is set up successfully and detection packets are periodically exchanged. * Init: indicates that the local end can communicate with the remote end and wants the session status to be Up. * Admin down: indicates that the session is in the administratively Down state (The shutdown command is run in the BFD session view). * Down: indicates that the BFD session is Down. |
| 100GE1/0/1 (10.1.2.2) | Type, number, and IP address of an interface. |