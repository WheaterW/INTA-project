Notification Capabilities
=========================

Notification Capabilities

#### Notification 1.0

A device can send alarms and events to a client using the NETCONF notification capability, thereby allowing the client to promptly detect device configuration or other changes. You can perform the <create-subscription> operation to subscribe to device alarms and events. If the <rpc-reply> element returned by the device contains an <ok> element, the <create-subscription> operation is successful. In this case, the device will proactively report the generated alarms and events to the client through NETCONF.

1. Alarms and events can be subscribed to in either of the following modes: long-term subscription and subscription within a specified period.
   * Long-term subscription: After the subscription is successful, if the <startTime> element is specified in the subscription message, the device sends historical alarms and events to the NMS and then sends a <replayComplete> message to notify the NMS that the replay is complete. If a new alarm or event is generated, the device also sends it to the NMS. If the <startTime> element is not specified in the subscription message, the device sends all newly generated alarms and events to the NMS. After a NETCONF session is terminated, the subscription is automatically canceled.
   * Subscription within a specified period: After the subscription is successful, the device sends the alarms and events that are generated during the specified period and that meet the filtering conditions to the NMS. Because the <startTime> element is specified in the subscription message, the device sends historical alarms and events to the NMS and then sends a <replayComplete> message to notify the NMS that the replay is complete. When the specified <stopTime> has been reached, the NETCONF module sends a <notificationComplete> message to notify the NMS that the subscription is terminated.
   
   Historical alarms and events refer to those generated from the <startTime> specified in the subscription message to when the user performs the subscription operation. If <stopTime> is not specified, the subscription is a long-term one. If both <startTime> and <stopTime> are specified, the subscription is within a specified period. The format of the subscription message sent by the device to the NMS is as follows:
   
   RPC request (NETCONF subscription)
   
   ```
   <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
     <create-subscription xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
       <stream>NETCONF</stream>
       <filter type="subtree">
          <netconf-config-change xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications"/>
       </filter>
       <startTime>2016-10-20T14:50:00Z</startTime>
       <stopTime>2016-10-23T06:22:04Z</stopTime>
     </create-subscription>
   </rpc>
   ```
   
   RPC reply (NETCONF subscription)
   
   ```
   <rpc-reply message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
     <ok/>
   </rpc-reply>
   ```
   
   RPC request (NETCONF-WITH-RES-CONFIG subscription)
   
   ```
   <?xml version="1.0" encoding="utf-8"?>
   <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="5">
     <create-subscription xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
       <stream>NETCONF-WITH-RES-CONFIG</stream>
       <filter type="subtree">
         <netconf-config-change xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications"/>
       </filter>
     </create-subscription>
   </rpc>
   ```
   
   RPC reply (NETCONF-WITH-RES-CONFIG subscription)
   
   ```
   <?xml version="1.0" encoding="utf-8"?>
   <rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="5">
     <ok/>
   </rpc-reply>
   ```
   
   Example of reporting a notification (NETCONF-WITH-RES-CONFIG subscription)
   
   ```
   <notification xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
     <eventTime>2020-12-09T20:41:14Z</eventTime>
     <alt-resource-config xmlns="urn:huawei:yang:huawei-notification-common">
       <notification-id>135598331</notification-id>
       <notification-class>event</notification-class>
       <event-level>informational</event-level>
     </alt-resource-config>
     <netconf-config-change xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications">
       <changed-by>
         <server/>
       </changed-by>
       <datastore>running</datastore>
     </netconf-config-change>
   </notification>
   ```
   
   **Table 1** Element descriptions
   | Element | Description | Value Range | Mandatory | Constraints |
   | --- | --- | --- | --- | --- |
   | stream | Event flow type | The value is a case-sensitive enumerated type and can be:  * NETCONF: indicates that the NETCONF notification mechanism is used to report alarms and events. * NETCONF-WITH-RES-CONFIG: indicates that the reported alarms or events carry Huawei's proprietary extension attribute huawei-notification-common. | No | N/A |
   | filter | Alarm or event filter | The value is a string of characters in the format of <alarm name xmlns=namespace of the alarm name/> or <event name xmlns=namespace of the event name/>. | No | If no filter is specified, all alarms and events that can be reported through notifications are subscribed to. |
   | startTime | Start time | The value is in the time format. | No | The start time must be earlier than the time when the subscription operation is performed. |
   | stopTime | End time | The value is in the time format. | No | The end time must be later than the start time. |

2. After the subscription is successful, the device encapsulates the alarm or event information into notification messages and sends them to the NMS.
   ```
   <notification xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
     <eventTime>2016-11-26T13:51:00Z</eventTime>
     <hwCPUUtilizationResume xmlns="urn:huawei:yang:huawei-sem">
     <TrapSeverity>0</TrapSeverity>
     <ProbableCause>0</ProbableCause>
     <EventType>0</EventType>
     <PhysicalIndex>0</PhysicalIndex>
     <PhysicalName>SimulateStringData</PhysicalName>
     <RelativeResource>SimulateStringData</RelativeResource>
     <UsageType>0</UsageType>
     <SubIndex>0</SubIndex>
     <CpuUsage>0</CpuUsage>
     <Unit>0</Unit>
     <CpuUsageThreshold>0</CpuUsageThreshold>
     </hwCPUUtilizationResume>
   </notification>
   ```

3. After alarms and events are reported to the NMS, the NETCONF module sends a subscription completion message to the NMS.
   * After historical alarms and events are reported to the NMS, the NETCONF module sends a replayComplete message to the NMS.
     
     ```
     <notification xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
       <eventTime>2016-11-29T11:57:15Z</eventTime>
       <replayComplete xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0" />
     </notification>
     ```
   * When <stopTime> specified in the subscription message has been reached, the NETCONF module sends a notificationComplete message to notify the NMS that the subscription is terminated.
     
     ```
     <notification xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
       <eventTime>2016-11-29T11:57:25Z</eventTime>
       <notificationComplete xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0" />
     </notification>
     ```
   
   **Table 2** Element descriptions
   | Element | Description | Value Range | Mandatory | Constraints |
   | --- | --- | --- | --- | --- |
   | replayComplete | After historical alarms and events are reported to the NMS, the NETCONF module sends a replayComplete message to the NMS. | N/A | No | N/A |
   | notificationComplete | When <stopTime> specified in the subscription message has been reached, the NETCONF module sends a notificationComplete message to notify the NMS that the subscription is terminated. | N/A | No | N/A |