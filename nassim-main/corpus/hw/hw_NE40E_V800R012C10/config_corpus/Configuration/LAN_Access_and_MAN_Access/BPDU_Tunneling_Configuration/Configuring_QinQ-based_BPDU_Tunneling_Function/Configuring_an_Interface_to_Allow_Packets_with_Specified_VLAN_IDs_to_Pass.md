Configuring an Interface to Allow Packets with Specified VLAN IDs to Pass
=========================================================================

To enable users to communicate through a carrier network, configure interfaces on provider edges (PEs) that are connected to the carrier network to allow the passing of packets with specified virtual local area network (VLAN) IDs.

#### Context

Perform the following steps on PEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface connected to the carrier network is displayed.
3. Run [**port trunk allow-pass**](cmdqueryname=port+trunk+allow-pass) **vlan** {{ *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** }
   
   
   
   The interface connected to the carrier network is configured to allow the passing of packets with specified VLAN tags.
   
   
   
   The specified VLAN tags must be the same as the outer VLAN tags carried in BPDUs that the PE receives.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.