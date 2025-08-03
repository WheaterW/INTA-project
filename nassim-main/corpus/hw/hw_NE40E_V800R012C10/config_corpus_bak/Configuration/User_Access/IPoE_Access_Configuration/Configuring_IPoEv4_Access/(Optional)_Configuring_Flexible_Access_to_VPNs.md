(Optional) Configuring Flexible Access to VPNs
==============================================

Service priorities can be identified based on 802.1p values of service packets and then transmitted to corresponding VPNs.

#### Context

On the network shown in[Figure 1](#EN-US_TASK_0172373978__fig_dc_ne_ipox_cfg_002201), service packets carry 802.1p values to identify their priorities. The BRAS can identify service priorities based on the 802.1p values of received Layer 2 service packets and transmit the service packets to corresponding VPNs. To allow this, enable a BAS interface to transmit packets to different VPNs based on 802.1p priorities of the packets and bind VPN instances to different 802.1p priorities.

**Figure 1** Flexible access to VPNs  
![](figure/en-us_image_0258250025.png)
Perform the following steps on the BRAS:

1. [Create a VPN instance. (Both user and service VPN instances must be configured.)](#EN-US_TASK_0172373978__step_1)
2. [Create a local address pool.](#EN-US_TASK_0172373978__step_2)
3. [Configure a user domain.](#EN-US_TASK_0172373978__step_3)
4. [Configure a user access interface.](#EN-US_TASK_0172373978__step_4)
5. [Configure a network-side ACL and define redirection for the ACL.](#EN-US_TASK_0172373978__step_5)
6. [Configure a network-side interface.](#EN-US_TASK_0172373978__step_6)


#### Procedure

1. Create a VPN instance. (Both user and service VPN instances must be configured.)
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      A VPN instance is created, and the VPN instance view is displayed.
   3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
   4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is configured for the VPN instance IPv4 address family.
   5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      
      
      VPN targets are configured for the VPN instance IPv4 address family.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the VPN instance view.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Create a local address pool.
   1. Run [**ip pool**](cmdqueryname=ip+pool) *pool-name* [ **bas** { **local** [ **rui-slave** ] | **remote** [ **rui-slave** ] | **dynamic** } ]
      
      
      
      An address pool is created.
   2. Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
      
      
      
      A VPN instance is specified for the address pool.
      
      
      
      The VPN instance specified for the address pool must be the user VPN instance configured in step 1.
   3. Run [**gateway**](cmdqueryname=gateway) *ip-address* { *mask* | *mask-length* }
      
      
      
      The gateway IP address and subnet mask are configured for the address pool.
   4. Run [**section**](cmdqueryname=section) *section-number* *start-ip-address* [ *end-ip-address* ]
      
      
      
      An address segment is configured for the address pool.
   5. Run [**import vpn-instance**](cmdqueryname=import+vpn-instance) *vpn-instance-name*
      
      
      
      A VPN instance is imported to the address pool.
      
      The VPN instance imported to the address pool must be the service VPN instance created in step 1.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a user domain.
   1. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   2. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      A domain is created, and the domain view is displayed.
   3. Run [**authentication-scheme**](cmdqueryname=authentication-scheme) *authentication-scheme-name*
      
      
      
      An authentication scheme is configured for the domain.
   4. Run [**accounting-scheme**](cmdqueryname=accounting-scheme) *accounting-scheme-name*
      
      
      
      An accounting scheme is configured for the domain.
   5. Run [**ip-pool**](cmdqueryname=ip-pool) *pool-name*
      
      
      
      An address pool is bound to the domain.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the AAA view.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Configure a user access interface.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      A sub-interface is created.
   2. Run [**user-vlan**](cmdqueryname=user-vlan) { *start-vlan-id* [ *end-vlan-id* ] | *cevlan* } **qinq** { *start-pe-vlan* [ *end-pe-vlan* ] | *pevlan* }
      
      
      
      A user-VLAN sub-interface is configured.
   3. Run [**802.1p**](cmdqueryname=802.1p) *8021p-priority* **binding** **vpn-instance** *vpn-instance-name*
      
      
      
      A VPN instance is bound to an 802.1p priority.
      
      
      
      The VPN instance bound to the 802.1p priority must be the service VPN instance created in step 1.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      When users are online on a BRAS interface, the function of transmitting service packets to different VPNs based on 802.1p priorities cannot be modified or deleted.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the sub-interface view.
   5. Run [**bas**](cmdqueryname=bas)
      
      
      
      The sub-interface is configured as a BAS interface, and the BAS interface view is displayed.
   6. Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **default-domain** { **authentication** [ **force** | **replace** ] *dname* | **pre-authentication** *predname* } \* | **bas-interface-name** *bname* | **accounting-copy** **radius-server** *rd-name* ] \*
      
      
      
      The access type of the BAS interface is configured as Layer 2 subscriber access.
   7. Run [**authentication-method**](cmdqueryname=authentication-method) { **bind** | { **fast** |  **web** } }
      
      
      
      An authentication method is configured for the BAS interface.
   8. Run [**802.1p-to-vpn**](cmdqueryname=802.1p-to-vpn)
      
      
      
      The BAS interface is enabled to transmit packets to different VPNs based on the 802.1p priorities of the packets.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the sub-interface view.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   11. Run commit
       
       
       
       The configuration is committed.
5. Configure a network-side ACL and define redirection for the ACL.
   1. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
      
      
      
      A basic ACL is created.
   2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
      
      
      
      A rule is created for the ACL.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   4. Run [**vpn-group**](cmdqueryname=vpn-group) *vpn-group-name* [ **vpn-instance** { *vpn-name* } &<1-8> ]
      
      
      
      A VPN group is created, and a VPN instance is added to the VPN group.
      
      The VPN instance added to the VPN group must be the user VPN instance created in step 1.
   5. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
      
      
      
      A traffic behavior is configured, and the traffic behavior view is displayed.
   6. Run [**redirect vpn-group**](cmdqueryname=redirect+vpn-group) *vpn-group-name*
      
      
      
      Packet redirection to a specified VPN group is configured.
      
      The VPN group to which packets are redirected must be the one created in step d.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is configured, and the traffic classifier view is displayed.
   9. Run [**if-match acl**](cmdqueryname=if-match+acl) { *acl-number* | **name** *acl-name* }
      
      
      
      An IPv4 ACL is specified for MF classification.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
   11. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
       
       
       
       A traffic policy is configured.
   12. Run [**share-mode**](cmdqueryname=share-mode)
       
       
       
       The shared mode is specified for the traffic policy.
   13. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* ]
       
       
       
       A traffic behavior is specified for a traffic classifier in the traffic policy.
   14. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
6. Configure a network-side interface.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      A sub-interface is created.
   2. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlanid* { **8021p** { *8021p-value1* [ **to** *8021p-value2* ] } &<1-8> | **dscp** { *dscp-value1* [ **to** *dscp-value2* ] } &<1-10> | **eth-type** **PPPoE** | **default** }
      
      
      
      A matching policy is configured on the common dot1q sub-interface.
   3. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
      
      
      
      A VPN instance is bound to the sub-interface.
      
      The VPN instance bound to the sub-interface must be the service VPN instance created in step 1.
   4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      An IP address is configured for the sub-interface.
   5. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** }
      
      
      
      The traffic policy is applied to the sub-interface.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.