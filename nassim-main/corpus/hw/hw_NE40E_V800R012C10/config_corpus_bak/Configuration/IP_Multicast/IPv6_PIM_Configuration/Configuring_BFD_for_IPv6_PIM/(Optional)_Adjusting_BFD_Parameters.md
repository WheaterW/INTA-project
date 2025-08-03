(Optional) Adjusting BFD Parameters
===================================

IPv6 PIM BFD does not apply to Point-to-point (P2P) interfaces. IPv6 PIM BFD parameters include the minimum interval for sending and receiving PIM BFD packets and the local detection multiplier. BFD negotiates actual parameter values of detection packets based on configurations on the two ends.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If there is no special requirement for the detection period and the link is stable, you are recommended to configure the same parameter values for the routing devices of the same performance on the shared network segment.

Perform the following steps on the Routers that have set up a PIM neighbor relationship:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim ipv6 bfd**](cmdqueryname=pim+ipv6+bfd) { **min-tx-interval** *min-tx-interval-val* | **min-rx-interval**  *min-rx-interval-val* | **detect-multiplier** *detect-multiplier-value* } \*
   
   
   
   The minimum sending interval, minimum receiving interval, and local detection multiplier of BFD packets are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The default parameter values are defined uniformly in the BFD module.
   
   
   The two ends negotiate the actual sending interval and receiving interval, and detection period of PIM IPv6 BFD packets based on the following negotiation mechanism:
   * Actual sending interval and receiving interval of PIM IPv6 BFD packets:
     + Actual sending interval = max (local **min-tx-interval**, remote **min-rx-interval**)
     + Actual receiving interval = max (remote **min-tx-interval**, local **min-rx-interval**)
   * Actual detection period = Remote **detect-multiplier** x max (remote **min-tx-interval**, local **min-rx-interval**)BFD parameters can be configured on both the receive and transmit ends, and the configurations on the two ends are both effective.