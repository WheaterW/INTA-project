next-server
===========

next-server

Function
--------

The **next-server** command configures the IP address of a server for the DHCP client after the client automatically obtains the IP address.

The **undo next-server** command deletes a configured IP address of a server for the DHCP client after the client automatically obtains the IP address.

By default, no IP address of a server is configured for the DHCP client after the client automatically obtains the IP address.



Format
------

**next-server** *ip-address*

**undo next-server**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a server IP address. | The value is in dotted decimal notation. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The **next-server** command is used on DHCP servers. When assigning a client an IP address, a DHCP server can also assign the client an IP address of the server that provides network services for the client. For example, after obtaining IP addresses, clients such as IP phones need parameters such as the startup configuration file to work normally. You can run the **next-server** command to specify the server address used after a client obtains an IP address. The client then requests the configuration parameters from the specified server after obtaining an IP address.

If users use addresses in the interface address pool, run the
**dhcp server next-server** command to specify the DHCP server IP address. If users use addresses in the global address pool, run the
**next-server** command to specify the DHCP server IP address.

**Precautions**

* Only one IP address of a server that provides network services can be configured in each IP address pool view or DHCP Option template view. If the system needs multiple IP addresses of servers that provide network services, configure multiple IP address pools or DHCP Option templates.
* If you run the **next-server** command multiple times, only the latest configuration takes effect.


Example
-------

# In the IP address pool view, set the IP address of a server for the DHCP client after the client automatically obtains the IP address to 10.1.2.2.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] next-server 10.1.2.2

```