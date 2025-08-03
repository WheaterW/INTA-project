cost-style
==========

cost-style

Function
--------



The **cost-style** command sets a cost type for the routes that can be received and those to be sent by an IS-IS device.

The **undo cost-style** command restores the default value.



By default, the cost type of IS-IS routes is narrow.


Format
------

**cost-style** { **narrow** | **wide** | **wide-compatible** | { **compatible** | **narrow-compatible** } [ **relax-spf-limit** ] }

**undo cost-style**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **narrow** | Indicates that the cost type for the routes that can be received and those to be sent by an IS-IS device is narrow. | - |
| **wide** | Indicates that the cost type for the routes that can be received and those to be sent by an IS-IS device is wide. | - |
| **wide-compatible** | Indicates that the route with the cost type of narrow or wide can be received, but only the route with the cost type of wide can be sent. | - |
| **compatible** | Indicates the route with the cost type of narrow or wide can be received and sent. | - |
| **narrow-compatible** | Indicates that the route with the cost type of wide or narrow can be received, but only the route with the cost type of narrow can be sent. | - |
| **relax-spf-limit** | Enables an IS-IS device to accept routes with cost greater than 1023.   * If relax-spf-limit is not specified: * If the cost of a route is smaller than or equal to 1023 and the link costs of all interfaces through which the route passes are smaller than or equal to 63:   The cost of the route is the sum of the link costs of all the interfaces through which the route passes.   * If the cost of a route is smaller than or equal to 1023 but the link costs of some interfaces through which the route passes are greater than 63:   The device can learn only the direct routes of other interfaces on the device where the interface resides and the routes imported by the interface. The cost of the route is the actual value. The interface through which the route passes discards the route. The routes after the interface are discarded.   * If the cost of a route is greater than 1023:   The device can receive all the routes to the network segment where the interface whose cost is smaller than 1023 resides. If the cost of a route is greater than 1023, the device receives the route as 1023. The device cannot receive all the routes to the network segment where the interface whose cost is greater than 1023 resides.   * Set relax-spf-limit.   There is no limit on the link costs of interfaces or route costs. The route is received according to the actual cost. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the cost style of IS-IS routes is narrow. In this mode, routes with the interface cost ranging from 1 to 63 can be advertised, and routes with the interface cost ranging from 1 to 1023 can be accepted. When IS-IS needs to carry tag information to apply a routing policy, LSPs carry additional information. As a result, these LSPs cannot be flooded in narrow mode. You can run the **cost-style** command to change the cost style of IS-IS routes according to network requirements so that LSPs can be transmitted successfully.In actual applications, the cost style of IS-IS routes is usually set to wide to facilitate the implementation of extended IS-IS functions.relax-spf-limit is valid only when the cost-style is compatible or narrow-compatible.

**Prerequisites**

An IS-IS process has been created using the **isis** command.

**Configuration Impact**

When the cost type of a route is changed from wide to narrow, transmission of the route may be interrupted.

**Precautions**

To change the cost type of IS-IS routes, configure the cost-style when configuring basic IS-IS functions. Otherwise, changing the cost type of IS-IS routes during network operation will restart the IS-IS process and disconnect IS-IS neighbors.When you set the IS-IS cost type, the cost type set on the interconnected devices affects link reachability. Therefore, exercise caution when setting the IS-IS cost type. When the interface cost is set to maximum (16777215), the bidirectional link between the two devices is unreachable. When the cost of an interface is smaller than 16777215, assume that device A and device B are connected. The following table lists the reachability in an IPv4 topology.

| Cost type of device A | Cost type of device B | Link reachability from device A to device B | Link reachability from device B to device A |
| --- | --- | --- | --- |
| wide | wide | Y | Y |
| wide | wide-compatible | Y | Y |
| wide-compatible | wide-compatible | Y | Y |
| narrow | narrow | Y | Y |
| narrow | narrow-compatible | Y | Y |
| narrow | compatible | Y | Y |
| narrow-compatible | narrow-compatible | Y | Y |
| narrow-compatible | compatible | Y | Y |
| compatible | compatible | Y | Y |
| wide | narrow | N | N |
| narrow | wide-compatible | N | Y |
| wide | narrow-compatible | N | Y (The interface cost of device A is less than or equal to 63.) <br/> Y (The interface cost of device A is greater than 63.) The relax-spf-limit parameter is configured on device B. <br/> N (The cost of the interface on device A is greater than 63, and the relax-spf-limit parameter is not configured on device B.) |
| wide | compatible | Y | Ibid. |
| wide-compatible | compatible | Y | Ibid. |
| wide-compatible | narrow-compatible | Y | Ibid. |

The following table lists the reachability of an IPv6 topology.

| Cost type of device A | Cost type of device B | Link reachability from device A to device B | Link reachability from device B to device A |
| --- | --- | --- | --- |
| wide | wide | Y | Y |
| wide | wide-compatible | Y | Y |
| wide-compatible | wide-compatible | Y | Y |
| narrow | narrow | Y | Y |
| narrow | narrow-compatible | Y | Y |
| narrow | compatible | Y | Y |
| narrow-compatible | narrow-compatible | Y | Y |
| narrow-compatible | compatible | Y | Y |
| compatible | compatible | Y | Y |
| wide | narrow | Y | Y (The cost of the interface on device A is smaller than or equal to 63.) Y (The cost of the interface on device A is greater than 63, and relax-spf-limit is configured on device B.) N (The cost of the interface on device A is greater than 63, and relax-spf-limit is not configured on device B.) |
| wide | compatible | Y | Ibid. |
| wide | narrow-compatible | Y | Ibid. |
| wide-compatible | narrow | Y | Ibid. |
| wide-compatible | compatible | Y | Ibid. |
| wide-compatible | narrow-compatible | Y | Ibid. |



Example
-------

# Configure an IS-IS device to send only the packets with the cost type narrow and to receive the packets with the cost type narrow or wide.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] cost-style narrow-compatible

```