Creating a DS-Lite Address Pool
===============================

A DS-Lite address pool can be created so that you can define a public IPv4 address segment for a DS-Lite address pool and assign the address pool to a specific DS-Lite instance before the instance translates between private and public IPv4 addresses.

#### Context

DS-Lite only supports network address port translation (NAPT). In NAPT mode, DS-Lite translates both source IP addresses and port numbers between public and private networks. For packets with the same private source IP address and different source port numbers, DS-Lite in NAPT mode translates the private source IP address in each packet into the same public source IP address and each private source port number into a specific public source port number. A DS-Lite address pool in a DS-Lite instance can be configured and used to translate addresses based on 5- or 3-tuple information in user packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
   
   
   
   The DS-Lite instance view is displayed.
3. Use either of the following methods to configure a DS-Lite address pool:
   
   
   * To configure a single public address segment for a single DS-Lite address pool, run the [**ds-lite address-group**](cmdqueryname=ds-lite+address-group) *address-group-name* **group-id** *id* *start-address* { **mask** { *mask-length* | *address-mask* } | *end-address* } [ **vpn-instance** *vpn-instance-name* ] command.
     
     + Run the [**ds-lite address-group**](cmdqueryname=ds-lite+address-group) command with *start-address* **mask** specified to configure a public IP address segment.
     + Run the [**ds-lite address-group**](cmdqueryname=ds-lite+address-group) command with *start-address* and *end-address* specified to configure a public IP address segment with the specified start and end addresses.
     
     The **mask** mode is recommended. With this mode enabled, the length of routes to be advertised is the same as the mask length specified in the [**ds-lite address-group**](cmdqueryname=ds-lite+address-group) command. If the *start-address* and *end-address* modes are used, the mask length of routes to be advertised is 32 bits.
   * To create multiple public network segments for a single DS-Lite address pool, run the [**ds-lite address-group**](cmdqueryname=ds-lite+address-group) *address-group-name* [ **group-id** *group-id* [ **vpn-instance** *vpn-instance-name* ] ] command to enter the DS-Lite address pool view, and then run the [**section**](cmdqueryname=section) *section-num* *start-ip-address* { **mask** { *mask-length* | *mask-ip* } | *end-ip-address* } command.
     
     + Run the [**section**](cmdqueryname=section) command with *start-address* **mask** specified to configure a public IP address segment.
     + Run the [**section**](cmdqueryname=section) command with *start-address* and *end-address* specified to configure a public IP address segment with the specified start and end addresses.
     
     The **mask** mode is recommended. With this mode enabled, the length of routes to be advertised is the same as the mask length specified in the [**ds-lite address-group**](cmdqueryname=ds-lite+address-group) command. If the *start-address* and *end-address* modes are used, the mask length of routes to be advertised is 32 bits. In the view of the same DS-Lite address pool, if the [**section**](cmdqueryname=section) command is run multiple times, all configurations take effect, and multiple address segments are created; if the [**ds-lite address-group**](cmdqueryname=ds-lite+address-group) command is run multiple times, the latest configuration overrides the previous one, and only a single address segment takes effect.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Addresses in a public address pool cannot be the same as interface IP addresses.
   
   The DS-Lite address pool cannot contain the IP address of a DHCP server. Otherwise, a message indicating a conflict is displayed.
4. (Optional) Exclude an IP address or IP address segment from a DS-Lite address pool.
   
   
   * If the [**ds-lite address-group**](cmdqueryname=ds-lite+address-group) mode is used to create an address pool, run the [**ds-lite address-group**](cmdqueryname=ds-lite+address-group) *address-group-name* **exclude-ip-address** *start-address* [ *end-address* ] command.
     
     This command excludes addresses or address segments for you. If the above command is not run, you must divide a DS-Lite address pool into multiple sub-address pools before excluding some addresses or address segments from the DS-Lite address pool. However, if the above command is run, you do not need to divide the DS-Lite address pool into multiple sub-address pools.
   * If the [**section**](cmdqueryname=section) mode is used to create an address pool, run the [**section**](cmdqueryname=section) *section-id* **exclude-ip-address** *start-address* [ *end-address* ] command.
     
     This command excludes addresses or address segments for you. If the above command is not run, you must divide a section into multiple sub-sections before excluding some addresses or address segments from the DS-Lite address pool configured using the section mode. However, if the above command is run, you do not need to divide a section into multiple sub-sections.
5. (Optional) Run [**section**](cmdqueryname=section) *section-num* **lock**
   
   
   
   An address segment of the address pool is locked.
   
   
   
   IP addresses in the locked address segment cannot be allocated to users any more. To restore this address segment, run the **undo section** command.
6. (Optional) Run [**ds-lite filter mode full-cone**](cmdqueryname=ds-lite+filter+mode+full-cone)
   
   
   
   The full-cone mode is configured for all address pools in the DS-Lite instance.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.