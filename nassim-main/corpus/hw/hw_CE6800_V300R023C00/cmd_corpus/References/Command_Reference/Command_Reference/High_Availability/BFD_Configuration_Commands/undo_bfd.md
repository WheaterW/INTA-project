undo bfd
========

undo bfd

Function
--------



The **undo bfd** command deletes a specified BFD session and cancels the binding between a BFD session and a peer IP address.



By default, the binding between a BFD session and a peer address is not deleted.


Format
------

**undo bfd** *sessname-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sessname-value* | Specifies the name of a BFD session. | The value is a string of 1 to 64 case-insensitive characters without spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The undo bfd command deletes a specified BFD session and cancels the binding between a BFD session and a peer IP address.


Example
-------

# Deletes a specified BFD session and cancels the binding between a BFD session and a peer IP address.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ip address 10.1.10.1 24
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd test bind peer-ip 10.1.1.1 interface 100GE 1/0/1 one-arm-echo
[*HUAWEI-bfd-session-test] quit
[*HUAWEI] undo bfd test

```