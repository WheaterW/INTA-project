(Optional) Configuring a BPDU MAC Address
=========================================

(Optional) Configuring a BPDU MAC Address

#### Context

The device does not forward BPDUs at Layer 2 by default. When proprietary protocol packets of devices from other vendors need to be processed as BPDUs, you can configure the MAC addresses of these packets as BPDU MAC addresses. In this way, the device discards these packets with BPDU MAC addresses.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a BPDU MAC address.
   
   
   ```
   [mac-address bpdu](cmdqueryname=mac-address+bpdu) mac-address [ mac-address-mask ]
   ```
   
   By default, the device has the following BPDU MAC addresses:
   
   * 0180-c200-008a ffff-ffff-ffff
   * 0180-c200-8585 ffff-ffff-ffff
   * 010f-e200-0001 ffff-ffff-ffff
   * 0100-0ccc-cccc ffff-ffff-ffff
   * 0180-c200-0000 ffff-ffff-ffff
   * 0180-c200-0001 ffff-ffff-ffff
   * 0180-c200-0002 ffff-ffff-ffff
   * 0180-c200-0003 ffff-ffff-ffff
   * 0180-c200-0004 ffff-ffff-ffff
   * 0180-c200-0005 ffff-ffff-ffff
   * 0180-c200-0006 ffff-ffff-ffff
   * 0180-c200-0007 ffff-ffff-ffff
   * 0180-c200-0008 ffff-ffff-ffff
   * 0180-c200-0009 ffff-ffff-ffff
   * 0180-c200-000a ffff-ffff-ffff
   * 0180-c200-000b ffff-ffff-ffff
   * 0180-c200-000c ffff-ffff-ffff
   * 0180-c200-000d ffff-ffff-ffff
   * 0180-c200-000e ffff-ffff-ffff
   * 0180-c200-000f ffff-ffff-ffff
   * 0180-c200-0010 ffff-ffff-ffff
   * 0180-c200-0011 ffff-ffff-ffff
   * 0180-c200-0012 ffff-ffff-ffff
   * 0180-c200-0013 ffff-ffff-ffff
   * 0180-c200-0016 ffff-ffff-ffff
   * 0180-c200-0017 ffff-ffff-ffff
   * 0180-c200-0018 ffff-ffff-ffff
   * 0180-c200-0019 ffff-ffff-ffff
   * 0180-c200-001a ffff-ffff-ffff
   * 0180-c200-001b ffff-ffff-ffff
   * 0180-c200-001c ffff-ffff-ffff
   * 0180-c200-001d ffff-ffff-ffff
   * 0180-c200-001e ffff-ffff-ffff
   * 0180-c200-001f ffff-ffff-ffff
   * 0180-c200-0020 ffff-ffff-ffe0
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```