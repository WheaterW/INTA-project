if-match acl(IFIT traffic-classifier view)
==========================================

if-match acl(IFIT traffic-classifier view)

Function
--------



The **if-match acl** command configures an ACL rule for IFIT.

The **undo if-match acl** command deletes an ACL rule for IFIT.



By default, no ACL rule is specified for IFIT.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match** [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* }

**undo if-match** [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Specifies IPv6 packets as a matching rule. | - |
| **acl** *acl-number* | Specifies the ACL number. | The value is an integer that ranges from 3000 to 3999. |
| **name** *acl-name* | Specifies the ACL name. | The value is a string of 1 to 32 characters. |



Views
-----

IFIT traffic-classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure IFIT, you need to run this command to configure an ACL rule for IFIT. IFIT measurement is performed only for the traffic that matches the ACL rule in the IFIT measurement domain.The supported ACL rules can contain only the following fields. An ACL rule containing unsupported information will not be delivered. As a result, the IFIT function cannot be enabled for the corresponding traffic.

* TCP protocol
* UDP protocol
* Destination IPv4 or IPv6 address
* Destination IPv4 or IPv6 mask
* Source IPv4 or IPv6 address
* Source IPv4 or IPv6 mask
* TCP destination port number (The value must be the same as the specified port number.)
* TCP source port number (The value must be the same as the specified port number.)
* UDP destination port number (The value must be the same as the specified port number.)
* UDP source port number (The value must be the same as the specified port number.)

**Prerequisites**

IFIT has been enabled.


Example
-------

# Specify an IFIT ACL rule and bind it to IPv4 ACL 3000.
```
<HUAWEI> system-view
[~HUAWEI] acl 3000
[*HUAWEI-acl4-advance-3000] quit
[*HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic classifier class1
[*HUAWEI-ifit-dcn-instance-classifier-class1] if-match acl 3000

```