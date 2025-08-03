Configuring PCP Functions
=========================

Configuring PCP Functions

#### Context

PCP is enabled by default in a NAT or DS-Lite instance. A CGN device (PCP server) must be assigned an IP address so that a CPE (PCP client) can send a request to establish a PCP connection to the CGN device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsm on-board-mode disable**](cmdqueryname=vsm+on-board-mode+disable)
   
   
   
   The dedicated board working mode is specified.
3. Run [**license**](cmdqueryname=license)
   
   
   
   The license view is displayed.
4. Run [**active pcp vsuf**](cmdqueryname=active+pcp+vsuf) **slot** *slot-id*
   
   
   
   PCP is enabled on a specified service board.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the license view.
7. Perform the following operations based on whether the CPE and CGN devices are deployed in a NAT444 or DS-Lite scenario:
   * In a NAT444 scenario, perform the following steps:
     1. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* **id** *id*
        
        The NAT instance view is displayed.
     2. Run [**pcp enable**](cmdqueryname=pcp+enable)
        
        The PCP function is enabled in the NAT instance.
     3. Run [**pcp server**](cmdqueryname=pcp+server) **ipv4** *ipv4âaddress* { *mask* | *mask-len* }An IPv4 address is configured for the PCP server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + Only one IPv4 address can be configured for a PCP server in each NAT instance, and the specified address cannot be used as a physical interface address, a loopback interface address, or an address in an address pool.
        + Static routes need to be configured when a CPE device is deployed on a VPN network.
     4. (Optional) Run [**pcp version1 ignore prefer-failure**](cmdqueryname=pcp+version1+ignore+prefer-failure)
        
        The device is configured to send PCPv1 response packets without the prefer\_failure option.
        
        A non-Huawei CPE may fail to identify PCPv1 response packets carrying the prefer\_failure option. As a result, the non-Huawei CPE cannot communicate with the CGN device in this situation. To prevent this issue, run the [**pcp version1 ignore prefer-failure**](cmdqueryname=pcp+version1+ignore+prefer-failure) command to enable the CGN device to send PCPv1 response packets without the prefer\_failure option.
     5. (Optional) Run [**port-reservation**](cmdqueryname=port-reservation) *start-port* **to** *end-port* [ **extend well-known-port** ]
        
        The port reservation function is enabled.
        
        If the port requested by the PCP client is not within the port range, the PCP client can apply for port preemption from the reserved port range.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        When users go offline and then go online again, to allow the users to obtain the same ports or port range as that before the users go offline, perform the following operations: Configure the port reservation function, and configure the RADIUS server to carry the HW-NAT-Start-Port (162) and HW-NAT-End-Port (163) private attributes and deliver the reserved ports or port range to the users.
     6. (Optional) Run [**nat log session port-reservation**](cmdqueryname=nat+log+session+port-reservation)
        
        The device is enabled to record PCP port reservation logs.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + The flow and user log functions must be enabled in the NAT instance and the log host information must be configured. For configuration details, see [Configuring the NAT Log Function](dc_ne_nat_cfg_0047.html).
        + When the port that the PCP client preempts is within the reserved port range and the device is enabled to send port reservation log messages in the instance, the device sends flow log messages. In the other situations, the device does not send flow log messages. User log messages can be used for source tracing.
     7. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     8. Run [**quit**](cmdqueryname=quit)
        
        Exit the NAT instance view.
   * In a DS-Lite scenario, perform the following steps:
     1. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* **id** *id*
        
        The DS-Lite instance view is displayed.
     2. Run [**pcp enable**](cmdqueryname=pcp+enable)
        
        The PCP function is enabled in the DS-Lite instance.
     3. Run [**pcp server**](cmdqueryname=pcp+server) { **ipv4** *ipv4âaddress* { *mask* | *mask-len* } | **ipv6** *ipv6âaddress* *prefix-length* }The IP address of the PCP server is configured.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        A single PCP server IPv4 address and a single PCP server IPv6 address can be specified in each DS-Lite instance, and the specified address cannot be used as a physical interface address, a loopback interface address, or an address in an address pool.
     4. (Optional) Run [**pcp version1 ignore prefer-failure**](cmdqueryname=pcp+version1+ignore+prefer-failure)
        
        The device is configured to send PCPv1 response packets without the prefer\_failure option.
        
        A non-Huawei CPE may fail to identify PCPv1 response packets carrying the prefer\_failure option. As a result, the non-Huawei CPE cannot communicate with the CGN device in this situation. To prevent this issue, run the [**pcp version1 ignore prefer-failure**](cmdqueryname=pcp+version1+ignore+prefer-failure) command to enable the CGN device to send PCPv1 response packets without the prefer\_failure option.
     5. (Optional) Run [**port-reservation**](cmdqueryname=port-reservation) *start-port* **to** *end-port* [ **extend well-known-port** ]
        
        The port reservation function is enabled.
        
        If the port requested by the PCP client is not within the port range, the PCP client can apply for port preemption from the reserved port range.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        When users go offline and then go online again, to allow the users to obtain the same ports or port range as that before the users go offline, perform the following operations: Configure the port reservation function, and configure the RADIUS server to carry the HW-NAT-Start-Port (162) and HW-NAT-End-Port (163) private attributes and deliver the reserved ports or port range to the users.
     6. (Optional) Run [**pcp port-set max-size**](cmdqueryname=pcp+port-set+max-size) *size-value*
        
        The maximum size of a port set is configured.
        
        If a PCP request packet sent by a client carries the Port Set Option field, you can run this command to apply for a group of public network ports.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + This function applies only to PCP request packets of the MAP protocol type.
        + This function applies only to the DS-Lite scenario.
     7. (Optional) Run [**ds-lite log session port-reservation**](cmdqueryname=ds-lite+log+session+port-reservation)
        
        The device is enabled to record PCP port reservation logs.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        + The flow and user log functions must be enabled in the DS-Lite instance and the log host information must be configured. For configuration details, see [Configuring the DS-Lite Log Function](dc_ne_ds-lite_cfg_0048.html).
        + When the port that the PCP client preempts is within the reserved port range and the device is enabled to send port reservation log messages in the instance, the device sends flow log messages. In the other situations, the device does not send flow log messages. User log messages can be used for source tracing.
     8. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     9. Run [**quit**](cmdqueryname=quit)
        
        Exit the DS-Lite instance view.
8. (Optional) Specify a PCP server name in a DHCP Option field.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Perform the following operations based on whether the CPE and CGN/BRAS are deployed on an IPv4 or IPv6 network:
      
      
      * On an IPv4 network, perform the following steps:
        1. Run [**ip pool**](cmdqueryname=ip+pool) *pool-name* **bas** **local**
           
           The IPv4 address pool view is displayed.
        2. Run [**option**](cmdqueryname=option) *code* { { **ip** *ip-address* } &<1-2> | **string** *string* | { **suboption** *subcode* { **ip** *ip-address* | **string** *string* } } &<1-16> }
           
           The PCP server name is specified in a specified DHCPv4 Option field.
      * On an IPv6 network, perform the following steps:
        1. Run [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* **bas** **local**
           
           The IPv6 address pool view is displayed.
        2. Run [**option**](cmdqueryname=option) *code* { { **ipv6** *ipv6-address* } &<1-2> | **string** *string* | **hex** *hex* | { **suboption** *subcode* { **ipv6** *ipv6-address* | **string** *string* | **hex** *hex* } } &<1-16> }
           
           The PCP server name is specified in a specified DHCPv6 Option field.
9. (Optional) Specify a PCP server name to be delivered by a RADIUS server.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
      
      
      
      The RADIUS server group view is displayed.
   3. Run [**radius-attribute assign**](cmdqueryname=radius-attribute+assign) **hw-pcp-server-name** { [**dhcp**](cmdqueryname=dhcp) **dhcp-option-code** | [**dhcpv6**](cmdqueryname=dhcpv6) **dhcpv6-option-code** }
      
      
      
      The HW-PCP-Server-Name attribute in a RADIUS Access-Accept packet is encapsulated into the DHCP/DHCPv6 Option field.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the RADIUS server group view.
10. (Optional) Run [**pcp prefer-failure enhance enable**](cmdqueryname=pcp+prefer-failure+enhance+enable)
    
    
    
    PCP prefer\_failure enhancement is enabled.
    
    
    
    For PCP MAP request packets carrying the prefer\_failure option and non-0 public network IP addresses, PCP prefer\_failure enhancement is enabled to allow the PCP server to randomly assign a public IP address.
11. (Optional) Run [**pcp lifetime**](cmdqueryname=pcp+lifetime) **min-time** *min-value* **max-time** *max-value*
    
    
    
    The minimum and maximum lifetime values for PCP connections are set.
    
    
    
    After the lifetime elapses, a CGN device terminates PCP connections to release resources. You can set the minimum and maximum lifetime values based on the network traffic volume and the number of resources.