Configuring Track BFD for IPv6 IS-IS
====================================

Configuring Track BFD for IPv6 IS-IS

#### Context

Track BFD allows you to manually bind an IS-IS interface to a link-bundle BFD session by specifying a session name to rapidly detect link faults.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD.
   
   
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
5. Set a NET.
   
   
   ```
   [network-entity](cmdqueryname=network-entity) net-addr
   ```
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Create an interface.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
8. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Create a BFD for link-bundle session to monitor an Eth-Trunk link, and enter the BFD session view.
   
   
   ```
   [bfd](cmdqueryname=bfd) session-name bind link-bundle compatible-mode peer-ipv6 ipv6-address [ vpn-instance vpn-name ] interface { interface-name | interface-type interface-number } source-ipv6 ipv6-address
   ```
10. Enter the interface view.
    
    
    ```
    [interface](cmdqueryname=interface) interface-type interface-number
    ```
11. Enable IPv6.
    
    
    ```
    [ipv6 enable](cmdqueryname=ipv6+enable)
    ```
12. Enable IS-IS on the interface.
    
    
    ```
    [isis ipv6 enable](cmdqueryname=isis+ipv6+enable) [ process-id ]
    ```
13. Enable Track BFD on the interface.
    
    
    ```
    [isis ipv6 bfd track session-name](cmdqueryname=isis+ipv6+bfd+track+session-name) bfd-session-name
    ```
14. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```