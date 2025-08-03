(Optional) Configuring Ethernet Interfaces to Retain the Original Outer TPID EtherType Value in Received QinQ Packets
=====================================================================================================================

All QinQ-enabled devices use 0x8100 as the inner TPID EtherType value. However, different devices use different outer TPID EtherType values. Upon receiving QinQ packets whose outer TPID EtherType value is not 0x8100 from a non-Huawei device, a Huawei device changes the value to 0x8100 by default. This may result in traffic interruptions. To prevent this issue, configure Ethernet interfaces on the Huawei device to retain the original outer TPID EtherType value in received QinQ packets.

#### Context

Perform the following steps on a device on which QinQ tunneling is to be configured:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**qinq protocol transport enable**](cmdqueryname=qinq+protocol+transport+enable)
   
   
   
   Ethernet interfaces are configured to retain the original outer TPID EtherType value in received QinQ packets instead of changing the value to 0x8100.