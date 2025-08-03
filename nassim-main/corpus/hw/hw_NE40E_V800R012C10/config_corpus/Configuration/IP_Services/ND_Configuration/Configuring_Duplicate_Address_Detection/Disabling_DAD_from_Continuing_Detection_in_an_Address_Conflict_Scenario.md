Disabling DAD from Continuing Detection in an Address Conflict Scenario
=======================================================================

Disabling DAD from Continuing Detection in an Address Conflict Scenario

#### Context

Before using an IPv6 unicast address for an interface, a device performs DAD. If DAD detects an address conflict, the detection ends. To remove the address conflict, you need to reconfigure an IPv6 address or change the interface status for the device to perform DAD again. This causes a long service interruption. To resolve this issue, enable DAD to continue detection in an address conflict scenario. In this case, after detecting an address conflict, DAD will continue detection until any of the following occurs:

* The loopback is released.
* No more NS messages are received from a neighbor.
* No more NA messages are received from a neighbor.

If the network is stable and no new IPv6 address needs to be configured, you can run the [**ipv6 nd dad detect disable**](cmdqueryname=ipv6+nd+dad+detect+disable) command to disable DAD from continuing detection in an address conflict scenario.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 nd dad detect disable**](cmdqueryname=ipv6+nd+dad+detect+disable)
   
   
   
   DAD is disabled from continuing detection in an IPv6 address conflict scenario.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.