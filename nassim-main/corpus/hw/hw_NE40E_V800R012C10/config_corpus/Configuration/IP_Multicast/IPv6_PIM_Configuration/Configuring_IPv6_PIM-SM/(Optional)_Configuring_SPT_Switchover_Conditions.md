(Optional) Configuring SPT Switchover Conditions
================================================

PIM-SM enables a Rendezvous Point (RP) or a receiver's Designated router (DR) to trigger a shortest path tree (SPT) switchover when the rate of IPv6 multicast packets is high. You can configure the SPT switchover conditions and the interval for checking the rate at which IPv6 multicast data is forwarded on the receiver's DR.

#### Context

During the forwarding of IPv6 multicast packets in a PIM-SM domain, only one rendezvous point tree (RPT) is set for each multicast group. All multicast sources encapsulate multicast data in Register messages, and then unicast the Register messages to the RP. After receiving the Register messages, the RP decapsulates them and then forwards multicast data along the RPT to group members.

Forwarding IPv6 multicast data along an RPT has the following disadvantages:

* The source's DR and the RP need to frequently encapsulate and decapsulate messages.
* The forwarding path may not be the shortest path from the source to receivers.
* Heavy IPv6 multicast traffic increases the load of the RP, which easily causes a fault.

The solutions to the preceding disadvantages are as follows:

* SPT switchover triggered by the RP
  
  The RP sends a Join message to the source to create an IPv6 multicast route along the shortest path from the source's DR to the RP to build an MDT. Then, subsequent packets are forwarded along this path.
* SPT switchover triggered by the receiver's DR
  
  The receiver's DR checks the forwarding rate of IPv6 multicast data. If the receiver's DR finds that the rate exceeds the threshold, the receiver's DR triggers the SPT switchover immediately. The receiver's DR sends a Join message to the source to set up an IPv6 multicast route along the shortest path from the source's DR to the receiver's DR. Subsequent IPv6 multicast packets are forwarded along this path.

By default, the RP triggers the SPT switchover immediately after receiving the first Register message, and the receiver's DR triggers the SPT switchover immediately after receiving the first IPv6 multicast data packet. The Router can work normally with default control parameters. You are allowed to adjust SPT switchover parameters based on the specific networking environment.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If there is no special requirement, default parameter values are recommended.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic numbered ACL6 or a named ACL6 as needed.
   
   
   * Configure a basic numbered ACL6.
     
     1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ]
        
        A basic numbered ACL6 is created, and the basic numbered ACL6 view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
        
        Rules are configured for the basic numbered ACL6.
   * Configure a named ACL6.
     1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) **name** *acl6-name* **basic** [ **match-order** { **auto** | **config** } ]
        
        A named ACL6 is created, and the named ACL6 view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
        
        Rules are configured for the named ACL6.
   
   You can use the **source** parameter in the [**rule**](cmdqueryname=rule) command to define a multicast group range.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
5. Run [**spt-switch-threshold**](cmdqueryname=spt-switch-threshold) { *traffic-rate* | **infinity** } [ **group-policy** { *basic-acl6-number* |**acl6-name** *acl6-name* } [ **order** *order-value* ] ]
   
   
   
   SPT switchover conditions are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command takes effect on all Routers that may become the receiver's DR, but does not take effect on the RP.
   
   * *traffic-rate*: specifies the threshold for the rate of IPv6 multicast data. When the rate of IPv6 multicast data exceeds the threshold, the receiver's DR triggers the SPT switchover.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The configuration in Step 4 makes sense only after *traffic-rate* is set.
   * **infinity**: indicates that the receiver's DR never triggers the SPT switchover. IPv6 multicast data can be transmitted to receivers only along the RPT.
   * **group-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* }: specifies the range of multicast groups to which the threshold is applied. By default, the threshold is applicable to all multicast groups.
   * **order** *order-value*: adjusts the order of the IPv6 ACLs in the group-policy list. If a group matches multiple IPv6 ACLs, the threshold is selected in the order specified by *order-value*.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If no ACL is configured, the device applies the specified rate threshold to all multicast groups.
   * If an ACL is configured, the device uses configured ACL rules to determine whether to apply the specified rate threshold to a multicast group.
     + If a multicast group matches an ACL rule and the action is **permit**, the device applies the specified rate threshold to this group.
     + If a multicast group matches an ACL rule and the action is **deny**, the device performs an SPT switchover immediately after the SPT switchover condition is met.
     + If a multicast group does not match any ACL rule or if the specified ACL does not exist or does not contain rules, the device performs an SPT switchover immediately after the SPT switchover condition is met.
6. (Optional) Run [**timer spt-switch**](cmdqueryname=timer+spt-switch) *interval*
   
   
   
   The interval for checking the forwarding rate of multicast packets is set.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.