ripng default-route
===================

ripng default-route

Function
--------



The **ripng default-route** command advertises a default route to the RIPng routing domain.

The **undo ripng default-route** command disables the advertisement of RIPng default routes and the forwarding of IPv6 default routes.



By default, a RIPng device does not advertise a default route to the RIPng routing domain.


Format
------

**ripng default-route only** [ [ **cost** *cost* ] | [ **tag** *tag* ] ] \*

**ripng default-route originate** [ [ **cost** *cost* ] | [ **tag** *tag* ] ] \*

**undo ripng default-route**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cost** *cost* | Specifies the cost of the default route. | The value is an integer ranging from 0 to 15. By default, the value is 0. |
| **tag** *tag* | Specifies the tag of the imported VPN routes. | The value is an integer that ranges from 0 to 65535. The default value is 0. |
| **originate** | Advertises the IPv6 default route (::/0) along with other routes. | - |
| **only** | Advertises only the IPv6 default route (::/0) and suppresses the advertisement of other routes. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

RIPng does not advertise default routes automatically. To enable an interface to advertise default routes in Update packets, run the ripng default-route command.


Example
-------

# Set the cost of the default route to 5.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ripng default-route only cost 5

```

# Advertise the default route along with other routes in the Update packet through a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ripng default-route originate

```

# Advertise only the default route in the Update packet through a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ripng default-route only

```