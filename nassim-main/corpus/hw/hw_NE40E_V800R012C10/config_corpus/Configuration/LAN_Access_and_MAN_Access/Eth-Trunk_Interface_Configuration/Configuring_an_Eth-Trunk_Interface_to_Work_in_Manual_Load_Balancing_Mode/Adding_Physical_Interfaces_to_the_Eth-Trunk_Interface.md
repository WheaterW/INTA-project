Adding Physical Interfaces to the Eth-Trunk Interface
=====================================================

After creating an Eth-Trunk interface and configuring it to work in manual load balancing mode, add physical interfaces to the Eth-Trunk interface to increase interface bandwidth and improve reliability.

#### Context

There are two methods for adding physical interfaces to an Eth-Trunk interface:

* Add physical interfaces in the view of the Eth-Trunk interface. Using this method, you can add a single physical interface or physical interfaces in batches.
* Add an interface in the interface view.

Note the following when adding physical interfaces to an Eth-Trunk interface:

* Eth-Trunk interfaces cannot be added to Eth-Trunk interfaces.
* Ethernet interfaces on different interface boards can be added to the same Eth-Trunk interface.
* Eth-Trunk interfaces work in either Layer 2 or Layer 3 mode. Ethernet interfaces can join an Eth-Trunk interface regardless of the mode in which the Eth-Trunk interface works.

![](../../../../public_sys-resources/note_3.0-en-us.png) After a physical interface is added to an Eth-Trunk interface, the physical interface will undergo status changes according to the command run on the Eth-Trunk interface.

* If you run the [**shutdown**](cmdqueryname=shutdown) command on the Eth-Trunk interface, the physical status of both the Eth-Trunk interface and its member interface becomes **Administratively DOWN**, and the configuration file of the member interface displays **shutdown** automatically.
* If you run the [**undo shutdown**](cmdqueryname=undo+shutdown) command on the Eth-Trunk interface, the configuration file of the member interface displays **undo shutdown** automatically.



#### Procedure

* Add one or more physical interfaces in the Eth-Trunk interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **eth-trunk** *trunk-id*
     
     
     
     The Eth-Trunk interface view is displayed.
  3. Run either of the following commands as required.
     
     
     + To add physical interfaces to the Eth-Trunk interface in batches, run the [**trunkport**](cmdqueryname=trunkport) *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-64> [ **mode** { **active** | **passive** } ] command.
     + To add a single physical interface to an Eth-Trunk interface, run the [**trunkport**](cmdqueryname=trunkport) *interface-type* *interface-number* [ **mode** { **active** | **passive** } ] command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Add a physical interface to an Eth-Trunk interface in the view of the physical interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of a physical interface that needs to be added to an Eth-Trunk interface is displayed.
  3. Run [**eth-trunk**](cmdqueryname=eth-trunk) *trunk-id* [ **mode** { **active** | **passive** } ]
     
     
     
     The physical interface is added to the Eth-Trunk interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Member interfaces cannot be configured with services or Layer 3 configurations such as IP addresses.
     + Member interfaces cannot be manually configured with MAC addresses.
     + An Ethernet interface can be added to only one Eth-Trunk interface. The Ethernet interface must be deleted from the original Eth-Trunk interface before joining another Eth-Trunk interface.
     + Before adding a Layer 2 interface on the Router to an Eth-Trunk interface, run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to configure the interface to work in Layer 3 mode.
     + If an Eth-Trunk member interface is directly connected to an interface on the peer, the peer interface must also be an Eth-Trunk member interface; otherwise, the devices cannot communicate with each other.
     + If the Port State Table (PST) status of a member interface is down, the member interface does not function as an outbound interface to forward packets for the Eth-Trunk interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Follow-up Procedure

![](../../../../public_sys-resources/note_3.0-en-us.png) If services are running on a live network, it is recommended that you perform the following operations when adding an interface to an Eth-Trunk interface:

1. Run the [**shutdown**](cmdqueryname=shutdown) command on the interface to be added to an Eth-Trunk interface.
2. Add the interface to the Eth-Trunk interface.
3. Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command on the interface that has been added to the Eth-Trunk interface.

When Eth-Trunk member interfaces change from up to down or down to up, you need to learn the status changes through trap messages so to determine whether the status changes are caused by device faults.