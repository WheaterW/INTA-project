(Optional) Enabling One-to-Many Mapping Between One MAC Address and Many Sessions
=================================================================================

(Optional)_Enabling_One-to-Many_Mapping_Between_One_MAC_Address_and_Many_Sessions

#### Context

When the NE40E functions as a BRAS or DHCP server, it can assign IP addresses only to IPoE users with different MAC addresses. If you want the NE40E to assign IP addresses to users with the same MAC address, configure one-to-many mapping between one MAC address and many sessions. These users with the same MAC address must have
different VLAN IDs or interface numbers, and different circuit IDs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipoe-server multi-sessions per-mac enable**](cmdqueryname=ipoe-server+multi-sessions+per-mac+enable)
   
   
   
   One-to-many mapping between one MAC address and many sessions is enabled for IPoE users to allow the NE40E to assign IP addresses to IPoE users with the same MAC address.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.