display pim neighbor
====================

display pim neighbor

Function
--------



The **display pim neighbor** command displays information about PIM neighbors.




Format
------

**display pim neighbor** [ *nbrAddrValue* | **interface** { *port-name* | *port-type* *port-num* } | **verbose** ] \*

**display pim** { **vpn-instance** *vpn-instance-name* | **all-instance** } **neighbor** [ *nbrAddrValue* | **interface** { *port-name* | *port-type* *port-num* } | **verbose** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *nbrAddrValue* | Specifies the IP address of a PIM neighbor. | The value is in dotted decimal notation. |
| **interface** *port-type* | Specifies the type an interface. | - |
| *port-name* | Specifies the name of an interface. | - |
| *port-num* | Specifies the number of an interface. | - |
| **verbose** | Displays detailed information about PIM neighbors. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Indicates all instances. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check information about PIM neighbors that PIM-enabled interfaces have established with interfaces of other devices, run the **display pim neighbor** command. The command output includes the IP address of a PIM neighbor, total Up time of a neighbor relationship, and designated router (DR) priority.

**Precautions**

If neither vpn-instance nor all-instance is specified, the command displays information about PIM neighbors in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the PIM-DM neighbor 10.1.2.2 in the public network instance.
```
<HUAWEI> display pim neighbor 10.1.2.2 verbose
 VPN-Instance: public net
Neighbor: 10.1.2.2
     Interface: 100GE1/0/1
     Uptime: 05:32:08
     Expiry time: 00:01:41
     DR Priority: 1
     Generation ID: 0x3E4E01A6
     Holdtime: 105 s
     LAN delay: 500 ms
     Override interval: 2500 ms
     State refresh interval: 60 s
     Neighbor tracking: disabled
     PIM BFD-session: N
     PIM join attribute: disabled
     PIM BIDIR: N

```

# Display information about PIM neighbors in the public network instance.
```
<HUAWEI> display pim neighbor
 VPN-Instance: public net
 Total Number of Neighbors = 2
Neighbor        Interface      Uptime       Expires      Dr-Priority  BFD-Session 
 10.1.1.2        100GE1/0/1       02:50:49     00:01:31     1            Y
 10.1.1.4        100GE1/0/2      02:49:39     00:01:42     1            Y

```

# Display detailed information about the PIM-SM neighbor 10.1.1.2 in the public network instance.
```
<HUAWEI> display pim neighbor 10.1.1.2 verbose
 VPN-Instance: public net
 Neighbor: 10.1.1.2
     Interface: 100GE1/0/1
     Uptime: 02:53:50
     Expiry time: 00:01:30
     DR Priority: 1
     Generation ID: 0X90B0360B
     Holdtime: 105 s
     LAN delay: 500 ms
     Override interval: 2500 ms
     Neighbor tracking: disabled
     PIM BFD-Session: Y
     PIM BFD-Session Actual min-tx-interval: 1000 ms
     PIM BFD-Session Actual min-rx-interval: 1000 ms
     PIM BFD-Session Active detect-multiplier: 3
     PIM BIDIR: Y

```

**Table 1** Description of the **display pim neighbor** command output
| Item | Description |
| --- | --- |
| Expiry time | Time after which the PIM neighbor relationship will expire. |
| DR Priority | DR priority. |
| Generation ID | Random number of the PIM neighbor status. |
| LAN delay | Delay for transmitting Prune messages. |
| Override interval | Interval for overriding the Prune action. |
| State refresh interval | Interval at which the PIM state is refreshed. |
| Neighbor | Address of the PIM neighbor. |
| Neighbor tracking | Whether neighbor tracking is enabled. |
| PIM BFD-session | Whether the BFD session is set up. |
| PIM BFD-Session Actual min-tx-interval | Actual minimum interval at which PIM BFD messages are sent. |
| PIM BFD-Session Actual min-rx-interval | Actual minimum interval at which PIM BFD messages are received. |
| PIM BFD-Session Active detect-multiplier | Actual detection multiplier of the PIM BFD session. |
| PIM join attribute | Whether the Join attribute capability is enabled on the PIM neighbor. |
| PIM BIDIR | Whether BIDIR-PIM is enabled on the neighbor. |
| Total Number of Neighbors = 2 | Total number of PIM neighbors. |
| Interface | Interface on which the PIM neighbor relationship is established. |
| Uptime | Time since the PIM neighbor relationship was established. |
| VPN-Instance | Instance to which the PIM neighbor belongs. |
| Holdtime | Holdtime of the PIM neighbor relationship. |