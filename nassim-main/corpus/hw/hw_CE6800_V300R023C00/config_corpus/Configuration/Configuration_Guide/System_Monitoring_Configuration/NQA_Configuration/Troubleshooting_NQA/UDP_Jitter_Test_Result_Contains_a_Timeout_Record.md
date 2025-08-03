UDP Jitter Test Result Contains a Timeout Record
================================================

UDP Jitter Test Result Contains a Timeout Record

#### Fault Symptom

The value of the **Operation timeout number** field in the **display nqa results** command output is not **0**.

![](../public_sys-resources/note_3.0-en-us.png) 

Unless otherwise specified, the commands provided in "Procedure" are run in the NQA test instance view.



#### Possible Causes

* The destination IP address does not exist.
* The packet version configured using the **nqa jitter tag-version** command is 2, and the UDP server function is not configured on the NQA server.

#### Procedure

1. On the NQA client, check whether the route to the destination is reachable.
   
   
   ```
   [ping](cmdqueryname=ping) host
   ```
   
   
   * If so, go to step 2.
   * If not, ensure that the destination IP address is correct and the network is normal, and then perform the NQA test again. If the fault persists, go to step 2.
2. On the NQA client, check whether the packet version configured for the test instance is 2 in the system view. The packet version is displayed only when it is set to 2.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
   
   
   * If so, go to step 3.
   * If not, go to step 4.
3. Check whether the UDP server function is configured on the NQA server.
   
   
   ```
   [display nqa server](cmdqueryname=display+nqa+server)
   ```
   
   
   * If so, go to step 4.
   * If not, configure the UDP server function on the NQA server.
     ```
     [nqa server udpecho](cmdqueryname=nqa+server+udpecho) ip-address port-number
     ```
     
     In the preceding command, *ip-address* and *port-number* must be the same as those in the [**destination-address**](cmdqueryname=destination-address) **ipv4** *ip-address* and [**destination-port**](cmdqueryname=destination-port) *port-number* configurations respectively on the NQA client.
     
     + If the fault is rectified, go to step 5.
     + If the fault persists, go to step 4.
4. Contact technical support and provide the following information:
   
   
   * Results of the preceding troubleshooting procedure
   * Configuration, log, and trap information
5. End.