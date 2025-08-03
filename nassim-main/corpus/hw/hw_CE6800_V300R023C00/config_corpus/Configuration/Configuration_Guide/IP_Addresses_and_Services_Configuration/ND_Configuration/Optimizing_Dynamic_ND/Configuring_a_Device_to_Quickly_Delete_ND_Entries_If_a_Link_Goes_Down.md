Configuring a Device to Quickly Delete ND Entries If a Link Goes Down
=====================================================================

Configuring a Device to Quickly Delete ND Entries If a Link Goes Down

#### Context

If a Layer 2 link goes down, ND entries change to the Delay state. This change triggers ND probing after 5 seconds. If ND probing is unreachable, ND entries are deleted. If a large number of ND entries exist on the link, the deletion takes a long time. As a result, some ND entries may remain for a long time. To address this issue, run the **[**ipv6 nd delete trigger link-down enable**](cmdqueryname=ipv6+nd+delete+trigger+link-down+enable)** command. After the command is run, the device directly deletes ND entries without performing ND probing if a link goes down.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLANIF interface view.
   
   
   ```
   [interface](cmdqueryname=interface) vlanif vlan-id
   ```
3. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
4. Configure the device to quickly delete ND entries if a link goes down.
   
   
   ```
   [ipv6 nd delete trigger link-down enable](cmdqueryname=ipv6+nd+delete+trigger+link-down+enable)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```