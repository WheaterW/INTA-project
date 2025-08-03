Configuring Layer 2/Layer 3 Mode Switching on an Ethernet Interface
===================================================================

Configuring Layer 2/Layer 3 Mode Switching on an Ethernet Interface

#### Context

Ethernet interfaces on Layer 3 devices typically work in Layer 3 mode. To add such interfaces to a VLAN or perform other Layer 2 configurations, switch their working mode to Layer 2. You can switch the working mode of an interface between Layer 2 and Layer 3 as required. In Layer 2 mode, the interface functions as a Layer 2 Ethernet interface. In Layer 3 mode, the interface functions as a Layer 3 Ethernet interface.

![](public_sys-resources/note_3.0-en-us.png) 

Determine whether to switch the working mode of an interface between Layer 2 and Layer 3 based on the interface type.

Eth-Trunk member interfaces do not support the configuration of switching between Layer 2 and Layer 3 modes.



#### Procedure

* Switch the working mode of a single Ethernet interface to Layer 2 in the Ethernet interface view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the Ethernet interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the working mode of the interface to Layer 2.
     
     
     ```
     [portswitch](cmdqueryname=portswitch)
     ```
     
     The mode switching function takes effect when the interface only has attribute configurations, such as [**shutdown**](cmdqueryname=shutdown) and [**description**](cmdqueryname=description) configurations, or configurations supported by both Layer 2 and Layer 3 modes. Before switching the working mode, ensure that the configurations on the interface still support the new working mode. If unsupported configurations exist on the interface, delete the configurations before running the [**portswitch**](cmdqueryname=portswitch) command.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Switch the working mode of a single Ethernet interface to Layer 3 in the Ethernet interface view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the Ethernet interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the working mode of the interface to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     The mode switching function takes effect when the interface only has attribute configurations, such as [**shutdown**](cmdqueryname=shutdown) and [**description**](cmdqueryname=description) configurations, or configurations supported by both Layer 2 and Layer 3 modes. Configurations that are not supported by the target working mode cannot exist on the interface. If unsupported configurations exist on the interface, delete the configurations before running the [**undo portswitch**](cmdqueryname=undo+portswitch) command.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Switch the working modes of Ethernet interfaces to Layer 2 in batches in the system view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Switch the working modes of Ethernet interfaces to Layer 2 in batches.
     
     
     ```
     [portswitch batch](cmdqueryname=portswitch+batch) interface-type { interface-number1 [ to interface-number2 ] } &<1-10>
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Switch the working modes of Ethernet interfaces to Layer 3 in batches in the system view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Switch the working modes of Ethernet interfaces to Layer 3 in batches.
     
     
     ```
     [undo portswitch batch](cmdqueryname=undo+portswitch+batch) interface-type { interface-number1 [ to interface-number2 ] } &<1-10>
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command in any view or the [**display this interface**](cmdqueryname=display+this+interface) command in the interface view to check the current interface status. If the **Switch Port** field is displayed in the command output, the interface is a Layer 2 interface; if the **Route Port** field is displayed, it is a Layer 3 interface.