Failed to Establish a Multicast Static Route
============================================

Failed to Establish a Multicast Static Route

#### Fault Symptom

No dynamic routing protocol is configured on a device, and the physical status and link layer protocol status of the interface are both up. However, a multicast static route fails to be established. As a result, multicast data cannot be forwarded to user hosts.

#### Possible Causes

The multicast static route is incorrectly configured.


#### Procedure

* Check whether the multicast static route is configured correctly and added to the multicast routing table.
  
  
  ```
  [display multicast routing-table static](cmdqueryname=display+multicast+routing-table+static)
  ```
  
  Check whether the multicast static route configured on the device is correct. If the multicast static route is not correctly configured or updated to match the current network condition, the multicast routing table does not contain the route or the configuration of the multicast static route. In this case, run the [**ip rpf-route-static**](cmdqueryname=ip+rpf-route-static) command to reconfigure a multicast static route that matches the current network condition.