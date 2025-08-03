Applying a QPPB Local Policy to an Interface
============================================

After a QPPB local policy is applied to an interface, the associated traffic behavior is performed for the packets that meet the matching rule.

#### Context

You can apply a QPPB local policy to the incoming or outgoing traffic.

BGP routes in QPPB refer to only BGP routes on the public network. Private routes are involved in the QPPB application on the L3VPN.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

On the ingress, QPPB is not applicable to downstream traffic on the IP access MPLS tunnel over a public or private network.

Perform the following operations on a BGP route receiver:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run one of the following commands as needed to apply a QPPB local policy:
   
   
   * To apply a QPPB local policy to the incoming traffic, run the [**qppb-policy**](cmdqueryname=qppb-policy) *policy-name* **destination inbound** command on the inbound interface.
   * To apply a QPPB local policy to the outgoing traffic, run the [**qppb-policy**](cmdqueryname=qppb-policy) **qos-local-id** **destination inbound** and [**qppb-policy**](cmdqueryname=qppb-policy) *policy-name* **outbound** commands on the inbound and outbound interfaces respectively.
   * To apply a QPPB local policy to the IP precedence, run the [**qppb-policy ip-precedence**](cmdqueryname=qppb-policy+ip-precedence) **destination** command to perform the QPPB action for destination addresses based on the traffic behavior specified by a routing policy.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The keyword **destination** indicates destination-based QPPB.