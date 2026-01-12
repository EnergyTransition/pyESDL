<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" name="New Energy System" id="8984244e-7127-4de7-90a7-ea1761f73592" version="2" esdlVersion="v2507">
  <instance xsi:type="esdl:Instance" id="4bb9e1cd-409b-4340-96e2-8fd28b220854" name="Untitled Instance">
    <area xsi:type="esdl:Area" id="42654cc8-1a67-4e9d-819a-6a904155ee65" name="Untitled Area">
      <asset xsi:type="esdl:GeothermalSource" id="70d29bc1-812c-4c71-a1b8-16d4631b381f" name="GeothermalSource_70d2" maximumFlowRate="3.0">
        <geometry xsi:type="esdl:Point" lat="52.01926092014589" lon="4.438159981977963" CRS="WGS84"/>
        <port xsi:type="esdl:OutPort" id="b314a24d-26ba-42eb-bd83-1b95b74839b9" name="Out">
          <profile xsi:type="esdl:SingleValue" id="cf2d87e6-b37c-422e-86bd-bd75ef009a0b" name="Energy output" value="4.0">
            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitType" id="b1c65b28-b9f1-4322-9bc1-a35a7c5dc203" description="Energy in TJ" multiplier="TERRA" unit="JOULE" physicalQuantity="ENERGY"/>
          </profile>
        </port>
      </asset>
    </area>
  </instance>
</esdl:EnergySystem>
