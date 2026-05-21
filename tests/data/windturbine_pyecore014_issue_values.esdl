<?xml version='1.0' encoding='UTF-8'?>
<esdl:WindTurbine xmlns:xmi="http://www.omg.org/XMI"
                  xmlns:esdl="http://www.tno.nl/esdl"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  type="WIND_AT_SEA" id="140255e6-d528-4bc6-be04-f51cae5229c9" height="160.0" rotorDiameter="270.0"
                  power="18000000.0" name="WindTurbine_1402" xmi:version="2.0">
    <port xsi:type="esdl:OutPort" name="Out" id="bf3d5d1d-4ae0-4119-a345-f51d8b102364"/>
    <powerCurveTable xsi:type="esdl:Table" name="Power curve table">
        <row xsi:type="esdl:TableRow">
            <value>3.0</value>
            <value>217.0</value>
        </row>
        <row xsi:type="esdl:TableRow" value="3.5 481.0"/>
        <row xsi:type="esdl:TableRow" value="4.0 863.0"/>
        <row xsi:type="esdl:TableRow" value="4.5 1343.0"/>
        <row xsi:type="esdl:TableRow" value="5.0 1928.0"/>
        <row xsi:type="esdl:TableRow" value="5.5 2623.0"/>
        <row xsi:type="esdl:TableRow" value="6.0 3439.0"/>
        <row xsi:type="esdl:TableRow" value="6.5 4391.0"/>
        <row xsi:type="esdl:TableRow" value="7.0 5499.0"/>
        <row xsi:type="esdl:TableRow" value="7.5 6775.0"/>
        <row xsi:type="esdl:TableRow" value="8.0 8232.0"/>
        <row xsi:type="esdl:TableRow" value="8.5 9869.0"/>
        <row xsi:type="esdl:TableRow" value="9.0 11650.0"/>
        <row xsi:type="esdl:TableRow" value="9.5 13476.0"/>
        <row xsi:type="esdl:TableRow" value="10.0 15177.0"/>
        <row xsi:type="esdl:TableRow" value="10.5 16580.0"/>
        <row xsi:type="esdl:TableRow" value="11.0 17588.0"/>
        <row xsi:type="esdl:TableRow" value="11.5 18222.0"/>
        <row xsi:type="esdl:TableRow" value="12.0 18575.0"/>
        <row xsi:type="esdl:TableRow" value="12.5 18754.0"/>
        <row xsi:type="esdl:TableRow" value="13.0 18838.0"/>
        <row xsi:type="esdl:TableRow" value="13.5 18874.0"/>
        <row xsi:type="esdl:TableRow" value="14.0 18890.0"/>
        <row xsi:type="esdl:TableRow" value="14.5 18896.0"/>
        <row xsi:type="esdl:TableRow" value="15.0 18898.0"/>
        <row xsi:type="esdl:TableRow" value="15.5 18899.0"/>
        <row xsi:type="esdl:TableRow" value="16.0 18900.0"/>
        <row xsi:type="esdl:TableRow" value="16.5 18900.0"/>
        <row xsi:type="esdl:TableRow" value="17.0 18900.0"/>
        <row xsi:type="esdl:TableRow" value="17.5 18900.0"/>
        <row xsi:type="esdl:TableRow" value="18.0 18900.0"/>
        <row xsi:type="esdl:TableRow" value="18.5 18900.0"/>
        <row xsi:type="esdl:TableRow" value="19.0 18900.0"/>
        <row xsi:type="esdl:TableRow" value="19.5 18900.0"/>
        <row xsi:type="esdl:TableRow" value="20.0 18900.0"/>
        <row xsi:type="esdl:TableRow" value="20.5 18900.0"/>
        <row xsi:type="esdl:TableRow" value="21.0 18900.0"/>
        <row xsi:type="esdl:TableRow" value="21.5 18900.0"/>
        <row xsi:type="esdl:TableRow" value="22.0 18675.0"/>
        <row xsi:type="esdl:TableRow" value="22.5 18337.0"/>
        <row xsi:type="esdl:TableRow" value="23.0 18084.0"/>
        <row xsi:type="esdl:TableRow" value="23.5 18000.0"/>
        <row xsi:type="esdl:TableRow" value="24.0 18000.0"/>
        <row xsi:type="esdl:TableRow" value="24.5 18000.0"/>
        <row xsi:type="esdl:TableRow" value="25.0 18000.0"/>
        <row xsi:type="esdl:TableRow" value="25.5 17100.0"/>
        <row xsi:type="esdl:TableRow" value="26.0 13680.0"/>
        <row xsi:type="esdl:TableRow" value="26.5 9576.0"/>
        <row xsi:type="esdl:TableRow" value="27.0 4788.0"/>
        <row xsi:type="esdl:TableRow" value="27.5 1436.0"/>
        <row xsi:type="esdl:TableRow" value="28.0 0.0"/>
        <header xsi:type="esdl:QuantityAndUnitType" physicalQuantity="SPEED" description="Windspeed in m/s" unit="METRE"
                perUnit="SECOND"/>
        <header xsi:type="esdl:QuantityAndUnitType" physicalQuantity="POWER" description="Power in kW" unit="WATT"
                multiplier="KILO"/>
    </powerCurveTable>
    <geometry xsi:type="esdl:Point" lat="52.70301871296327" lon="3.5375976562500004" CRS="WGS84"/>
</esdl:WindTurbine>