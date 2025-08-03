peer sa-policy import
=====================

peer sa-policy import

Function
--------



The **peer sa-policy import** command configures a policy for filtering (S, G) information in source active (SA) messages to be received from a specified Multicast Source Discovery Protocol (MSDP) peer.

The **undo peer sa-policy import** command restores the default configuration.



By default, (S, G) information in SA messages is not filtered, so that all (S, G) entry information can be received from an MSDP peer.


Format
------

**peer** *peer-address* **sa-policy** **import** { *advanced-acl-number* | **acl-name** *acl-name* }

**peer** *peer-address* **sa-policy** **import**

**undo peer** *peer-address* **sa-policy** **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | It is in dotted decimal notation. |
| *advanced-acl-number* | Specifies the number of an advanced ACL. | The value is an integer that ranges from 3000 to 3999. If this parameter is not specified, all the SA messages that carry (S, G) entries are filtered out. |
| **acl-name** *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The value must start with a letter (a to z or A to Z, case sensitive). |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To filter (S, G) information in SA messages to be received from or forwarded to a specified MSDP peer, run the **peer sa-policy import** command, implementing control over the receiving of multicast source information.In addition, you can run the **import-source** command on an MSDP peer to specify (S, G) information that can be advertised by SA messages.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.MSDP peers have been configured.

**Configuration Impact**

If the **peer sa-policy import** command is run more than once, the latest configuration overrides the previous one.

* If the import parameter is specified, the local Router determines how to process a received SA message as follows:
* If acl is not set, the Router does not accept the (S, G) information in the SA message.
* If acl is set, the Router accepts only the (S, G) information that matches the permit clause in an ACL rule.

Example
-------

# In the public network instance, configure an ACL 3100 and configure the Router to filter (S, G) information to be received from the peer 10.10.7.6 based on ACL 3100.
```
<HUAWEI> system-view
[~HUAWEI] acl number 3100
[*HUAWEI-acl4-advance-3100] rule permit ip source 10.15.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-advance-3100] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.10.7.6 connect-interface Vlanif 1
[*HUAWEI-msdp] peer 10.10.7.6 sa-policy import 3100

```