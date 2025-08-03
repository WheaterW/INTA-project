dldp work-mode
==============

dldp work-mode

Function
--------



The **dldp work-mode** command configures a DLDP working mode.

The **undo dldp work-mode** command restores the default mode.



By default, DLDP works in the enhanced mode.


Format
------

**dldp work-mode** { **enhance** | **normal** }

**undo dldp work-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enhance** | Indicates that DLDP works in enhanced mode. | - |
| **normal** | Indicates that DLDP works in normal mode. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A unidirectional link occurs for either of two reasons. One reason is that the fibers are cross connected. The other is that either fiber in a pair is disconnected or broken. The dldp work-mode command configures a working mode in which DLDP operates to detect a specific type of unidirectional link.DLDP operates in either of the following modes:

* In normal mode, DLDP does not actively probe whether a peer exists when the peer entry ages. DLDP detects the existence of unidirectional links caused by cross-connected fibers only. Once the Peer Entry Aging timer expires, the port on which DLDP detects the existence of a unidirectional link removes the peer entry and sends an Advertisement packet with RSY flags.
* In enhanced mode, DLDP actively checks whether a peer exists after the peer entry ages. DLDP detects the existence of unidirectional links caused both by cross-connected fibers and by a disconnected or broken fiber. Once the Peer Entry Aging timer expires, DLDP in enhanced mode triggers the Enhanced timer. After the Enhanced timer is started, the local device sends eight Probe packets to the peer device at intervals of one packet per second. If no Echo packet is received from the peer device after the Echo timer on the local device expires, the port on the local device enters Disable state and sends Disable packets.

**Prerequisites**

DLDP has been enabled globally using the **dldp enable** command.


Example
-------

# Enable DLDP to work in enhanced mode.
```
<HUAWEI> system-view
[~HUAWEI] dldp enable
[*HUAWEI] dldp work-mode enhance

```