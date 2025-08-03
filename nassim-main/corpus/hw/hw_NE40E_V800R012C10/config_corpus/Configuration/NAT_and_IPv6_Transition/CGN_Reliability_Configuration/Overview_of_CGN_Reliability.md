Overview of CGN Reliability
===========================

CGN reliability allows proper traffic forwarding without letting users perceive faults and save resources for users.

Currently, IPv4 address shortage is an extremely serious problem and has become an insurmountable obstacle for the rapid growth of Internet, especially in mobile broadband and Internet of things (IoT). The most significant advantage of IPv6 is that IPv6 provides more than enough globally unique IP addresses, addressing the fundamental issue of IPv4 address exhaustion. However, because mass IPv4 services are still carried on the Internet, service providers cannot transform their existing IPv4 networks to IPv6-only networks in a short time. A solution is to enable IPv6 offerings while continuing to use the existing IPv4 infrastructures. As IPv6 offerings become more and more popular, service providers can gradually upgrade their infrastructures to IPv6. This means that IPv4 and IPv6 will coexist for some time during the transition from IPv4 to IPv6.

Traditionally NAT is in most cases deployed on user-side CPEs to implement address translation for a small number of users. Carrier grade NAT (CGN) is deployed on carrier networks to implement address translation for a large number of users. Therefore, CGN outperforms traditional NAT in terms of capacity, performance, and reliability.

* Functionally, CGN implements translation between addresses, such as translation between private IPv4 addresses, between a private IPv4 address and a public IPv4 address, and between an IPv4 address and an IPv6 address. Some CGN technologies also provide tunnel functions.
* CGN functions can be provided by either a standalone CGN device or a CGN board. If you insert a CGN board into a BRAS, the BRAS will be able to provide both access and CGN functions.

CGN can be deployed in either centralized or distributed mode, as shown in the following figure.**Figure 1** CGN deployment  
![](images/fig_dc_ne_cgn-reliability_cfg_0000.png)

* In centralized CGN deployment mode, one or more standalone CGN devices are independently deployed at metro core or close to nodes (CRs) at the metro core. This mode applies to the initial stage of IPv6 deployment, when there is little IPv6 traffic and few IPv6 users.
* In distributed CGN deployment mode, CGN boards are inserted into BRASs and are deployed at the edge of a metro network. This mode applies to networks with mass IPv6 users and heavy IPv6 traffic.

CGN is used to implement address translation for a large number of users. This is why CGN is also called large scale NAT (LSN). If a CGN fault occurs and no appropriate protection measure is taken, a large number of users may be affected. The impact is more severe in centralized deployment mode. Therefore, CGN reliability needs to be deployed to achieve CGN hot backup (intra-chassis inter-board backup), ultimately enhancing reliability of CGN devices.


#### Backup Features

* Warm backup
  
  Warm backup allows user tables to be backed up between the master and slave service boards. In load balancing scenarios, warm backup also requires the backup of global address pool table entries. After a master/slave switchover is performed, user sessions need to be re-established. Warm backup is enabled by default, with no need for manual operation.
* Hot backup
  
  Hot backup allows user tables and session tables to be backed up between the master and slave service boards. In load balancing scenarios, hot backup also requires the backup of global address pool table entries. After a master/slave switchover is performed, user sessions are not interrupted. The hot backup mode can work only after HA hot backup is enabled.

#### Backup Scenarios

* Inter-board backup
  
  If a CGN device has multiple service boards, you can configure a master service board and a slave service board on the CGN device to implement inter-board backup. This mechanism ensures data consistency between the master and slave service boards. Once a fault occurs on the master service board, a master/slave switchover is trigger to ensure service continuity without letting users perceive the fault.
* Inter-chassis backup
  
  If multiple CGN devices equipped with service boards exist on a network, you can configure a service board on a master device and a service board on a backup device to implement inter-chassis backup. This mechanism ensures data consistency between chassis. Once the master device, the service board on it, or the link between the master and backup devices fails, a master/slave switchover is triggered to ensure service continuity without letting users perceive faults.

#### Backup Overlapping Scenarios

* Inter-board backup + inter-chassis backup in centralized NAT444
* Inter-board backup + inter-chassis backup in distributed NAT444
* VPN over NAT inter-chassis hot backup
* Load balancing over NAT inter-board backup and inter-chassis backup
* Centralized NAT providing backup for distributed NAT in the inter-board backup scenario