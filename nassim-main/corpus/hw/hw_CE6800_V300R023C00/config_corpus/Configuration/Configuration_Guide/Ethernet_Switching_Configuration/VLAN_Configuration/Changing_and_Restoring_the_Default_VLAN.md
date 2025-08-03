Changing and Restoring the Default VLAN
=======================================

Changing and Restoring the Default VLAN

#### Context

If an interface works in Layer 3 mode, you need to run the [**portswitch**](cmdqueryname=portswitch) command to change its working mode to Layer 2 before you can change or restore the default VLAN of this interface.


#### Procedure

* Change the default VLAN of an access interface.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [interface](cmdqueryname=interface) interface-type interface-number
  [port link-type](cmdqueryname=port+link-type) access
  [port default vlan](cmdqueryname=port+default+vlan) vlan-id
  [commit](cmdqueryname=commit)
  ```
* Change the default VLAN of a trunk interface.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [interface](cmdqueryname=interface) interface-type interface-number
  [port link-type](cmdqueryname=port+link-type) trunk
  [port trunk pvid vlan](cmdqueryname=port+trunk+pvid+vlan) vlan-id
  [commit](cmdqueryname=commit)
  ```
* Change the default VLAN of a hybrid interface.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [interface](cmdqueryname=interface) interface-type interface-number
  [port link-type](cmdqueryname=port+link-type) hybrid
  [port hybrid pvid vlan](cmdqueryname=port+hybrid+pvid+vlan) vlan-id
  [commit](cmdqueryname=commit)
  ```
* Restore the default VLAN of an access interface.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [interface](cmdqueryname=interface) interface-type interface-number
  [port link-type](cmdqueryname=port+link-type) access
  [undo port default vlan](cmdqueryname=undo+port+default+vlan) [ vlan-id ]
  [commit](cmdqueryname=commit)
  ```
* Restore the default VLAN of a trunk interface.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [interface](cmdqueryname=interface) interface-type interface-number
  [port link-type](cmdqueryname=port+link-type) trunk
  [undo port trunk pvid vlan](cmdqueryname=undo+port+trunk+pvid+vlan) [ vlan-id ]
  [commit](cmdqueryname=commit)
  ```
* Restore the default VLAN of a hybrid interface.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [interface](cmdqueryname=interface) interface-type interface-number
  [port link-type](cmdqueryname=port+link-type) hybrid
  [undo port hybrid pvid vlan](cmdqueryname=undo+port+hybrid+pvid+vlan) [ vlan-id ]
  [commit](cmdqueryname=commit)
  ```

#### Verifying the Configuration

Run the [**display port vlan**](cmdqueryname=display+port+vlan) [ *interface-type interface-number* ] [ **active** ] command to check the default VLAN to which an interface belongs.