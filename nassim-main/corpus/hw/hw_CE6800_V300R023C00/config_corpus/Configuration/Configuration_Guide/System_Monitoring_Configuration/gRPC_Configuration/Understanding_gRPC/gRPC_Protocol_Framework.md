gRPC Protocol Framework
=======================

gRPC Protocol Framework

#### gRPC Protocol Stack Layers

[Figure 1](#EN-US_CONCEPT_0000001563766157__fig18535429429) shows the gRPC protocol stack layers.

**Figure 1** gRPC protocol stack layers  
![](figure/en-us_image_0000001512846282.png)

[Table 1](#EN-US_CONCEPT_0000001563766157__table163772030114417) describes each gRPC protocol stack layer.

**Table 1** gRPC protocol stack layer description
| Layer | Description |
| --- | --- |
| TCP layer | Underlying communication protocol, which is based on TCP connections. |
| TLS layer | Optional layer, which is based on the TLS encryption channel. |
| HTTP/2 layer | Carries gRPC and provides HTTP/2 features such as bidirectional streaming, flow control, header compression, and multiplexing request of a single connection for gRPC. |
| gRPC layer | Defines the protocol interaction format for remote procedure calls. |
| Encoding layer | Defines the encoding format such as Google Protocol Buffer (GPB) and JavaScript Object Notation (JSON) for gRPC data. |
| Data model layer | Carries service module data. Communication parties must recognize each other's data models before calling each other's information. Currently, the device provides the configuration, subscription, and query service modules. |



#### gRPC Networking Architecture

In [Figure 2](#EN-US_CONCEPT_0000001563766157__fig1767455975816), gRPC uses the client/server model in combination with HTTP/2 to transmit packets.

**Figure 2** gRPC networking architecture  
![](figure/en-us_image_0000001513045846.png)

The gRPC mechanism is as follows:

* The gRPC server waits for connection requests from the client by listening to the specified service port.
* A user logs in to the gRPC server through a client.
* The gRPC client calls the gRPC method provided by the .proto file to send a request.
* The gRPC server sends a response.

![](public_sys-resources/note_3.0-en-us.png) 

The device can function as a gRPC server or client.



#### Dial-In and Dial-Out Modes

The device can connect to a collector in the dial-in and dial-out modes.

1. Dial-in mode: The device functions as a gRPC server, and the collector functions as a gRPC client, which initiates a gRPC connection request to the device to obtain data or deliver configurations. This mode applies to small-scale networks.The following operations can be performed in dial-in mode:
   * Subscribe: collects interface traffic statistics, CPU usage, and memory usage of the device at a high speed. Currently, this operation can be performed based on the gRPC Network Management Interface (gNMI) protocol and telemetry.
   * Get: obtains the running status and configuration of the device. Currently, this operation can only be performed based on gNMI.
   * Capabilities: obtains capabilities of the device. Currently, this operation can only be performed based on gNMI.
   * Set: delivers configurations to the device. Currently, this operation can only be performed based on gNMI.
2. Dial-out mode: The device functions as a gRPC client, and the collector functions as a gRPC server. The device proactively establishes a gRPC connection with the collector to push the subscribed data configured on the device to the collector. This mode applies to large-scale networks.