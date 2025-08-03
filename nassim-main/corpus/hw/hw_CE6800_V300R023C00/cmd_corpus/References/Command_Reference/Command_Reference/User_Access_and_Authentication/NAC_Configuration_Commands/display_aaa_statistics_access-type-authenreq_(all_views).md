display aaa statistics access-type-authenreq (all views)
========================================================

display aaa statistics access-type-authenreq (all views)

Function
--------



The **display aaa statistics access-type-authenreq** command displays the number of NAC authentication requests.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display aaa statistics access-type-authenreq**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When users send authentication requests, the device collects statistics on the number of NAC authentication requests.To view the number of NAC authentication requests, run the **display aaa statistics access-type-authenreq** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the number of NAC authentication requests.
```
<HUAWEI> display aaa statistics access-type-authenreq
dot1x   authentication request     :0

```

**Table 1** Description of the **display aaa statistics access-type-authenreq (all views)** command output
| Item | Description |
| --- | --- |
| dot1x authentication request | Number of 802.1X authentication requests. |