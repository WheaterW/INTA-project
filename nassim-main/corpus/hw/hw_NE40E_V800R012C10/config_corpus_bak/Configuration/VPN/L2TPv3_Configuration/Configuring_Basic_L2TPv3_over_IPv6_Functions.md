Configuring Basic L2TPv3 over IPv6 Functions
============================================

L2TPv3 over IPv6 is used to establish L2TPv3 tunnels on an IPv6 public network, so that Layer 2 user packets can be transparently transmitted across the IPv6 public network.

#### Usage Scenario

L2TPv3 over IPv6 tunnels can be used to transparently transmit Layer 2 Ethernet services. Tags can be used for flexible access. L2TPv3 tunnels can be deployed on a PE to transmit users' Layer 2 Ethernet packets to a remote end.


#### Prerequisites

Before configuring L2TPv3 over IPv6, complete the following tasks:

* Connect interfaces and configure physical interface parameters for interfaces to go Up at the physical layer.
* Configure link-layer protocol parameters for interfaces to go Up at the link layer.
* Configure static IPv6 routes for devices to communicate.
* Enable IPv6 both globally and on specific interfaces.
* Configure IPv6 addresses for devices.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tpv3 enable**](cmdqueryname=l2tpv3+enable)
   
   
   
   L2TPv3 is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
4. Run [**l2tpv3 pw**](cmdqueryname=l2tpv3+pw) *pwname*
   
   
   
   An L2TPv3 tunnel is created, and its view is displayed.
5. (Optional) Run [**l2tpv3 local session-id**](cmdqueryname=l2tpv3+local+session-id) *local-session-id*
   
   
   
   The local session ID is configured.
6. (Optional) Run [**l2tpv3 remote session-id**](cmdqueryname=l2tpv3+remote+session-id) *remote-session-id*
   
   
   
   The remote session ID is configured.
7. Run [**source**](cmdqueryname=source) **interface** { *interface-type* *interface-number* | *interface-name* } **ipv6** *source-address*
   
   
   
   The source interface of the L2TPv3 tunnel is configured.
   
   
   
   The IP address must be an IPv6 address.
8. Run [**destination**](cmdqueryname=destination) *destination-address*
   
   
   
   The destination IPv6 address of the L2TPv3 tunnel is configured.
9. Configure L2TPv3 tunnel security. Cookies are used in security checks performed at the endpoints of a tunnel to prevent network spoofing and attacks.
   1. Run the [**l2tpv3 local cookie**](cmdqueryname=l2tpv3+local+cookie) { **key cipher** *local-cookie* | **length 4 plain lower-value** *local-low-value* | **length 8 plain lower-value** *local-low-value* **upper-value** *local-high-value* } command to configure the local cookie.
      
      
      
      Either an extended or standard cookie can be configured. The local cookie of the local device must be the same as the remote cookie of the remote device. The device compares the Cookie field of a packet with the pre-configured value. If the Cookie field does not match the pre-configured value, the device discards the packet.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      You are advised to select the **cipher** mode. In **plain** mode, a value is saved in the configuration file in plaintext, posing a high risk. To ensure device security, change the cookie periodically.
   2. (Optional) Run [**l2tpv3 local cookie secondary**](cmdqueryname=l2tpv3+local+cookie+secondary) { **key cipher** *local-cookie* | **length 4 plain lower-value** *local-low-value* | **length 8 plain lower-value** *local-low-value* **upper-value** *local-high-value* }
      
      
      
      The local cookie is changed.
      
      
      
      After the local cookie is configured for the first time, you can run this command to change it without interrupting services
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      You are advised to select the **cipher** mode. In **plain** mode, a value is saved in the configuration file in plaintext, which poses a high risk. To ensure device security, change the cookie periodically.
   3. Run the [**l2tpv3 remote cookie**](cmdqueryname=l2tpv3+remote+cookie) { **key cipher** *remote-cookie* | **length 4 plain lower-value** *remote-low-value* | **length 8 plain lower-value** *remote-low-value* **upper-value** *remote-high-value* } command to configure the remote cookie.
      
      
      
      Either an extended or standard cookie can be configured. The remote cookie of the local device must be the same as the local cookie of the remote device. The device compares the Cookie field of a packet with the pre-configured value. If the Cookie field does not match the pre-configured value, the device discards the packet.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      You are advised to select the **cipher** mode. In **plain** mode, a value is saved in the configuration file in plaintext, posing a high risk. To ensure device security, change the cookie periodically.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
10. Bind services to the L2TPv3 PW.
    1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* **mode l2**
       
       
       
       The Layer 2 sub-interface view is displayed.
    2. Run [**l2tpv3 instance**](cmdqueryname=l2tpv3+instance) *instance-name*
       
       
       
       An L2TPv3 instance is configured on the interface.
       
       
       
       The *instance-name* value must begin with a letter.
    3. Run [**l2tpv3 static binding pw**](cmdqueryname=l2tpv3+static+binding+pw) *pwname*
       
       
       
       An L2TPv3 tunnel is bound to the L2TPv3 instance.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
12. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the L2TPv3 instance view.
13. Run [**encapsulation**](cmdqueryname=encapsulation) [ **default** | **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **qinq** [ **vid** *pe-vid* ****ce-vid**** { *l**ow-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] | **untag** ]
    
    
    
    The encapsulation type on an EVC Layer 2 sub-interface is configured.
14. Run [**rewrite pop**](cmdqueryname=rewrite+pop) { **single** | **double** }
    
    
    
    The traffic behavior is set to pop, enabling an EVC Layer 2 sub-interface removes VLAN tags from received packets.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If L2TPv3 is configured on a Layer 3 sub-interface, you only need to configure an encapsulation type for the sub-interface. Step 13 or 14 does not need to be performed.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

Run the [**display l2tpv3 pw**](cmdqueryname=display+l2tpv3+pw) *pwname* command to check whether the L2TPv3 tunnel is correctly configured.

Run the [**display l2tpv3 statistics pw**](cmdqueryname=display+l2tpv3+statistics+pw) *pwname* command to check packet statistics about the L2TPv3 tunnel.