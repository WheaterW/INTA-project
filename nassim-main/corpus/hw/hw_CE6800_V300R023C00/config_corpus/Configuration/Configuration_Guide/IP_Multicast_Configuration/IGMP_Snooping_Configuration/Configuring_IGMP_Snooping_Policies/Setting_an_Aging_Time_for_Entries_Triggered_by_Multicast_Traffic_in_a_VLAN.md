Setting an Aging Time for Entries Triggered by Multicast Traffic in a VLAN
==========================================================================

Setting an Aging Time for Entries Triggered by Multicast Traffic in a VLAN

#### Context

When a multicast source no longer sends multicast data to a multicast group, the device needs to delete the corresponding (S, G) or (\*, G) entry. To achieve this, the device continuously detects whether there is multicast traffic sent to the multicast group. After an aging time is set for entries triggered by multicast traffic in a VLAN, the device considers that no traffic exists for a multicast group and deletes the corresponding (S, G) or (\*, G) entry if the device does not receive any multicast data packets destined for the multicast group within the specified time. In this manner, multicast entries are updated and entry resources are released in a timely manner.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Set an aging time for entries triggered by multicast traffic in the VLAN.
   
   
   ```
   [multicast layer-2 source-lifetime](cmdqueryname=multicast+layer-2+source-lifetime) lifetime 
   ```
   
   By default, the aging time of an entry triggered by multicast traffic is 210 seconds.
   
   The aging time can be flexibly configured based on the number of multicast entries used on the network. If many multicast entries exist and the configured time is too short, some entries cannot be generated. Conversely, if the time is too long, unused entries cannot be promptly deleted and system resources cannot be released. The recommended values are as follows:
   
   **Table 1** Aging time for multicast entries in a VLAN
   | Number of Entries | Recommended Value |
   | --- | --- |
   | Within 1000 | Default value |
   | 1000 to 2000 | 1000 seconds |
   | 2000 to 8000 | 2000 seconds |
   | More than 8000 | 3000 seconds or 4000 seconds |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```