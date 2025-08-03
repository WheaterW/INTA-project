local-source-interface
======================

local-source-interface

Function
--------



The **local-source-interface** command sets a source interface and a source port number when a protocol is used for data sending.

The **undo local-source-interface** command deletes the source interface and source port number configured when a protocol is used for data sending.



By default, the source interface and source port are not configured.


Format
------

**local-source-interface** { *if-name* | *if-type* *if-number* } [ **port** *port-value* ]

**undo local-source-interface** { *if-name* | *if-type* *if-number* } [ **port** *port-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *if-name* | Specifies an interface name. | The value is a string of 1 to 63 characters without spaces. |
| *if-type* | Interface type. | - |
| *if-number* | Specifies an interface number. | The value is a string of 1 to 63 characters without spaces. |
| **port** *port-value* | Specifies the IPv4 source port number in protocol-based packet sending mode. | The value is an integer ranging from 1 to 65535. |



Views
-----

Subscription view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To statically subscribe to the data sampled, you need to run the **local-source-interface** command to configure a source interface and a source port number (a source port number is required only when UDP is used for data sending) in the subscription view for data sending. This ensures that devices can communicate with the collector.Only one combination that consists of a source interface and a source port number can be configured for a subscription. After the configuration is complete:

* The UDP message header sent along the UDP channel contains the configured source interface and source port number.
* The gRPC message header sent along the gRPC channel contains the configured source interface.

**Precautions**



Only one of the local-source-interface and local-source-address commands can be configured in the same subscription view.




Example
-------

# Set the source interface to LoopBack0 and the source port number to 2345 for UDP packets.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] subscription test
[*HUAWEI-telemetry-subscription-test] local-source-interface LoopBack0 port 2345

```

# Set the source interface of gRPC packets to LoopBack0.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] subscription test
[*HUAWEI-telemetry-subscription-test] local-source-interface LoopBack0

```