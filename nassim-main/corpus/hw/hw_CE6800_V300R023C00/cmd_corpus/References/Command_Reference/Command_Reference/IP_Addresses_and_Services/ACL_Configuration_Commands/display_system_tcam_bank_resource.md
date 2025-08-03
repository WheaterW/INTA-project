display system tcam bank resource
=================================

display system tcam bank resource

Function
--------



The **display system tcam bank resource** command displays the resource usage of each service.




Format
------

**display system tcam bank resource** [ **slot** *slot-id* [ **chip** *chip-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | The value is an integer. You can enter the question mark (?) and select the value as prompted. |
| **chip** *chip-id* | Specifies the ID of a chip. | The value is an integer. It must be the ID of an available chip. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to view the resource usage of each service. If you do not specify the slot parameter, the resource usage of each service on all cards is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the resource usage of each service in slot 1.
```
<HUAWEI> display system tcam bank resource slot 1
Slot: 1    Chip: 0                                                              
----------------------------------------------------------------------------------------------------------------------              
Service           BankId                 Entry     Entry     Entry     GroupId   Stage       ServiceName                            
Type                                     Size      Free      Used                                                                   
----------------------------------------------------------------------------------------------------------------------              
CPCAR             0-3                    320Bit    279       24        5         Ingress     Default Rule                           
                                                             3         5         Ingress     App-Session                            
                                                             101       5         Ingress     CPCAR CP                               
                                                             63        6         Ingress     BPDU Deny                              
                                                             30        6         Ingress     CPCAR PA                               
Free              4-63                                                                       --                                     
----------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display system tcam bank resource** command output
| Item | Description |
| --- | --- |
| Service Type | operation type. |
| BankId | Bank ID, which varies depending on switch models. |
| Entry Size | Bank size. |
| Entry Used | Number of used KB resources. |
| Entry Free | Number of remaining KB resources. |
| GroupId | Group ID. |
| Stage | Packet forwarding stage:   * Ingress: inbound direction. * Egress: outbound direction. |
| ServiceName | Name of a delivered service. If no service is delivered in a bank, this item is displayed as --. |
| Slot | Slot ID. |
| Chip | Chip ID. |