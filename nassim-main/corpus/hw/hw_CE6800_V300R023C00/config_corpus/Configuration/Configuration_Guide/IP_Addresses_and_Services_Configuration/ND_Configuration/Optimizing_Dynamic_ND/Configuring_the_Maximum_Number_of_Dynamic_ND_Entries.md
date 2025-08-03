Configuring the Maximum Number of Dynamic ND Entries
====================================================

Configuring the Maximum Number of Dynamic ND Entries

#### Context

Configuring the maximum number of dynamic ND entries protects against RA flood attacks.


#### Procedure

* Configure the maximum number of dynamic ND entries allowed by a Layer 3 interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  4. Enable IPv6.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  5. Configure the maximum number of dynamic ND entries allowed by the interface.
     
     
     ```
     [ipv6 nd neighbor-limit](cmdqueryname=ipv6+nd+neighbor-limit) max-number
     ```
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the maximum number of dynamic ND entries related to a Layer 2 interface that the VLANIF interface corresponding to the Layer 2 interface can learn.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 2.
     
     
     ```
     [portswitch](cmdqueryname=portswitch)
     ```
  4. Configure the maximum number of dynamic ND entries related to the Layer 2 interface that the corresponding VLANIF interface can learn.
     
     
     ```
     [ipv6 nd neighbor-limit vlan](cmdqueryname=ipv6+nd+neighbor-limit+vlan) vlanBegValue [ to vlanEndValue ] maximum limit-number
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```