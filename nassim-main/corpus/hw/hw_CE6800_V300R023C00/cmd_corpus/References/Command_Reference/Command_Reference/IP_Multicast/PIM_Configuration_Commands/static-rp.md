static-rp
=========

static-rp

Function
--------



The **static-rp** command configures a static rendezvous point (RP).

The **undo static-rp** command deletes the configuration.



By default, no static RP is configured.


Format
------

**static-rp** *rp-address* [ *basic-acl-number* | **acl-name** *acl-name* ] [ **preferred** ]

**undo static-rp** *rp-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rp-address* | Specifies a static RP address. | The value is in dotted decimal notation. It must be a valid unicast IP address and cannot be configured as an address on the network segment 127.0.0.0/8. |
| *basic-acl-number* | Specifies the name of a named basic ACL. | The value is an integer that ranges from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **preferred** | Indicates that a static RP is preferred. | - |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When only one RP exists on a network, you can run the **static-rp** command to configure a static RP. Compared with dynamic RP election using the bootstrap router (BSR) mechanism, the static RP mechanism can reduce bandwidth occupied by messages exchanged between candidate-rendezvous points (C-RPs) and the BSR. To make the static RP work properly, you must run the **static-rp** command on all Routers.

**Precautions**

Up to 50 static RPs can be configured using the **static-rp** command, but a same ACL can be applied to only one static RP.If an ACL is not specified, only one static RP can be configured.


Example
-------

# In the public network instance view, specify the address 192.168.0.6 as the static RP address that serves groups permitted by the ACL 2001. Configure the static RP to be used preferentially.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] acl number 2001
[*HUAWEI-acl4-basic-2001] rule permit source 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-basic-2001] quit
[*HUAWEI] pim
[*HUAWEI-pim] static-rp 192.168.0.6 2001 preferred

```