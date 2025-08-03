Configuring LDP GTSM
====================

To apply LDP GTSM, you need to configure GTSM on both ends of the corresponding LDP peer relationship.

#### Usage Scenario

GTSM checks TTL values to defend against attacks. Attackers may simulate unicast LDP messages and continuously send them to a device. After receiving these messages, an interface board on the device sends them directly to the control plane for LDP processing, without validating them, if they are destined for the device. Consequently, the device becomes extremely busy, and CPU usage is high because the control plane needs to process these unverified messages.

GTSM protects the device by checking whether the TTL value in the IP header is within a predefined range, thereby improving system security.


#### Pre-configuration Tasks

Before configuring LDP GTSM, complete the following task:

* Enable MPLS and MPLS LDP.

#### Context

Perform the following steps on both ends of the LDP peer relationship for which GTSM is to be enabled:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**mpls ldp**](cmdqueryname=mpls+ldp) command to enter the MPLS-LDP view.
3. Run the [**gtsm peer**](cmdqueryname=gtsm+peer) *ip-address* **valid-ttl-hops** *hops* command to configure LDP GTSM.
   
   
   
   If the value of *hops* is set to the maximum number of valid hops permitted by GTSM, when the TTL values carried in the messages sent by an LDP peer are within the range [255 â *hops* + 1, 255], the messages are accepted; otherwise, the messages are dropped.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The valid TTL range is from 1 to 255 or from 1 to 64, depending on the device vendor. If a Huawei device is connected to a non-Huawei device, set *hops* to an appropriate value based on the valid TTL range defined by the vendor. Otherwise, the Huawei device will drop messages sent by the non-Huawei device, causing LDP session interruption.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display gtsm statistics**](cmdqueryname=display+gtsm+statistics) { *slot-id* | **all** } command to check GTSM statistics.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this command is supported only by the admin VS.