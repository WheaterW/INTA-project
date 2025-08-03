Configuring IPv6 PIM Silent
===========================

To protect router interfaces directly connected to hosts against pseudo PIM Hello packets, configure IPv6 PIM silent.

#### Usage Scenario

At the access layer, if an interface on the Router directly connected to a host is enabled with the IPv6 PIM protocol, PIM neighbors can be established on the interface to process various PIM protocol packets. However, the configuration brings security risks. If some hosts send a large number of malicious PIM IPv6 Hello messages, there is a possibility that the Router crashes.

To address this problem, configure PIM silent on the interface. After PIM silent is configured, the interface cannot receive or forward PIM packets. All PIM neighbors and PIM state machines on this interface are deleted. Then, this interface automatically becomes a Designated router (DR). Multicast Listener Discovery (MLD) is not affected on the interface.

PIM silent applies only to the Router interface that directly connects the Router to only one host network segment.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If PIM silent is enabled on the interface connected to a Router, the IPv6 PIM neighbor relationships cannot be established and a multicast fault occurs.

If the host network segment is connected to multiple Routers and IPv6 PIM silent is enabled on interfaces of multiple Routers, the interfaces become static DRs. In this situation, multiple DRs exist in this network segment, which incurs multicast faults.



#### Pre-configuration Tasks

Before configuring IPv6 PIM silent, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure IPv6 PIM-SM](dc_vrp_multicast_cfg_2005.html).
* Configure MLD.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim ipv6 silent**](cmdqueryname=pim+ipv6+silent)
   
   
   
   IPv6 PIM silent is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display pim ipv6 interface**](cmdqueryname=display+pim+ipv6+interface) [ *interface-type interface-number* | **up** | **down** ] [ **verbose** ] command to check information about IPv6 PIM interfaces.

Run the [**display pim ipv6 interface**](cmdqueryname=display+pim+ipv6+interface) **verbose** command to check whether PIM silent is enabled.