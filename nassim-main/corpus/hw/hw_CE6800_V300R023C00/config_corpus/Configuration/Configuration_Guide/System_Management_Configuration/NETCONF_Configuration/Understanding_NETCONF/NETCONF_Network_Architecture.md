NETCONF Network Architecture
============================

NETCONF Network Architecture

#### Basic Network Architecture of NETCONF

[Figure 1](#EN-US_TOPIC_0000001564002177__fig_dc_vrp_netconf_feature_001901) shows the basic network architecture of NETCONF. It must contain at least one network management system (NMS) that runs on an NMS server and manages devices.

**Figure 1** Basic network architecture of NETCONF  
![](figure/en-us_image_0000001563882065.png)

The architecture consists of two main elements: client and server.

**Table 1** Main elements in the basic network architecture of NETCONF
| Main Element | Function |
| --- | --- |
| NETCONF client | A client manages network devices using NETCONF.   * The client sends RPC requests to a server to query or modify one or more parameter values. * The client learns the status of a managed device based on the alarms and events sent by the server. |
| NETCONF server | A server maintains information of managed devices, responds to RPC requests sent by clients, and sends the requested management data to the clients.   * After receiving a request from a client, the server parses the request, processes the request based on the configuration management framework (CMF), and then returns a response to the client. * If a fault or another type of event occurs on a managed device, the server reports the alarm or event to the client through the notification mechanism. This allows the client to learn the status of the managed device. |

A network device must support at least one NETCONF session, which is a logical connection between a client and a server. The information that a client obtains from a server can be configuration or status data.

* The client can modify and operate configuration data to implement a user-expected status of the server.
* The client cannot modify status data, which mainly includes the running status and statistics of the server.

#### Establishing a Basic NETCONF Session

1. The client triggers the establishment of a NETCONF session. It then completes SSH connection setup after authentication and authorization are complete.
2. The client and server complete NETCONF session establishment and capability negotiation.
3. The client sends one or more requests to the server for RPC interaction (authorization). For example:
   
   * Modify and commit the configuration.
   * Query the configuration data or status.
   * Perform maintenance operations on the device.
4. Terminate the NETCONF session.
5. Tear down the SSH connection.

#### Session Interaction Between the Client and Server

After a NETCONF session is established, the client and server immediately exchange Hello messages with each other (these messages include the <hello> element, which contains the set of capabilities supported locally). If both ends support a capability, they can implement special management functions based on this capability.

The result of negotiating standard capabilities (except the notification capability) depends on the server-side capability set whereas that of extended capabilities depends on which capabilities both ends support.

![](public_sys-resources/note_3.0-en-us.png) 

A NETCONF server can send a <hello> element to advertise the capabilities that it supports.

When a Huawei device is connected to a non-Huawei device, if the capabilities contained in a <hello> packet sent from the peer are all standard capabilities, the Huawei device replies with a YANG packet.

After a server exchanges <hello> elements with a client, the server waits for <rpc> elements from the client. The server returns an <rpc-reply> element in response to each <rpc> element. [Figure 2](#EN-US_TOPIC_0000001564002177__fig_dc_vrp_netconf_feature_002101) shows the capability interaction between the NETCONF server and client.

**Figure 2** Capability interaction between the server and client  
![](figure/en-us_image_0000001564122177.png)