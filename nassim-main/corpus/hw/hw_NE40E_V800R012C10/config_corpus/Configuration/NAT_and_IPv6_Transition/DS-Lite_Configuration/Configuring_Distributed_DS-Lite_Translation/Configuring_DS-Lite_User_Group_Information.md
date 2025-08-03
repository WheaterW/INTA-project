Configuring DS-Lite User Group Information
==========================================

In a distributed DS-Lite scenario, a DS-Lite device identifies user traffic from each CPE by checking user identities. Therefore, DS-Lite user group information must be configured on the DS-Lite device.

#### Context

Multiple associations between user groups and DS-Lite instances can be configured in a domain. After a user gets online, a DS-Lite device checks the number of users in each user group and adds the user to the group that has the least members, so that the user's traffic can be allocated to the least busy DS-Lite instance to implement load sharing among DS-Lite instances.


#### Procedure

1. Configure a user access mode.
   
   
   
   For detailed configurations, see *HUAWEI NE40E-M2 series NE40E Configuration Guide - User Access*.
2. Bind a user group to the DS-Lite instance.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**user-group**](cmdqueryname=user-group) *group-name*
      
      
      
      A new user group is created.
   3. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   4. (Optional) Run [**cut access-user cgn-pub-user**](cmdqueryname=cut+access-user+cgn-pub-user) [ **dhcp** | **exclude-dhcp** ]
      
      
      
      CGN public users are manually logged out, and CGN public users are to get online using private IP addresses.
   5. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The AAA domain view is displayed.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   7. Run [**user-group**](cmdqueryname=user-group) *user-group-name* **bind ds-lite instance** *instance-name*
      
      
      
      A user group is bound to the DS-Lite instance.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * Each user group can be bound to a single DS-Lite instance.
      * A DS-Lite instance can be bound to multiple user groups.
      * When multiple user groups are bound to DS-Lite instances in an AAA domain, the number of users who can be assigned addresses is determined by the DS-Lite instance that provides the least number of public IP addresses. As a result, some IP addresses of other DS-Lite instances waste. To prevent such a problem, ensure that multiple DS-Lite instances provide the same number of valid public IP addresses.
   8. (Optional) Run [**public-address nat enable**](cmdqueryname=public-address+nat+enable)
      
      
      
      In distributed CGN, the device is enabled to perform DS-Lite translation for users in a domain before forwarding the traffic based on the routing table.
   9. (Optional) Run [**public-address nat-instance-down**](cmdqueryname=public-address+nat-instance-down) The device is enabled to allow CGN users to use public IP addresses to access networks when a CGN service board fails.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the AAA view.
   12. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.