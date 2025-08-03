reset ip pool
=============

reset ip pool

Function
--------

The **reset ip pool** command resets the IP address pool configured on the device.



Format
------

**reset ip pool** { **interface** *interface-pool-name* | **name** *ip-pool-name* } { *start-ip-address* [ *end-ip-address* ] | **all** | **conflict** | **expired** | **used** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-pool-name* | Specifies the name of the interface address pool to be reset, which is represented by the type and number of an interface. | The value is a string of 1 to 64 case-insensitive characters without spaces. It can contain digits, letters, and special characters underscores (\_), hyphens (-), and periods (.). It cannot be set to - or --. |
| **name** *ip-pool-name* | Specifies the name of the global address pool to be reset. | The value is a string of 1 to 64 case-insensitive characters without spaces. It can contain digits, letters, and special characters underscores (\_), hyphens (-), and periods (.). It cannot be set to - or --. |
| *start-ip-address* | Specifies the start IP address of the IP address pool to be reset. | The value is in dotted decimal notation. |
| *end-ip-address* | Specifies the end IP address of the IP address pool to be reset. | The value is in dotted decimal notation. |
| **all** | Indicates that all the IP addresses need to be reset. | - |
| **conflict** | Indicates that the conflicting IP addresses need to be reset. | - |
| **expired** | Indicates that the expired IP addresses need to be reset. | - |
| **used** | Indicates that the used IP addresses need to be reset. | - |




Views
-----

User view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The **reset ip pool** command resets the IP addresses that cannot be released in an IP address pool. If an IP address conflict occurs because two clients use the same IP address, run the **reset ip pool** command to reset the specified IP address pool.

**Follow-up Procedure**

After the address pool is set to idle, the client can obtain an IP address from the global address pool.

**Precautions**

If a user's IPv6 address is within the IPv6 address range specified when this command is run, the user cannot continue to use the IPv6 address after this command is run, and needs to send an IPv6 address application request again.

The address pool status cannot be restored after this command is run. Therefore, exercise caution when deciding to run this command.If an IP address is bound to a MAC address in an address pool, the static binding still exists after the
**reset ip pool** command is run.

Example
-------

# Reset the conflicting IP addresses in the IP address pool mypool.
```
<HUAWEI> reset ip pool name mypool conflict

```