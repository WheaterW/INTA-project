Understanding BGP GR
====================

Graceful restart (GR) is a high availability (HA) technology. HA comprises a comprehensive set of techniques, such as fault-tolerant redundancy, link protection, faulty node recovery, and traffic engineering. As a fault-tolerant redundancy technology, GR ensures normal forwarding of data during the restart of routing protocols to prevent the interruption of key services, and has been widely applied to the master/slave switchover and system upgrade.

GR is typically used when the active route processor (RP) fails due to a software or hardware error or when an administrator performs an active/standby switchover.

![](public_sys-resources/note_3.0-en-us.png) 

You are advised not to configure both BFD and BGP GR on the same device. If both are configured and a BFD session detects a fault on an interface, the session exits GR. As a result, traffic forwarded based on GR is interrupted, which may cause network problems.


#### Related Concepts

Concepts related to GR are as follows:

* GR Restarter: indicates a device that performs active/standby switchover triggered by the administrator or a failure. A GR Restarter must support GR.
  
  + Force-Quit timer: indicates the timer used to exit GR forcibly in a scenario where GR cannot exit automatically due to internal errors.
  + Protection timer: indicates the timer used for protection in a scenario where no peers are up.
  + Wait-All-Peer-Up timer: indicates the timer for waiting for all peers to go up in a scenario where some peers are not up.
  + Selection-Deferral timer: indicates the timer used for protection in a scenario where a Helper does not send End-of-RIB (EOR) messages.
  + EOR timer: indicates the maximum period during which a GR Restarter waits for EOR messages from a GR Helper. If a GR Restarter does not receive any EOR message from a GR Helper within the EOR timer, the GR Restarter selects routes based on the existing routes.
* GR Helper: indicates a peer of a GR Restarter. A GR Helper must support GR.
  
  + GR timer: indicates the period during which a GR Helper retains the topology information or routes obtained from the GR Restarter after the GR Helper finds that the GR Restarter is down.
  + EOR timer: indicates the maximum period during which a GR Helper waits for EOR messages from the GR Restarter. If the GR Helper does not receive an EOR message from the GR Restarter within the EOR timer, the GR Helper selects the optimal route based on the existing routes.
* GR session: indicates a session, through which a GR Restarter and a GR Helper negotiate GR capabilities.
* EOR: indicates a type of BGP message used to notify a peer that the first route upgrade is complete after the BGP session is established.


#### Fundamentals

Fundamentals of a BGP GR Helper are as follows:

1. During BGP peer relationship establishment, devices negotiate GR capabilities by sending supported GR capabilities to each other.
2. When detecting that the GR Restarter is down, the GR Helper starts the GR timer and waits for the Restarter to go up.
   
   * Before the GR timer expires, it retains the routes and forwarding entries related to the GR Restarter until the GR Restarter goes up. The process then goes to Step 3.
   * When the GR timer expires, it deletes the routes and forwarding entries related to the GR Restarter and exits the GR Helper state.
3. After the GR Restarter goes up, the GR Helper receives routes from the GR Restarter and starts the EOR timer. The GR Helper exits the GR Helper state and ages the routes related to the GR Restarter when one of the following conditions is met:
   * The GR Helper receives an EOR message from the GR Restarter, and the EOR timer is deleted.
   * The EOR timer expires but the GR Helper fails to receive an EOR message from the GR Restarter.

Fundamentals of a BGP GR Restarter are as follows:

1. When a BGP process is restarted, a GR-capable device enters the GR Restarter state, starts the Protection Timer and Force-Quit Timer, and waits for BGP peer relationships to be reestablished.
   
   * After the first BGP peer relationship is established, the Protection Timer is deleted, and the process goes to Step 2.
   * No BGP peer relationship is established, and the Protection timer expires. In this case, the GR Restarter state exits.
2. The GR Restarter continues to wait for the remaining BGP peer relationships to be established, receives routes and EOR messages from the BGP peers with which BGP peer relationships have been established, starts the Wait-All-Peer-Up timer and Selection-Deferral timer, and waits for the establishment of all BGP peer relationships and EOR messages. The GR Restarter starts route selection when one of the following conditions is met:
   * The BGP peer relationships are established, and the GR Restarter receives EOR messages from the peers.
   * The Wait-All-Peer-Up timer expires.
   * The Selection-Deferral timer expires.
3. After the GR Restarter finishes route selection, it exits the GR Restarter state and re-advertises routes to its BGP peers.

#### GR Reset

Currently, BGP does not support dynamic capability negotiation. Therefore, each time a new BGP capability (such as the IPv4 and IPv6 capabilities) is enabled or disabled on a BGP speaker, that speaker tears down existing sessions with its peers and renegotiates BGP capabilities.

If a BGP IPv4 unicast peer session has been established and IPv4 services are running properly, establishing a BGP peer relationship in another address family on the basis of the BGP IPv4 unicast peer session will cause the BGP IPv4 unicast peer relationship to be re-established, affecting IPv4 services. To resolve this problem, you can reset the BGP connection in GR mode.

With the GR function configured, if a BGP peer relationship in another address family is established based on an IPv4 BGP unicast peer session, the BGP speaker enters the GR state and renegotiates BGP capabilities with its peer. Throughout the entire process, the BGP speaker re-establishes the BGP IPv4 unicast peer session but retains the original routing entries. The forwarding module forwards the existing services based on the routing entries, thereby ensuring that the services are not interrupted.