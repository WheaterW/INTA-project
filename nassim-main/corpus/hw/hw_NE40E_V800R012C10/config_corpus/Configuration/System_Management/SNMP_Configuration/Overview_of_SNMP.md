Overview of SNMP
================

An NMS performs Get and Set operations on a managed device running the SNMP agent to manage objects, which are uniquely identified in the management information base (MIB).

On a large network, if a fault occurs on a device and the device does not report it, the network administrator is unable to rapidly detect, locate, and rectify the fault. This affects maintenance efficiency and increases the overall maintenance workload. To resolve this problem, device vendors integrate network management functions into some of their products, enabling the NMS to query the status of remote devices and allowing devices to report alarms to the NMS if an event occurs.

SNMP operates at the application layer of the IP suite and defines the transmission of management information between the NMS and devices. It also defines several device management operations that can be performed by the NMS and allows devices to notify the NMS of device faults through alarms.

#### SNMP Components

An SNMP managed network consists of the following three components:

* **NMS**: sends various packets to query managed devices and receives alarms from these devices.
* **Agent**: a network management process on a managed device. An agent provides the following functions:
  
  + Receives and parses query messages sent from the NMS.
  + Reads or writes management variables based on the query type, and generates and sends response messages to the NMS.
  + Sends alarms to the NMS when an event occurs (for example, when the system view is displayed or closed, or if the device is restarted). Protocol modules on the device define the conditions that trigger alarms.
* **Managed device**: managed by an NMS and generates and reports alarms to the NMS.

[Figure 1](#EN-US_CONCEPT_0172360954__fig_dc_vrp_snmp_feature_000601) shows the relationship between the NMS and agent.

**Figure 1** SNMP management model  
![](figure/en-us_image_0000001692640357.png)  


#### MIB

To uniquely identify managed objects, SNMP organizes them in a hierarchical tree structure and identifies each one by a path originating from the tree root, as shown in [Figure 2](#EN-US_CONCEPT_0172360954__fig_dc_vrp_snmp_cfg_000202). The NMS uses the MIB to identify and manage device objects. Each node on the tree is a managed object.

**Figure 2** MIB tree structure  
![](figure/en-us_image_0000001644400652.png)

As shown in [Figure 2](#EN-US_CONCEPT_0172360954__fig_dc_vrp_snmp_cfg_000202), object B is uniquely identified by a string of numbers â {1.2.1.1} in this example â known as an object identifier (OID). A MIB tree describes the hierarchy of data in a MIB that collects the definitions of variables on the managed devices.

You can use a standard MIB or define a MIB based on certain standards. Using a standard MIB reduces the costs on proxy deployment and therefore reduces the costs on the entire network management system.


#### SNMP Operations

SNMP uses Get and Set operations to replace a complex command set. The operations shown in [Figure 3](#EN-US_CONCEPT_0172360954__fig_dc_vrp_snmp_cfg_000203) can implement all necessary functions.

**Figure 3** SNMP operations  
![](images/fig_dc_vrp_snmp_cfg_000203.png)  

[Table 1](#EN-US_CONCEPT_0172360954__tab_dc_vrp_snmp_cfg_000201) lists the functions of SNMP operations.

**Table 1** SNMP operations
| Operation | Function |
| --- | --- |
| GetRequest | Retrieves the value of a variable. The NMS sends the request to a managed device to obtain the status of an object on the device. |
| GetNextRequest | Retrieves the value of the next variable. The NMS sends the request to a managed device to obtain the status of the next object on the device. |
| GetResponse | Responds to GetRequest, GetNextRequest, and SetRequest operations. GetResponse is sent from a managed device to the NMS and is processed by SNMP agent. |
| GetBulk | An NMS-to-agent request, which functions the same as continuous GetNext operations. |
| SetRequest | Sets the value of a variable. The NMS sends the request to a managed device to adjust the status of an object on the device. |
| Trap | Reports an event to the NMS. |
| Inform | Reports an event to the NMS and requires acknowledgement from the NMS. |