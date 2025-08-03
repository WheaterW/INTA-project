bfd all-interfaces (OSPF view)
==============================

bfd all-interfaces (OSPF view)

Function
--------



The **bfd all-interfaces** command sets the parameter values of a BFD session.

The **undo bfd all-interfaces** command restores the default parameter values of a BFD session.



By default, BFD is disabled.


Format
------

**bfd all-interfaces** { **min-tx-interval** *transmit-interval* | **min-rx-interval** *receive-interval* | **detect-multiplier** *multiplier-value* | **frr-binding** } \*

**undo bfd all-interfaces** { **min-tx-interval** [ *transmit-interval* ] | **min-rx-interval** [ *receive-interval* ] | **detect-multiplier** [ *multiplier-value* ] | **frr-binding** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-tx-interval** *transmit-interval* | Specifies the minimum interval at which BFD packets are sent to the remote device. | The value is an integer ranging from 3 to 1000, in milliseconds. |
| **min-rx-interval** *receive-interval* | Specifies the minimum interval for receiving BFD messages from the peer. | The value is an integer ranging from 3 to 1000, in milliseconds. |
| **detect-multiplier** *multiplier-value* | Specifies the local detect multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |
| **frr-binding** | Associates the BFD session status with the link status on an interface. If BFD detects a link fault on an interface, the BFD session goes Down, triggering FRR. Traffic is then quickly switched to the backup link, minimizing service loss. | - |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Any link failure or topology change causes routers to re-calculate routes, and the convergence of routing protocols affects network performance.If BFD is associated with routing protocols, BFD can fast detect faults and notify routing protocols of the faults immediately, which speeds up the convergence of routing protocols.OSPF IP FRR requires the lower layer to fast respond to the link change so that traffic can be rapidly switched to the backup link if a link fails. In such a case, if frr-binding is configured, the association between the BFD session status and link status is enabled on an interface. If the BFD session on the interface becomes Down, the link goes Down immediately.



**Prerequisites**

BFD has been enabled in the OSPF process using the **bfd all-interfaces enable** command.


Example
-------

# Configure BFD in an OSPF process and set the minimum interval at which BFD packets are sent to 300 ms.
```
<HUAWEI> system-view
[~HUAWEI] ospf
[*HUAWEI-ospf-1] bfd all-interfaces enable
[*HUAWEI-ospf-1] bfd all-interface min-tx-interval 300

```