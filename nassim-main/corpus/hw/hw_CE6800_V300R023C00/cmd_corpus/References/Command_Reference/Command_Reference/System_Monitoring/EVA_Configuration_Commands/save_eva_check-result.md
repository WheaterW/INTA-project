save eva check-result
=====================

save eva check-result

Function
--------



The **save eva check-result** command immediately writes the EVA script check result and collected data in the buffer to the eva folder in the storage medium.




Format
------

**save eva check-result**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

By default, the system saves the EVA script check result and collected data in the buffer to the eva folder in the storage medium only when the size of the buffer data exceeds 2 MB or the number of the result and data records exceeds 50, or the system saves the buffer data every 30 minutes.To write the buffer data to the storage medium immediately, run this command.


Example
-------

# Save the EVA script check result and collected data in the buffer to the eva folder in the storage medium.
```
<HUAWEI> save eva check-result

```