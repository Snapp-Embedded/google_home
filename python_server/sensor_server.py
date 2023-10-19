#!/usr/bin/env python3

from __future__ import print_function
from datetime import datetime, timezone
from gi.repository import GLib

import dbus
import dbus.service
import dbus.mainloop.glib
from scd4x import SCD4X

class DemoException(dbus.DBusException):
    _dbus_error_name = 'de.snapp.SensorException'

class SomeObject(dbus.service.Object):

    @dbus.service.method("de.snapp.SampleInterface",
                         in_signature='', out_signature='as')
    def GetSensorValue(self):
        # print the name of the bus name we are connected to
        print("GetSensorValue request:", session_bus.get_unique_name())
        # call the scd4x sensor and return the values
        co2, temperature, relative_humidity, timestamp = device.measure()
        return [f"Temperature: {temperature:.4f}°C", f"Humidity: {relative_humidity:.2f}%", f"CO2: {co2:.2f}PPM",
                session_bus.get_unique_name()]

    @dbus.service.method("de.snapp.SampleInterface",
                         in_signature='', out_signature='')
    def Exit(self):
        mainloop.quit()


if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)


    device = SCD4X(quiet=False)
    device.start_periodic_measurement()

    session_bus = dbus.SessionBus()
    name = dbus.service.BusName("de.snapp.SampleService", session_bus)
    object = SomeObject(session_bus, '/SomeObject')

    mainloop = GLib.MainLoop()
    print(usage)
    mainloop.run()