Mapping the UNK Clock Source to an SSM Quality Level
====================================================

Mapping the UNK Clock Source to an SSM Quality Level

#### Context

UNK specifies that the SSM quality level of a clock source is unknown. When clock source selection is enabled based on the SSM quality level, a UNK clock source cannot participate in clock source selection. To allow a UNK clock source to participate in clock source selection, you must map a valid SSM quality level for the UNK clock source.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Map the UNK clock source to an SSM quality level.
   
   
   ```
   [clock map unk](cmdqueryname=clock+map+unk) { dnu | prc | sec | ssua | ssub }
   ```
   
   
   
   By default, no SSM quality level is mapped to the UNK clock source.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```