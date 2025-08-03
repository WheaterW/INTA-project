Configuring BFD for IPv4 PIM
============================

After detecting a fault on a peer, BFD immediately instructs the PIM module to trigger a new Designated router (DR) election rather than waits until the neighbor relationship times out. This minimizes the multicast data interruptions and improves the reliability of multicast data transmission.

#### Usage Scenario

Generally, if the active DR on a shared network segment is faulty, other PIM neighbors triggers a new round of DR election only after the neighbor relationship times out. The data transmission interruption duration (usually for some seconds) is not shorter than the timeout period of the neighbor relationships.

BFD for PIM can detect a link's status on a shared network segment within milliseconds and respond quickly to a fault on a PIM neighbor. When BFD detects that a peer is faulty, BFD immediately reports this fault to PIM. PIM then triggers a new round of DR election without waiting for the timeout of neighbor relationships. This minimizes service interruptions and improves the multicast network reliability.

PIM BFD also applies to the assert election on a shared network segment. It can fast respond to the fault of the interface that wins the assert election.


#### Pre-configuration Tasks

Before adjusting other PIM parameters, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure PIM-SM](dc_vrp_multicast_cfg_0006.html).
* [Enable BFD globally](dc_vrp_bfd_cfg_0005.html).


[Enabling PIM BFD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0100.html)

Enable PIM BFD on the devices that set up PIM neighbor relationships.

[(Optional) Adjusting BFD Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0101.html)

PIM BFD parameters include the minimum interval for sending and receiving PIM BFD packets and the local detection multiplier. PIM BFD parameters can be adjusted as needed.

[(Optional) Configuring BFD-based BDR Fast Switching](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_3160.html)

BFD-based BDR fast switching reduces the convergence time and traffic loss during DR re-election triggered by a DR failure.

[Verifying the Configuration of BFD for IPv4 PIM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0102.html)

After configuring BFD for IPv4 PIM, verify information about BFD for IPv4 PIM sessions.