gRPC Protocol Framework
=======================

gRPC Protocol Framework

#### gRPC Protocol Stack Layers

[Figure 1](#EN-US_TOPIC_0000001513034226__d0e597) shows the gRPC protocol stack layers.

**Figure 1** gRPC protocol stack layers  
![](figure/en-us_image_0000001512834694.png "Click to enlarge")

[Table 1](#EN-US_TOPIC_0000001513034226__d0e606) describes each gRPC protocol stack layer.

**Table 1** Description of gRPC protocol stack layers
| Layer | Description |
| --- | --- |
| TCP layer | Underlying communication protocol, which is based on TCP connections. |
| TLS layer | Optional layer, which is based on TLS encryption channels. |
| HTTP/2 layer | Carries gRPC and provides HTTP/2 features such as bidirectional streaming, flow control, header compression, and multiplexing request of a single connection for gRPC. |
| gRPC layer | Defines the protocol interaction format for RPCs. |
| Data model layer | Communication parties must recognize each other's data models before interacting with each other. |



#### gRPC Networking Architecture

gRPC uses the client/server model in combination with HTTP/2 to transmit packets, as shown in [Figure 2](#EN-US_TOPIC_0000001513034226__fig20497185834616).

**Figure 2** gRPC networking architecture  
![](figure/en-us_image_0000001513034270.png)

The gRPC mechanism is as follows:

* The gRPC server waits for connection requests from the client by listening to the specified service port.
* A user logs in to the gRPC server from the client.
* The gRPC client sends a request by calling a gRPC method provided by a .proto file.
* The gRPC server sends a response.

![](public_sys-resources/note_3.0-en-us.png) 

The device can function as a gRPC server or client.



The device can connect to a collector in dial-in or dial-out mode.

**Table 2** Interconnection modes
| Interconnection Mode | Application Scenario | **Telemetry Implementation** |
| --- | --- | --- |
| Dial-out mode: The device functions as a gRPC client, and proactively pushes device data to a collector. | Large-scale networks | 1. A user defines a static or dynamic telemetry subscription.    * Static telemetry subscription: defined in the **huawei-grpc-dialout.proto** file    * Dynamic telemetry subscription: defined in the **huawei-grpc-dialin.proto** file. 2. The user encodes collected information in GPB or JSON format and defines key information including the sampling path and timestamp in the **huawei-telemetry.proto** file. For details about the GPB and JSON encoding formats, see [Encoding Formats](galaxy_telemetry_cfg_0029.html).    * When GPB encoding is used, the value of the **encoding** field in the **huawei-telemetry.proto** file is 0, the **data\_gpb** field carries sampled data in GPB format, and the **data\_str** field is empty.    * When JSON encoding is used, the value of the **encoding** field in the **huawei-telemetry.proto** file is 1, the **data\_str** field carries sampled data in JSON format. 3. The device transmits data to the collector, and the collector decodes and analyzes the data.    * The **data\_gpb** field in the **huawei-telemetry.proto** file needs to be decoded using the .proto file of the corresponding service, which is determined by the **sensor\_path** field in the **huawei-telemetry.proto** file. For example, if the value of the **sensor\_path** field is **huawei-ifm:ifm/interfaces/interface**, the .proto file is **huawei-ifm.proto**.    * When the pure JSON encoding format (both the telemetry layer and data model layer use JSON encoding) is used, the collector only needs to decode the **huawei-grpc-dialout.proto** or **huawei-grpc-dialin.proto** file. When the hybrid JSON encoding format (the telemetry layer uses GPB encoding and the data model layer uses JSON encoding) is used, the collector only needs to decode the **huawei-grpc-dialout.proto** or **huawei-grpc-dialin.proto** file and the **huawei-telemetry.proto** file. The corresponding service .proto files do not require decoding. NOTE:     * In static telemetry subscription mode: If the connection between the device and collector is interrupted, the device reconnects to the collector and sends data again. However, the data sampled during connection re-establishment is lost.  After an active/standby switchover is performed or the system saves telemetry service configurations and restarts, the telemetry service reloads its configurations and continues to run. However, the data sampled during the active/standby switchover or restart is lost.    * In dynamic telemetry subscription mode: If the connection that carries dynamic telemetry subscription is interrupted, the device cancels the dynamic subscription and stops data sampling and reporting. The configuration cannot be restored unless the NMS sends a gRPC request again. |
| Dial-in mode: The device functions as a gRPC server, and a collector delivers configurations to the device. | Small-scale networks |