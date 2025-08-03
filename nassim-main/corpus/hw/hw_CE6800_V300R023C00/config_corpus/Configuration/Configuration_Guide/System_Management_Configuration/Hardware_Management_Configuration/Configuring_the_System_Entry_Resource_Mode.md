Configuring the System Entry Resource Mode
==========================================

Configuring the System Entry Resource Mode

#### Context

Typically, entry resources in a system are shared among services. If the resources cannot meet service requirements, you can adjust the system entry resource mode to obtain more configuration entries.

A device supports the following system entry resource modes:

* standard: This is the default mode.
* large-mac: This mode provides more MAC address entries.
* user-defined: This mode allows users to customize the number of MAC address entries as required.
* large-route: This mode provides more routing entries. The large-route mode is applicable to the core layer of a Layer 3 network and enables a device to learn a large number of network segment routes for Layer 3 forwarding.
* balance: This mode enables magnitude-based flow scheduling on a board. In this mode, elephant and mice flows in a queue are differentiated, packets of mice flows are preferentially scheduled, and the delay of mice flows is not affected by elephant flows.
* large-multicast: This mode increases the capacity of the multicast forwarding table.
* large-flow: This mode increases the capacity of the flow table.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the system entry resource mode.
   
   
   * For CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
     ```
     [system resource](cmdqueryname=system+resource) { standard | large-mac | large-route | balance }
     ```
   * For CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM:
     ```
     [system resource](cmdqueryname=system+resource) { standard | large-mac | user-defined { mac mac-value } | large-multicast } 
     ```
   * For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ:
     ```
     [system resource](cmdqueryname=system+resource) { standard | large-mac | large-route | large-multicast | large-flow }
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     For the CE6885-LL series, this configuration is supported only by the CE6885-LL (standard forwarding mode).
   
   The system entry resource mode is defaulted to **standard**.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
4. Exit the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Save the configuration.
   
   
   ```
   [save](cmdqueryname=save)
   ```
6. Restart the device for the configuration to take effect.
   
   
   ```
   [reboot](cmdqueryname=reboot)
   ```

#### Verifying the Configuration

Run the [**display system resource mode**](cmdqueryname=display+system+resource+mode) command to check the configured resource mode and the resource mode that takes effect.