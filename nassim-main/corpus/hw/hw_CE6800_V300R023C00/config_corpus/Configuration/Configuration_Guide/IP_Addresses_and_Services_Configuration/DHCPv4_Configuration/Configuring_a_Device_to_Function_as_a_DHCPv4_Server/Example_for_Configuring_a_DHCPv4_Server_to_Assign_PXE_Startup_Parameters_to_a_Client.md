Example for Configuring a DHCPv4 Server to Assign PXE Startup Parameters to a Client
====================================================================================

Example for Configuring a DHCPv4 Server to Assign PXE Startup Parameters to a Client

#### Networking Requirements

The Preboot Execution Environment (PXE) allows a client to boot an operating system using a startup file downloaded from a TFTP server.

On the network shown in [Figure 1](#EN-US_TASK_0000001513046146__fig_dc_esap_cfg_001307), a PXE client and a DHCPv4 server reside on the same network segment. The PXE client needs to obtain an IP address, TFTP server address (Option 66), and startup file name (Option 67) from the DHCPv4 server.

**Figure 1** Network diagram of configuring a DHCPv4 server to assign PXE startup parameters to a client![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](../images/en-us_image_0000001564126265.png)

#### Procedure

1. Enable DHCP on DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] dhcp enable
   ```
2. Create VLAN 10 and add 100GE 1/0/1 to it.
   
   
   ```
   [*DeviceA] vlan 10
   [*DeviceA-vlan10] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   ```
3. Configure an IP address for a VLANIF interface.
   
   
   ```
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 192.168.1.1 24
   ```
4. Configure the DHCPv4 server function on VLANIF 10.
   
   
   ```
   [*DeviceA-Vlanif10] dhcp select interface
   ```
5. Configure Option 66 and Option 67.
   
   
   ```
   [*DeviceA-Vlanif10] dhcp server option 66 ip-address 192.168.2.1
   [*DeviceA-Vlanif10] dhcp server option 67 ascii boot\x64\wdsnbp.com
   [*DeviceA-Vlanif10] dhcp server next-server 192.168.2.1
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, the TFTP server and PXE client are on different network segments. Therefore, you need to run the **dhcp server next-server** command to specify the IP address of the TFTP server from which the PXE client downloads the startup file.
   
   If the TFTP server and PXE client are on the same network segment, run the **dhcp server excluded-ip-address** command to exclude the TFTP server address from the address pool.
6. Verify the configuration.
   
   
   
   # Run the [**display this**](cmdqueryname=display+this) command on VLANIF 10 of DeviceA to check the DHCPv4 server configuration.
   
   ```
   [~DeviceA-Vlanif10] display this  
   #                                                                               
   interface Vlanif10                                                              
    ipv6 enable                                                                    
    ip address 192.168.1.1 255.255.255.0                                           
    ipv6 address auto link-local                                                   
    dhcp select interface                                                          
    dhcp server next-server 192.168.2.1                                            
    dhcp server option 66 ip-address 192.168.2.1                                   
    dhcp server option 67 ascii boot\x64\wdsnbp.com                                                                          
   #                                                                               
   return   
   ```
   
   # Run the [**display ip pool interface vlanif10**](cmdqueryname=display+ip+pool+interface+vlanif10) command on VLANIF 10 of DeviceA to check the option configuration and the allocation of addresses in the interface address pool.
   
   ```
   [~DeviceA-Vlanif10] display ip pool interface vlanif10
     Pool-name        : Vlanif10                                                   
     Pool-No          : 0                                                          
     Lease            : 1 Days 0 Hours 0 Minutes
     Next-server      : 192.168.2.1                                       
     Domain-name      : -                                                          
     Option-code      : 66                                                         
       Option-subcode : --                                                         
        Option-type   : ip-address                                                
       Option-value   : 192.168.2.1                                                
     Option-code      : 67                                                        
       Option-subcode : --                                                         
        Option-type   : ascii                                                     
       Option-value   : boot\x64\wdsnbp.com                                        
     DNS-server0      : -                                                          
     NBNS-server0     : -                                                          
     Netbios-type     : -                                                          
     Position         : Interface                                                  
     Status           : Unlocked                                                   
     Gateway-0        : 192.168.1.1                                                
     Network          : 192.168.1.0                                                
     Mask             : 255.255.255.0                                              
     VPN instance     : --                                                         
     Logging          : Disable                                                    
     Conflicted address recycle interval: -                                        
     Address Statistic: Total       :253       Used        :1                      
                        Idle        :251       Expired     :0                      
                        Conflict    :0         Disabled    :1
                           
   
    -------------------------------------------------------------------------------                                                                      
     Network section                                                               
            Start           End       Total    Used Idle(Expired) Conflict Disabled
    -------------------------------------------------------------------------------                                                                          
        192.168.1.1   192.168.1.254     253       1        251(0)       0     1    
    -------------------------------------------------------------------------------                                  
   ```

#### Configuration Scripts

# DeviceA

```
#
sysname DeviceA
#
vlan batch 10
#
dhcp enable
#
interface Vlanif10                                                            
 ip address 192.168.1.1 255.255.255.0
 dhcp select interface
 dhcp server next-server 192.168.2.1
 dhcp server option 66 ip-address 192.168.2.1
 dhcp server option 67 ascii boot\x64\wdsnbp.com                                                            
#                                                                               
interface 100GE1/0/1                                                         
 port link-type trunk                                                          
 port trunk allow-pass vlan 10
#
return
```