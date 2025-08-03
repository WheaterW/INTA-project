Configuring BFD for IPv6 PIM
============================

After detecting a fault on the peer, Bidirectional Forwarding Detection (BFD) immediately instructs the PIM module to trigger a new Designated router (DR) election rather than waits until the neighbor relationship times out. This shortens the period during which multicast data transmission is discontinued and thus improves the reliability of multicast data transmission.

#### Usage Scenario

Generally, if the active DR on a shared network segment is faulty, other IPv6 PIM neighbors triggers a new round of DR election only after the neighbor relationship times out. The duration that data transmission is interrupted is not shorter than the timeout period of the neighbor relationship. Generally, it is of second level.

BFD features fast detection of faults, and is up to the millisecond level. BFD can detect statuses of IPv6 PIM neighbors in the shared network segment. When BFD detects that a peer is faulty, BFD immediately reports this fault to PIM. PIM then triggers a new round of DR election without waiting for the timeout of the neighbor relationship. This shortens the duration of interruption of data transmission and enhances the reliability of the network.

IPv6 BFD for PIM is also applicable to the assert election in a shared network segment. It can fast respond to the fault of the interface that wins the assert election.


#### Pre-configuration Tasks

Before configuring IPv6 BFD for PIM, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure IPv6 PIM-SM](dc_vrp_multicast_cfg_2005.html).
* [Enable BFD globally](dc_vrp_bfd_cfg_0005.html).


[Enabling BFD for IPv6 PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2176.html)

BFD detection responds to the fault occurring on the current Designated router (DR) or Assert winner on the shared network segment and instructs the PIM to trigger a new DR or Assert election. This shortens the period during which multicast data transmission is discontinued.

[(Optional) Adjusting BFD Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2177.html)

IPv6 PIM BFD does not apply to Point-to-point (P2P) interfaces. IPv6 PIM BFD parameters include the minimum interval for sending and receiving PIM BFD packets and the local detection multiplier. BFD negotiates actual parameter values of detection packets based on configurations on the two ends.

[Verifying the Configuration of BFD for IPv6 PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2178.html)

After configuring BFD for IPv6 PIM, verify statistics about and configurations of BFD for IPv6 PIM sessions.