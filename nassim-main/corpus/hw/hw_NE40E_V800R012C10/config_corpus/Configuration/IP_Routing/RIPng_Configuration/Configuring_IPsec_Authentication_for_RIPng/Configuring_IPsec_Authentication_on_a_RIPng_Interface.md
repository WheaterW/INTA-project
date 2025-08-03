Configuring IPsec Authentication on a RIPng Interface
=====================================================

Configuring IP security (IPsec) authentication in the interface view is the other method used to configure IPsec authentication for RIPng.

#### Context

An SA configured on an RIPng interface is used to authenticate the packets sent and received by the interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ripng ipsec sa**](cmdqueryname=ripng+ipsec+sa) *sa-name*
   
   
   
   IPsec authentication is enabled on the interface, and the name of an SA is specified.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**ripng ipsec sa**](cmdqueryname=ripng+ipsec+sa) command takes precedence over the [**ipsec sa**](cmdqueryname=ipsec+sa) command. If both commands are run in respective views and different SA names are specified, only the configuration of the [**ripng ipsec sa**](cmdqueryname=ripng+ipsec+sa) command takes effect.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.