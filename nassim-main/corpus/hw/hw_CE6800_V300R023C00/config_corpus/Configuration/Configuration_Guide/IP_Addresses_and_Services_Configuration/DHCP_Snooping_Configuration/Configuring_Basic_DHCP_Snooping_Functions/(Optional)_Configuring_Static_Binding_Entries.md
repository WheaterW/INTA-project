(Optional) Configuring Static Binding Entries
=============================================

(Optional) Configuring Static Binding Entries

#### Context

After DHCP snooping is enabled:

* The device can automatically generate dynamic binding entries for users who obtain IP addresses through DHCP.

* The device cannot automatically generate binding entries through DHCP snooping for users whose IP addresses were manually allocated by the administrator.

To ensure that the messages of static users can be forwarded properly, you need to configure static binding entries. After the configuration is complete, the messages that match the binding entries are allowed to pass through, and those that do not match are discarded.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure static binding entries.
   
   
   ```
   [user-bind static](cmdqueryname=user-bind+static) { ip-address { start-ip [ [to](cmdqueryname=to) end-ip ] } &<1-10> | [mac-address](cmdqueryname=mac-address) mac-address }* [ interface interface-type interface-number ] [ vlan vlan-id [ [ce-vlan](cmdqueryname=ce-vlan) ce-vlan-id ] ]
   ```
   
   By default, no static binding entry is generated.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```