Disabling MAC Address Learning on an Interface
==============================================

Disabling MAC Address Learning on an Interface

#### Context

You can disable MAC address learning on an interface in some situations to improve security. For example, if an interface is connected to a server, you can configure a static MAC address entry with the MAC address of the server, disable MAC address learning, and set an action to discard packets with unknown MAC addresses. This configuration prevents other servers or terminals from accessing the interface, improving network stability and security.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Ethernet interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 3 to Layer 2. Determine whether to perform this step based on the current interface working mode.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
4. Disable MAC address learning.
   
   
   ```
   [mac-address learning disable](cmdqueryname=mac-address+learning+disable) [ action { discard | forward } ]
   ```
   
   By default, a device performs the **forward** action after MAC address learning is disabled. That is, the device forwards a packet if it finds a matching entry in the MAC address table. Otherwise, the device broadcasts the packet. When the action is set to **discard**, the device searches for the source MAC address of a packet in the MAC address table. If the source MAC address and source interface are found in the MAC address table, the device forwards the packet according to the MAC address entry. Otherwise, the device discards the packet.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **interface** *interface-type interface-number* command to check whether MAC address learning has been disabled on the interface.