Configuring the Dynamic Secure MAC Address Function
===================================================

Configuring the Dynamic Secure MAC Address Function

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
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the port security function is enabled, the dynamic secure MAC address function takes effect.
5. (Optional) Configure a protection action for port security on an interface.
   
   
   ```
   port-security protect-action { protect | restrict | error-down }
   ```
6. (Optional) Set the aging time for dynamic secure MAC address entries.
   
   
   ```
   [port-security aging-time](cmdqueryname=port-security+aging-time) time [ type { absolute | inactivity } ]
   ```
   
   If the aging time is too short (for example, 1 minute), dynamic secure MAC address entries will age fast, which may cause traffic forwarding failures.
7. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
8. (Optional) Delete the dynamic secure MAC address entries.
   
   
   ```
   [undo mac-address security](cmdqueryname=undo+mac-address+security) { [ interface-type interface-number | interface-name ] | [ vlan vlanId ] } *
   ```
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the **display port-security** [ **interface** { *interface-type**interface-number* | *interface-name* } ] command to check port security information.
* Check the port security-related alarms by running the [**display trapbuffer**](cmdqueryname=display+trapbuffer) command or through the NMS.