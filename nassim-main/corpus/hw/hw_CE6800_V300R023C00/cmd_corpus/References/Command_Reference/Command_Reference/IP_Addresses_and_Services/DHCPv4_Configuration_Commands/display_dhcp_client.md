display dhcp client
===================

display dhcp client

Function
--------



The **display dhcp client** command displays DHCP/BOOTP client lease information.




Format
------

**display dhcp client** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays DHCP/BOOTP client lease information on a specified interface. | - |
| *interface-name* | Displays DHCP/BOOTP client lease information on a specified interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When a device functions as the DHCP/BOOTP client, this command displays DHCP/BOOTP client lease information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display DHCP client lease information.
```
<HUAWEI> display dhcp client
DHCP client lease information on interface Vlanif119 :                           
 Current machine state         : Bound                                          
 Internet address assigned via : DHCP                                           
 Physical address              : 00e0-fc12-3456                                 
 IP address                    : 192.168.119.254                                
 Subnet mask                   : 255.255.255.0                                  
 Gateway ip address            : 192.168.119.1                                  
                                 192.168.119.3                                  
                                 192.168.119.2                                  
 DHCP server                   : 192.168.119.1                                  
 Lease obtained at             : 2008-10-01 04:35:10                            
 Lease expires at              : 2008-10-01 04:36:10                            
 Lease renews at               : 2008-10-01 04:35:40                            
 Lease rebinds at              : 2008-10-01 04:36:03                            
 Classless static route        : 192.168.0.0/16 via 192.168.119.1               
                                 10.10.0.0/16 via 192.168.119.2       
 Host name                     : client  
 Request option list           : 1 3 6 15 28 33 44 121 184       
 Class identifier              : huawei  
 Client identifier             : 00e0-fc12-3456

```

**Table 1** Description of the **display dhcp client** command output
| Item | Description |
| --- | --- |
| DHCP client lease information on interface | DHCP client lease information on the interface. |
| DHCP server | DHCP server address (no value for a BOOTP client). |
| Current machine state | Current device status. |
| Internet address assigned via | IP address obtained using DHCP or BOOTP. |
| Physical address | Device MAC address. |
| IP address | Device IP address. |
| Subnet mask | Mask of the device IP address. |
| Gateway ip address | Gateway address of the DHCP or BOOTP server. |
| Lease obtained at | Time when the DHCP client obtains an IP address. |
| Lease expires at | Time the lease expires (no value for a BOOTP client). |
| Lease renews at | Lease renewal time, which is 50% of the total lease (not displayed in BOOTP). |
| Lease rebinds at | Rebinding time, 87.5% of the lease (not displayed for BOOTP). |
| Classless static route | Classless static route. |
| Host name | Information about Option 12, which is the host name of the client. |
| Request option list | Information about Option 55, which is the request option list of the client. |
| Class identifier | Information about Option 60, which is the vendor type identifier. |
| Client identifier | Information about Option 61, which is the client identifier. |