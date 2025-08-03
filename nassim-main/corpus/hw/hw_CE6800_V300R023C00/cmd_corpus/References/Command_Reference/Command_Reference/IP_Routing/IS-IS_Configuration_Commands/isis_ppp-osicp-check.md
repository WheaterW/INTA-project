isis ppp-osicp-check
====================

isis ppp-osicp-check

Function
--------



The **isis ppp-osicp-check** command enables OSICP check on a PPP interface.

The **undo isis ppp-osicp-check** command cancels the setting.



By default, IS-IS ignores checking OSICP.


Format
------

**isis ppp-osicp-check**

**undo isis ppp-osicp-check**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, OSICP status of PPP does not affect IS-IS interface status.After the isis ppp-osicp-check command is run, OSI network negotiation status of PPP affects IS-IS interface status. When PPP detects a failure on the OSI network, the link status of the IS-IS interface goes Down, and the route to the network segment where the interface resides is not advertised through LSPs.For a broadcast interface, set the link type of the interface to P2P before running the isis ppp-osicp-check command.


Example
-------

# Enable a specified interface to perform PPP OSICP check.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable
[*HUAWEI-100GE1/0/1] isis circuit-type p2p
[*HUAWEI-100GE1/0/1] isis ppp-osicp-check

```