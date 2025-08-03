Maintaining Logical Interfaces
==============================

Maintaining Logical Interfaces

#### Context

You can configure the alarm and statistics collection functions for logical interfaces to maintain them.

![](public_sys-resources/note_3.0-en-us.png) 

This configuration is not supported by the CE6885-LL (low latency mode).



#### Disabling Sub-interfaces from Generating linkDown Alarms

Run the [**subinterface trap updown disable**](cmdqueryname=subinterface+trap+updown+disable) command in the system view to disable sub-interfaces from generating linkDown alarms.

![](public_sys-resources/note_3.0-en-us.png) 

After the command is run, linkDown alarms are no longer generated on any of the device's sub-interfaces when their status changes. Exercise caution when running this command.



#### Enabling Traffic Statistics Collection on a Layer 3 Sub-interface

To check the network status or troubleshoot network faults, enable traffic statistics collection on a Layer 3 sub-interface.

![](public_sys-resources/note_3.0-en-us.png) 

By default, traffic statistics collection is disabled on Layer 3 sub-interfaces.

After traffic statistics collection is enabled, you can run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command in any view or the [**display this interface**](cmdqueryname=display+this+interface) command in the interface view to check traffic statistics on the interface.

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Layer 3 sub-interface view.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number.subinterface-number
   ```
3. (Optional) Enable IPv6 on the sub-interface.
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To enable IPv6 packet statistics collection on a Layer 3 sub-interface, you must first enable IPv6 on the sub-interface.
4. Enable traffic statistics collection on the Layer 3 sub-interface.
   ```
   [statistics](cmdqueryname=statistics) { ipv4 | ipv6 } enable [ inbound | outbound ]
   ```
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Enabling Traffic Statistics Collection on a Layer 2 Sub-interface

To check the network status or troubleshoot network faults, enable traffic statistics collection on a Layer 2 sub-interface.

![](public_sys-resources/note_3.0-en-us.png) 

By default, traffic statistics collection is disabled on Layer 2 sub-interfaces.

After traffic statistics collection is enabled, you can run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command in any view or the [**display this interface**](cmdqueryname=display+this+interface) command in the interface view to check traffic statistics on the interface.

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Exit the main interface view.
   ```
   [quit](cmdqueryname=quit)
   ```
3. Enter the Layer 2 sub-interface view.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number.subinterface-number mode l2
   ```
4. Enable traffic statistics collection on the Layer 2 sub-interface.
   ```
   [statistics enable](cmdqueryname=statistics+enable)
   ```
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```