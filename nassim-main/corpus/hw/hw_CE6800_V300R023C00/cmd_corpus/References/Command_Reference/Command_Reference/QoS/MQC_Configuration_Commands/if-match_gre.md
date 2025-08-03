if-match gre
============

if-match gre

Function
--------



The **if-match gre** command configures a matching rule based on inner information in GRE packets in a traffic classifier.

The **undo if-match gre** command deletes a matching rule based on inner information in GRE packets in a traffic classifier.



By default, a matching rule based on inner information in GRE packets is not configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match gre** [ **inner-source-ip** *source-ip-address* [ **mask** *source-masklen* ] | **inner-destination-ip** *dest-ip-address* [ **mask** *dest-masklen* ] | **inner-protocol** *protocol* | **inner-source-port** *source-port-begin* | **inner-destination-port** *dest-port-begin* ] \*

**undo if-match gre** [ **inner-source-ip** *source-ip-address* [ **mask** *source-masklen* ] | **inner-destination-ip** *dest-ip-address* [ **mask** *dest-masklen* ] | **inner-protocol** *protocol* | **inner-source-port** *source-port-begin* | **inner-destination-port** *dest-port-begin* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **inner-source-ip** *source-ip-address* | Specifies the inner source IP address in GRE packets. | The value is in dotted decimal notation. |
| **mask** *dest-masklen* | Specifies the mask length of an IP address. | The value is an integer in the range from 0 to 32. |
| **mask** *source-masklen* | Specifies the mask length of an IP address. | The value is an integer in the range from 0 to 32. |
| **inner-destination-ip** *dest-ip-address* | Specifies the inner destination IP address in GRE packets. | The value is in dotted decimal notation. |
| **inner-protocol** *protocol* | Specifies the inner protocol number in GRE packets. | The value is an integer in the range from 0 to 255. |
| **inner-source-port** *source-port-begin* | Specifies the inner source port number in GRE packets. | The value is an integer in the range from 0 to 65535. |
| **inner-destination-port** *dest-port-begin* | Specifies the inner destination port number in GRE packets. | The value is an integer that ranges from 0 to 65535. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

GRE encapsulates packets of a protocol into packets of another protocol to transparently transmit packets over GRE tunnels. GRE solves the transmission problem on heterogeneous networks.You can run the **if-match gre** command to classify GRE packets inner information in GRE packets so that the device processes GRE packets matching the same traffic classifier in the same manner and provides fine-granular services.

**Precautions**

* A traffic policy containing this matching rule takes effect only on the device at the GRE tunnel egress.
* A traffic policy containing this matching rule cannot be applied to the outbound direction.
* If you do not specify any parameter in the command, GRE packets are matched.
* When a traffic classifier contains this matching rule, only packet filtering, traffic policing, redirection, and traffic statistics collection can be configured in the traffic behavior.

Example
-------

# Configure a matching rule based on the inner packet information of the GRE tunnel in the traffic classifier.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier class1
[*HUAWEI-classifier-class1] if-match gre inner-source-ip 192.168.1.1 mask 24

```