Creating an OSPFv3 Area
=======================

Creating an OSPFv3 Area

#### Context

OSPFv3 divides an AS into different areas to prevent the LSDB, which route calculation depends on, from growing too large.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Enter the OSPFv3 area view.
   
   
   ```
   [area](cmdqueryname=area) area-id
   ```
   
   The specified area ID can be a decimal integer or in the IPv4 address format. Regardless of the specified format, the area ID is displayed as an IPv4 address.
4. (Optional) Configure a description for the OSPFv3 area.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   
   To easily identify the OSPFv3 area, you can configure a description for it.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```