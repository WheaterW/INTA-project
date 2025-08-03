Changing the DHCPv6 Option Code for Interconnection Between Huawei and Non-Huawei Devices
=========================================================================================

On the NE40E, the vendor-class attribute is carried in DHCPv6 Option 16. However, on a non-Huawei device, a different option code may be used. To enable a Huawei device to communicate with a non-Huawei device, you can modify the DHCPv6 option code.

#### Context

If the mapping between the vendor-class attribute and a DHCPv6 option code is configured in both system and BAS interface views, the configuration in the BAS interface view takes effect.


#### Procedure

* Configure a mapping between the vendor-class attribute and a DHCPv6 option code in the system view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vendor-class dhcpv6**](cmdqueryname=vendor-class+dhcpv6) { **option-code** *option-code* | **offset** *offset* } \*
     
     
     
     The mapping between the vendor-class attribute and a DHCPv6 option code as well as the offset value are configured. After the configuration is complete, the BRAS uses the offset value to obtain the desired content in the Value field of the DHCPv6 option.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a mapping between the vendor-class attribute and a DHCPv6 option code in the BAS interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [*. subinterface-number* ]
     
     
     
     The interface view is displayed.
  3. Run [**bas**](cmdqueryname=bas)
     
     
     
     A BAS interface is created, and its view is displayed.
  4. Configure a user access type and related attributes:
     
     
     + To set the access type to Layer 2 common users and configure related attributes, run the [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **bas-interface-name** *bname* | **default-domain** { **pre-authentication** *predname* | **authentication** [ **force** | **replace** ] *dname* } \* | **accounting-copy** **radius-server** *rd-name* ] \* command.
     + To configure the access type and related attributes for Layer 3 common users, run the [**access-type**](cmdqueryname=access-type) **layer3-subscriber** [ **default-domain** { [ **pre-authentication** *predname* ] **authentication** [ **force** | **replace** ] *dname* }\* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       When setting the user access type on a BAS interface, you can set the service attributes of the access users at the same time or later.
       
       - To specify an IP address segment and an associated authentication domain name for Layer 3 common users, run the [**layer3-subscriber**](cmdqueryname=layer3-subscriber) { *start-ip-address* [ *end-ip-address* ] | *start-ipv6-address* [ *end-ipv6-address* ] | **delegation-prefix** *start-ipv6-address* [ *end-ipv6-address* ] [ *end-ip-address* ] *mask-length*} \* [ **vpn-instance** *instance-name* ] **domain-name** *domain-name* and [**layer3-subscriber ip-address any**](cmdqueryname=layer3-subscriber+ip-address+any) **domain-name** *domain-name* commands in the system view.
       - To specify an IPv4 address segment and an associated authentication domain name for Layer 3 static users using the mask mode, run the [**layer3-subscriber subnet-session**](cmdqueryname=layer3-subscriber+subnet-session) *start-ip-address* { *mask-address* | *mask-length* } [ **vpn-instance** *instance-name* ] **domain-name** *domain-name* command in the system view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       - The access type cannot be configured on an Ethernet interface that is added to an Eth-Trunk interface. You can configure the access type of such an Ethernet interface only on the associated Eth-Trunk interface.
       - When configuring static routes for Layer 3 users, specify the next hop as the user IP address and do not specify the outbound interface. Otherwise, network-to-user traffic may fail to be forwarded.
  5. Run [**vendor-class dhcpv6**](cmdqueryname=vendor-class+dhcpv6) { **option-code** *option-code* | **offset** *offset* } \*
     
     
     
     The mapping between the vendor-class attribute and a DHCPv6 option code as well as the offset value are configured. After the configuration is complete, the BRAS uses the offset value to obtain the desired content in the Value field of the DHCPv6 option.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.