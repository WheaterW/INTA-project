Configuring NAT User Group Information
======================================

In a distributed NAT scenario, the NAT device identifies user traffic from each CPE by checking user identities. Therefore, NAT user group information must be configured on the NAT device.

#### Context

Multiple associations between user groups and NAT instances can be configured in a domain. After a user goes online, the system checks the number of users in each user group and adds the user to the group that has the least number of members so that the user's traffic can be allocated to the least busy NAT instance to implement load balancing among NAT instances.


#### Procedure

1. Configure a user access mode.
   
   
   
   For detailed configurations, see the HUAWEI NE40E Configuration Guide - User Access.
2. Associate a NAT user group with a NAT instance.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**user-group**](cmdqueryname=user-group) *group-name*
      
      
      
      A new user group is created.
   3. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   4. (Optional) Run [**cut access-user cgn-pub-user**](cmdqueryname=cut+access-user+cgn-pub-user) [ **dhcp** | **exclude-dhcp** ]
      
      
      
      CGN public network user offline is triggered to make the user access the network with a private IP address.
   5. (Optional) Run [**load-balance user-group refer-service-location**](cmdqueryname=load-balance+user-group+refer-service-location)
      
      
      
      The device is enabled to check the active/standby status of service-location groups when performing load balancing in scenarios where multiple user groups are configured in the AAA domain and bound to a NAT instance.
   6. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The AAA domain view is displayed.
   7. Run [**user-group**](cmdqueryname=user-group) *user-group-name* [**bind**](cmdqueryname=bind) [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **ip-pool** *pool-name* ]
      
      
      
      A NAT instance is bound to the NAT user group.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * One user group can be bound to only one NAT instance.
      * One NAT instance can be bound to multiple user groups.
      * If a static source tracing algorithm policy has been applied to a NAT instance, you are advised to specify the [**ip-pool**](cmdqueryname=ip-pool) *pool-name* parameter in the command to bind the private address pool whose address segment is a subset of the static source tracing address segments to the NAT instance. In this way, private IP addresses are assigned from the address pool specified by the NAT instance, and the address pool configured in the domain or the address pool delivered by the RADIUS server will not be used.
   8. (Optional) Run [**public-address nat enable**](cmdqueryname=public-address+nat+enable)
      
      
      
      NAT is implemented for users who go online from a domain before user data is forwarded based on a routing table in distributed CGN scenarios.
   9. (Optional) Run [**public-address nat-instance-down**](cmdqueryname=public-address+nat-instance-down)
      
      
      
      The function of allowing CGN users to access the network with a public IP address in the event of a CGN service board fault is enabled.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.