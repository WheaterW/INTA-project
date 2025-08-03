Enabling GVRP
=============

Enabling_GVRP

#### Context

You must enable GVRP globally as well as on trunk interfaces which require dynamic VLAN registration and deregistration. In addition, you must enable packets of all dynamic VLANs to pass the trunk interfaces.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**gvrp**](cmdqueryname=gvrp)
   
   
   
   GVRP is enabled globally.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**port link-type**](cmdqueryname=port+link-type) **trunk**
   
   
   
   The interface is configured as a trunk interface.
5. Run [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) { { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> } | **all** }
   
   
   
   VLANs in which packets are allowed to pass the trunk interface are specified.
6. Run [**gvrp**](cmdqueryname=gvrp)
   
   
   
   GVRP is enabled on the trunk interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   VLAN configuration will trigger GVRP messages. If a large number of VLANs require configuration, configure VLANs in batches on devices one by one and configure timers to control the sending of GVRP messages. Otherwise, dynamic VLANs may flap.
   
   If a trunk interface is switched to an access, hybrid, or dot1q-tunnel interface, you are prompted to enable interface GVRP.
   
   The blocked interface in instance 0 of Spanning Tree Protocol (STP)/Rapid STP (RSTP)/Multiple STP (MSTP) blocks GVRP PDUs. To ensure that GVRP runs properly and to prevent GVRP loops, do not enable GVRP on blocked interfaces of ring network protocols, such as STP, RSTP, and MSTP.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.