Configuring the Sticky MAC Address Function
===========================================

Configuring the Sticky MAC Address Function

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
   ```
3. Change the interface working mode from Layer 3 to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
4. Enable the port security function and set the maximum number of MAC addresses that the interface can learn.
   
   
   ```
   [port-security enable](cmdqueryname=port-security+enable) [ maximum max-number ]
   ```
5. Enable the sticky MAC address function.
   
   
   ```
   [port-security mac-address sticky](cmdqueryname=port-security+mac-address+sticky)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the sticky MAC address function is enabled on an interface, existing dynamic secure MAC address entries and MAC address entries learned subsequently on the interface are converted into sticky MAC address entries.
   
   After the sticky MAC address function is enabled on an interface, sticky MAC address entries will not age even if the [**port-security aging-time**](cmdqueryname=port-security+aging-time) command is configured.
   
   When new sticky MAC address entries are configured or existing sticky MAC address entries are changed, you need to run the [**save**](cmdqueryname=save) command to ensure that the new or changed MAC address entries take effect after the device restarts.
   
   Sticky MAC address entries are saved into a .dtbl, .ztbl, or .ctbl file by running the [**save**](cmdqueryname=save) command. This ensures that sticky MAC address entries will not be lost when the device restarts. The file name must be the same as the name of the system configuration file. For example, if the name of the system configuration file is **test.cfg**, the name of the sticky MAC address entry file must be **test.ctbl**. Otherwise, sticky MAC address entries will fail to recover after the device restarts.
6. (Optional) Configure a protection action for port security on an interface.
   
   
   ```
   port-security protect-action { protect | restrict | error-down }
   ```
7. (Optional) Add a sticky MAC address entry manually.
   
   
   ```
   [port-security mac-address sticky](cmdqueryname=port-security+mac-address+sticky) mac-address vlan vlan-id
   ```
8. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. (Optional) Delete a sticky MAC address entry.
   
   
   ```
   [undo mac-address sticky](cmdqueryname=undo+mac-address+sticky) { [ portType portNum | portName ] | [ vlan vlanId ] } *
   ```
   
   This command is not supported on the CE6885-LL (low latency mode).
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the **display port-security** [ **interface** { *interface-type**interface-number* | *interface-name* } ] command to check port security information.
* Check the port security-related alarms by running the [**display trapbuffer**](cmdqueryname=display+trapbuffer) command or through the NMS.