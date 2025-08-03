SNMP Proxy
==========

SNMP Proxy

#### Context

With SNMP, an NMS runs network management software to manage NEs. If the NMS and device use different SNMP versions, the NMS cannot manage the device.

To resolve this problem, configure SNMP proxy on a device between the NMS and device to be managed, as shown in [Figure 1](#EN-US_CONCEPT_0000001564110453__fig_dc_vrp_snmp_feature_200201). In the following description, the device on which SNMP proxy needs to be configured is referred to as a middle-point device.

The NMS manages the middle-point device and managed device as an independent NE, reducing the number of managed NEs and management costs.

**Figure 1** SNMP proxy  
![](figure/en-us_image_0000001563870461.png)
An SNMP proxy provides the following functions:

* Receives SNMP messages from other SNMP entities, forwards SNMP messages to other SNMP entities, or forwards responses to SNMP request originators.
* Supports SNMPv1, SNMPv2c, and SNMPv3 and enables communication between SNMP entities running SNMPv1, SNMPv2c, and SNMPv3.

An SNMP proxy can work between one or more NMSs and multiple NEs.


#### Fundamentals

The principles of SNMP proxy are described as follows:

In [Figure 2](#EN-US_CONCEPT_0000001564110453__fig_dc_vrp_snmp_feature_200202), the middle-point device allows you to manage the network access, configurations, and system software version of the managed device. The NE MIB files loaded to the NMS include the MIB tables of both the middle-point device and managed device. After you configure SNMP proxy on the middle-point device, the middle-point device automatically forwards SNMP requests from the NMS to the managed device and forwards SNMP responses from the managed device to the NMS.

**Figure 2** SNMP proxy working principles  
![](figure/en-us_image_0000001564110545.png)

[Figure 3](#EN-US_CONCEPT_0000001564110453__fig_dc_vrp_snmp_feature_200203) shows the SNMP proxy schematic diagram.

**Figure 3** SNMP proxy schematic diagram  
![](figure/en-us_image_0000001512830922.png)

* The process in which an NMS uses a middle-point device to query the MIB information of a managed device is as follows:
  
  1. The NMS sends an SNMP request that contains the MIB object ID of the managed device to the middle-point device.
     
     + The engine ID carried in an SNMPv3 request must be the same as the engine ID of the SNMP agent on the managed device.
     + If the SNMP request is an SNMPv1 or SNMPv2c message, a proxy community name must be configured on the middle-point device with the engine ID of the SNMP agent on the managed device be specified. The community name carried in the SNMP request message must match the community name configured on the managed device.
  2. Upon receipt, the middle-point device searches its proxy table for a forwarding entry based on the engine ID.
     
     + If a matching forwarding entry exists, the middle-point device caches the request and encapsulates the request based on forwarding rules.
     + If no matching forwarding entry exists, the middle-point device drops the request.
  3. The middle-point device forwards the encapsulated request to the managed device and waits for a response.
  4. After the middle-point device receives a response from the managed device, the middle-point device forwards the response to the NMS.
     
     If the middle-point device fails to receive a response within a specified period, the middle-point device drops the SNMP request.
* The process in which a managed device uses a middle-point device to send a notification to an NMS is as follows:
  
  1. The managed device generates a notification due to causes such as overheating and sends the notification to the middle-point device.
  2. Upon receipt, the middle-point device searches its proxy table for a forwarding entry based on the engine ID.
     
     + If a matching forwarding entry exists, the middle-point device encapsulates the notification based on forwarding rules.
     + If no matching forwarding entry exists, the middle-point device drops the notification.
  3. The middle-point device forwards the encapsulated notification to the NMS.
     
     If the notification is sent as an inform by the managed device, the middle-point device forwards the notification to the NMS and waits for a response after forwarding the notification to the NMS. If the middle-point device does not receive any response from the NMS within a specified period, the middle-point device drops the notification.
  4. The NMS receives the notification.