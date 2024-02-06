import datetime

from esdl.profiles.influxdbprofilemanager import InfluxDBProfileManager, ConnectionSettings

conn = ConnectionSettings(
    host="localhost",
    port=8086,
    database="pyesdl_test",
    username="admin",
    password="admin",
    ssl=False,
    verify_ssl=False
)

start = datetime.datetime(year=2019, month=1, day=1, hour=0, minute=0)
end = datetime.datetime(year=2019, month=1, day=1, hour=3, minute=0)

ipm = InfluxDBProfileManager(conn)
ipm.load_influxdb(
    measurement="test",
    fields=["column1", "column2"],
    from_datetime=start,
    to_datetime=end
)

print(ipm.get_esdl_datetime_profile("column1"))