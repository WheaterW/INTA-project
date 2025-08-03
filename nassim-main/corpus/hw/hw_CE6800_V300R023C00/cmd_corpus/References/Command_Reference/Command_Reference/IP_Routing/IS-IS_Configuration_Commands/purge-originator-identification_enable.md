purge-originator-identification enable
======================================

purge-originator-identification enable

Function
--------



The **purge-originator-identification enable** command enables whether IS-IS adds the purge originator identification (POI) TLV and hostname TLV to Purge LSPs to be sent.

The undo purge-originator-identification command restores the default configuration.



By default, Purge packets do not carry POI TLV or hostname TLV.


Format
------

**purge-originator-identification enable**

**purge-originator-identification enable always**

**undo purge-originator-identification enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **always** | Enables IS-IS to always add the POI TLV and dynamic hostname TLV to Purge LSPs to be sent. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When Remaining Lifetime of an LSP is 0, the LSP is invalid, and this invalid packet is a Purge packet. In most cases, a Purge packet does not carry any information about the router that generated the Purge packet. Without such information, troubleshooting is difficult if a network problem occurs.To address this issue, you can run the**purge-originator-identification enable** command to configure IS-IS to add POI TLV to Purge packets. If a dynamic hostname has been configured for the local device, the hostname TLV is also added to the Purge packets, which facilitates troubleshooting.

* If the **purge-originator-identification enable** command is run and the send-only parameter is specified when configuring authentication, generated Purge LSPs do not carry the POI TLV or hostname TLV.
* If the **purge-originator-identification enable** command is run and HMAC-MD5 authentication is configured, generated Purge LSPs do not carry the POI TLV or hostname TLV. If the **purge-originator-identification enable** command is run and authentication of another type is configured or no authentication is configured, generated Purge LSPs carry the POI TLV and hostname TLV.For the sake of security, using the HMAC-SHA256 algorithm rather than the HMAC-MD5 algorithm is recommended.
* If the **purge-originator-identification enable always** command is run, generated Purge LSPs carry the POI TLV and hostname TLV, regardless of whether authentication is configured or whether the send-only parameter is specified when configuring authentication.

**Prerequisites**

An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.

**Configuration Impact**

This command requires that all IS-IS devices on the network support standard protocol. If any IS-IS device does not support standard protocol, a routing loop or black hole may occur.


Example
-------

# Configure IS-IS to add POI TLV to Purge packets.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] purge-originator-identification enable

```