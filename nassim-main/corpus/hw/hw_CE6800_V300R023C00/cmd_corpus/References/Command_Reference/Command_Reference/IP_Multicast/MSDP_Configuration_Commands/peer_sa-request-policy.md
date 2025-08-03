peer sa-request-policy
======================

peer sa-request-policy

Function
--------



The **peer sa-request-policy** command configures a filtering policy to respond to the source active (SA) Request messages sent by a specified Multicast Source Discovery Protocol (MSDP) peer. Once the SA Request message passes the filtering, the router responds to the SA message immediately.

The **undo peer sa-request-policy** command restores the default configuration.



By default, the router responds to all SA request messages sent by all MSDP peers.


Format
------

**peer** *peer-address* **sa-request-policy** { *basic-acl-number* | **acl-name** *acl-name* }

**peer** *peer-address* **sa-request-policy**

**undo peer** *peer-address* **sa-request-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | The value is in dotted decimal notation. |
| *basic-acl-number* | Specifies the number of a basic ACL. | The number is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an ACL is not specified, all SA Requests of an MSDP peer are ignored. If an ACL is specified, only SA Request messages that contain group addresses permitted by the ACL are processed.

**Configuration Impact**

If the peer sa-request-policy command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, configure an ACL for filtering SA request messages sent by the MSDP peer 10.58.6.5,Only SA request messages for the group 225.1.1.0/24 are accepted.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2001
[*HUAWEI-acl4-basic-2001] rule permit source 225.1.1.0 0.0.0.255
[*HUAWEI-acl4-basic-2001] quit
[~HUAWEI] interface loopback1
[*HUAWEI-LoopBack1] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.58.6.5 connect-interface LoopBack 1
[*HUAWEI-msdp] peer 10.58.6.5 sa-request-policy 2001

```