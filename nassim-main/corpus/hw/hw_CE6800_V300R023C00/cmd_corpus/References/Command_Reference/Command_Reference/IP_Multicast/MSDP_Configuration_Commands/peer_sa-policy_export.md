peer sa-policy export
=====================

peer sa-policy export

Function
--------



The **peer sa-policy export** command configures a policy for filtering (S, G) information in source active (SA) messages to be forwarded to a specified Multicast Source Discovery Protocol (MSDP) peer.

The **undo peer sa-policy export** command restores the default configuration.



By default, (S, G) information in SA messages is not filtered, so that all (S, G) entry information can be forwarded to an MSDP peer.


Format
------

**peer** *peer-address* **sa-policy** **export** { *advanced-acl-number* | **acl-name** *acl-name* }

**peer** *peer-address* **sa-policy** **export**

**undo peer** *peer-address* **sa-policy** **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | The value is in dotted decimal notation. |
| *advanced-acl-number* | Specifies the number of an advanced ACL. | The value is an integer ranging from 3000 to 3999. If the ACL is not specified, all SA messages carrying (S, G) information are filtered. |
| **acl-name** *acl-name* | Specifies the name of an advanced ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To filter (S, G) information in SA messages to be forwarded to a specified MSDP peer, run the **peer sa-policy export** command, implementing control over the receiving or sending of multicast source information.In addition, you can run the **import-source** command on an MSDP peer to specify (S, G) information that can be advertised by SA messages.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.MSDP peers have been configured.

**Precautions**

The **peer sa-policy export** command takes effect only on forwarded SA messages, but not on locally generated SA messages.


Example
-------

# In the public network instance, configure an ACL 3100 and configure the Router to filter (S, G) information to be forwarded to the peer 10.10.7.6 based on ACL 3100.
```
<HUAWEI> system-view
[~HUAWEI] acl number 3100
[*HUAWEI-acl4-advance-3100] rule permit ip source 10.15.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-advance-3100] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.10.7.6 connect-interface Vlanif 1
[*HUAWEI-msdp] peer 10.10.7.6 sa-policy export 3100

```