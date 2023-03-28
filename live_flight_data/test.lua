local telemetry_file = nil

function LuaExportStart()
  telemetry_file = io.open("telemetry.csv", "w")
  telemetry_file:write("time, lat, long, heading, baralt, radalt, pitch, bank, yaw, ias, tas, gx, gy, gz, aoa, vs\n")
end

function LuaExportBeforeNextFrame()
end

function LuaExportAfterNextFrame()
  local time = LoGetModelTime() -- OK returns current model time (args - 0, results - 1 (sec))
  local selfdata = LoGetSelfData()
  local lat = selfdata.LatLongAlt.Lat
  local long = selfdata.LatLongAlt.Long
  local heading = selfdata.Heading
  local baralt = LoGetAltitudeAboveSeaLevel() -- OK (args - 0, results - 1 (meters))
  local radalt = LoGetAltitudeAboveGroundLevel() -- OK (args - 0, results - 1 (meterst))
  local pitch, bank, yaw = LoGetADIPitchBankYaw() -- OK (args - 0, results - 3 (rad))
  local ias = LoGetIndicatedAirSpeed() -- (args - 0, results - 1 (m/s))
  local tas = LoGetTrueAirSpeed() -- (args - 0, results - 1 (m/s))
  local g =  LoGetAccelerationUnits() -- (args - 0, results - table {x = Nx,y = NY,z = NZ} 1 (G))
  local gx = g.x
  local gy = g.y
  local gz = g.z
  local aoa = LoGetAngleOfAttack() -- (args - 0, results - 1 (rad))
  local vs = LoGetVerticalVelocity()  -- (args - 0, results - 1(m/s))

  -- local atmp = LoGetBasicAtmospherePressure() -- (args - 0,results - 1) (mm hg)
  -- local slipball = LoGetSlipBallPosition()  -- (args - 0,results - 1)( -1 < result < 1)
  -- LoGetGlideDeviation()    -- (args - 0,results - 1)( -1 < result < 1)
  -- LoGetSideDeviation()     -- (args - 0,results - 1)( -1 < result < 1)

  telemetry_file:write(string.format("%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f\n", time, lat, long, heading, baralt, radalt, pitch, bank, yaw, ias, tas, gx, gy, gz, aoa, vs))
end

function LuaExportStop()
  if telemetry_file then
    telemetry_file:close()
    telemetry_file = nil
  end
end

function LuaExportActivityNextEvent(t)
end