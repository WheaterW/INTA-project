Adding a Layer 2 Port to an ERPS Ring and Configuring the Port Role
===================================================================

Adding a Layer 2 Port to an ERPS Ring and Configuring the Port Role

#### Prerequisites

* If the port is a Layer 3 port, run the [**portswitch**](cmdqueryname=portswitch) command to configure the port to work in Layer 2 mode.
* Disable STP and Smart Link on the Layer 2 port to be added to an ERPS ring.
  + If STP has been enabled on the port, run the [**stp disable**](cmdqueryname=stp+disable) command in the interface view to disable STP.
  + If Smart Link has been enabled on the port, run the [**undo port**](cmdqueryname=undo+port) command in the Smart Link group view to disable Smart Link.
* Before adding a port to an ERPS ring, run the [**control-vlan**](cmdqueryname=control-vlan) command to configure a control VLAN and the [**protected-instance**](cmdqueryname=protected-instance) command to configure an ERP instance.

#### Context

After an ERPS ring is created, add Layer 2 ports to the ERPS ring and configure the port roles so that ERPS can work properly.

Use either of the following methods to add a Layer 2 port to an ERPS ring:

* In the ERPS ring view, add a specified port to the ERPS ring and configure the port role.
* In the interface view, add the port to an ERPS ring and configure the port role.

![](public_sys-resources/note_3.0-en-us.png) 

* An ERPS-enabled port must be configured as a trunk or hybrid port because it needs to allow packets from both the control VLAN and data VLAN to pass through.
* Currently, packets for updating MAC addresses cannot be sent separately. Therefore, it is not recommended that a direct link between two upstream nodes be configured as the RPL.
* Before changing the port role, run the [**shutdown**](cmdqueryname=shutdown) command to shut down the port. After the port role is changed, run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to enable the port. Otherwise, traffic cannot be forwarded.
* Before adding a port to an ERPS ring, disable port security on the port. Otherwise, loops cannot be prevented.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Add a Layer 2 port to an ERPS ring.
   
   
   * In the ERPS ring view, add a specified port to the ERPS ring and configure the port role.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [portswitch](cmdqueryname=portswitch)
     [stp](cmdqueryname=stp) [disable](cmdqueryname=disable)
     [port link-type](cmdqueryname=port+link-type) trunk
     [port trunk allow-pass vlan](cmdqueryname=port+trunk+allow-pass+vlan) { { vlan-id1 [ to vlan-id2 ] }&<1-10> | all }
     [quit](cmdqueryname=quit)
     [erps ring](cmdqueryname=erps+ring) ring-id
     [port](cmdqueryname=port) interface-type interface-number [ rpl { owner | neighbour } ]
     ```
   * In the interface view, add the port to an ERPS ring and configure the port role.
     ```
     interface interface-type interface-number
     [portswitch](cmdqueryname=portswitch)
     [stp](cmdqueryname=stp) [disable](cmdqueryname=disable)
     [port link-type](cmdqueryname=port+link-type) trunk
     [port trunk allow-pass vlan](cmdqueryname=port+trunk+allow-pass+vlan) { { vlan-id1 [ to vlan-id2 ] }&<1-10> | all }
     [erps ring](cmdqueryname=erps+ring) ring-id [ rpl { owner | neighbour } ]
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```