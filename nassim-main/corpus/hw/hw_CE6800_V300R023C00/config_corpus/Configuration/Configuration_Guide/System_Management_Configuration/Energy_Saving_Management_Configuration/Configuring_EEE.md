Configuring EEE
===============

Configuring EEE

#### Context

Energy Efficient Ethernet (EEE) enables the system to dynamically adjust the power of electrical interfaces according to the network traffic. Specifically, the system automatically reduces the power supply to idle interfaces, thereby reducing the overall energy consumption.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Enable EEE for the electrical interface.
   
   
   ```
   [eee enable](cmdqueryname=eee+enable)
   ```
   
   By default, EEE is disabled on an electrical interface.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The EEE function can be configured only on a combo interface working in electrical mode or on an electrical interface (except the management interface).
   
   After the [**eee enable**](cmdqueryname=eee+enable) command is run on an interface in Up state, the interface alternates between Up and Down states.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```