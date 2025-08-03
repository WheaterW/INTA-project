Configuring a DSCP Value for Telnet/SSH Packets
===============================================

This section describes how to configure a DSCP value for Telnet/SSH packets.

#### Context

A device can send multiple types of protocol packets, such as NETCONF, Telnet, and SSH packets. You can run the [**host-packet type**](cmdqueryname=host-packet+type) command to uniformly configure a DSCP value for the protocol packets. If a large number of protocol packets with the same DSCP value are sent, network congestion may occur. To address this issue, configure different DSCP values for the packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run one or more of the following commands based on the service type and protocol packet type:
   1. Run [**ssh client dscp**](cmdqueryname=ssh+client+dscp) *value*
      
      
      
      A DSCP value is configured for the SSH packets sent by a client.
   2. Run [**telnet client dscp**](cmdqueryname=telnet+client+dscp) *value*
      
      
      
      A DSCP value is configured for the Telnet packets sent by a client.
   3. Run [**ssh server dscp**](cmdqueryname=ssh+server+dscp) *value*
      
      
      
      A DSCP value is configured for the SSH packets sent by a server.
   4. Run [**telnet server dscp**](cmdqueryname=telnet+server+dscp) *value*
      
      
      
      A DSCP value is configured for the Telnet packets sent by a server.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Example

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the configured DSCP value.

```
<HUAWEI> system-view
```
```
[~HUAWEI] display current-configuration include-default | include dscp
```
```
Info: It will take a long time if the content you search is too much or the string you input is too long, you can press CTRL_C to break.
 telnet server dscp 10
 telnet client dscp 10
 ssh server dscp 10 
 ssh client dscp 10
```