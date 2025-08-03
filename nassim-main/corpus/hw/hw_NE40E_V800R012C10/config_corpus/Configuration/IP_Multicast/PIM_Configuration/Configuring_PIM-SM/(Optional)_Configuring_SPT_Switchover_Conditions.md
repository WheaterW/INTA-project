(Optional) Configuring SPT Switchover Conditions
================================================

PIM-SM allows a Rendezvous Point (RP) or a receiver's Designated router (DR) to trigger a shortest path tree (SPT) switchover when the rate of multicast packets is high. You can configure SPT switchover conditions and set the interval for checking the forwarding rate of multicast packets on the receiver's DR.

#### Context

In PIM-SM forwarding, each multicast group corresponds to a rendezvous point tree (RPT) only. At first, all multicast sources encapsulate data in Register messages, and send the messages to the RP in unicast mode. The RP decapsulates the messages and forwards the data along the RPT.

Forwarding multicast data along an RPT has the following disadvantages:

* The source's DR and the RP need to frequently encapsulate and decapsulate messages.
* The forwarding path may not be the shortest path from the source to receivers.
* Heavy data traffic increases the load of the RP, which may cause a fault.

The solutions to this problem are as follows:

* SPT switchover triggered by the RP
  
  The RP sends a Join message to the source to create a multicast route along the shortest path from the source's DR to the RP. Then, subsequent multicast packets are directly transmitted along this path.
* SPT switchover triggered by the receiver's DR
  
  The receiver's DR checks the forwarding rate of multicast data. If the receiver's DR finds that the rate exceeds the threshold, the receiver's DR triggers the SPT switchover immediately. The receiver's DR then sends a Join message to the source to set up a multicast route along the shortest path from the source's DR to the receiver's DR. Subsequent packets are forwarded along this path.

By default, the RP triggers the SPT switchover immediately after receiving the first Register message and the receiver's DR triggers the SPT switchover immediately after receiving the first multicast data packet. The Router can work normally with default control parameters. You are allowed to adjust SPT switchover parameters based on the specific networking environment.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If there is no special requirement, default parameter values are recommended.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic numbered ACL or a named ACL as needed.
   
   
   * Configure a basic numbered ACL.
     
     1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
        
        A basic numbered ACL is created, and the basic numbered ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the basic numbered ACL.
   * Configure a named ACL.
     
     1. Run [**acl**](cmdqueryname=acl) **name** *acl-name* **basic** [ **match-order** { **auto** | **config** } ]
        
        A named ACL is created, and the named ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the named ACL.
   
   If a basic numbered ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to a multicast group range to which the specified rate threshold applies.
   
   If a named ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **destination** parameter to a multicast group range to which the specified rate threshold applies.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
5. Run [**spt-switch-threshold**](cmdqueryname=spt-switch-threshold) { *traffic-rate* | **infinity** } [ **group-policy** { *basic-acl-number* | **acl-name** *acl-name* } [ **order** *order-value* ] ]
   
   
   
   SPT switchover conditions are configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command takes effect on all Routers that may function as a receiver's DRs, but does not take effect on the RP.
   
   * *traffic-rate*: specifies the rate threshold of the multicast data at which the receiver's DR triggers the SPT switchover.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If *traffic-rate* is specified, Step 4 is required.
   * **infinity**: indicates that the receiver's DR never triggers the SPT switchover. Thus, multicast data can be transmitted to the receiver only along the RPT.
   * **group-policy** *basic-acl-number*: specifies the range of the multicast groups to which the set rate threshold applies.
   * **order** *order-value*: adjusts the order of the ACLs in the group-policy list. If a group matches multiple ACLs, the threshold is selected in the order specified by *order-value*.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If no ACL is configured, the device applies the specified rate threshold to all multicast groups.
   * If an ACL is configured, the device uses configured ACL rules to determine whether to apply the specified rate threshold to a multicast group.
     + If a multicast group matches an ACL rule and the action is **permit**, the device applies the specified rate threshold to this group.
     + If a multicast group matches an ACL rule and the action is **deny**, the device performs an SPT switchover immediately after the SPT switchover condition is met.
     + If a multicast group does not match any ACL rule or if the specified ACL does not exist or does not contain rules, the device performs an SPT switchover immediately after the SPT switchover condition is met.
6. (Optional) Run [**timer spt-switch**](cmdqueryname=timer+spt-switch) *interval*
   
   
   
   The interval for checking the forwarding rate of multicast packets is set.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.