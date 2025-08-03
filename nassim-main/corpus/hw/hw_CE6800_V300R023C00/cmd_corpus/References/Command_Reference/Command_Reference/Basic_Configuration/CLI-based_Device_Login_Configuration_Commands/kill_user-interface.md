kill user-interface
===================

kill user-interface

Function
--------



The **kill user-interface** command frees a particular user interface.




Format
------

**kill user-interface** { *ui-number* | { { **console** | **vty** | **nca** | **rpc** } *ui-number1* | *ui-name* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ui-number* | Specifies the absolute number of a user interface. | It is an integer data type. The port number range is from 0 to 164. |
| **console** | Disconnects from the user interface of the console port. | - |
| **vty** | Disconnects an interface from the VTY user interface. | - |
| **nca** | Disconnects an interface from the NETCONF user interface. | - |
| **rpc** | Disconnects an interface from the RPC user interface. | - |
| *ui-number1* | Specifies the relative user interface ID. The relative user interface ID is based on the ui-type that is configured. | * If the ui-type is console, the value of <ui-number1> is 0. * If the ui-type is vty, the value of <ui-number1> is 0 to 20. * If the ui-type is nca, the value of <ui-number1> is 0 to 19. |
| *ui-name* | Display the information of the interface. | The value is a string ranging from 1 to 11. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



By executing this command you can free a particular user interface.




Example
-------

# Tear down the connection with console user interface Console 0.
```
<HUAWEI> kill user-interface console 0

```

# Tear down the connection with VTY user interface VTY 0.
```
<HUAWEI> kill user-interface vty 0

```