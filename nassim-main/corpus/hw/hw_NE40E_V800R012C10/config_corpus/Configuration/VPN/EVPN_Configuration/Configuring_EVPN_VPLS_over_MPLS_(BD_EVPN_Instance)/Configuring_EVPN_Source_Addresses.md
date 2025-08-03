Configuring EVPN Source Addresses
=================================

An EVPN source address uniquely identifies a PE in EVPN networking.

#### Context

EVPN source addresses, which can be used to identify PEs on an EVPN, are part of EVPN route information. Configuring EVPN source addresses is a mandatory task for EVPN configuration.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn source-address**](cmdqueryname=evpn+source-address) *ip-address*
   
   
   
   An EVPN source address is configured.
   
   
   
   In scenarios where a CE is dual-homed or multi-homed to PEs, you need to configure an EVPN source address on each PE to generate RDs for Ethernet segment routes and Ethernet A-D per ES routes.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.