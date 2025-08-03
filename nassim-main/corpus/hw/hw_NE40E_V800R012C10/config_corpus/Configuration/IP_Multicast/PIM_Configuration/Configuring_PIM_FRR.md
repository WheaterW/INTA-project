Configuring PIM FRR
===================

PIM fast reroute (FRR) is a link protection measure used to minimize service loss when link or node faults occur on PIM-SM or PIM-SSM SPTs.

#### Usage Scenario

If a multicast link fails, services are interrupted before unicast routes are converged. Route convergence generally takes a long time, which is unacceptable by multicast services that have high requirements on real-time data transmission. To resolve this problem, configure PIM FRR. After PIM FRR is configured, PIM sets up primary and backup MDTs based on unicast backup FRR routes, allowing multicast traffic transmission through both the primary and backup links. The device's forwarding plane permits the multicast traffic on the primary link and discards that on the backup link. However, the forwarding plane permits the multicast traffic on the backup link immediately after the primary link fails, thus minimizing traffic loss.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

PIM FRR can be configured only in IPv4 multicast and Rosen MVPN scenarios. If PIM FRR is needed in a Rosen MVPN scenario, PIM FRR must be configured on both the source and receiving ends. If PIM FRR is configured only on one end, PIM FRR does not work properly.



#### Pre-configuration Tasks

Before configuring PIM FRR, complete the following tasks:

* Configure a unicast routing protocol to ensure that devices are reachable.
* [Configure IGP FRR.](dc_vrp_ip-route_cfg_0019.html)
* [Configure basic PIM-SM functions.](dc_vrp_multicast_cfg_0006.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**multicast frr monitor cycle**](cmdqueryname=multicast+frr+monitor+cycle) *cycle-value*
   
   
   
   The multicast FRR monitoring interval is set.
3. (Optional) Run [**multicast static-frr**](cmdqueryname=multicast+static-frr) **source** *source-address* **group** *group-address* [ **mask** *mask-value* | **mask-length** *mask-length* ] [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   Static multicast FRR is enabled.
4. Run [**pim**](cmdqueryname=pim) [ **vpn-instance***vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
5. Run [**rpf-frr**](cmdqueryname=rpf-frr) [ **policy** { *acl-number* | **acl-name***acl-name* } ]
   
   
   
   PIM FRR is enabled.
6. (Optional) Run [**rpf-prune-delay**](cmdqueryname=rpf-prune-delay) *delay-time* [ **policy** { *acl-number* | **acl-name** *acl-name* } ]
   
   
   
   The delay in sending Prune messages to the upstream device is set.
7. (Optional) Run [**backup-rpf-switchover-delay**](cmdqueryname=backup-rpf-switchover-delay) { **flow-based** | **interval** *hold-time* } [ **policy** { *acl-number* | **acl-name** *acl-name* } ]
   
   
   
   The delay in generating forwarding entries corresponding to the interface connected to the backup upstream device is set.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring PIM FRR, run the [**display pim**](cmdqueryname=display+pim) **routing-table** command to check the PIM routing table.

Run the [**display multicast frr-table**](cmdqueryname=display+multicast+frr-table) command to check multicast FRR entries of multicast groups.