(Optional) Configuring MAC Address Check for ND
===============================================

(Optional)_Configuring_MAC_Address_Check_for_ND

#### Context

To enable MAC address check for ND, run the [**ipv6 nd mac-check enable**](cmdqueryname=ipv6+nd+mac-check+enable) command. After the command is run, the system proactively checks source MAC address consistency to improve network reliability.

The system checks source MAC address consistency for four different types of ICMPv6 messages.

* NS: The system checks whether the source MAC address is the same as the MAC address in the Source Link-Layer Address (SLLA) option. If not, the NS message is discarded.
* NA: The system checks whether the source MAC address is the same as the MAC address in the Target Link-layer Address (TLLA) option. If not, the NA message is discarded.
* RS: The system checks whether the source MAC address is the same as the MAC address in the SLLA. If not, the RS message is discarded.
* RA: The system checks whether the source MAC address is the same as the MAC address in the SLLA. If not, the RA message is discarded.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**ipv6 nd mac-check enable**](cmdqueryname=ipv6+nd+mac-check+enable)
   
   MAC address check for ND is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.