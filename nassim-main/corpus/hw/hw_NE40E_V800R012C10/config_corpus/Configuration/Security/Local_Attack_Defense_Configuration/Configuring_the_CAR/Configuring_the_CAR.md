Configuring the CAR
===================

This section describes how to configure the CAR. Traffic policing prevents packets to be sent to the CPU from causing higher CPU usage to affect normal services.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run [**car**](cmdqueryname=car+index+whitelist+bgp+ldp+ospf+radius+rsvp+isis+cir+cbs) { *protocol-name* | **index** *index* | **whitelist** [ **bgp** | **ldp** | **ospf** | **radius** | **rsvp** | **isis** ] | **whitelist-v6** [ **bgpv6** | **ospfv3** ] | **blacklist** | **tcpsyn** | **fragment** | **user-defined-flow** *flow-id* } { **cir** *cir-value* | **cbs** *cbs-value* | **min-packet-length** *min-packet-length-value* } \*
   
   
   
   The packet CAR is set.
4. Run [**car total-packet**](cmdqueryname=car+total-packet+high+low+middle) { **high** | **low** | **middle** | *total-packet-rate* }
   
   
   
   The rate of sending packets to the CPU is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.