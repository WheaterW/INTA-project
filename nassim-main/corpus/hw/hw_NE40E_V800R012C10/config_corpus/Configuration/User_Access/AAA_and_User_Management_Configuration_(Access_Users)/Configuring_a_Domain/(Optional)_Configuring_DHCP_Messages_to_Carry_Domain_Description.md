(Optional) Configuring DHCP Messages to Carry Domain Description
================================================================

(Optional) Configuring DHCP Messages to Carry Domain Description

#### Context

When IP addresses are assigned from a remote address pool, to enable the DHCP or DHCPv6 server to differentiate the carriers of users going online through the same interface in the same VLAN but in different domains, the messages to be sent to the DHCP or DHCPv6 server must carry a domain description.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**description**](cmdqueryname=description) *description-text*
   
   
   
   A domain description is configured.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the AAA view.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ *.subinterface-number* ]
   
   
   
   The interface view is displayed.
8. Run [**bas**](cmdqueryname=bas)
   
   
   
   The BAS interface view is displayed.
9. Run [**access-type**](cmdqueryname=access-type)
   
   
   
   The access type is set to Layer 2 common user access, Layer 2 private line user access, Layer 3 common user access, Layer 3 private line user access, or Layer 2 VPN private line user access.
10. Configure DHCP/DHCPv6 messages to carry a domain description. Run either of the following commands according to the remote address pool's type:
    
    
    * To configure the device to encapsulate a user domain description into the Option 82 attribute of messages to be sent to the DHCP server, run the [**dhcp option82 rebuild self-define**](cmdqueryname=dhcp+option82+rebuild+self-define) ****circuit-id**** **circuit-id-value** **add-domain-description** **send-to-server** command.
    * To configure the device to encapsulate a user domain description into the Option 18 attribute of messages to be sent to the DHCPv6 server, run the **[**dhcpv6 option-18 rebuild self-define**](cmdqueryname=dhcpv6+option-18+rebuild+self-define)** *self-define-value* **add-domain-description send-to-server** command.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.