Configuring a Device to Permit IPv6 Packets Whose First Fragment Carries an Incomplete Header
=============================================================================================

Configuring a Device to Permit IPv6 Packets Whose First Fragment Carries an Incomplete Header

#### Context

After IPv6 is enabled on a device, the device does not permit IPv6 packets whose first fragment carries an incomplete header by default. To use IPv6 packets whose first fragment carries an incomplete header in special scenarios, configure the device to permit such IPv6 packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to permit IPv6 packets whose first fragment carries an incomplete header in the system or interface view.
   * To configure the device to permit IPv6 packets whose first fragment carries an incomplete header in the system view, run the following command:
     ```
     [ipv6 security permit incomplete-first-fragment](cmdqueryname=ipv6+security+permit+incomplete-first-fragment)
     ```
   * To configure the device to permit IPv6 packets whose first fragment carries an incomplete header in the interface view, perform the following steps:
     1. Enter the interface view.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        ```
     2. Switch the interface working mode to Layer 3.
        ```
        [undo portswitch](cmdqueryname=undo+portswitch)
        ```
     3. Enable IPv6.
        ```
        [ipv6 enable](cmdqueryname=ipv6+enable)
        ```
     4. Configure the device to permit IPv6 packets whose first fragment carries an incomplete header.
        
        ```
        [ipv6 security permit incomplete-first-fragment](cmdqueryname=ipv6+security+permit+incomplete-first-fragment)
        ```
     5. Exit the interface view.
        ```
        [quit](cmdqueryname=quit)
        ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```