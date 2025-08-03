set-overload
============

set-overload

Function
--------



The **set-overload** command sets the overload bit for non-pseudonode LSPs.

The **undo set-overload** command clears the set overload bit.



By default, the overload bit is not set.


Format
------

**set-overload**

**set-overload** { **allow** { **interlevel** | **external** } \* }

**set-overload** { **on-startup** [ *timeout1* | **start-from-nbr** *system-id* [ *timeout1* [ *timeout2* ] ] | **wait-for-bgp** [ *timeout1* ] ] [ **route-delay-distribute** *timeout4* ] [ **send-sa-bit** [ *timeout3* ] ] [ **route-max-metric** ] }

**set-overload** { **on-startup** [ *timeout1* | **start-from-nbr** *system-id* [ *timeout1* [ *timeout2* ] ] | **wait-for-bgp** [ *timeout1* ] ] [ **route-delay-distribute** *timeout4* ] [ **send-sa-bit** [ *timeout3* ] ] [ **route-max-metric** ] } { **allow** { **interlevel** | **external** } \* }

**undo set-overload**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **allow** | Indicates that the learned address prefixes can be advertised. By default, when the system enters the overload state, the address prefixes learned from other protocols, other IS-IS processes, or IS-IS of a different level cannot be advertised. | - |
| **interlevel** | Enables the device to advertise the IP prefixes learned from IS-IS of different levels when allow is configured. | - |
| **external** | Indicates that if allow is configured, the IP address prefixes learned from other protocols or other IS-IS processes can be advertised. | - |
| **on-startup** | Sets the overload bit within the specified period when a device is restarted or faulty. | - |
| *timeout1* | Specifies the period during which the overload bit remains set after the device is started and the IS-IS component is registered. | The value is an integer ranging from 5 to 86400, in seconds. The default value is 600 seconds. |
| **start-from-nbr** *system-id* | Sets the overload bit based on the status of the neighbor with the specified system ID. | The value is a string of 1 to 19 case-sensitive characters, spaces not supported. |
| *timeout2* | Specifies the period during which the overload bit remains set based on the neighbor status.  * If the specified neighbor does not go Up within timeout2, the overload bit of the system remains set over a period specified by timeout2. * If the specified neighbor goes Up within timeout2, the overload bit of the system remains set over a period specified by timeout1. | The value is an integer ranging from 5 to 86400, in seconds. The default value is 1200 seconds. |
| **wait-for-bgp** | Sets the duration of the overload bit to wait for the completing of BGP convergence. The duration can be set according to the BGP convergence time on the device.  After this parameter is set, the device notifies other devices that it is in the Overload state and instruct them not to use itself as a traffic forwarding node. The overload bit set in the LSP is cleared only after timeout1 expires. | - |
| **route-delay-distribute** *timeout4* | Configures delayed route advertisement.  Description:  After the device is restarted, if other devices still use old LSPs to calculate the routes to the restarted device, traffic is imported to the restarted device. To prevent this problem, set this parameter with send-sa-bit.  If this parameter is used independently, due to residual LSPs on the network, traffic may fail to be prevented from being sent to the restarted device. | The value is an integer ranging from 5 to min (timeout1, 1000), in seconds. |
| **send-sa-bit** | Indicates that Hello packets sent after the device restarts carry the SA bit. When a neighbor receives a Hello packet in which the SA bit is set to TRUE from the restarter, the LSP of the neighbor does not carry adjacency information. The SA bit is the Suppress Adjacency Bit field carried in the Restart Signaling flag TLV of an IS-IS Hello packet. The SA bit is used to prevent a faulty device from establishing adjacencies with neighboring devices. | - |
| *timeout3* | Specifies the period during which the overload bit remains in Hello packets after the device is started. | The value is an integer ranging from 5 to 600, in seconds. The default value is 30 seconds. |
| **route-max-metric** | Set the local originating route to the maximum metric. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the system cannot store new LSPs or synchronize LSDBs due to insufficient memory, the routing information calculated by the system is incorrect. In this case, the system automatically enters the Overload state, regardless of the configuration.You can run this command to configure an IS-IS process to enter the Overload state when the device starts or restarts and instruct other devices not to use it as a traffic forwarding node.To prevent other devices from using the local device for SPF calculation (for example, when the local device is started for the first time or fails), run the **set-overload** command on the local device without specifying on-startup. In this case, the system immediately sets the overload bit in the LSPs to be sent. You can only run the **undo set-overload** command to cancel the overload bit.To prevent other devices from using the local device for SPF calculation when the local device restarts, run the **set-overload** command with on-startup specified on the local device.When on-startup is specified, you can use the route-delay-distribute timeout4 parameter to control the delay in advertising routes. After the device configured with the route-delay-distribute timeout4 parameter is restarted, route advertisement is delayed until timeout4 expires or the overload bit disappears. After the device restarts, if routes need to be advertised immediately before timeout4 expires, you can use the following methods for timely route advertisement:

* Perform an active/standby switchover.
* Run the command again, without the route-delay-distribute keyword.
* Run the **reset isis all** command.After on-startup is specified, you can use the route-max-metric parameter to adjust the metric of locally originated routes to the maximum value. After the device configured with route-max-metric restarts, the metric of the locally originated route is set to the maximum value. The metric is restored to the original value only when timeout1 expires or the overload bit is set to 0. After the device is restarted, if the original metric of the route needs to be restored before timeout1 expires, you can use the following methods:
* Run this command again, without the route-max-metric keyword.
* Run the **reset isis all** command.Running the **reset isis all** command may cause link flapping for a short period of time. Therefore, exercise caution when running this command.

**Prerequisites**

An IS-IS process has been created.

**Configuration Impact**

After this command is run:

* If on-startup is specified, the LSPs with the overload bit are flooded on the network only when the device restarts.
* If on-startup is not specified, the system immediately sets the overload bit in the LSPs to be sent.After a device is configured with the overload bit, other devices ignore the device when performing SPF calculation. The direct routes of the device and the default routes advertised through the [ ipv6 ] default-route-advertise command, however, are not ignored.

**Precautions**

When a device is experiencing a memory shortage, the system automatically sets the overload bit in the LSP to be sent, regardless of whether the **set-overload** command is run.After the device is restarted, if you change the value of timeout4 when it has not yet expired, the current value is still used until the timer expires.Using the delayed route advertisement function only when a backup path is available is recommended.


Example
-------

# Configure IS-IS process 1 to enter the Overload state during the startup, and configure the local device to maintain the Overload state for 300 seconds after it establishes the neighbor relationship with neighbor 0000.0000.0002 within 1000 seconds during which the system starts.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] set-overload on-startup start-from-nbr 0000.0000.0002 300 1000

```

# Set the overload bit for IS-IS process 1.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] set-overload

```

# Configure IS-IS process 1 to enter the Overload state during the startup, allow IS-IS to advertise the IP prefixes learned from IS-IS of different levels, and prevent IS-IS from advertising the IP prefixes learned from other protocols.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] set-overload on-startup allow interlevel

```