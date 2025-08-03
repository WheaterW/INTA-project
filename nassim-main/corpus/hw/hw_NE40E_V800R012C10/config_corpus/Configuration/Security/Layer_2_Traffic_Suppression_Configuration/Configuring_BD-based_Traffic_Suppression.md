Configuring BD-based Traffic Suppression
========================================

This section describes how to configure BD-based traffic suppression in order to reduce the traffic burden on a network.

#### Prerequisites

Before configuring Layer 2 traffic suppression, complete the following task:

Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is up.


#### Context

As broadcast, multicast, and unknown unicast packets increase on a network, more network resources are consumed, adversely affecting network services.

When the rates of broadcast, multicast, and unknown unicast packets exceed the configured committed information rate (CIR), the system discards excess packets to control the packet rate within a proper range.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **[**bridge-domain**](cmdqueryname=bridge-domain)** *bd-id*
   
   
   
   The BD view is displayed.
3. Run [**unknown-multicast discard**](cmdqueryname=unknown-multicast+discard)
   
   
   
   Interfaces in the BD are disabled from forwarding unknown multicast packets.
4. Run [**unknown-unicast discard**](cmdqueryname=unknown-unicast+discard)
   
   
   
   Interfaces in the BD are disabled from forwarding unknown unicast packets.
5. Run [**broadcast-suppression**](cmdqueryname=broadcast-suppression) **cir** *cirVal* [ **cbs** *cbsVal* ] { **uni-inbound** | **uni-outbound** }
   
   
   
   The maximum volume of broadcast traffic allowed in the BD is configured.
6. Run [**multicast-suppression**](cmdqueryname=multicast-suppression) **cir** *cirVal* [ **cbs** *cbsVal* ] { **uni-inbound** | **uni-outbound** }
   
   
   
   The maximum volume of multicast traffic allowed in the BD is configured.
7. Run [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cirVal* [ **cbs** *cbsVal* ] { **uni-inbound** | **uni-outbound** }
   
   
   
   The maximum volume of unknown unicast traffic allowed in the BD is configured.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

After the configuration is complete, perform the following operation to verify the configuration:

Run the **display traffic-statistics suppression interface** { *interface-name* | *interface-type* *interface-num* } **bd** *bd-id* command to check Layer 2 traffic suppression statistics about the specified BD.