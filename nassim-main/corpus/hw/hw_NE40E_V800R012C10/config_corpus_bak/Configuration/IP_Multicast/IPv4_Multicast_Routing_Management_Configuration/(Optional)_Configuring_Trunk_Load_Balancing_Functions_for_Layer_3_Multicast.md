(Optional) Configuring Trunk Load Balancing Functions for Layer 3 Multicast
===========================================================================

To implement better load balancing for Layer 3 multicast traffic on trunk member interfaces, configure optional trunk load balancing functions.

#### Usage Scenario

If multicast traffic is sent out through trunk interfaces, configure some optional load balancing functions to adjust load balancing on trunk member interfaces.


#### Pre-configuration Tasks

Before configuring optional trunk load balancing functions for Layer 3 multicast, specify outbound interfaces as trunk interfaces for multicast traffic.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**trunk multicast load-balance hash-mode multicast-member**](cmdqueryname=trunk+multicast+load-balance+hash-mode+multicast-member)
   
   
   
   Multicast group- and trunk sub-interface-based multicast load balancing is enabled for hash-mode route selection.
   
   
   
   This configuration implements better load balancing for multicast flows that belong to the same multicast group but have different sub-interfaces of the same outbound trunk interface.
3. (Optional) Run [**trunk multicast load-balance**](cmdqueryname=trunk+multicast+load-balance) **interface** *if-type if-number* **trunk-member backup** { **l3mcv4** | **l3mcv6** }
   
   
   
   Master/backup protection is enabled for trunk member interfaces, so that traffic can be quickly switched if a trunk member interface fails.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This configuration is supported only by the NE40E-M2E.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.