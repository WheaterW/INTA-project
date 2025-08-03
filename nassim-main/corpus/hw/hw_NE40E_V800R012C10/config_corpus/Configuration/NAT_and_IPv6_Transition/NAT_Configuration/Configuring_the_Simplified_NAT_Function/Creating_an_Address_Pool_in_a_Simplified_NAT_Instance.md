Creating an Address Pool in a Simplified NAT Instance
=====================================================

You can create a NAT address pool and assign available public IPv4 address segments to a specified NAT instance for translation between private and public IPv4 addresses.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations:
   * To configure a NAT address pool in non-Easy IP mode:
     
     Run the [**nat address-group**](cmdqueryname=nat+address-group) *address-group-name* **group-id** *id* *start-address* { **mask** { *address-mask-length* | *address-mask* } | *end-address* } [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ] command in the system view.
   * To configure a NAT address pool in Easy IP mode:
     
     Run the [**nat address-group**](cmdqueryname=nat+address-group) *address-group-name* **group-id** *id* **unnumbered interface** *interface-type* *interface-number* command in the system view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An address pool of a simplified NAT instance cannot contain the address of a common NAT instance, a DS-Lite address, address-level server's address, or DHCP server's address. Otherwise, a message indicating a conflict is displayed.
   
   The address pool of a simplified NAT instance can be configured only in the global system view.
3. (Optional) Configure No-PAT.
   1. Run the [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ] **simple-configuration** command to enter the NAT instance view.
   2. Run the [**nat no-pat enhance**](cmdqueryname=nat+no-pat+enhance) command to enable No-PAT for IP-layer protocol packets. After this command is run, only No-PAT address pools can be configured in the instance. And PAT and No-PAT address pools cannot be configured in an instance at the same time.
   3. Run the [**quit**](cmdqueryname=quit) command to exit the NAT instance view.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.