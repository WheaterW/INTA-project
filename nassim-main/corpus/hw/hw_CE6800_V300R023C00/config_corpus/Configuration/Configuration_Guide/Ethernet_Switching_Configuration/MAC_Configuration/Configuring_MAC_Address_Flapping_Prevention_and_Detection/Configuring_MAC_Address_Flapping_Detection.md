Configuring MAC Address Flapping Detection
==========================================

Configuring MAC Address Flapping Detection

#### Context

MAC address flapping detection enables a device to check for MAC address flapping among all MAC addresses. If MAC address flapping occurs, the device will send a trap to the NMS. In addition, you can run the **[**display mac-address flapping active-table**](cmdqueryname=display+mac-address+flapping+active-table)** command to view MAC address flapping records and run the **[**display mac-address flapping aged-table**](cmdqueryname=display+mac-address+flapping+aged-table)** command to view MAC address flapping aging records.

![](public_sys-resources/note_3.0-en-us.png) 

* When MAC address flapping occurs on a device's interface, the device suppresses broadcast, unknown-unicast, and multicast (BUM) traffic, and sets the outbound forwarding rate of the interface to 1% of the inbound bandwidth of the interface. You can run the **storm suppression mac-address flapping** command to configure the committed information rate (CIR) for traffic suppression triggered by MAC address flapping and enable the device to forward packets based on the specified CIR. In this case, you need to check whether a loop exists on the network. Packets are not suppressed due to MAC address flapping in the following scenarios:
  + Storm control or traffic suppression is configured on an interface. For example, if you run the **storm suppression broadcast** command to set the maximum traffic rate of broadcast packets that can pass through an interface, broadcast traffic will not be automatically suppressed if MAC address flapping occurs on the interface.
  + If MAC address flapping occurs on a peer-link interface, traffic suppression associated with MAC address flapping does not take effect on that interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable global MAC address flapping detection.
   
   
   ```
   [mac-address flapping detection](cmdqueryname=mac-address+flapping+detection) [ security-level { low | middle | high } | security-threshold flapCnt ]
   ```
   
   By default, the security level of MAC address flapping detection is middle. At this level, the system considers that MAC address flapping occurs when a MAC address changes 10 times between interfaces.
3. (Optional) Configure a VLAN whitelist for MAC address flapping detection, that is, specify the VLANs where MAC address flapping detection is not performed.
   
   
   ```
   [mac-address flapping detection exclude vlan](cmdqueryname=mac-address+flapping+detection+exclude+vlan) { vlan-id1 [ to vlan-id2 ] } &<1-10>
   ```
4. (Optional) Exclude a MAC address from MAC address flapping detection.
   
   
   ```
   [mac-address flapping detection exclude](cmdqueryname=mac-address+flapping+detection+exclude) mac-address mac-address-mask
   ```
5. (Optional) Set an aging time for flapping MAC addresses.
   
   
   ```
   [mac-address flapping aging-time](cmdqueryname=mac-address+flapping+aging-time) aging-time
   ```
   
   By default, the aging time for flapping MAC addresses is 5 minutes.
6. (Optional) Set the interval for sending traps if MAC address flapping occurs.
   1. Enable the function of periodically reporting traps if MAC address flapping occurs.
      
      
      ```
      [mac-address flapping periodical trap enable](cmdqueryname=mac-address+flapping+periodical+trap+enable)
      ```
      
      By default, the device is disabled from periodically sending traps if MAC address flapping occurs.
   2. Set the interval for sending traps if MAC address flapping occurs.
      
      
      ```
      [mac-address flapping periodical trap interval](cmdqueryname=mac-address+flapping+periodical+trap+interval) interval
      ```
      
      By default, a device sends traps at an interval of 2 minutes if MAC address flapping occurs.
7. (Optional) Configure the action for the device to take after MAC address flapping is detected on an interface.
   1. Enter the interface view.
      
      
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   2. Switch the interface working mode from Layer 3 to Layer 2. Determine whether to perform this step based on the current interface working mode.
      
      
      ```
      [portswitch](cmdqueryname=portswitch)
      ```
   3. Configure the interface to enter the error-down state if MAC address flapping occurs on the interface.
      
      
      ```
      [mac-address flapping trigger](cmdqueryname=mac-address+flapping+trigger) error-down
      ```
      
      By default, an interface will not enter the error-down state when MAC address flapping occurs.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display mac-address flapping**](cmdqueryname=display+mac-address+flapping) [ **slot** *slot-id* ] [ **begin***datetime* *hourtime* ] command to check MAC address flapping records.


#### Follow-up Procedure

When the **mac-address flapping trigger error-down** command is run, the interface where MAC address flapping has occurred will enter the error-down state and sends a trap. The device sets an interface to the error-down state when it detects that MAC address flapping occurs on the interface. An interface in error-down state cannot receive or send packets and the interface indicator is off. You can run the [**display error-down recovery**](cmdqueryname=display+error-down+recovery) command to check information about all error-down interfaces on the device.

If an interface is in error-down state, you are advised to determine the cause first. You can use either one of the following methods for interface recovery, depending on the number of error-down interfaces:

* Manually recover an error-down interface.
  
  This method applies when only a few interfaces need to be recovered. Run either the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands, or the [**restart**](cmdqueryname=restart) command on an interface to recover it.
* Enable automatic interface recovery before any interface enters the error-down state.
  
  This method applies if a large number of interfaces may enter the error-down state. Manually recovering a large number of error-down interfaces is time-consuming and may not cover all the desired interfaces. To avoid this issue, you can run [**error-down auto-recovery**](cmdqueryname=error-down+auto-recovery) **cause** **mac-address-flapping** **interval** *interval-value* command to enable delayed automatic interface recovery to prevent interfaces from being stuck in the error-down state. You can run the [**display error-down recovery**](cmdqueryname=display+error-down+recovery) command to view information about automatic interface recovery.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  This method does not affect interfaces that are already in the error-down state. It affects only interfaces that enter the error-down state after the [**error-down auto-recovery**](cmdqueryname=error-down+auto-recovery) command is run.