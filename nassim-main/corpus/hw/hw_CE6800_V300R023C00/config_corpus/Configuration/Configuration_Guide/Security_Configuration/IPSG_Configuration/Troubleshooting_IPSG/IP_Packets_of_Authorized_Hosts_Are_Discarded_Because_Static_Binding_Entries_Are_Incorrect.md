IP Packets of Authorized Hosts Are Discarded Because Static Binding Entries Are Incorrect
=========================================================================================

IP Packets of Authorized Hosts Are Discarded Because Static Binding Entries Are Incorrect

#### Fault Symptom

A static binding table has been created and IPSG has been enabled; however, the IP packets of an authorized host are discarded.

#### Possible Causes

The binding entries are improperly configured.


#### Procedure

1. Check whether the binding entries are correct.
   
   
   ```
   [display ip source check user-bind status static](cmdqueryname=display+ip+source+check+user-bind+status+static) [ { interface interface-type interface-number | ip-address ip-address | mac-address mac-address | vlan  vlan-id } * ] [ valid | invalid ] [ slot slot-id ]
   ```
2. If the binding entry of the host is not in the binding table, add the host's binding entry to the binding table. The device forwards the packets from a host only when the host's binding entry exists in the binding table.
   
   
   ```
   [user-bind static](cmdqueryname=user-bind+static) { ip-address { start-ip [ to end-ip ] } &<1-10> | mac-address mac-address } * [ interface { interface-type interface-number | interface-name }] [ vlan vlan-id [ ce-vlan ce-vlan-id ] ]
   ```
3. If the host's binding entry exists in the binding table, check whether the MAC address in the entry is the same as the host's MAC address. If the NIC of the host has been replaced but the MAC address in the entry has not been updated, delete the original entry and configure a new one for the host.
   
   
   ```
   [undo user-bind static](cmdqueryname=undo+user-bind+static) [ ip-address { start-ip [ to end-ip ] } &<1-10> | mac-address mac-address | interface { interface-type interface-number | interface-name } | vlan vlan-id [ ce-vlan ce-vlan-id ] ] *
   ```
4. Check whether the entry contains VLAN information. If so, check whether the interface connected to the host has been added to the VLAN. The device forwards the packets from the host only when the interface is added to the VLAN.
   
   
   ```
   [display vlan](cmdqueryname=display+vlan)
   ```