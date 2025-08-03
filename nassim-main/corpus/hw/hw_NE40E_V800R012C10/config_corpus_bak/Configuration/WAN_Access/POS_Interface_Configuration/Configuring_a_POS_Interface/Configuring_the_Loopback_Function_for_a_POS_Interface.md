Configuring the Loopback Function for a POS Interface
=====================================================

Loopback is enabled on an interface only when some special function tests need to be carried out.

#### Context

If local loopback has been enabled on an interface, the physical status of the interface changes to Up, whereas the link layer protocol of the interface remains Down.

If remote loopback has been enabled on an interface and PPP is used as the link layer protocol, the physical status of the interface changes to Up, whereas the link layer protocol of the interface remains Down. If HDLC is used as the link layer protocol, both the physical status and the link layer protocol status of the interface are Up.

Local loopback and remote loopback cannot be both enabled on a POS interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The loopback configurations on a POS interface are different for different LPUs. In the actual configuration, note the following points:

* To enable local loopback on a POS interface, ensure that the clock of the POS interface works in master mode.
* To enable remote loopback on a POS interface, ensure that the clock of the POS interface works in slave mode.

Perform the following steps on the Routers:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **pos** *interface-number*
   
   
   
   The POS interface view is displayed.
3. Run [**loopback**](cmdqueryname=loopback) { **local** | **remote** }
   
   
   
   The loopback function is configured for the POS interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.