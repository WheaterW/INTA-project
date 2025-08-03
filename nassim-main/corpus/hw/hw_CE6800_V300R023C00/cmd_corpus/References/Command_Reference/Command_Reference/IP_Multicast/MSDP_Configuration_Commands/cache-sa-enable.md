cache-sa-enable
===============

cache-sa-enable

Function
--------



The **cache-sa-disable** command disables the source active (SA) cache function.

The **undo cache-sa-disable** command enables the SA cache function on a router, allowing the router to cache (S, G) information carried in received SA messages.

The SA cache function is enabled on a router.



By default, the SA cache function is enabled on a Router.


Format
------

**cache-sa-disable**

**undo cache-sa-disable**


Parameters
----------

None

Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The device enabled with the SA cache function can locally save (S, G) information carried in the received SA messages. Upon a reception request, it directly obtains available (S, G) information from the SA cache.After the SA cache function is disabled, the device does not save (S, G) information carried in the received SA messages locally. Upon a reception request, the device must wait for the SA message sent by the MSDP peer in the next period, which causes a delay for receivers to obtain multicast data.


Example
-------

# In the public network instance, disable the SA cache function.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] cache-sa-disable

```