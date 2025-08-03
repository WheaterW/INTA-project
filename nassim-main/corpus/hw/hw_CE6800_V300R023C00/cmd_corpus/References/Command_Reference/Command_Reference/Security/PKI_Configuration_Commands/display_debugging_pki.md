display debugging pki
=====================

display debugging pki

Function
--------



The **display debugging pki** command displays the enabled PKI debugging function.




Format
------

**display debugging pki**


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

To view the enabled PKI debugging function, run the **display debugging pki** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the enabled PKI debugging function.
```
<HUAWEI> debugging pki pki all
<HUAWEI> display debugging pki
pki pki information VsysID:0 debugging switch is on                              
pki pki timer VsysID:0 debugging switch is on                                   
pki pki event VsysID:0 debugging switch is on                                   
pki pki message VsysID:0 debugging switch is on                                 
pki pki error VsysID:0 debugging switch is on

```

**Table 1** Description of the **display debugging pki** command output
| Item | Description |
| --- | --- |
| pki information | PKI information. |
| pki timer | PKI timer. |
| pki event | PKI event. |
| pki message | PKI message. |
| pki error | PKI error. |