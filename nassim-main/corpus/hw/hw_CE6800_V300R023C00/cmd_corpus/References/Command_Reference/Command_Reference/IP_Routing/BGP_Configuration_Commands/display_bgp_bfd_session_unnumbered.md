display bgp bfd session unnumbered
==================================

display bgp bfd session unnumbered

Function
--------



The **display bgp bfd session unnumbered all** command displays information about BFD sessions established using BGP unnumbered.

The **display bgp bfd session unnumbered peer interface** command displays information about a BFD session with a specified BGP unnumbered peer.




Format
------

**display bgp bfd session unnumbered all**

**display bgp bfd session unnumbered peer interface** { *interface-name* | *IfType* *IFNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **all** | Displays all BFD sessions established by BGP. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



Displays information about BFD sessions established using BGP unnumbered.You can view BFD information about a specified peer by specifying the interface.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all BFD sessions established by BGP unnumbered.
```
<HUAWEI> display bgp bfd session unnumbered all
--------------------------------------------------------------------------------
  Local_Address  : FE80::3A76:9CFF:FE11:300(100GE1/0/1)
  Peer_Address   : FE80::3A76:9CFF:FE21:300(100GE1/0/1)
  Tx-interval(ms): 1000        Rx-interval(ms): 1000
  Multiplier     : 3
  Session-State  : Up
  Wtr-interval(m): 0

  Local_Address  : FE80::3A76:9CFF:FE11:301(100GE1/0/1)
  Peer_Address   : FE80::3A76:9CFF:FE21:301(100GE1/0/1)
  Tx-interval(ms): 1000        Rx-interval(ms): 1000
  Multiplier     : 3
  Session-State  : Up
  Wtr-interval(m): 0

--------------------------------------------------------------------------------

```

# Display information about the BFD session established between 100GE1/0/1 and its peer.
```
<HUAWEI> display bgp bfd session unnumbered peer interface 100GE1/0/1
--------------------------------------------------------------------------------
  Local_Address  : FE80::3A76:9CFF:FE11:301(100GE1/0/1)
  Peer_Address   : FE80::3A76:9CFF:FE21:301(100GE1/0/1)
  Tx-interval(ms): 1000        Rx-interval(ms): 1000
  Multiplier     : 3
  Session-State  : Up
  Wtr-interval(m): 0

--------------------------------------------------------------------------------

```

**Table 1** Description of the **display bgp bfd session unnumbered** command output
| Item | Description |
| --- | --- |
| Local\_Address | Local IP address. |
| Peer\_Address | IP address of a neighbor. |
| Multiplier | Remote detection multiplier. |
| Session-State | BFD status.   * BFD global disable: BFD is disabled. * Up: The BFD session is in the Up state. * Down: The BFD session is in the Down state. * Unknown: When BFD does not go Up through negotiation for the first time, whether the link is faulty is unknown. |
| Tx-interval(ms) | Interval at which BFD packets are sent, in ms. |
| Rx-interval(ms) | Interval at which BFD packets are received, in ms. |
| Wtr-interval(m) | WTR time of the BFD session, in minutes. |