reset aaa statistics access-type-authenreq
==========================================

reset aaa statistics access-type-authenreq

Function
--------



The **reset aaa statistics access-type-authenreq** command clears the number of requesting for authentication.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**reset aaa statistics access-type-authenreq**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When users send authentication requests, the device collects statistics on the number of initiating authentications.To clear the number of requesting for authentication, run the **reset aaa statistics access-type-authenreq** command.


Example
-------

# Clear the number of requesting for authentication.
```
<HUAWEI> reset aaa statistics access-type-authenreq

```