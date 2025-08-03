local-source-address
====================

local-source-address

Function
--------



The **local-source-address ipv4** command sets a source IPv4 address and a source port number when UDP or gRPC is used for data sending.

The **undo local-source-address ipv4** command deletes the source IPv4 address and source port number configured when UDP or gRPC is used for data sending.

The **local-source-address ipv6** command sets a source IPv6 address and a source port number when UDP or gRPC is used for data sending.

The **undo local-source-address ipv6** command deletes the source IPv6 address and source port number configured when UDP or gRPC is used for data sending.



By default, the source IP address is the IP address of route's outbound interface selected by UDP or gRPC and the source port number is randomly selected.


Format
------

**local-source-address ipv4** *ipv4-address* [ **port** *port-value* ]

**local-source-address ipv6** *ipv6-address* [ **port** *port-value6* ]

**undo local-source-address ipv4**

**undo local-source-address ipv4** *ipv4-address* [ **port** *port-value* ]

**undo local-source-address ipv6**

**undo local-source-address ipv6** *ipv6-address* [ **port** *port-value6* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **port** *port-value* | Specifies a IPv4 source port number when UDP is used for data sending. | The value is an integer ranging from 1 to 65535. |
| **port** *port-value6* | Specifies a IPv6 source port number when UDP is used for data sending. | The value is an integer ranging from 1025 to 65535. |
| **ipv4** *ipv4-address* | Specifies a source IPv4 address for data sending. | The value is in dotted decimal notation. |
| **ipv6** *ipv6-address* | Specifies a source IPv6 address for data sending. | The value is a 32-bit hexadecimal string in the format of X:X:X:X:X:X:X:X. |



Views
-----

Subscription view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To statically subscribe to sampled data, you need to configure the source IP address and source port number (only for UDP) in the subscription view to ensure that the device and collector can communicate with each other.Only one combination of the source IP address and source port number can be configured for a subscription. After the configuration is complete:

* The configured source IP address and source port number are filled in the UDP message header of the data sent through UDP.
* The configured source IP address is filled in the gRPC message header of the data sent through gRPC.

**Precautions**

* The configured IP address must be routable to the collector's IP address.
* If a source IPv6 address has been configured, the address cannot be directly changed to a source IPv4 address. To change the address to a source IPv4 address, you must delete the source IPv6 address first.
* After a source IPv4 address is configured for a subscription, this address takes effect only for the IPv4 collector in the subscription. The IPv6 collector in the subscription uses an outbound interface's IPv6 address as the source address.
* After a source IPv6 address is configured for a subscription, this address takes effect only for the IPv6 collector in the subscription. The IPv4 collector in the subscription uses an outbound interface's IPv4 address as the source address.
* A maximum of two pairs of source IP addresses and source ports can be configured for all subscriptions in each VS. If more than two pairs of source IP addresses and source ports are configured, an error message is displayed.


Example
-------

# Set the source IPv4 address to 10.10.1.1 and the source port number to 11111 when UDP is used for data sending.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] subscription test
[*HUAWEI-telemetry-subscription-test] local-source-address ipv4 10.10.1.1 port 11111

```

# Set the source IPv4 address to 10.10.1.1 when gRPC is used for data sending.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] subscription test
[*HUAWEI-telemetry-subscription-test] local-source-address ipv4 10.10.1.1

```

# Set the source IPv6 address to 2001:db8:4::1 when gRPC is used for data sending.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] subscription test
[*HUAWEI-telemetry-subscription-test] local-source-address ipv6 2001:db8:4::1

```