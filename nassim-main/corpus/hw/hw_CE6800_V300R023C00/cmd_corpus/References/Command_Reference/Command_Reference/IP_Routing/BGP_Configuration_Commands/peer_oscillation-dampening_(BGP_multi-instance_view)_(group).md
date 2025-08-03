peer oscillation-dampening (BGP multi-instance view) (group)
============================================================

peer oscillation-dampening (BGP multi-instance view) (group)

Function
--------



The **peer oscillation-dampening disable** command disables a device from suppressing the establishment of BGP connections with peers in a BGP peer group that flap continuously.

The **undo peer oscillation-dampening disable** command cancels the configuration of disabling a device from suppressing the establishment of BGP connections with peers in a BGP peer group that flap continuously.

The **peer oscillation-dampening** command suppresses the establishment of peer relationships that flap continuously in a BGP peer group.

The **undo peer oscillation-dampening** command cancels the configuration of suppressing the establishment of BGP connections with peers in a BGP peer group that flap continuously and restores the default configuration.



By default, BGP suppresses the establishment of a specified peer group's peer relationships that flap continuously.


Format
------

**peer** *peerGroupName* **oscillation-dampening** **disable**

**peer** *peerGroupName* **oscillation-dampening**

**undo peer** *peerGroupName* **oscillation-dampening** **disable**

**undo peer** *peerGroupName* **oscillation-dampening**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After a BGP peer relationship is established, the local device learns all routes from the peer and also advertises its local routes to the peer. If the peer relationship is disconnected, the local device deletes all the routes learned from the peer.Generally, a large number of BGP routes exist, and in this case, a large number of routes change and a large amount of data is processed when the BGP peer relationship is flapping. As a result, a high volume of resources are consumed, causing high CPU usage. To prevent high CPU usage in this case, BGP needs to be enabled to suppress the establishment of the peer relationship if it flaps continuously. Such suppression is implemented for a BGP peer relationship that flaps for more than five times consecutively, and the suppression period increases as the number of flapping times increases. You can run the **display bgp peer verbose** command to check the remaining time that BGP waits to establish the BGP peer relationship.After the peer relationship stops flapping for a certain period, suppression on the peer relationship establishment is automatically removed. To immediately remove the suppression, you can run the **peer oscillation-dampening disable** command. Alternatively, you can run a **reset** command or another command that can cause the peer relationship to be disconnected and re-established.



**Precautions**



By default, the initial time that the device waits to establish a peer relationship is 10s. If the **peer timer connect-retry** command is run, the configured ConnectRetry interval is used as the initial waiting time.If peer dampening is configured and the initial time of waiting for peer relationship establishment is less than 600s, the actual time that the device waits to establish the peer relationship equals the initial waiting time plus the dampening period. The dampening time increases with the number of flapping times until the waiting time for establishing a peer relationship reaches 600s.If the peer oscillation-dampening [ disable ] command is run on the local peer and the specified peer is added to the peer group, the configuration of the peer takes precedence over the configuration of the peer group.If the peer oscillation-dampening [ disable ] command is not run on a local peer, the peer inherits the configurations of the peer group after being added to the peer group, and retains the configurations of the peer group even after being removed from the peer group.




Example
-------

# Disable BGP from suppressing the establishment of a specified peer group's peer relationships that flap continuously.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instanc a
[*HUAWEI-bgp-instance-a] group test internal
[*HUAWEI-bgp-instance-a] peer test oscillation-dampening disable

```