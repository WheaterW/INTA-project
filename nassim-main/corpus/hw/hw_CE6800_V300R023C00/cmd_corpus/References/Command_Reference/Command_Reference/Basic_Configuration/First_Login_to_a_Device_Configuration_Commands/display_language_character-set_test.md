display language character-set test
===================================

display language character-set test

Function
--------



The **display language character-set test** command displays whether the character set on a terminal is the same as that configured in the system.




Format
------

**display language character-set test**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

To check whether the character set on a terminal is the same as that configured in the system, run the display language character-set test command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display character set information to check whether the character set on a terminal is the same as that configured in the system.
```
<HUAWEI> display language character-set test
-------------------------------------------------
No.  Current-Set    Character-Set    Hello-String
-------------------------------------------------
1    *              UTF-8                   
-------------------------------------------------

```

**Table 1** Description of the **display language character-set test** command output
| Item | Description |
| --- | --- |
| No. | Item number. |
| Current-Set | The asterisk (\*) indicates the current character set indicator. |
| Character-Set | List of character sets supported by the system. Currently, the system supports only UTF-8. |
| Hello-String | If "chinese character" is displayed in this field, Chinese characters are supported, and the character set on the terminal is the same as that configured in the system. |