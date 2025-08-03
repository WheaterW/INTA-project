timer connect-retry (BGP view)
==============================

timer connect-retry (BGP view)

Function
--------



The **timer connect-retry** command sets a global ConnectRetry interval.

The **undo timer connect-retry** command restores the default setting.



By default, the ConnectRetry interval is 32s.


Format
------

**timer connect-retry** *connect-retry-time*

**undo timer connect-retry**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *connect-retry-time* | Specifies a ConnectRetry interval. | The value ranges from 1 to 65535, in seconds. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When BGP initiates a TCP connection, the ConnectRetry timer is stopped if the TCP connection is established successfully. If the first attempt to establish a TCP connection fails, BGP tries again to establish the TCP connection after the ConnectRetry timer expires. The ConnectRetry interval can be adjusted as needed.

* The ConnectRetry interval can be reduced in order to lessen the time BGP waits to retry establishing a TCP connection after the first attempt fails.
* To suppress route flapping caused by constant peer flapping, the ConnectRetry interval can be increased to accelerate route convergence.

**Precautions**



A ConnectRetry interval can be configured globally, or on a particular peer or peer group. A ConnectRetry interval configured on a specific peer or peer group takes precedence over a global ConnectRetry interval.If both the peer timer connect-retry command and the timer connect-retry command are run on a device, the configuration of the **peer timer connect-retry** command takes effect, but the configuration of the timer connect-retry command does not.




Example
-------

# Set a global BGP ConnectRetry interval to 60s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] timer connect-retry 60

```