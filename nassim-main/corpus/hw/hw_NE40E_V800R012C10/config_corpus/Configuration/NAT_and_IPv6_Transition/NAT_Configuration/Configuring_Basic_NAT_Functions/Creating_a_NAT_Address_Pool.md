Creating a NAT Address Pool
===========================

You can create a NAT address pool and bind it to a NAT instance to translate between private and public IPv4 addresses.

#### Context

A NAT address pool can be configured in a NAT instance for address translation based on 5-tuple or 3-tuple information in user packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. Use the non-Easy IP or Easy IP mode to configure a NAT address pool.
   
   
   * In non-Easy IP mode, create or enter a NAT address pool. When a device performs NAT to access the public network, the device obtains a public IP address from the address pool as the source IP address.
     
     + Run the [**nat address-group**](cmdqueryname=nat+address-group+group-id+mask+vpn-instance+no-pat) *address-group-name* [ **group-id** *id* ] [ *start-address* { **mask** { *address-mask-length* | *address-mask* } | *end-address* } ] [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ] command.
       
       When the [**nat address-group**](cmdqueryname=nat+address-group+group-id) mode is used to create a NAT address pool, the **group-id** parameter needs to be specified. *id* specifies the ID of an address pool. Different address pools have different IDs.
       
       The [**nat address-group**](cmdqueryname=nat+address-group) command configures a range of public IP addresses in a single public address pool. The configuration mode can be one of the following:
       - Specify the **mask** parameter in the [**nat address-group**](cmdqueryname=nat+address-group) command. The device generates the same number of public UNR routes as there are NAT address pools, and each route mask is the same as the mask specified in the corresponding command.
       - Specify the start and end IP addresses (i.e., **start-end** mode) in the [**nat address-group**](cmdqueryname=nat+address-group) command. The device generates the same number of public UNR routes as there are public IP addresses in the range specified by the **start-end** mode. The mask of the public UNR routes is 32 bits. For details about UNR routes, see [UNR Route Feature Description](dc_ne_feature_013010.html)
     + Run the [**nat address-group**](cmdqueryname=nat+address-group) *address-group-name* command to enter the NAT address pool view, and then run the [**section**](cmdqueryname=section+mask) *section-num* *start-ip-address* { **mask** { *mask-length* | *mask-ip* } | *end-ip-address* } command.
       
       The [**section**](cmdqueryname=section) command configures multiple public IP address ranges in a single public IP address pool. The configuration mode can be one of the following:
       - Specify the **mask** parameter in the [**section**](cmdqueryname=section) command. The device generates the same number of public UNR routes as there are sections, and each route mask is the same as the mask specified in the corresponding command.
       - Specify the start and end IP addresses (i.e., **start-end** mode) in the [**section**](cmdqueryname=section) command. The device generates the same number of public UNR routes as there are public IP addresses in the range specified by the **start-end** mode. The mask of the public UNR routes is 32 bits. For details about UNR routes, see [UNR Route Feature Description](dc_ne_feature_013010.html)
       
       The **mask** mode is recommended. With this mode enabled in NAT public IP address pools, the mask of each public UNR route to be advertised is the same as the mask specified in the [**nat address-group**](cmdqueryname=nat+address-group) command. In **start-end** mode, the mask of public UNR routes to be advertised is 32 bits.
   * In Easy IP mode, create the reusing relationship between a NAT address pool and an interface IP address and use the interface address to access the public network.
     
     + Run the [**nat address-group**](cmdqueryname=nat+address-group+group-id+unnumbered+interface) *address-group-name* **group-id** *id* **unnumbered interface** { *interface-name* | *interface-type* *interface-number* } command.
     + Run the [**nat address-group**](cmdqueryname=nat+address-group) *address-group-name* command to enter the NAT address pool view and then the [**section**](cmdqueryname=section+unnumbered+interface) *section-num* **unnumbered interface** { *interface-name* | *interface-type* *interface-number* } command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A NAT address pool cannot contain a DHCP server address. You need to properly allocate address segments. Otherwise, NAT traffic cannot be forwarded.
4. (Optional) Create a NAT overloaded address pool and bind the public address pool to this overloaded address pool.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only the NE40E-M2K and NE40E-M2K-B support this configuration.
   
   1. Configure a NAT overloaded address pool or enter the view of a NAT overloaded address pool.
      
      You can configure an address segment for the NAT overloaded address pool using either of the following methods:
      * Method 1: Run the [**nat address-group**](cmdqueryname=nat+address-group+group-id+mask+vpn-instance+over-load) *address-group-name* **group-id** *group-id* *start-address* { **mask** { *address-mask-length* | *address-mask* } | *end-address* } [ **vpn-instance** *vpn-instance-name* ] **over-load** command directly in the NAT instance view.
      * Method 2: Run the [**nat address-group**](cmdqueryname=nat+address-group+group-id+vpn-instance+over-load) *address-group-name* [ **group-id** *group-id* [ **vpn-instance** *vpn-instance-name* ] ] **over-load** command to enter the NAT overloaded address pool view first, and then run the [**section**](cmdqueryname=section+mask) *section-num* *start-ip-address* { **mask** { *mask-length* | *mask-ip* } | *end-ip-address* } command.
      ![](../../../../public_sys-resources/note_3.0-en-us.png) Note the following issues when configuring a NAT overloaded address pool:
      * The common IP address pool in no-PAT mode cannot be used as a NAT overloaded address pool.
      * The address pool created in Easy IP mode cannot be used as, or bound to a NAT overloaded address pool.
      * The [**nat outbound**](cmdqueryname=nat+outbound) command cannot be run for a NAT overloaded address pool to configure a NAT conversion policy.
   2. Run the [**nat address-group**](cmdqueryname=nat+address-group+bind-over-load) *address-group-name* **bind-over-load** *address-group-name* command to bind a common address pool to the overloaded address pool.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) After the common address pool is bound to the NAT overloaded address pool, note the following:
      * [Step 5](#EN-US_TASK_0172374495__exclude-ip) is not allowed. This is because the binding is mutually exclusive with the [**nat address-group exclude-ip-address**](cmdqueryname=nat+address-group+exclude-ip-address) and [**section exclude-ip-address**](cmdqueryname=section+exclude-ip-address) commands.
      * The NAT instance in which the binding is configured cannot be configured as a load-balancing instance group.
5. (Optional) Exclude an IP address or IP address range from a NAT address pool.
   
   
   * If the [**nat address-group**](cmdqueryname=nat+address-group) mode is used, run the [**nat address-group**](cmdqueryname=nat+address-group+exclude-ip-address) *address-group-name* **exclude-ip-address** *start-address* [ *end-address* ] command.
   * If the [**section**](cmdqueryname=section) mode is used, run the [**section**](cmdqueryname=section+exclude-ip-address) *section-id* **exclude-ip-address** *start-address* [ *end-address* ] command.
6. (Optional) Run [**section**](cmdqueryname=section+lock) *section-num* **lock**
   
   
   
   An address segment in the address pool is locked.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only the NE40E-M2K and NE40E-M2K-B support this configuration.
   
   IP addresses in the locked address segment cannot be allocated to users anymore. To unlock this address segment, run the [**undo section**](cmdqueryname=undo+section+lock) *section-num* **lock** command.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the NAT instance view.
8. (Optional) Run [**nat filter mode full-cone**](cmdqueryname=nat+filter+mode+full-cone+5-tuple-session) [ **5-tuple-session** ]
   
   
   
   The address translation mode of all address pools is set to the full-cone mode in the NAT instance.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only the NE40E-M2K and NE40E-M2K-B support this configuration.
   
   To configure the full-cone mode (3-tuple mode) to be implemented based on 5-tuple sessions in a NAT instance, run the [**nat filter mode full-cone**](cmdqueryname=nat+filter+mode+full-cone+5-tuple-session) **5-tuple-session** command. In a NAT444 scenario, when the full-cone mode is configured and a private network source communicates with multiple public network destinations, to record session logs of each destination, 5-tuple sessions are used for the full-cone mode. In this situation, 5- and 3-tuple sessions are generated, with both consuming session license resources.
9. (Optional) Run [**nat no-pat enhance**](cmdqueryname=nat+no-pat+enhance)
   
   
   
   The no-PAT conversion function is enabled for all IP protocol packets.
   
   After this command is run, the address pool mode in the instance can only be no-PAT, and the PAT and no-PAT address pools cannot both be configured.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.