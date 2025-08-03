ipv6 extension-header (interface view)
======================================

ipv6 extension-header (interface view)

Function
--------



The **ipv6 extension-header option-code** command configures a filtering policy for the IPv6 Hop-by-Hop Options or Destination Options header.

The **undo ipv6 extension-header option-code** command restores the default configuration for the IPv6 Hop-by-Hop Options or Destination Options header.

The **ipv6 extension-header routing routing-type** command configures a filtering policy for the IPv6 Routing header.

The **undo ipv6 extension-header routing routing-type** command restores the default configuration for the IPv6 Routing header.

The **ipv6 extension-header** command configures a filtering policy for the IPv6 Fragment, Encapsulating Security Payload, or Authentication header.

The **undo ipv6 extension-header** command restores the default configuration for the IPv6 Fragment, Encapsulating Security Payload, or Authentication header.



By default, no filtering policy is configured for IPv6 extension headers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 extension-header** { **hop-by-hop** | **destination** } **option-code** { **all** | *optcodevalue* } { **deny** | **permit** }

**ipv6 extension-header routing routing-type** { **all** | *routing-number* } { **deny** | **permit** }

**ipv6 extension-header** { **fragment** | **esp** | **ah** } { **deny** | **permit** }

**undo ipv6 extension-header** { **hop-by-hop** | **destination** } **option-code** { **all** | *optcodevalue* } [ **deny** | **permit** ]

**undo ipv6 extension-header routing routing-type** { **all** | *routing-number* } [ **deny** | **permit** ]

**undo ipv6 extension-header** { **fragment** | **esp** | **ah** } [ **deny** | **permit** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hop-by-hop** | Indicates the IPv6 Hop-by-Hop Options header. | - |
| **destination** | Indicates the IPv6 Destination Options header. | - |
| **option-code** | Indicates the IPv6 extension header option. | - |
| **all** | Indicates all options in the IPv6 extension header. | - |
| *optcodevalue* | Specifies the value of the IPv6 extension header option. | The value is an integer ranging from 0 to 255. |
| **deny** | Indicates that the filtering policy of the IPv6 extension header is deny. | - |
| **permit** | Indicates that the filtering policy of the IPv6 extension header is permit. | - |
| **routing** | Indicates the IPv6 Routing header. | - |
| **routing-type** | Indicates the route type of the IPv6 route extension header. | - |
| *routing-number* | Specifies the route type value in the IPv6 route extension header. | The value is an integer ranging from 0 to 255. |
| **fragment** | Indicates the IPv6 Fragment header. | - |
| **esp** | Indicates the IPv6 Encapsulating Security Payload header. | - |
| **ah** | Indicates the IPv6 Authentication header. | - |



Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent the system from being attacked by specific packets, run the ipv6 extension-header command to configure a filtering policy (deny or permit) for an extension header in the packets. The methods of configuring filtering policies for different types of extended headers are as follows:

* If the extension header is Hop-by-Hop or Destination Options, you can configure a filtering policy for all options or a specified one in the header.
* If the extension header is Routing, you can configure a filtering policy for all routing types or a specified one in the header.
* If the extension header is Fragment, Encapsulation Security Payload, or Authentication, you can configure a filtering policy directly for the header because it carries neither options nor routing types.

**Precautions**

* If the extension header is Hop-by-Hop Options, Destination Options, or Routing, you can configure multiple filtering policies. A filtering policy configured for a specified option or routing type takes precedence over that for all options or routing types.
* A filtering policy configured in the interface view takes precedence over that in the system view.

Example
-------

# Configure an interface to discard the received IPv6 packets that contain the Destination Options header regardless of the Option field.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[~HUAWEI-Eth-Trunk1] undo portswitch
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 extension-header destination option-code all deny

```

# Set a filtering policy to deny for the Authentication header on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[~HUAWEI-Eth-Trunk1] undo portswitch
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 extension-header ah deny

```

# Configure an interface to receive and process IPv6 packets with the Segment Routing header (routing-number=4).
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[~HUAWEI-Eth-Trunk1] undo portswitch
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 extension-header routing routing-type 4 permit

```

# Configure an interface to discard the received IPv6 packets that carry the Router Alert (optcodevalue=5) Hop-by-Hop Options header.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[~HUAWEI-Eth-Trunk1] undo portswitch
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 extension-header hop-by-hop option-code 5 deny

```