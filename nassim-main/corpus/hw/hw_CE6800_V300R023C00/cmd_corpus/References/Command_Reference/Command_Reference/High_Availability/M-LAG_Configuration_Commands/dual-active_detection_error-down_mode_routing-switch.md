dual-active detection error-down mode routing-switch
====================================================

dual-active detection error-down mode routing-switch

Function
--------



The **dual-active detection error-down mode routing-switch** command triggers logical interfaces to enter the Error-Down state when the peer-link fails but the DAD status is normal in an M-LAG scenario.

The **undo dual-active detection error-down mode routing-switch** command restores the default configuration.



By default, logical interfaces are not triggered to enter the Error-Down state when the peer-link fails but the DAD status is normal in an M-LAG scenario.


Format
------

**dual-active detection error-down mode routing-switch**

**undo dual-active detection error-down mode routing-switch**


Parameters
----------

None

Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, logical interfaces are not triggered to enter the Error-Down state when the peer-link fails but the DAD status is normal in an M-LAG scenario. When M-LAG is used for dual-homing access on a common Ethernet or IP network (VRRP active-active gateways), if the peer-link fails but the DAD status is normal, physical interfaces except the logical interfaces, interface configured with the reserved function, management interface, and peer-link interface on one device are triggered to enter the Error-Down state.On an IP network or a VXLAN network where M-LAG is deployed, when logical interfaces are configured to enter the Error-Down state when the peer-link fails but the DAD status is normal, only VLANIF interfaces, VBDIF interfaces, loopback interfaces, and M-LAG member interface on one M-LAG device are triggered to enter the Error-Down state.

**Precautions**

1. Before this command is used, ensure that the heartbeat link is independent or is not connected to the interface in Error-Down state.
2. After logical interfaces are configured to change to Error-Down state when the peer-link fails but the DAD heartbeat status is normal in an M-LAG, if a faulty peer-link interface in the M-LAG recovers, the devices restore VLANIF interfaces, VBDIF interfaces, and loopback interfaces to Up state 6 seconds after DFS group pairing succeeds to ensure that ARP entry synchronization on a large number of VLANIF interfaces is normal. If a delay after which the Layer 3 protocol status of the interface changes to Up is configured, the delay after which VLANIF interfaces, VBDIF interfaces, and loopback interfaces go Up is the configured delay plus 6s.

Example
-------

# Configure logical interfaces to enter the Error-Down state when the peer-link fails but the DAD status is normal in an M-LAG scenario.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] dual-active detection error-down mode routing-switch

```