service restconf
================

service restconf

Function
--------



The **service restconf** command creates the Service-Restconf view and displays it, or displays the Service-Restconf view that has been created.

The **undo service restconf** command deletes the Service-Restconf view and all configurations in this view.



By default, the Service-Restconf view is not created.


Format
------

**service restconf**

**undo service restconf**


Parameters
----------

None

Views
-----

HTTP view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Before you perform HTTP configurations, run the **service restconf** command to enter the Service-Restconf view.


Example
-------

# Display the Service-Restconf view.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] service restconf

```