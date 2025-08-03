Configuring IPv6 PIM
====================

Configuring IPv6 PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

#### Context

IPv6 NG MVPNs also use IPv6 PIM as the multicast routing protocol on the user network. PIM neighbor relationships can be established between devices only after PIM-SM is enabled on interfaces. Then a VPN multicast routing table can be established to guide multicast traffic forwarding.


#### Procedure

* Perform the following steps on the PE interfaces bound to a VPN instance.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed. The interface is bound to a VPN instance.
  3. Run [**pim ipv6 sm**](cmdqueryname=pim+ipv6+sm)
     
     PIM-SM is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Perform the following steps on the CE.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable)
     
     Multicast routing is enabled.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  4. Run [**pim ipv6 sm**](cmdqueryname=pim+ipv6+sm)
     
     PIM-SM is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.