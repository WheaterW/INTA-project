display diffserv domain
=======================

display diffserv domain

Function
--------



The **display diffserv domain** command displays the DiffServ domain configuration.




Format
------

**display diffserv domain** [ *ds-domain-name* | **brief** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ds-domain-name* | Displays the detailed configuration of a specified DiffServ domain. | The value must be the name of an existing DiffServ domain on the device. |
| **brief** | Displays summary configurations of all DiffServ domains. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After creating a DiffServ domain and configuring the mappings in the DiffServ domain, you can use the display diffserv domain command to view the configuration of the DiffServ domain.

**Precautions**

If parameters brief and ds-domain-name are not specified, detailed configurations of all DiffServ domains are displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the detailed configuration of DiffServ domain d1.
```
<HUAWEI> display diffserv domain d1
Diffserv domain name:d1                                                         
 8021p-inbound 0 phb be green
 8021p-inbound 1 phb af1 green
 8021p-inbound 2 phb af2 green     
 8021p-inbound 3 phb af3 green  
 8021p-inbound 4 phb af4 green
 8021p-inbound 5 phb ef green
 8021p-inbound 6 phb cs6 green                                     
 8021p-inbound 7 phb cs7 green                    
 8021p-outbound be green map 0  
 8021p-outbound be yellow map 0
 8021p-outbound be red map 0
 8021p-outbound af1 green map 1
 8021p-outbound af1 yellow map 1 
 8021p-outbound af1 red map 1 
 8021p-outbound af2 green map 2
 8021p-outbound af2 yellow map 2 
 8021p-outbound af2 red map 2  
 8021p-outbound af3 green map 3 
 8021p-outbound af3 yellow map 3 
 8021p-outbound af3 red map 3  
 8021p-outbound af4 green map 4   
 8021p-outbound af4 yellow map 4  
 8021p-outbound af4 red map 4   
 8021p-outbound ef green map 5  
 8021p-outbound ef yellow map 5  
 8021p-outbound ef red map 5    
 8021p-outbound cs6 green map 6   
 8021p-outbound cs6 yellow map 6  
 8021p-outbound cs6 red map 6 
 8021p-outbound cs7 green map 7 
 8021p-outbound cs7 yellow map 7 
 8021p-outbound cs7 red map 7  
 ip-dscp-inbound 0 phb be green   
 ip-dscp-inbound 1 phb be green 
 ip-dscp-inbound 2 phb be green  
 ip-dscp-inbound 3 phb be green
 ip-dscp-inbound 4 phb be green  
 ip-dscp-inbound 5 phb be green
 ip-dscp-inbound 6 phb be green 
 ip-dscp-inbound 7 phb be green 
 ip-dscp-inbound 8 phb af1 green 
 ip-dscp-inbound 9 phb af1 green 
 ip-dscp-inbound 10 phb af1 green 
 ip-dscp-inbound 11 phb af1 green 
 ip-dscp-inbound 12 phb af1 yellow 
 ip-dscp-inbound 13 phb af1 green  
 ip-dscp-inbound 14 phb af1 red   
 ip-dscp-inbound 15 phb af1 green 
 ip-dscp-inbound 16 phb af2 green 
 ip-dscp-inbound 17 phb af2 green  
 ip-dscp-inbound 18 phb af2 green 
 ip-dscp-inbound 19 phb af2 green 
 ip-dscp-inbound 20 phb af2 yellow 
 ip-dscp-inbound 21 phb af2 green  
 ip-dscp-inbound 22 phb af2 red    
 ip-dscp-inbound 23 phb af2 green  
 ip-dscp-inbound 24 phb af3 green  
 ip-dscp-inbound 25 phb af3 green  
 ip-dscp-inbound 26 phb af3 green 
 ip-dscp-inbound 27 phb af3 green      
 ip-dscp-inbound 28 phb af3 yellow 
 ip-dscp-inbound 29 phb af3 green  
 ip-dscp-inbound 30 phb af3 red 
 ip-dscp-inbound 31 phb af3 green 
 ip-dscp-inbound 32 phb af4 green 
 ip-dscp-inbound 33 phb af4 green 
 ip-dscp-inbound 34 phb af4 green 
 ip-dscp-inbound 35 phb af4 green  
 ip-dscp-inbound 36 phb af4 yellow  
 ip-dscp-inbound 37 phb af4 green 
 ip-dscp-inbound 38 phb af4 red   
 ip-dscp-inbound 39 phb af4 green          
 ip-dscp-inbound 40 phb ef green   
 ip-dscp-inbound 41 phb ef green  
 ip-dscp-inbound 42 phb ef green  
 ip-dscp-inbound 43 phb ef green  
 ip-dscp-inbound 44 phb ef green  
 ip-dscp-inbound 45 phb ef green  
 ip-dscp-inbound 46 phb ef green   
 ip-dscp-inbound 47 phb ef green  
 ip-dscp-inbound 48 phb cs6 green  
 ip-dscp-inbound 49 phb cs6 green  
 ip-dscp-inbound 50 phb cs6 green  
 ip-dscp-inbound 51 phb cs6 green  
 ip-dscp-inbound 52 phb cs6 green  
 ip-dscp-inbound 53 phb cs6 green  
 ip-dscp-inbound 54 phb cs6 green    
 ip-dscp-inbound 55 phb cs6 green  
 ip-dscp-inbound 56 phb cs7 green     
 ip-dscp-inbound 57 phb cs7 green    
 ip-dscp-inbound 58 phb cs7 green  
 ip-dscp-inbound 59 phb cs7 green  
 ip-dscp-inbound 60 phb cs7 green 
 ip-dscp-inbound 61 phb cs7 green   
 ip-dscp-inbound 62 phb cs7 green    
 ip-dscp-inbound 63 phb cs7 green  
 ip-dscp-outbound be green map 0 
 ip-dscp-outbound be yellow map 0  
 ip-dscp-outbound be red map 0    
 ip-dscp-outbound af1 green map 10 
 ip-dscp-outbound af1 yellow map 12 
 ip-dscp-outbound af1 red map 14 
 ip-dscp-outbound af2 green map 18    
 ip-dscp-outbound af2 yellow map 20  
 ip-dscp-outbound af2 red map 22  
 ip-dscp-outbound af3 green map 26 
 ip-dscp-outbound af3 yellow map 28 
 ip-dscp-outbound af3 red map 30  
 ip-dscp-outbound af4 green map 34 
 ip-dscp-outbound af4 yellow map 36
 ip-dscp-outbound af4 red map 38  
 ip-dscp-outbound ef green map 46 
 ip-dscp-outbound ef yellow map 46 
 ip-dscp-outbound ef red map 46 
 ip-dscp-outbound cs6 green map 48 
 ip-dscp-outbound cs6 yellow map 48 
 ip-dscp-outbound cs6 red map 48  
 ip-dscp-outbound cs7 green map 56 
 ip-dscp-outbound cs7 yellow map 56 
 ip-dscp-outbound cs7 red map 56

```

# Displays summary configurations of all DiffServ domains.
```
<HUAWEI> display diffserv domain brief
Diffserv Domain Maximum: 8                                                      
Total: 2                                                                        
 ---------------------------------------------                                  
   index       DS name                                                          
 ---------------------------------------------                                  
     0         default                                                          
     1         d1                                                              
 ---------------------------------------------

```

**Table 1** Description of the **display diffserv domain** command output
| Item | Description |
| --- | --- |
| Diffserv domain name | Name of the DiffServ domain. To create a DiffServ domain, run the diffserv domain command. |
| Diffserv Domain Maximum | Maximum number of DiffServ domains supported by the device. |
| index | Index of the DiffServ domain. |
| DS name | Name of the DiffServ domain. To create a DiffServ domain, run the diffserv domain command. |
| Total | Number of created DiffServ domains on the device. |