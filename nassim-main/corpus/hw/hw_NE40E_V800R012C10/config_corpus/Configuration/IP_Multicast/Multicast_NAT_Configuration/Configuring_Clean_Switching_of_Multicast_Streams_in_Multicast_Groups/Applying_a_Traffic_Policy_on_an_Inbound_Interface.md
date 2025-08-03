Applying a Traffic Policy on an Inbound Interface
=================================================

A traffic policy can be applied on an inbound interface of multicast streams to match the packet header information of input multicast streams.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the inbound interface of multicast streams is displayed.
3. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound**
   
   
   
   Traffic classification based on packet header information is configured.
4. Run [**multicast-nat inbound enable**](cmdqueryname=multicast-nat+inbound+enable)
   
   
   
   Multicast NAT is enabled on the inbound interface of multicast streams.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.