Monitoring the Status of Multicast Routing
==========================================

During the routine maintenance of IPv4 multicast routing management, you can run the display commands in any view to learn the running of the multicast forwarding table.

#### Context

In routine maintenance, you can run the following commands in any view to check the status of multicast forwarding.


#### Procedure

* Run the following commands in any view to check the multicast forwarding table.
  
  
  + [**display multicast**](cmdqueryname=display+multicast) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **forwarding-table** [ *group-address* | *source-address* | **incoming-interface** { *interface-type* *interface-number* | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type interface-number* | **register** | **none** } | **statistics** | **slot** *slot-number* ] \*