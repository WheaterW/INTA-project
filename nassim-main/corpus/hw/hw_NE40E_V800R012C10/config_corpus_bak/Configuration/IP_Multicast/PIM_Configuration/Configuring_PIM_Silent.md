Configuring PIM Silent
======================

To protect Router interfaces directly connected to hosts against pseudo PIM Hello packets, configure PIM silent.

#### Usage Scenario

If PIM-SM is enabled on Router interfaces directly connected to user hosts, these interfaces can set up PIM neighbor relationships and process PIM packets, so these interfaces may be attacked if malicious hosts send numerous PIM Hello packets.

To address this problem, configure PIM silent. After PIM silent is configured on an interface, the interface is not allowed to receive or forward any PIM packets and all PIM neighbor relationships and PIM state machines on this interface are deleted. Then, this interface automatically becomes a designated router (DR). IGMP is not affected on the interface.

PIM silent applies only to the Router interface that directly connects the Router to only one host network segment.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If PIM silent is enabled on the interface connected to a Router, PIM neighbor relationships cannot be established, and multicast faults occur.

If a host network segment connects to multiple Routers and PIM silent is enabled on interfaces of multiple Routers, the interfaces become static DRs. As a result, multiple DRs exist in this network segment, which will result in multicast faults.



#### Pre-configuration Tasks

Before configuring PIM silent, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure PIM-SM](dc_vrp_multicast_cfg_0006.html).
* Configure IGMP.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim silent**](cmdqueryname=pim+silent)
   
   
   
   PIM silent is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check information about PIM interfaces.

Run the [**display pim interface**](cmdqueryname=display+pim+interface) **verbose** command to check whether PIM silent is enabled.