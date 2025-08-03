domain-name
===========

domain-name

Function
--------

The **domain-name** command configures the domain name suffix for the DHCP client.

The **undo domain-name** command deletes a configured domain name suffix.

By default, no domain name suffix is configured.



Format
------

**domain-name** *domain-name*

**undo domain-name**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *domain-name* | Specifies a domain name. | The value is a string of 1 to 63 case-sensitive characters. If the string is enclosed in double quotation marks ("), spaces are allowed in the string. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

This command applies to DHCP servers. When allocating IP addresses to the client, the DHCP server also specifies domain names for clients. Run the **domain-name** command on the DHCP server to specify a domain name. When allocating IP addresses to clients, the DHCP server also sends the domain names to the clients.

To configure a domain name for an interface address pool, run the dhcp server domain-name (interface view) command.

Example
-------

# In the IP address pool view, configure the domain name suffix as example.com.
```
<HUAWEI> system-view
[~HUAWEI] ip pool test
[*HUAWEI-ip-pool-test] domain-name example.com

```