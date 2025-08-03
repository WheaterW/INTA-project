Configuring Parameters Carried in RA Messages
=============================================

An RA message carries the hop limit, prefix option, neighbor reachable time, and lifetime.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 nd hop-limit**](cmdqueryname=ipv6+nd+hop-limit) *limit*
   
   
   
   A hop limit is configured for RA messages.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled.
5. Run [**ipv6 nd ra prefix**](cmdqueryname=ipv6+nd+ra+prefix) **default** **no-advertise**
   
   
   
   The device is configured not to include the default address prefix generated based on an interface IPv6 address in an RA message.
6. Run [**ipv6 nd ra prefix**](cmdqueryname=ipv6+nd+ra+prefix) *ipv6-address* *prefix-length* *valid-lifetime* **preferred-lifetime** [ **no-autoconfig** ] [ **off-link** ]
   
   
   
   An address prefix is configured for an RA message.
   
   
   
   The address prefix configured using the [**ipv6 nd ra prefix**](cmdqueryname=ipv6+nd+ra+prefix) command has a higher priority than the default address prefix. Given that an RA message can carry a maximum of 17 address prefixes, the default address prefix will not be carried if 17 address prefixes have been manually configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If stateless address autoconfiguration is used, you must specify the prefix length as 64. Otherwise, the address does not take effect, and RA messages will be discarded.
7. Run [**ipv6 nd autoconfig managed-address-flag**](cmdqueryname=ipv6+nd+autoconfig+managed-address-flag)
   
   
   
   The managed address configuration flag of stateful address autoconfiguration in an RA message is configured.
8. Run [**ipv6 nd autoconfig other-flag**](cmdqueryname=ipv6+nd+autoconfig+other-flag)
   
   
   
   The other configuration flag of stateful address autoconfiguration in an RA message is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the managed address configuration flag is set to 1 in an RA message, the other configuration flag must also be set to 1.
9. Run [**ipv6 nd nud reachable-time**](cmdqueryname=ipv6+nd+nud+reachable-time) *value*
   
   
   
   A neighbor reachable time is configured.
10. Run [**ipv6 nd ra router-lifetime**](cmdqueryname=ipv6+nd+ra+router-lifetime) *ra-lifetime*
    
    
    
    A lifetime is configured for an RA message.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The advertisement interval of an RA message configured using the [**ipv6 nd ra**](cmdqueryname=ipv6+nd+ra) command must be less than or equal to its lifetime.
11. Run [**ipv6 nd ra advertised-mtu disable**](cmdqueryname=ipv6+nd+ra+advertised-mtu+disable)
    
    
    
    The device is configured not to include the MTU option in an RA message.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.