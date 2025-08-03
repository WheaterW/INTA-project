Configuring a PBB-EVPN Source Address
=====================================

A provider backbone bridge Ethernet VPN (PBB-EVPN) source address uniquely identifies a provider edge (PE) in PBB-EVPN networking.

#### Context

A PBB-EVPN source address is part of the EVPN route information. Configuring PBB-EVPN source addresses is a mandatory task for PBB-EVPN configuration.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn source-address**](cmdqueryname=evpn+source-address) *ip-address*
   
   
   
   A PBB-EVPN source address is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.