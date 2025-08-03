Configuring Track BFD for IPv6 IS-IS
====================================

Track BFD allows you to manually bind an IS-IS interface to a link-bundle BFD session by specifying a session name. This function can quickly detect link faults and prevent BFD session faults caused by faults of the board on which a trunk member interface resides.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
5. Run [**network-entity**](cmdqueryname=network-entity) *net-addr*
   
   
   
   A network entity title (NET) is configured.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   An interface is created.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**bfd**](cmdqueryname=bfd) *session-name* **bind** **link-bundle** [ **compatible-mode** ] **peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **interface** *interface-type* *interface-number* **source-ipv6** *ipv6-address*
   
   
   
   A BFD for link-bundle session is created to detect Eth-Trunk faults, and the BFD session view is displayed.
10. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
    
    
    
    The interface view is displayed.
11. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
    
    
    
    IPv6 is enabled.
12. Run [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable) [ *process-id* ]
    
    
    
    IS-IS is enabled on the interface.
13. Run [**isis ipv6 bfd track session-name**](cmdqueryname=isis+ipv6+bfd+track+session-name) *bfd-session-name*
    
    
    
    Track BFD is enabled on the interface.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.