radius-server framed-ip-address
===============================

radius-server framed-ip-address

Function
--------



The **radius-server framed-ip-address no-user-ip enable** command enables the device to encapsulate the RADIUS attribute Framed-IP-Address into a RADIUS authentication request packet when the RADIUS authentication request packet sent by a user does not carry the user IP address.

The **undo radius-server framed-ip-address no-user-ip enable** command disables the device from encapsulating the RADIUS attribute Framed-IP-Address into a RADIUS authentication request packet when the RADIUS authentication request packet sent by a user does not carry the user IP address.



By default, the device does not encapsulate the RADIUS attribute Framed-IP-Address into a RADIUS authentication request packet when the RADIUS authentication request packet sent by a user does not carry the user IP address.


Format
------

**radius-server framed-ip-address no-user-ip enable**

**undo radius-server framed-ip-address no-user-ip enable**


Parameters
----------

None

Views
-----

RADIUS server template view,Vsys radius server template view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



If the RADIUS server connected to the device requires that the received RADIUS authentication request packet contain the RADIUS attribute Framed-IP-Address, run the **radius-server framed-ip-address no-user-ip enable** command. Then the device uses the IP address 0.0.0.0 to encapsulate the RADIUS attribute Framed-IP-Address when receiving the RADIUS authentication request packets that do not contain the user IP address.




Example
-------

# Enable the device to encapsulate the RADIUS attribute Framed-IP-Address into a RADIUS authentication request packet when the RADIUS authentication request packet sent by a user does not carry the user IP address.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template template1
[*HUAWEI-radius-template1] radius-server framed-ip-address no-user-ip enable

```