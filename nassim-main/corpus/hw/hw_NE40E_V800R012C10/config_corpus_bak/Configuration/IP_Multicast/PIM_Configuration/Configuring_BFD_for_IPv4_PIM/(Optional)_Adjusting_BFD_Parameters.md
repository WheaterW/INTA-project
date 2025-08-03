(Optional) Adjusting BFD Parameters
===================================

PIM BFD parameters include the minimum interval for sending and receiving PIM BFD packets and the local detection multiplier. PIM BFD parameters can be adjusted as needed.

#### Context

Perform the following steps on PIM Routers that set up neighbor relationships:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim bfd**](cmdqueryname=pim+bfd) { **min-tx-interval** *tx-value* | **min-rx-interval** *rx-value* | **detect-multiplier** *multiplier-value* } \*
   
   
   
   PIM BFD parameters are adjusted.
   
   If BFD parameters configured for other protocols are the same as those configured for PIM, the configurations of the PIM BFD parameters are affected.
   
   The two ends negotiate the actual sending interval and receiving interval, and detection period of PIM IPv6 BFD packets based on the following negotiation mechanism:
   * Actual sending interval and receiving interval of PIM BFD packets:
     + Actual sending interval = max (local **min-tx-interval**, remote **min-rx-interval**)
     + Actual receiving interval = max (remote **min-tx-interval**, local **min-rx-interval**)
   * Actual detection period = remote **detect-multiplier** x max (remote **min-tx-interval**, local **min-rx-interval**)BFD parameters can be configured on both the receive and transmit ends, and the configurations on the two ends are both effective.