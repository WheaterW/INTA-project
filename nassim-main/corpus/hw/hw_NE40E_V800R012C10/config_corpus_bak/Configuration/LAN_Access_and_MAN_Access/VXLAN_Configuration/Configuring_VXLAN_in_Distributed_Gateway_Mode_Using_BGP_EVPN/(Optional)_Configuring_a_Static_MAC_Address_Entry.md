(Optional) Configuring a Static MAC Address Entry
=================================================

Using static MAC address entries to forward user packets helps reduce BUM traffic on the network and prevent bogus attacks.

#### Context

When the source NVE on a VXLAN tunnel receives BUM packets, the NVE sends these packets along paths specified in static MAC address entries if there are such entries. This helps reduce BUM traffic on the network and prevent unauthorized data access from bogus users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mac-address static**](cmdqueryname=mac-address+static) *mac-address* **bridge-domain** *bd-id* **source-ipv6** *sourceIpv6* **peer-ipv6** *peerIPv6* **vni** *vni-id*
   
   
   
   A static MAC address entry is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.