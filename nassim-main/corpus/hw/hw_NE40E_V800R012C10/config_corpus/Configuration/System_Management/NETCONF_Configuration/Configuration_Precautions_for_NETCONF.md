Configuration Precautions for NETCONF
=====================================

Configuration Precautions for NETCONF

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| 1. A maximum of 15 active NETCONF session disconnection alarms are allowed. If the number of active alarms exceeds the upper limit, the earliest active alarms are cleared.  2. After the device is restarted, lost alarms are not reported again. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| NETCONF has a limitation on the maximum number of imported packets. The maximum size of the configuration data imported through the URL cannot exceed 30 MB.  The following operations are involved:  1. In the edit-config operation, the value of source is url.  2. In the copy-config operation, the value of source is url.  The size of target data in the URL cannot exceed 30 MB. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| For a NETCONF operation, if no service response is received within 32 seconds, a timeout occurs and a response timeout error packet is returned. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If a schema patch operation is performed when a user is performing a schema operation, the schema operation will fail. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The size of a delivered RPC message cannot be greater than 30 MB. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The device can use only SSH as the transport protocol of NETCONF. Before using NETCONF to manage network devices, you must configure SSH. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If the NMS client only notifies the base capability in compliance with the standard, the YANG mode is used for interconnection. If the exchange capability is advertised, the Huawei proprietary schema mode is used for interconnection. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| During schema patch installation, data configuration may be locked. In this case, operations such as full synchronization and locking cannot be performed. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| 1. If the capability set carried in the Hello packet sent by the peer contains extended capabilities, the device replies with a schema packet.  2. The exchange capability set is advertised to identify the mode of processing high-specification data.  3. The sync capability set is advertised to determine whether the packet returned by edit-config carries a flow ID. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |