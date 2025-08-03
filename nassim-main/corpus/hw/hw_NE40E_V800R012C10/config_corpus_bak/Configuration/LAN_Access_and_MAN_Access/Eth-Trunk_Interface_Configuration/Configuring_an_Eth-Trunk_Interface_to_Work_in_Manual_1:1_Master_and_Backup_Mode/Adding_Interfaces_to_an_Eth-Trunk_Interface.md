Adding Interfaces to an Eth-Trunk Interface
===========================================

An Eth-Trunk interface in manual 1:1 master/backup mode can contain only two member interfaces.

#### Context

Two methods are available for adding interfaces to an Eth-Trunk interface:

* Add interfaces in batches or a single interface in the Eth-Trunk interface view.
* Add an interface in the interface view. When adding interfaces to an Eth-Trunk interface, note the following:
  + Eth-Trunk interfaces cannot be added to Eth-Trunk interfaces.
  + Different Ethernet interfaces can be added to the same Eth-Trunk interface.
  + Ethernet interfaces on different interface boards can be added to the same Eth-Trunk interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) After interfaces are added to an Eth-Trunk interface, the following situations occur:

* If the Eth-Trunk interface is shut down using the [**shutdown**](cmdqueryname=shutdown) command, the physical status of both the Eth-Trunk interface and member interfaces becomes **Administratively DOWN**, and the **shutdown** command configuration is automatically generated for the member interfaces in the configuration file.
* If the Eth-Trunk interface is enabled using the [**undo shutdown**](cmdqueryname=undo+shutdown) command, the [**undo shutdown**](cmdqueryname=undo+shutdown) command configuration is automatically generated for the member interfaces in the configuration file.



#### Procedure

* Add one or more interfaces in the Eth-Trunk interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     
     
     The Eth-Trunk interface view is displayed.
  3. Run either of the following commands:
     
     
     + To add interfaces to the Eth-Trunk interface in batches, run the [**trunkport**](cmdqueryname=trunkport) *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-64> command.
       
       A maximum of two interfaces can be added to or deleted from an Eth-Trunk interface that works in manual 1:1 master/backup mode.
     + To add a single interface to the Eth-Trunk interface, run the [**trunkport**](cmdqueryname=trunkport) *interface-type* *interface-number* command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Add an interface in the interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface to be added to an Eth-Trunk interface is displayed.
  3. Run [**eth-trunk**](cmdqueryname=eth-trunk) *trunk-id*
     
     
     
     The interface is added to an Eth-Trunk interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Interfaces to be added to an Eth-Trunk interface cannot have services or Layer 3 configurations, such as IP addresses.
     + Interfaces to be added to an Eth-Trunk interface cannot have static MAC addresses configured.
     + Layer 2 interfaces must be switched to Layer 3 interfaces using the [**undo portswitch**](cmdqueryname=undo+portswitch) command before they can be added to an Eth-Trunk interface.
     + An Ethernet interface can be added to only one Eth-Trunk interface. The Ethernet interface must be removed from the original Eth-Trunk interface before it can be added to another Eth-Trunk interface.
     + If the Port State Table (PST) status of a member interface is down, the member interface does not function as an outbound interface to forward packets for the Eth-Trunk interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Follow-up Procedure

When Eth-Trunk member interfaces change from up to down or down to up, you need to learn the status changes through trap messages so to determine whether the status changes are caused by device faults.