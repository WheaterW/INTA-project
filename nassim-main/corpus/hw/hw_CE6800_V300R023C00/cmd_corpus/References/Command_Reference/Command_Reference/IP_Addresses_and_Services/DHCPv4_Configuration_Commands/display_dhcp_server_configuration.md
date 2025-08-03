display dhcp server configuration
=================================

display dhcp server configuration

Function
--------



The **display dhcp server configuration** command displays configurations about a DHCP server.




Format
------

**display dhcp server configuration**


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

When the device functions as a DHCP server, you can run the **display dhcp server configuration** command to display configurations about the DHCP server.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configurations about a DHCP server.
```
<HUAWEI> display dhcp server configuration
  DHCP server global running information :                                                                                          
  DHCP server bootp                : Enable (default)                                                                              
  DHCP server bootp automatic      : Enable (default)                                                                            
  DHCP server ping packet          : 2       (default)                                                                              
  DHCP server ping timeout         : 500     (default)                                                                              
  DHCP server trust option82       : Enable  (default)                                                                              
  DHCP server force response       : Disable (default)                                                                                
                                                                                                                                    
  DHCP server running information for interface Vlanif10 :                                                                         
  DHCP server mode                 : Interface                                                                                      
                                                                                                                                    
  DHCP server running information for interface Vlanif20 :                                                                           
  DHCP server mode                 : Global

```

**Table 1** Description of the **display dhcp server configuration** command output
| Item | Description |
| --- | --- |
| DHCP server global running information | Global configurations about the DHCP server. |
| DHCP server bootp | Whether the DHCP server is enabled to respond to BOOTP requests. To configure this item, run the dhcp server bootp command. |
| DHCP server bootp automatic | Whether the DHCP server is enabled to dynamically allocate IP addresses to BOOTP clients. To configure this item, run the dhcp server bootp automatic command. |
| DHCP server ping packet | Maximum number of ping packets sent by the DHCP server. To configure this item, run the dhcp server ping command. |
| DHCP server ping timeout | Maximum response time of a ping packet sent by the DHCP server. To configure this item, run the dhcp server ping command. |
| DHCP server trust option82 | Whether the DHCP server is enabled to trust the Option82 field. To configure this item, run the dhcp server trust option82 command. |
| DHCP server force response | Whether the DHCP server is enabled to reply with DHCP NAK messages. To configure this item, run the dhcp server force response command. |
| DHCP server running information for interface | Configurations about the DHCP server on an interface. |
| DHCP server mode | DHCP server mode. The value can be:   * Interface: DHCP server based on an interface address pool. To configure this item, run the dhcp select interface command. * Global: DHCP server based on the global address pool. To configure this item, run the dhcp select global command. |