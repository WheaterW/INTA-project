Configuring ARP and ND Entry Synchronization
============================================

Configuring ARP and ND Entry Synchronization

#### Context

When M-LAG master and backup devices function as Layer 3 gateways, M-LAG member interfaces need to periodically synchronize learned ARP and ND entries so that the M-LAG works properly. In this case, the two devices synchronize ARP and ND entries in batches to improve their synchronization efficiency. To ensure that the devices run properly when synchronization efficiency is improved, you can run commands to set proper ARP and ND entry synchronization rates.

For the CE6820H, CE6820H-K, and CE6820S: VXLAN-related configurations are not supported.

For the CE6885-LL (low latency mode): VXLAN and IPv6-related configurations are not supported.


#### Procedure

* (Optional) Configure ARP entry synchronization.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Set the rate at which ARP entries are synchronized.
     
     
     ```
     [arp remote-backup-rate limit](cmdqueryname=arp+remote-backup-rate+limit) ratelimit
     ```
     
     By default, the system synchronizes 2000 ARP entries per second in an M-LAG.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + Changing the rate at which ARP entries are synchronized using this command may affect the CPU usage.
     + If the dynamic ARP entries learned through an M-LAG member interface are deleted, the device is triggered to learn the ARP entries again when receiving corresponding traffic.
     + This command takes effect for synchronization of dynamic ARP entries and interface ARP entries.
     + The ARP entries that are synchronized from the remote end are also dynamic ARP entries, and share the specifications with dynamic ARP entries on the local end.
     + If the device fails to learn dynamic ARP entries through the M-LAG member interface because the number of ARP entries on the device reaches the maximum value, you can delete other ARP entries based on service requirements so that the device can be triggered to learn the dynamic ARP entries again when receiving corresponding traffic.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure ND entry synchronization.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VLANIF or VBDIF interface view.
     
     
     + Enter the VLANIF interface view.
       ```
       [interface](cmdqueryname=interface) vlanif vlan-id
       ```
     + Enter the VBDIF interface view.
       ```
       [interface](cmdqueryname=interface) vbdif bd-id 
       ```
  3. Enable IPv6 on the interface.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  4. Configure the device to generate ND entries on the interface upon receipt of valid NA messages if no ND entry exists on the interface.
     
     
     ```
     [ipv6 nd na glean](cmdqueryname=ipv6+nd+na+glean)
     ```
     
     By default, the device does not generate ND entries on an interface upon receipt of valid NA messages if no ND entry exists on the interface.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     To synchronize ND entries in an M-LAG, configure the [**ipv6 nd na glean**](cmdqueryname=ipv6+nd+na+glean) command. This configuration enables the M-LAG backup device to generate ND entries upon receipt of valid NA messages if no ND entry exists. After learning the entries, the M-LAG backup device synchronizes the entries to the M-LAG master device.
  5. Exit the interface view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
  7. (Optional) Set the rate at which ND entries are synchronized.
     
     
     ```
     [ipv6 nd remote-backup-rate limit](cmdqueryname=ipv6+nd+remote-backup-rate+limit) ratelimit
     ```
     
     By default, the system synchronizes 2000 ND entries per second in an M-LAG.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + If the dynamic ND entries learned through an M-LAG member interface are deleted, the device is triggered to learn the ND entries again when receiving corresponding traffic.
     + This command takes effect only for synchronization of dynamic ND entries.
     + After a dynamic entry is switched to a static or remote entry, the entry is not synchronized to the remote end, and the local end does not instruct the remote end to delete the entry.
     + The ND entries that are synchronized from the remote end are also dynamic ND entries, and share the specifications with dynamic ND entries on the local end.
     + If the device fails to learn dynamic ND entries through the M-LAG member interface because the number of ND entries on the device reaches the maximum value, you can delete other ND entries based on service requirements so that the device can be triggered to learn the dynamic ND entries again when receiving corresponding traffic.
  8. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```