Configuring ARP Entry Limiting
==============================

Configuring ARP Entry Limiting

#### Context

If a device receives excessive ARP messages in a short period, the device's buffer will overflow, interrupting the services of authorized users. This issue can be solved by configuring ARP entry limiting for interfaces.

ARP entry limiting controls the maximum number of dynamic ARP entries that a gateway's interface can learn. By default, the maximum number of dynamic ARP entries that an interface can learn is the same as that supported by the gateway. After ARP entry limiting is deployed, if the number of dynamic ARP entries that a specified interface learned reaches the maximum, the interface cannot continue to learn dynamic ARP entries. This prevents ARP entries from being exhausted when a user host connected to this interface initiates ARP attacks.


#### Procedure

* Configure ARP entry limiting for a Layer 2 interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
     ```
  3. Switch the interface working mode to Layer 2.
     
     
     ```
     [portswitch](cmdqueryname=portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure ARP entry limiting.
     
     
     ```
     [arp limit](cmdqueryname=arp+limit) vlan vlan-id1 [ to vlan-id2 ] maximum
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure ARP entry limiting for a Layer 3 interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure ARP entry limiting.
     
     
     ```
     [arp limit](cmdqueryname=arp+limit) limitMaxNum
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display arp limit**](cmdqueryname=display+arp+limit) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ **vlan** *vlan-id* ] command to check the configuration of ARP entry limiting.


#### Follow-up Procedure

* (Optional) After configuring ARP entry limiting on a VBDIF interface, you can run the [**arp limit alarm-threshold**](cmdqueryname=arp+limit+alarm-threshold) command on the interface to configure an alarm threshold. When the number of ARP entries learned by the VBDIF interface reaches the alarm threshold, the device sends an alarm, indicating that excess dynamic ARP entries need to be deleted.![](public_sys-resources/note_3.0-en-us.png) 
  
  This configuration is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6820H, CE6820H-K, CE6820S, CE6885-LL in standard forwarding mode, and CE6863E-48S8CQ.

* If the [**arp limit**](cmdqueryname=arp+limit) command is not run on an interface, the maximum number of dynamic ARP entries that the interface can learn is not limited. If the [**arp limit**](cmdqueryname=arp+limit) command has been run, the default alarm threshold is 80%.