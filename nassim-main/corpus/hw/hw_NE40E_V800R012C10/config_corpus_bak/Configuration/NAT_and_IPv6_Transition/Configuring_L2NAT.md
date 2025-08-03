Configuring L2NAT
=================

L2-Aware NAT (L2NAT) translates private IP addresses into public IP addresses based on user location information.

#### Context

Three NAT technologies are available on a network: NAT444, NAT44, and L2NAT.

* NAT444: A CPE performs NAT for user traffic before forwarding it to a NAT device, which then performs NAT again for the user traffic. NAT444 allows users on different private networks to use the same private IP address.
* NAT44: A CPE does not perform NAT for user traffic. Instead, it directly forwards user traffic to a NAT device for NAT. NAT44 does not allow users on different private networks to use the same private IP address.
* L2NAT: A CPE does not perform NAT for user traffic. Instead, it adds user location information into packets when forwarding them. A NAT device then translates the private IP address carried in each packet into a public IP address based on the user location information. L2NAT allows users on different private networks to use the same private IP address.

After CPEs connected to an L2NAT device are assigned the same IP address, parameters related to external hosts must be configured on the L2NAT device to establish static mappings between the CPEs and external hosts. This allows external hosts to maintain access to online CPEs.


#### Procedure

1. Configure the L2NAT license function.
   1. Run [**license**](cmdqueryname=license)
      
      
      
      The license view is displayed.
   2. Run [**active l2nat vsuf slot**](cmdqueryname=active+l2nat+vsuf+slot) *slot-id*
      
      
      
      The L2NAT license is activated for the service board.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure the L2NAT function.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
      
      
      
      The NAT instance view is displayed.
   3. Run [**l2-aware enable**](cmdqueryname=l2-aware+enable)
      
      
      
      The L2NAT function is enabled.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Binding the service board or the service board's CPU to the NAT instance.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
      
      
      
      A service-location group is created, and its view is displayed.
   3. Run [**location**](cmdqueryname=location) **slot** *slot-id* [ **backup** **slot** *slot-id* ]
      
      
      
      The service board's CPU is bound.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
      
      
      
      A service-instance group is created, and its view is displayed.
   7. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
      
      
      
      The service-location group is bound.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   10. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
       
       
       
       The NAT instance view is displayed.
   11. Run [**service-instance-group**](cmdqueryname=service-instance-group) *service-instance-group-name*
       
       
       
       The service-instance group is bound.
   12. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
   13. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
4. (Optional) Configure parameters related to external hosts so that they can maintain access to CPEs connected to the L2NAT device.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**nat external-host**](cmdqueryname=nat+external-host) { **tcp** | **udp** | **any** } **destination-ip** *ip-address* [ **destination-port** *port-number* ]
      
      
      
      Parameters related to the external host that needs to visit the CPEs are configured.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. Verify the configuration. Specifically, run the **display l2nat vsuf status** command to check license allocation for the L2NAT service.