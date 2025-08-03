Configuring MAC Accounting
==========================

If the MAC accounting function is enabled on an interface of a device, the device collects IPv4 or IPv6 traffic statistics corresponding to MAC addresses learned by the interface.

#### Usage Scenario

**Figure 1** MAC accounting usage scenario
  
![](figure/en-us_image_0172377462.png)  


MAC accounting can be used in either of the following
scenarios:

* When a Huawei device on an ISP network functions as an Internet
  exchange point (IXP), the networks connected to the IXP are provided
  by other carriers. When the ISP leases the other carriers' networks,
  for example, Network1 and Network2, they charge the ISP by traffic
  volume. To check traffic of MAC addresses, run the **mac accounting
  enable** command to enable the MAC accounting function on the IXP's
  interface, so that traffic of the peer routers can be obtained. This
  facilitates the ISP to verify or analyze traffic.
* If the IXP is under DDoS attacks, the MAC accounting function
  helps the ISP to check the traffic of peer routers with specified
  MAC addresses. If traffic of a specified MAC address is huge, the
  attack traffic may be from this device with the specified MAC address.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The user interface view is displayed.
3. Run [**mac accounting enable**](cmdqueryname=mac+accounting+enable)
   
   
   
   MAC accounting is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After MAC accounting is enabled, run the [**display mac accounting**](cmdqueryname=display+mac+accounting) command to check MAC accounting statistics on the interface or its sub-interfaces.

If you need to re-check MAC accounting statistics after a period, run the [**reset mac accounting counters**](cmdqueryname=reset+mac+accounting+counters) command to delete the existing statistics and then run the [**display mac accounting**](cmdqueryname=display+mac+accounting) command. This ensures statistics accuracy.