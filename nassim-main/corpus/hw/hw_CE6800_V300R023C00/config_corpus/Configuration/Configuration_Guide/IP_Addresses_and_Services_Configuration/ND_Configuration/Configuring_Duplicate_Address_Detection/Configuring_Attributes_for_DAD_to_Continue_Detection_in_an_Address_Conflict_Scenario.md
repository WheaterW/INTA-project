Configuring Attributes for DAD to Continue Detection in an Address Conflict Scenario
====================================================================================

Configuring Attributes for DAD to Continue Detection in an Address Conflict Scenario

#### Context

Before using an IPv6 unicast address for an interface, a device performs DAD. If DAD detects an address conflict, the detection ends. To remove the address conflict, you need to reconfigure an IPv6 address or change the interface status for the device to perform DAD again. This causes a long service interruption. To resolve this issue, enable DAD to continue detection in an address conflict scenario. In this case, after detecting an address conflict, DAD will continue detection until any of the following occurs:

* The loopback is released.
* No more NS messages are received from a neighbor.
* No more NA messages are received from a neighbor.

If the network is stable and no new IPv6 address needs to be configured, you can run the [**ipv6 nd dad detect disable**](cmdqueryname=ipv6+nd+dad+detect+disable) command to disable DAD from continuing detection in an address conflict scenario.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure attributes for DAD to continue detection in an address conflict scenario.
   
   
   
   **Table 1** Configuring attributes for DAD to continue detection in an address conflict scenario
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure a threshold for DAD to consider an address available in an address conflict self-recovery scenario. | [**ipv6 nd dad detect attempts**](cmdqueryname=ipv6+nd+dad+detect+attempts) *attempts-value* | If an address conflict occurs on an interface in an address conflict self-recovery scenario, DAD continues detection on the interface until the address conflict is removed. The device considers the address conflict removed when DAD does not receive conflict packets for a specified number of consecutive times. This number, referred to as the address conflict removal threshold, can be configured using the [**ipv6 nd dad detect attempts**](cmdqueryname=ipv6+nd+dad+detect+attempts) command. In this case, DAD considers the address available. Otherwise, DAD considers the address unavailable and continues detection. |
   | Configure a limit on the rate at which NS messages are sent for DAD to continue detection in an address conflict scenario. | [**ipv6 nd dad detect rate-limit**](cmdqueryname=ipv6+nd+dad+detect+rate-limit) *rate-value* | By default, address conflict self-recovery is enabled, and the limit on the rate at which NS messages are sent for DAD to continue detection is 50 messages per second. You can run this command to adjust this limit. |
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```