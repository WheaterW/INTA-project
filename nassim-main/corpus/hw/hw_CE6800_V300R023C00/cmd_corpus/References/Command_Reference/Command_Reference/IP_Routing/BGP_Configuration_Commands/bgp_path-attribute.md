bgp path-attribute
==================

bgp path-attribute

Function
--------



The **bgp path-attribute** command configures the processing mode of the specified incorrect path attribute.

The **undo bgp path-attribute** command restores the default configuration.



By default, path attribute messages are processed according to the standard protocol.

If the value of the Originator\_ID attribute is 0, the route corresponding to the attribute is withdrawn. If the value of the Originator\_ID attribute in the Attr\_Set attribute is 0, the route corresponding to the attribute is withdrawn.

If the length of the Community, Ext-community, IPv6 ext-community, Large-community, Wide-community or Cluster\_List attribute is 0, the route corresponding to the attribute is withdrawn. If the length of the Community, Ext-community, IPv6 ext-community, Large-community, Wide-community or Cluster\_List sub-attribute in the Attr\_Set attribute is 0, the route corresponding to the attribute is withdrawn.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**bgp path-attribute** { **originator-id** | **attr-set** } **accept-zero-value**

**undo bgp path-attribute** { **originator-id** | **attr-set** } **accept-zero-value**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**bgp path-attribute** { **community** | **ext-community** | **ipv6-ext-community** | **large-community** | **attr-set** | **wide-community** | **cluster-list** } **accept-zero-length**

**undo bgp path-attribute** { **community** | **ext-community** | **ipv6-ext-community** | **large-community** | **attr-set** | **wide-community** | **cluster-list** } **accept-zero-length**

For CE6885-LL (low latency mode):

**bgp path-attribute** { **community** | **ext-community** | **large-community** | **attr-set** | **wide-community** | **cluster-list** } **accept-zero-length**

**undo bgp path-attribute** { **community** | **ext-community** | **large-community** | **attr-set** | **wide-community** | **cluster-list** } **accept-zero-length**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **originator-id** | Indicates the Originator\_ID attribute. | - |
| **attr-set** | Indicates the Attr\_Set attribute. | - |
| **accept-zero-value** | Indicates to accept the path attributes with a value of 0. | - |
| **community** | Indicates the community attribute. | - |
| **ext-community** | Indicates the Ext-community attribute. | - |
| **ipv6-ext-community** | Indicates the IPv6-ext-community attribute.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **large-community** | Indicates the Large-community attribute. | - |
| **wide-community** | Indicates the Wide-community attribute. | - |
| **cluster-list** | Indicates the Cluster\_List attribute. | - |
| **accept-zero-length** | Indicates to accept zero-length path attributes. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the local device receives an Update message with an incorrect format (containing a path attribute with a length of 0 or a value of 0), BGP session flapping may occur. To resolve this problem, run the **bgp path-attribute** command to configure special processing for the specified incorrect BGP path attribute. The options are as follows:

* accept-zero-value: indicates that the path attribute with a zero value is accepted.
* accept-zero-length: accepts zero-length path attributes.After the **bgp path-attribute attr-set accept-zero-value** command is run, if the value of the Originator\_ID attribute in the Attr\_Set attribute is 0, the route corresponding to the attribute can be accepted.After the **bgp path-attribute attr-set accept-zero-length** command is run, if the length of the Community, Ext-community, IPv6 ext-community, Large-community, Wide-community or Cluster\_List attribute in the Attr\_Set attribute is 0, the route corresponding to the attribute can be accepted.

**Precautions**

This function takes effect immediately for the routes received after this command is executed. However, the routes received before this command is run do not take effect immediately. You need to run the **refresh bgp** command to make the configuration take effect.The bgp path-attribute wide-community accept-zero-length command does not take effect for the RPD address family. After an RPD route with the Wide-Community attribute of 0 is received, the route is still withdrawn.


Example
-------

# Configure the Originator\_ID path attribute with a value of 0 to be accepted.
```
<HUAWEI> system-view
[~HUAWEI] bgp path-attribute originator-id accept-zero-value

```

# Configure the device to accept the community path attribute with the length of 0.
```
<HUAWEI> system-view
[~HUAWEI] bgp path-attribute community accept-zero-length

```