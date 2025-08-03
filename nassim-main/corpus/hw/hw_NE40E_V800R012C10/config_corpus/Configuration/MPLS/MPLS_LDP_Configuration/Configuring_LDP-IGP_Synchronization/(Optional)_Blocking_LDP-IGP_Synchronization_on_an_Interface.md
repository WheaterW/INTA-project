(Optional) Blocking LDP-IGP Synchronization on an Interface
===========================================================

If you do not want to run LDP-IGP synchronization on some interfaces, you can block the function on these interfaces.

#### Context

After LDP-IGP synchronization is enabled in an IGP process using the [**ldp-sync enable**](cmdqueryname=ldp-sync+enable) command, it is enabled on all interfaces whose neighbor status is up on a P2P network, enabled on all interfaces whose neighbor status is up between a DR and a non-DR/BDR on an OSPF-enabled broadcast network, and enabled on all interfaces whose neighbor status is up between a DIS and a non-DIS on an IS-IS-enabled broadcast network.

If the interfaces on a device carry key services, ensure that the backup path does not pass through this device. The NE40E allows you to block LDP-IGP synchronization on a specified interface.


#### Procedure

* If OSPF is used, perform the following configuration on the interfaces on both ends of the link between the node where the primary LSP and the backup LSP diverge from each other and its LDP peer on the primary LSP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of an OSPF interface is displayed.
  3. Run [**ospf ldp-sync block**](cmdqueryname=ospf+ldp-sync+block)
     
     
     
     LDP-OSPF synchronization is blocked on the interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To block LDP-OSPF synchronization on a multi-area adjacency interface, run the [**ospf ldp-sync block multi-area**](cmdqueryname=ospf+ldp-sync+block+multi-area) *area-id* command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* If IS-IS is used, perform the following configuration on the interfaces on both ends of the link between the node where the primary LSP and the backup LSP diverge from each other and its LDP peer on the primary LSP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of an IS-IS interface is displayed.
  3. Run [**isis ldp-sync block**](cmdqueryname=isis+ldp-sync+block)
     
     
     
     LDP-IS-IS synchronization is blocked on the interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.