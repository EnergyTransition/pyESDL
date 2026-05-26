<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" id="fc30544f-c4a2-4227-ac28-c6542dbba734" name="Test ES deepcopy" description="" esdlVersion="v2211" version="1">
  <instance xsi:type="esdl:Instance" id="5f34b8bf-e3cc-4c07-b4db-862ec81f5452" name="Untitled instance">
    <area xsi:type="esdl:Area" id="35df64f4-fa02-4bf3-b494-4cb04d0f2578" name="Untitled area">
      <asset xsi:type="esdl:GenericConsumer" id="87d5b022-e509-4620-9d99-5f67eaf91848" name="Consumer">
        <costInformation xsi:type="esdl:CostInformation" id="3699656d-a9cf-4460-8f42-c9d38995a43c">
          <investmentCosts xsi:type="esdl:SingleValue" value="10.0" id="893e8c44-5fb7-462a-8d02-a9e90cb1147f">
            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitType" id="958b4ba9-faf2-4e20-b226-71b21c700645" description="Cost in EUR/MW" perUnit="WATT" perMultiplier="MEGA" unit="EURO" physicalQuantity="COST"/>
          </investmentCosts>
        </costInformation>
        <geometry xsi:type="esdl:Point" CRS="WGS84" lat="52.17056279155013" lon="4.82574462890625"/>
        <port xsi:type="esdl:InPort" carrier="20610790-16af-4fd9-abc9-7ec4862fcb91" connectedTo="ffd17fa0-3938-45a4-9d32-b5fc827f969e" name="In" id="10d3d38c-a4bd-4e92-a931-bbb5813d0d03"/>
        <port xsi:type="esdl:OutPort" id="82cd9093-9430-4132-adce-c4d7f3339858" name="Out"/>
      </asset>
      <asset xsi:type="esdl:GenericProducer" id="7a498855-4a30-4637-875e-1fe1c27f07fc" name="GenericProducer_7a49">
        <geometry xsi:type="esdl:Point" CRS="WGS84" lat="52.14697334064471" lon="4.534606933593751"/>
        <port xsi:type="esdl:OutPort" carrier="20610790-16af-4fd9-abc9-7ec4862fcb91" connectedTo="c48c595b-c0b0-4539-ab39-50020ae8e864" name="Out" id="c0736c68-5d87-4d8b-bb30-55e6948d4f08"/>
        <port xsi:type="esdl:InPort" id="e566df2d-ec67-4ff0-897d-a09619e0e0cb" name="In"/>
      </asset>
      <asset xsi:type="esdl:Pipe" id="9983ed8b-01c8-4b22-ba3b-5eddd55dd3fb" length="23836.6" name="Pipe_9983">
        <geometry xsi:type="esdl:Line" CRS="WGS84">
          <point xsi:type="esdl:Point" lat="52.14697334064471" lon="4.534606933593751"/>
          <point xsi:type="esdl:Point" lat="52.16593013608593" lon="4.612884521484376"/>
          <point xsi:type="esdl:Point" lat="52.13938836186961" lon="4.684295654296876"/>
          <point xsi:type="esdl:Point" lat="52.184878859051345" lon="4.740600585937501"/>
          <point xsi:type="esdl:Point" lat="52.17056279155013" lon="4.815444946289063"/>
          <point xsi:type="esdl:Point" lat="52.17056279155013" lon="4.82574462890625"/>
        </geometry>
        <port xsi:type="esdl:InPort" carrier="20610790-16af-4fd9-abc9-7ec4862fcb91" connectedTo="c0736c68-5d87-4d8b-bb30-55e6948d4f08" name="In" id="c48c595b-c0b0-4539-ab39-50020ae8e864"/>
        <port xsi:type="esdl:OutPort" carrier="20610790-16af-4fd9-abc9-7ec4862fcb91" connectedTo="10d3d38c-a4bd-4e92-a931-bbb5813d0d03" name="Out" id="ffd17fa0-3938-45a4-9d32-b5fc827f969e"/>
      </asset>
    </area>
  </instance>
  <energySystemInformation xsi:type="esdl:EnergySystemInformation" id="3e21fea8-5d40-4739-8044-eab53a4e4ca7">
    <carriers xsi:type="esdl:Carriers" id="c5f90141-e1b8-4bbd-8e10-ac0a172e611f">
      <carrier xsi:type="esdl:ElectricityCommodity" id="20610790-16af-4fd9-abc9-7ec4862fcb91" name="Electricity"/>
    </carriers>
  </energySystemInformation>
</esdl:EnergySystem>
