Specifying the Packet Priority Trusted on an Interface
======================================================

Specifying the Packet Priority Trusted on an Interface

#### Context

The priority trusted on an interface determines the type of priority to be mapped for packets on the interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
   
   To enter the Layer 2 sub-interface view, run the [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2** command.
3. Specify the priority to be mapped for packets.
   
   
   ```
   [trust](cmdqueryname=trust) { 8021p { inner | outer } | dscp }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The Ethernet interface working in Layer 3 mode trusts DSCP values by default, and the priority to be mapped for packets cannot be specified.
   
   Layer 3 sub-interfaces do not support the **trust 8021p inner** command.
   
   The **inner** parameter, that is, performing mapping for packets based on the 802.1p priority in the inner VLAN tag, is not supported by the CE6885-LL (low latency mode).
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```