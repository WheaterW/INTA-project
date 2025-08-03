ipv6 extension-header (system view)
===================================

ipv6 extension-header (system view)

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
| **option-code** | Indicates all options or a specified one for an IPv6 extension header. | - |
| **all** | Indicates all options for an IPv6 extension header. | - |
| *optcodevalue* | Specifies the type value of an option for an IPv6 extension header. | The value is an integer ranging from 0 to 255. |
| **deny** | Sets a filtering policy to deny for an IPv6 extension header. | - |
| **permit** | Sets a filtering policy to permit for an IPv6 extension header. | - |
| **routing** | Indicates the IPv6 Routing header. | - |
| **routing-type** | Indicates all routing types or a specified one for the IPv6 Routing header. | - |
| *routing-number* | Specifies the value of a routing type for the IPv6 Routing header. | The value is an integer ranging from 0 to 255. |
| **fragment** | Indicates the IPv6 Fragment header. | - |
| **esp** | Indicates the IPv6 Encapsulation Security Payload header. | - |
| **ah** | Indicates the IPv6 Authentication header. | - |



Views
-----

System view


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

# Set a filtering policy to deny for the Router Alert option (option type 5) in the Hop-by-Hop Options header.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 extension-header hop-by-hop option-code 5 deny

```

# Set a filtering policy to deny for all options in the Destination Options header.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 extension-header destination option-code all deny

```

# Set a filtering policy to deny for the Authentication header.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 extension-header ah deny

```

# Set a filtering policy to permit for the Segment Routing header (routing type 4).
```
<HUAWEI> system-view
[~HUAWEI] ipv6 extension-header routing routing-type 4 permit

```